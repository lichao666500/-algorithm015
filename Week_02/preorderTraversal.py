class Solution(object):
    def preorderTraversal(self, root):
    	res = []
    	stack = []
    	while root or stack:
    		while root:
    			res.append(root.val)
    			stack.append(root)
    			root = root.left
    		top = stack.pop()
    		root = top.right
    	return res