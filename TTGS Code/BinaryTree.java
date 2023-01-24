// Java program to print top
// view of binary tree
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Map;
import java.util.Queue;
import java.util.TreeMap;

// class to create a node
class Node {
	int data;
	Node left, right;

	public Node(int data)
	{
		this.data = data;
		left = right = null;
	}
}

// class of binary tree
class BinaryTree {
	Node root;
     ArrayList<Integer> ans = new ArrayList<>();
	public BinaryTree() { root = null; }

	// function should print the topView of
	// the binary tree
	private void TopView(Node root)
	{
		class Pair {
			Node node;
			int lvl;

			Pair(Node node, int lvl)
			{
				this.node = node;
				this.lvl = lvl;
			}
		}
		Queue<Pair> q = new LinkedList<Pair>();
		Map<Integer, Node> topViewMap
			= new TreeMap<Integer, Node>();

		if (root == null) {
			return;
		}
		else {
			q.offer(new Pair(root, 0));
		}

		System.out.println(
			"The top view of the tree is : ");

		// count function returns 1 if the container
		// contains an element whose key is equivalent
		// to lvl, or returns zero otherwise.
		while (!q.isEmpty()) {
			Pair tmpNode = q.poll();
			if (topViewMap.get(tmpNode.lvl) == null) {
				topViewMap.put(tmpNode.lvl, tmpNode.node);
			}

			if (tmpNode.node.left != null) {
				q.offer(new Pair(tmpNode.node.left,
								tmpNode.lvl - 1));
			}
			if (tmpNode.node.right != null) {
				q.offer(new Pair(tmpNode.node.right,
								tmpNode.lvl + 1));
			}
		}

		for (Map.Entry<Integer, Node> entry :
			topViewMap.entrySet()) {
			ans.add(entry.getValue().data);
		 }
	for (Integer elem: ans) {
			System.out.print(elem + " ");
		}
		
	}

	// Driver code
	public static void main(String[] args)
	{
		/* Create following Binary Tree
	 1
	/ \
   2   3
	\
	 4
	  \
	   5
		\
		 6
*/
		BinaryTree tree = new BinaryTree();
		tree.root = new Node(1);
		tree.root.left = new Node(2);
		tree.root.right = new Node(3);
		tree.root.left.right = new Node(4);
		tree.root.left.right.right = new Node(5);
		tree.root.left.right.right.right = new Node(6);
		tree.TopView(tree.root);
	}
}