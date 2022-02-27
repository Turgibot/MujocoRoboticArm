import numpy as np
import cv2
def proccess_shared_data(shared_data):
    prev_frame = None
    colored_frame = None

    while True:
        width = shared_data[0]
        height = shared_data[1]
        image_data = shared_data[2]
        depth_data = shared_data[3]
        timestamp = shared_data[4]
        try:
            params = list(shared_data[5])
            frame = np.array(list(image_data), dtype = np.uint8)
            depth_frame = np.array(list(depth_data), dtype = np.uint8)
        except:
            params = None

        if params is None:
            continue

        #if shared_data is x than y

        frame = get_frame(width, height, frame)
        depth_frame = get_depth_frame(width, height, depth_frame)
        depth_frame_bgr = cv2.cvtColor(depth_frame, cv2.COLOR_GRAY2BGR)
        # spikes

       
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        prev_frame, colored_frame = get_spike_frame(width, height, frame_gray, prev_frame) # TODO add thresholds
        if colored_frame is not None:
            all_frames = cv2.vconcat([frame, depth_frame_bgr, colored_frame])
            cv2.imshow("", all_frames)
            if cv2.waitKey(1) == 27:
                break
    
    cv2.destroyAllWindows()

def get_frame(width, height, frame):
    
    frame = frame.reshape((height*2,width, 3))
    left = frame[:height]
    right = frame[height:]
    frame = np.concatenate([left, right], axis=1)
    
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = cv2.flip(frame, 0)
    return frame

def get_depth_frame(width, height, frame):
    frame = frame.reshape((height*2, width, 3))
    left = frame[:height]
    right = frame[height:]
    frame = np.concatenate([left, right], axis=1)
    frame *= 2
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.flip(frame, 0)
    return frame

def get_spike_frame(width, height, frame, prev_frame):
    pos_th = 4
    neg_th = 4
    
    src_shape = (frame.shape[0], frame.shape[1], 3) 
    colored_frame = None
    if prev_frame is not None:
        spikes_frame = getSpikesFrom2Frames(prev_frame, frame, pos_th, neg_th).flatten()
        shape = [int(x) for x in spikes_frame.shape]
        colored_frame = np.zeros(shape=shape+[3], dtype="uint8")
        colored_frame[spikes_frame==-1] = [255, 0, 0] 
        colored_frame[spikes_frame==1] = [0, 0, 255] 
        colored_frame = colored_frame.reshape(src_shape)
        
    return frame, colored_frame

def getSpikesFrom2Frames(prev_frame, frame, pos_th, neg_th):

        deltas = np.array(np.array(prev_frame, dtype=np.int16)-np.array(frame, dtype=np.int16), dtype=np.int16)
        deltas = np.where(deltas == 1, 0, deltas)
        deltas = np.where(deltas == -1, 0, deltas)
        deltas = np.where(deltas >= pos_th, 1, deltas)
        deltas = np.where(deltas < -neg_th, -1, deltas)
        deltas = np.where(deltas > 1, 0, deltas)
        deltas = np.where(deltas < -1 , 0, deltas)
        
        return deltas
