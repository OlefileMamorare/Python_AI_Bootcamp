from __future__ import annotations

import os
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI


def build_transcript(history: list[dict[str, str]]) -> str:
    """Turn role/content history into a simple text transcript."""
    return "\n".join(f"{m['role'].upper()}: {m['content']}" for m in history)


def main() -> None:
    # Load .env (make sure OPENAI_API_KEY is set there)
    load_dotenv(find_dotenv(), override=True)

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "OPENAI_API_KEY not found. Add it to your .env file like:\n"
            "OPENAI_API_KEY=sk-..."
        )

    client = OpenAI(api_key=api_key)

    system_instruction = (
        "You are a helpful, friendly tutor. Explain clearly, step by step. "
        "When useful, include short Python examples. Keep answers concise."
    )

    history: list[dict[str, str]] = [{"role": "system", "content": system_instruction}]

    print("🤖 Terminal Chatbot (type 'exit' to quit, 'reset' to clear chat)\n")

    while True:
        user_text = input("You: ").strip()

        if not user_text:
            continue

        cmd = user_text.lower()
        if cmd in {"exit", "quit"}:
            print("Bot: Bye! 👋")
            break

        if cmd in {"reset", "/reset"}:
            history = [{"role": "system", "content": system_instruction}]
            print("Bot: Chat reset ✅\n")
            continue

        # Add user message
        history.append({"role": "user", "content": user_text})

        # Limit memory: keep system + last 12 messages
        history = history[:1] + history[-12:]

        transcript = build_transcript(history)

        response = client.responses.create(
            model="gpt-4o-mini",
            input=transcript,
            temperature=0.7,
        )

        bot_text = (response.output_text or "").strip()
        if not bot_text:
            bot_text = "I didn't get that—could you rephrase?"

        print(f"Bot: {bot_text}\n")

        # Add assistant message
        history.append({"role": "assistant", "content": bot_text})


if __name__ == "__main__":
    main()
