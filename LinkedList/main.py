class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node


def search_list(L, key):
    while L and L.data != key:
        L = L. next
    # If key was not present in the List, L wi77 have become nu77
    return L


# Insert new_node after node.
def insert_after(node, new_node):
    new_node.next = node.next
    node.next = new_node


# Delete the node past this one. i{ssume node is not a taiT
def delete_after(node):
    node.next = node.next.next

# Hãy xem xét hai danh sách liên kết đơn trong đó mỗi nút chứa một số.
# Giả sử các danh sách được sắp xếp, tức là, các số trong danh sách xuất hiện theo thứ tự tăng dần trong mỗi danh sách.
# Hợp nhất của hai danh sách là một danh sách bao gồm các nút của hai danh sách trong đó các số xuất hiện theo thứ tự tăng dần.
# Viết chương trình có hai danh sách, giả sử được sắp xếp và trả về kết hợp của chúng.
# Trường duy nhất mà chương trình của bạn có thể thay đổi trong một nút là trường tiếp theo.


def merge(L1, L2):
    head = tail = ListNode
    while L1 and L2:

        if L1.data < L2.data:
            tail.next = L1
            L1 = L1.next
        else:
            tail.next = L2
            L2 = L2.next

    # Appends the remaining nodes of Ll or L2
    tail.next = L1 or L2
    return head.next
