import asyncio
import logging

import grpc

import llm_pb2
import llm_pb2_grpc

async def run() -> None:
    async with grpc.aio.insecure_channel('localhost:50051') as channel:
        stub = llm_pb2_grpc.LLMStub(channel)
        response = await stub.query(llm_pb2.LLMRequest(query="pwd", template=llm_pb2.TERMINAL))

        # response = await stub.query(llm_pb2.LLMRequest(query="""I want you to act as a linux terminal. I will type commands and you will reply with what the terminal should show. I want you to only reply with the terminal output inside one unique code block, and nothin else. do not write explanations. do not type commands unless I instruct you to do so. My first command is pwd"""))
    print("LLM client received: " + response.response)

if __name__ == '__main__':
    logging.basicConfig()
    asyncio.run(run())
