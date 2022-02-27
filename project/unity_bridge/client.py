
import asyncio
import logging
import random
from turtle import width
from typing import Iterable, List

import grpc
import guy_pb2
import guy_pb2_grpc
import cv2

def make_image_note(width: int, height: int, image_data: bytes) -> guy_pb2.Image:
    return guy_pb2.Image(
        width=width,
        height=height,
        image_data=image_data)



def generateStream()-> Iterable[guy_pb2.Image]:
    cam = cv2.VideoCapture(0)
    while True:
        ret_val, img = cam.read()
        
        frame = bytes(img)
        yield guy_pb2.Image(width=img.shape[0], height=img.shape[1], image_data=frame)
    #     cv2.imshow("N", img)
    # cv2.destroyAllWindows()


# Performs a client-streaming call
async def sendWebCamStream(stub: guy_pb2_grpc.GuyStub) -> None:
    
    stream_iterator = generateStream()

    # gRPC AsyncIO client-streaming RPC API accepts both synchronous iterables
    # and async iterables.
    received = await stub.SendVideo(stream_iterator)
    print(f"Finished stream successfully:  {received.ack}")
    

async def main() -> None:
    async with grpc.aio.insecure_channel('localhost:50051') as channel:
        stub = guy_pb2_grpc.GuyStub(channel)
        print("-------------- sendWebCamStream --------------")
        await sendWebCamStream(stub)
       


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())