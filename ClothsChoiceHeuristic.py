import sys
import inspect
import heapq, random
from collections import Counter

import numpy as np


class PriorityQueue:
    """
      Implements a priority queue data structure. Each inserted item
      has a priority associated with it and the client is usually interested
      in quick retrieval of the lowest-priority item in the queue. This
      data structure allows O(1) access to the lowest-priority item.

      Note that this PriorityQueue does not allow you to change the priority
      of an item.  However, you may insert the same item multiple times with
      different priorities.
    """

    def __init__(self):
        self.heap = []
        self.init = False

    def push(self, item, priority):
        if not self.init:
            self.init = True
            try:
                item < item
            except:
                item.__class__.__lt__ = lambda x, y: (True)
        pair = (priority, item)
        heapq.heappush(self.heap, pair)

    def pop(self):
        (priority, item) = heapq.heappop(self.heap)
        return item

    def isEmpty(self):
        return len(self.heap) == 0

class UniformCostNode:
    def __init__(self, neighbor, action, currNode, cost, secondaryPriority=0):
        self.neighbor = neighbor
        self.action = action
        self.currNode = currNode
        self.cost = cost
        self.secondaryPriority = secondaryPriority

    def open(self):
        return self.neighbor, self.action, self.currNode, self.cost

    def __lt__(self, other):
        return self.secondaryPriority < other.secondaryPriority


def uniform_cost_search(problem):
    """
    Search the node of least total cost first.
    """
    nodePath = dict()
    nodeCost = Counter()
    root = problem.get_start_state()
    fringe = PriorityQueue()
    fringe.push(UniformCostNode(root, None, root, 0), 0)
    while not fringe.isEmpty():
        currNode, currAction, prevNode, currNodeCost = fringe.pop().open()
        if currNode not in nodePath:
            nodePath[currNode] = list(nodePath.get(prevNode, []))
            nodePath[currNode].append(currAction)
            nodeCost[currNode] = nodeCost[prevNode] + currNodeCost
            if problem.is_goal_state(currNode):
                return nodePath[currNode][1:]
            currNeighbors = problem.get_successors(currNode)
            for (neighbor, action) in currNeighbors:
                cost = heuristic(problem.weatherRank, problem.casualityVal, action, currNode.chosenItems)
                if neighbor not in nodePath:
                    fringe.push(UniformCostNode(neighbor, action, currNode, cost,
                                                len(nodePath[currNode])), nodeCost[prevNode] + cost)




