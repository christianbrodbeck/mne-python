# Author: Christian Brodbeck <christianbrodbeck@nyu.edu>
from io import BytesIO


class PersistentBytesIO(BytesIO):

    def close(self):
        if not self.closed:
            self.flush()
            # self.value = self.getvalue()
            self.seek(0)
            self.__value = self.read()
            BytesIO.close(self)

    def get_value_after_close(self):
        return self.__value
