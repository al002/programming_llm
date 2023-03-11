import asyncio
import logging

import grpc

import llm_pb2
import llm_pb2_grpc

async def run() -> None:
    async with grpc.aio.insecure_channel('localhost:50051') as channel:
        stub = llm_pb2_grpc.LLMStub(channel)
        response = await stub.query(llm_pb2.LLMRequest(query="What did the author do growing up?"))
    print("LLM client received: " + response.response)

if __name__ == '__main__':
    logging.basicConfig()
    asyncio.run(run())
