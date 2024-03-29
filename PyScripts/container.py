from box import Box


class Container:
    def __init__(self, id: int, width: int, height: int, length: int, maxWeight: int):
        self.id = id
        self.width = width
        self.height = height
        self.length = length
        self.maxWeight = maxWeight
        self.currentWeight = 0
        self.putCargos = []
        self.currentWidth = 0

    def getSize(self):
        return {'height': self.height/1000, 'length': self.length/1000, 'width': self.width/1000}

    def getPosition(self):
        return [self.length/2000, self.height/2000, self.width/2000]

    def addBox(self, box: Box, addedPosition):
        if self.maxWeight - self.currentWeight < box.mass:
            return False
        position = addedPosition.copy()
        position["width"] += self.currentWidth
        if position["width"] + box.width / 2 <= self.width and position["width"] - box.width / 2 >= 0:
            if position["height"] + box.height / 2 <= self.height and position["height"] - box.height / 2 >= 0:
                if position["length"] + box.length / 2 <= self.length and position["length"] - box.length / 2 >= 0:
                    if not self.putCargos:
                        self.currentWeight += box.mass
                        newb = box.copy()
                        newb.setPosition(position)
                        self.putCargos.append(newb)
                        return True
                    else:
                        for checkedBox in self.putCargos:
                            checkedPosition = checkedBox.getPosition()
                            if abs(checkedPosition["width"] - position["width"]) >= checkedBox.width / 2 + box.width / 2 or abs(
                                checkedPosition["length"] - position["length"]) >= checkedBox.length / 2 + box.length / 2 or abs(
                                checkedPosition["height"] - position["height"]) >= checkedBox.height / 2 + box.height / 2:
                                self.currentWeight += box.mass
                                newb = box.copy()
                                newb.setPosition(position)
                                self.putCargos.append(newb)
                                return True
        return False