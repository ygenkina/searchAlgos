""" Attempt at writing a Deoth First Search and Breadth First Search alogorythms for an arrange the numbers game with a 3x3 board"""

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

class Node:
    nodes_visited = 0
    
    def __init__(self,state,parent,action):
        self.state = state
        self.parent = parent
        self.action = action
   #     self.path_cost = path_cost

        Node.nodes_visited += 1
    
    def get_parent(self):
        return self.parent

    def get_action(self):
        return self.action


"""-------- block below, i is L.index(0)-------"""
def isUp(i):
  return i > 3

def isDown(i):
  return i < 5

def isLeft(i):
  return i % 3 != 0

def isRight(i):
  return i % 3 != 2

def up(st,i):
  n1 = st[i]
  n2 = st[i-3]
  st = st[:i-3]+n1+st[i-2:i]+n2+st[i+1:]
  return st

def down(st,i): 
  n1 = st[i]
  n2 = st[i+3]
  st = st[:i]+n2+st[i+1:i+3]+n1+st[i+4:]
  return st

def left(st,i):
  n1 = st[i]
  n2 = st[i-1]
  st = st[:i-1]+n1+n2+st[i+1:]
  return st

def right(st,i):
  n1 = st[i]
  n2 = st[i+1]
  st = st[:i]+n2+n1+st[i+2:]
  return st


def makeBoard(st):
  out = ''
  count = 0
  while count < 9:
    out += st[count]
    count += 1
    if count % 3 == 0:
      out += '\n'
  return out
"----------------Breadth First Search Algorithm------"    
def bfsMoves(state,goalSt): #does the actual search, returns the path to goal
  frontier = Queue()     #create empty queue for fringe a.k.a frontier, states/nodes to explore
  frontier.enqueue(state) #add the initial state to the queue
  explored = {}  #create a dictionary storage for the explored nodes
  explored[state]= Node(state,state,'START_HERE') #record info about the root node state = state, parent = state, action = start_here for id
  count = 0 # count the number of expanded nodes
  while state != goalSt: #as long as there is no solution yet
    state = frontier.dequeue() #get a state out of the queue
#    print makeBoard(state) # test board to compare with nodes
    count += 1
    i = state.find('0') #location of blank space in the game
    if isUp(i):   #check if it is possible to move up
      newState = up(state,i) # if yes, create the new board
      if newState not in explored: #fi the board hasn't been explored yet
        node = Node(newState,state,'Up') #record info about the state in the Node object
        explored[newState] = node # add all that info to the explored dictionary
        frontier.enqueue(newState) #throw this into the queue for future exploration
    if isDown(i):
      newState = down(state,i)
      if newState not in explored:
        node = Node(newState,state,'Down')
        explored[newState] = node
        frontier.enqueue(newState)
    if isLeft(i):
      newState = left(state,i)
      if newState not in explored:
        node = Node(newState,state,'Left')
        explored[newState] = node
        frontier.enqueue(newState)
    if isRight(i):
      newState = right(state,i)
      if newState not in explored:
        node = Node(newState,state,'Right')
        explored[newState] = node
        frontier.enqueue(newState)
  moves=[]
  while explored[state].get_action() != "START_HERE":
    n = explored[state]
    moves.append(n.get_action())
    state = n.get_parent()
  return moves[::-1]+[count]

goal = '012345678'
def convert(given):
  out = given.split(',')
  out = ''.join(out)
  return out

def resultsBfs(inSt):
  inSt = convert(inSt)
  searchAns = bfsMoves(inSt,goal) 
  out = ''
  out += 'path_to_goal: '
  out += str(searchAns[:-1]) + '\n'
  out += 'cost_of_path: '
  out += str(len(searchAns[:-1])) + '\n'
  out += 'nodes_expanded: '
#  out += str(Node.nodes_visited)
  out += str(searchAns[-1]) + '\n'
  return out

