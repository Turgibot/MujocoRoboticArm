from scenes import basic, basic_stream
import data_handler
import multiprocessing as mp
import server
def run():
    basic_stream.run(True)


def display(shared_data):
    while True:
        print(shared_data[4])

if __name__ == "__main__":
    p1 = mp.Process(target=server.startServerAndPassData)
    p2 = mp.Process(target=run)
   
    p1.start()
    p2.start()
  
    
    p1.join()
    p2.join()