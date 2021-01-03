class Node(object):
        
    def __init__(self, location, parent=None, action=None, step_cost=0):
        self.location = location
        self.action = action
        if parent:  
            self.path_cost = parent.path_cost + step_cost
        else:
            self.path_cost = step_cost
        self.parent = parent

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    
    root = Node(problem.getStartState())
    frontier = util.Stack()
    frontier.push(root)
    explored = set()
    
    while(not frontier.isEmpty()):
        current = frontier.pop()
        
        if problem.isGoalState(current.location):
            break
        
        explored.add(current.location)
    
        for loc, action, cost in problem.getSuccessors(current.location):
            if loc in explored:
                continue
            frontier.push(Node(loc, current, action, cost))
    
        path = []
        while True:
            if not current.parent:
                break
            path.append(current.action)
            current = current.parent
            
        path = path[::-1]
        return path
