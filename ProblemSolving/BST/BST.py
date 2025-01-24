# class BinarySearchTree:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
#     def add_child(self,data):
#         if data == self.data:
#             return
#         if data < self.data:
#             # add data to left subtree
#             if self.left:
#                 self.left.add_child(data)
#             else:
#                 self.left = BinarySearchTree(data)
#         if data > self.data:
#             #add data to right subtree
#             if self.right:
#                 self.right.add_child(data)
#             else:
#                 self.right = BinarySearchTree(data)
#
#     def in_order(self):
#         elements = []
#
#         if self.left:
#             elements += self.left.in_order()
#
#         elements.append(self.data)
#
#         if self.right:
#             elements += self.right.in_order()DS
#
#         return elements
#
#
