学习笔记

## DFS 代码模板 ##

#### 递归写法 ####
    
    #Python
    visited = set() 
    
    def dfs(node, visited):
    	if node in visited: # terminator
    		# already visited 
    		return 
    
    	visited.add(node) 
    
    	# process current node here. 
    	...
    	for next_node in node.children(): 
    		if next_node not in visited: 
    			dfs(next_node, visited)

#### 非递归写法 ####

    
    #Python
    def DFS(self, tree): 
    
    	if tree.root is None: 
    		return [] 
    
    	visited, stack = [], [tree.root]
    
    	while stack: 
    		node = stack.pop() 
    		visited.add(node)
    
    		process (node) 
    		nodes = generate_related_nodes(node) 
    		stack.push(nodes) 
    
    	# other processing work 
    	...

## BFS 代码模板 ##
    
    # Python
    def BFS(graph, start, end):
    	visited = set()
    	queue = [] 
    	queue.append([start]) 

    	while queue: 
    		node = queue.pop() 
    		visited.add(node)
    		process(node) 
    		nodes = generate_related_nodes(node) 
    		queue.push(nodes)

    	# other processing work 
    	...

## 贪心算法 ##

在每一步选择中都采取在当前状态下最好或最优（即最有利）的选择，从而希望导致结果是全局最好或最优的算法。

