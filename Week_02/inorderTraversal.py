class Solution(object):
    def inorderTraversal(self, root):
    	res = []
    	stack = []
    	while root or stack:
    		if root:
    			stack.append(root)
    			root = root.left
    		else:
    			tmp = stack.pop()
    			res.append(tmp.val)
    			root = tmp.right

    	return res

