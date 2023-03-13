import asyncio
import logging

import grpc
import llm_pb2
import llm_pb2_grpc

from programming_llm import llm

class LLM(llm_pb2_grpc.LLMServicer):
    async def query(self, request: llm_pb2.LLMRequest,
                    context: grpc.aio.ServicerContext) -> llm_pb2.LLMReply:
        answer = llm.run(request.query, request.template)
        return llm_pb2.LLMReply(response=answer)


async def serve() -> None:
    server = grpc.aio.server()
    llm_pb2_grpc.add_LLMServicer_to_server(LLM(), server)
    listen_addr = '[::]:50051'
    server.add_insecure_port(listen_addr)
    logging.info("Starting server on %s", listen_addr)
    await server.start()
    await server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve())
