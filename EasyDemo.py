# 开发人员：泽天

# 开发时间：2024/4/11 13:34

# 项目定义：
# class EasyDemo:
#     def __init__(self, age, name):
#         self.age = age
#         self.name = name
#
#     def print(self):
#         print(f"age {self.age}\nname {self.name}")
#
#
# person1 = EasyDemo(12, '王三')
# person1.print()

# 打印菱形
# def main():
#     rows = int(input("请输入需要打印的个数："))
#     draw_equilateral_triangle(rows)
#
#
# def draw_equilateral_triangle(rows):
#     for i in range(rows):
#         spaces = rows - i - 1
#         stars = 2 * i + 1
#         print(' ' * spaces + '*' * stars)
#
#     for i in range(rows - 1, 0, -1):
#         spaces = rows - i
#         stars = 2 * i - 1
#         print(' ' * spaces + '*' * stars)
#
#
# if __name__ == '__main__':
#     main()


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# 定义二叉树类，可以包含插入、查找、前序遍历等方法
class BinaryTree:
    def __init__(self):
        self.root = None

    # 插入新节点
    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.data:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.data:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)
        # 如果value等于node.data，则不执行任何操作，假设树中不允许重复值

    # 查找特定值的节点
    def search(self, target):
        return self._search_recursive(self.root, target)

    def _search_recursive(self, node, target):
        if node is None or node.data == target:
            return node
        if target < node.data:
            return self._search_recursive(node.left, target)
        return self._search_recursive(node.right, target)

    # 前序遍历（根-左-右）
    def preorder_traversal(self):
        return self._preorder_traversal(self.root)

    def _preorder_traversal(self, node):
        if node is None:
            return []
        return [node.data] + self._preorder_traversal(node.left) + self._preorder_traversal(node.right)


# 示例用法
tree = BinaryTree()
values_to_insert = [4, 2, 6, 1, 3, 5, 7]
for value in values_to_insert:
    tree.insert(value)

# 打印前序遍历的结果
print(tree.preorder_traversal())

