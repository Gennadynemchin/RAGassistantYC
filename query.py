def ask(assistant, thread, question: str) -> str:
    thread.write(question)
    run = assistant.run(thread)
    result = run.wait()
    return result.text
