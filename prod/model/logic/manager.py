from prod.model.entity import *

class Manager:
    SHORT = (3, 0.5)
    NORM = (5, 1.0)
    SUPER = 2.0

    @staticmethod
    def calculate(transport, hour):
        if isinstance(transport, Transport) and hour > 0:
            if transport.square <= Manager.SHORT:
                amount = Manager.SHORT[1] * hour
            elif transport.square <= Manager.NORM[0]:
                amount = Manager.NORM[1]
            else:
                amount = Manager.SUPER[1]

            amount *= hour

            return amount

        else:
            Exception
