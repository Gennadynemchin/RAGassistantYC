from config import ASSISTANT_INSTRUCTION, model, sdk


def create_assistant(search_tool):
    assistant = sdk.assistants.create(
        model,
        ttl_days=7,
        expiration_policy="since_last_active",
        tools=[search_tool],
    )
    assistant.update(instruction=ASSISTANT_INSTRUCTION)
    return assistant


def get_assistant(assistant_id: str):
    return sdk.assistants.get(assistant_id)


def create_thread():
    return sdk.threads.create(ttl_days=1, expiration_policy="static")
