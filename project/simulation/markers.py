

class Arrow:
    def __init__(self, rot_mat=None, pos=None, label=None, size=None, rgba=None, dir="x"):
        self.rot_mat = rot_mat
        self.pos = pos
        self.label = label
        self.size = size
        self.rgba = rgba

    def set_z(self, pos=[-0.5, 0.5, 0]):
        self.rot_mat = [[1, 0, 0],[0, 1, 0],[0, 0, 1]]
        self.label = "z"
        if self.size is None:
            self.size = [0.01, 0.01, 0.35]
        self.rgba = [0, 0, 1, 1]
        self.pos = pos

    def set_y(self, pos=[-0.5, 0.5, 0]):
        self.rot_mat = [[1, 0, 0],[0, 0, 1],[0, -1, 0]]
        self.label = "y"
        if self.size is None:
            self.size = [0.01, 0.01, 0.35]
        self.rgba = [0, 1, 0, 1]
        self.pos = pos
    
    def set_x(self, pos=[-0.5, 0.5, 0]):
        self.rot_mat = [[0, 0, 1],[0, 1, 0],[-1, 0, 0]]
        self.label = "x"
        if self.size is None:
            self.size = [0.01, 0.01, 0.35]
        self.rgba = [1, 0, 0, 1]
        self.pos = pos

