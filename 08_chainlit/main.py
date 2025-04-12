import chainlit as cl

@cl.on_chat_start
def on_chat_start():
    cl.user_session.set("counter", 0)


@cl.on_message
async def on_message(message: cl.Message):
    counter = cl.user_session.get("counter")
    counter += 1
    cl.user_session.set("counter", counter)

    await cl.Message(content=f"You sent {counter} message(s)!").send()