test1 = '1,2,5,3,4,0,6,7,8'
test2 ='6,1,8,4,0,2,7,3,5'
test3 = '8,6,4,2,1,3,5,7,0'
test4 = '1,2,5,3,0,8,6,4,7'
test5 = '1,2,5,6,3,8,0,4,7'
test6 = '1,2,5,6,3,8,4,0,7'
test7 = '1,2,5,6,0,8,4,3,7'
test8 = '1,0,5,6,2,8,4,3,7'
test9 = '0,1,5,6,2,8,4,3,7'
test10 = '6,1,5,0,2,8,4,3,7' #error starts here!
test11 = '6,1,5,4,2,8,0,3,7'


print resultsBfs(test1)
print 'should be c_O_p: 3, nodes_exp: 10\n----------\n'

print resultsBfs(test4)
print 'should be c_O_p: 20, nodes_exp: 54094\n-------\n'

print resultsBfs(test5)
print 'should be c_O_p: 20, nodes_exp: 54094\n-------\n'

print resultsBfs(test6)
print 'should be c_O_p: 20, nodes_exp: 54094\n-------\n'

print resultsBfs(test7)
print 'should be c_O_p: 20, nodes_exp: 54094\n-------\n'

print resultsBfs(test8)
print 'should be c_O_p: 20, nodes_exp: 54094\n-------\n'

print resultsBfs(test9)
print 'should be c_O_p: 20, nodes_exp: 54094\n-------\n'

print resultsBfs(test10)
print 'should be c_O_p: 20, nodes_exp: 54094\n-------\n'

print resultsBfs(test11)
print 'should be c_O_p: 20, nodes_exp: 54094\n-------\n'


'''
print results(test3)
print 'should be c_O_p: 26, nodes_exp: 166786\n---------\n'

print resultsBfs(test4)
print 'should be c_O_p: 6, nodes_exp: ???\n-------\n'
'''

'''------------------------------Depth First Search----------------------------'''

def dfsMoves(state,goalSt): #does the actual search, returns the path to goal
  frontier = Stack()     #create empty stack for fringe a.k.a frontier, states/nodes to explore
  frontier.push(state) #add the initial state to the queue
  explored = {}  #create a dictionary storage for the explored nodes
  explored[state]= Node(state,state,'START_HERE') #record info about the root node state = state, parent = state, action = start_here for id
  count = 0 # count the number of expanded nodes
  while state != goalSt: #as long as there is no solution yet
    state = frontier.pop() #get a state out of the queue
#    print makeBoard(state) # test board to compare with nodes
    count += 1
    i = state.find('0') #location of blank space in the game
    if isRight(i):
      newState = right(state,i)
      if newState not in explored:
        node = Node(newState,state,'Right')
        explored[newState] = node
        frontier.push(newState)    
    if isLeft(i):
      newState = left(state,i)
      if newState not in explored:
        node = Node(newState,state,'Left')
        explored[newState] = node
        frontier.push(newState)
    if isDown(i):
      newState = down(state,i)
      if newState not in explored:
        node = Node(newState,state,'Down')
        explored[newState] = node
        frontier.push(newState)
    if isUp(i):   #check if it is possible to move up
      newState = up(state,i) # if yes, create the new board
      if newState not in explored: #fi the board hasn't been explored yet
        node = Node(newState,state,'Up') #record info about the state in the Node object
        explored[newState] = node # add all that info to the explored dictionary
        frontier.push(newState) #throw this into the queue for future exploration    
  moves=[]
  while explored[state].get_action() != "START_HERE":
    n = explored[state]
    moves.append(n.get_action())
    state = n.get_parent()
  return moves[::-1]+[count]


def resultsDfs(inSt):
  inSt = convert(inSt)
  searchAns = dfsMoves(inSt,goal) 
  out = ''
  out += 'path_to_goal: '
  out += str(searchAns[:-1]) + '\n'
  out += 'cost_of_path: '
  out += str(len(searchAns[:-1])) + '\n'
  out += 'nodes_expanded: '
#  out += str(Node.nodes_visited)
  out += str(searchAns[-1]) + '\n'
  return out



'''
print resultsDfs(test1)
print 'should be c_O_p: 3, nodes_exp: 181437\n----------\n'
'''


def fileOut(result):
  f = openFile('genkina.txt', 'w')
  f.write(result)
  f.close()
  







    












