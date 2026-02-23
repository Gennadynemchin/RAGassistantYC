import argparse

import state
from assistant import create_assistant, create_thread, get_assistant
from config import sdk
from indexing import create_index
from query import ask
from upload import upload_files


def setup(current_state: dict) -> object:
    if "index_id" in current_state:
        index_id = current_state["index_id"]
    else:
        files = upload_files()
        index_id = create_index(files)
        current_state["index_id"] = index_id
        state.save(current_state)

    search_tool = sdk.tools.search_index(index_id)

    if "assistant_id" in current_state:
        assistant = get_assistant(current_state["assistant_id"])
    else:
        assistant = create_assistant(search_tool)
        current_state["assistant_id"] = assistant.id
        state.save(current_state)

    return assistant


def main() -> None:
    parser = argparse.ArgumentParser(description="Kubernetes RAG-консультант")
    parser.add_argument(
        "--reset",
        action="store_true",
        help="Сбросить сохранённое состояние и загрузить всё заново",
    )
    args = parser.parse_args()

    if args.reset:
        state.clear()

    current_state = state.load()
    assistant = setup(current_state)
    thread = create_thread()

    while True:
        try:
            question = input("Вопрос: ").strip()
        except (EOFError, KeyboardInterrupt):
            break

        if question.lower() in ("выход", "exit", "quit"):
            break

        if not question:
            continue

        answer = ask(assistant, thread, question)
        print(answer)


if __name__ == "__main__":
    main()