class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def __init__(self, weatherRank, casualityVal, itemsList):
        self.weatherRank = weatherRank
        self.casualityVal = casualityVal
        self.chosePants = False
        self.choseTop = False
        self.choseCoat = False
        self.choseShoe = False
        self.choseBag = False
        self.chosenItems = []
        self.itemsList = itemsList

    def set_chosen_items(self, other):
        self.chosePants = other.chosePants
        self.choseTop = other.choseTop
        self.choseCoat = other.choseCoat
        self.choseShoe = other.choseShoe
        self.choseBag = other.choseBag
        self.chosenItems = other.chosenItems

    def add_item(self, item):
        if item.clothing_type == 8:
            self.choseBag = True
            self.chosenItems.append(item)
            for currItem in self.itemsList:
                if currItem.clothing_type == 8:
                    self.itemsList.remove(currItem)
        elif item.clothing_type in [0, 2, 6]:
            self.choseTop = True
            self.chosenItems.append(item)
            for currItem in self.itemsList:
                if currItem.clothing_type in [0, 2, 6]:
                    self.itemsList.remove(currItem)
        elif item.clothing_type in [1,3]:
            self.chosePants = True
            self.chosenItems.append(item)
            for currItem in self.itemsList:
                if currItem.clothing_type in [1, 3]:
                    self.itemsList.remove(currItem)
        elif item.clothing_type in [5,7,9]:
            self.choseShoe = True
            self.chosenItems.append(item)
            for currItem in self.itemsList:
                if currItem.clothing_type in [5, 7, 9]:
                    self.itemsList.remove(currItem)
        elif item.clothing_type == 4:
            self.choseCoat = True
            self.chosenItems.append(item)
            for currItem in self.itemsList:
                if currItem.clothing_type == 4:
                    self.itemsList.remove(currItem)


    def get_start_state(self):
        """
        Returns the start state for the search problem
        """
        itemsList = []
        if self.casualityVal in [1,2]:
            for currItem in self.itemsList:
                if (self.weatherRank <= 2) and (currItem.clothing_type in [1,2,4,7,8,9]):
                    itemsList.append(currItem)
                if (self.weatherRank >= 3) and (currItem.clothing_type in [0,1,2,3,5,7,8]):
                    itemsList.append(currItem)
        else:
            for currItem in self.itemsList:
                if (self.weatherRank <= 2) and (currItem.clothing_type in [1, 3, 4, 6, 7, 8]):
                    itemsList.append(currItem)
                if (self.weatherRank >= 3) and (currItem.clothing_type in [1, 3, 6, 7, 8]):
                    itemsList.append(currItem)
        return SearchProblem(self.weatherRank, self.casualityVal, itemsList)


    def is_goal_state(self, state):
        """
        state: Search state

        Returns True if and only if the state is a valid goal state
        """
        if state.weatherRank <= 2:
            return state.chosePants and state.choseTop and state.choseShoe and state.choseCoat and state.choseBag
        return state.chosePants and state.choseTop and state.choseShoe and state.choseBag

    def get_successors(self, state):
        """
        state: Search state

        For a given state, this should return a list of triples,
        (successor, action), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        itemsList = []
        if self.casualityVal in [1,2]:
            if self.weatherRank <= 2:
                clothingTypeList = [1, 2, 4, 7, 8, 9]
            else:
                clothingTypeList = [0, 1, 2, 3, 5, 7, 8]
        else:
            if self.weatherRank <= 2:
                clothingTypeList = [1, 3, 4, 6, 7, 8]
            else:
                clothingTypeList = [1, 3, 6, 7, 8]
        if self.choseCoat:
            if 4 in clothingTypeList: #remove coat
                clothingTypeList.remove(4)
        if self.choseTop:
            if 0 in clothingTypeList: #remove Tshirt
                clothingTypeList.remove(0)
            if 2 in clothingTypeList: #remove Pullover
                clothingTypeList.remove(2)
            if 6 in clothingTypeList: #remove shirt
                clothingTypeList.remove(6)
        if self.choseShoe:
            if 5 in clothingTypeList: #remove sandal
                clothingTypeList.remove(5)
            if 7 in clothingTypeList: #remove sneaker
                clothingTypeList.remove(7)
            if 9 in clothingTypeList: #remove boot
                clothingTypeList.remove(9)
        if self.chosePants:
            if 1 in clothingTypeList: #remove trousers
                clothingTypeList.remove(1)
            if 3 in clothingTypeList: #remove skirt
                clothingTypeList.remove(3)
        if self.choseBag:
            if 8 in clothingTypeList:
                clothingTypeList.remove(8)
        for currItem in state.itemsList:
            if currItem.clothing_type in clothingTypeList:
                itemsList.append(currItem)
        returnList = []
        for item in itemsList:
            currSearchProblem = SearchProblem(self.weatherRank, self.casualityVal, itemsList)
            currSearchProblem.set_chosen_items(state)
            returnList.append((currSearchProblem.add_item(item), item))
        return returnList

def computeColorCasuality(casualityRank, colors):
    result = 3
    if casualityRank == 1:
        if colors[0] > colors[1] and colors[0] > colors[2]:
            result = 0
        else:
            if colors[0] > colors[1]:
                result -= 1
            if colors[0] > colors[2]:
                result -= 1
    elif casualityRank == 2:
        if colors[1] > colors[2] and colors[1] > colors[0]:
            result = 0
        else:
            if colors[1] > colors[2]:
                result -= 1
            if colors[1] > colors[0]:
                result -= 1
    elif casualityRank == 3:
        if colors[2] > colors[0] and colors[2] > colors[1]:
            result = 0
        else:
            if colors[2] > colors[1]:
                result -= 1
            if colors[2] > colors[0]:
                result -= 1
    return result

def heuristic(casualityRank, currItem, ourItems):
    heuristicVal = 0
    for color in currItem.colors:
        heuristicVal += computeColorCasuality(casualityRank, color)
    return heuristicVal
