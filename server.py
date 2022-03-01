import asyncio
from cgitb import handler
from collections import defaultdict
from datetime import date
from email.policy import default
import logging
import time
from turtle import update
from typing import AsyncIterable, Iterable

import grpc
from sympy import im
import UnityStreamer_pb2
import UnityStreamer_pb2_grpc
import numpy as np
import cv2
import multiprocessing as mp
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import mpl_toolkits.mplot3d.axes3d as p3
import data_handler

from datetime import datetime
'''
  int32 width = 1;
  int32 height = 2;
  bytes image_data = 3;
  bytes depth_data = 4;
  int64 timestamp = 5;
  repeated int32 params =6;
'''

manager = mp.Manager()
shared_data = manager.list()
for i in range(6):
    shared_data.append(-1)



class UnityStreamerServicer(UnityStreamer_pb2_grpc.UnityStreamerServicer):
    def __init__(self):
      pass


    async def StreamData(self, request_iterator: AsyncIterable[
        UnityStreamer_pb2.UnityData], unused_context) -> UnityStreamer_pb2.Received:
    
        async for data in request_iterator:
            
            shared_data[0] = data.width
            shared_data[1] = data.height
            shared_data[2] = data.image_data
            shared_data[3] = data.depth_data
            shared_data[4] = data.timestamp
            shared_data[5] = list(data.params)

        return UnityStreamer_pb2.Received(timestamp=datetime.timestamp(datetime.now()))
    

async def serve(servicer) -> None:
    server = grpc.aio.server()
    UnityStreamer_pb2_grpc.add_UnityStreamerServicer_to_server(servicer, server)
    server.add_insecure_port('[::]:50051')
    await server.start()
    await server.wait_for_termination()
    cv2.destroyAllWindows()

 
def run():
    servicer = UnityStreamerServicer()
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(serve(servicer))


def startServerAndPassData():
    
    
    p2 = mp.Process(target=run)
    p1 = mp.Process(target=data_handler.proccess_shared_data , args=(shared_data, ))
    p2.start()
    p1.start()
    p2.join()
    p1.join()

  