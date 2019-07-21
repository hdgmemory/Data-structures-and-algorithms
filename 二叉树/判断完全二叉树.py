###https://www.cnblogs.com/jiaxin359/p/9257960.html#_label7   二叉树

def is_complete_tree(head):
    """判断一个树是不是一个完全二叉树

    主要考虑这么两种情况：
    情况1：当前节点，有右节点，但是没有左节点，那么直接返回False
    情况2：当前节点，有左节点没有右节点，或者没有双节点，那么后面的节点都应该没有双节点
    """
    if head is None:
        return True

    is_last = False

    queue = [head]
    while(queue):

        node = queue.pop(0)

        left = node.left
        right = node.right

        if is_last and  (left or right): # 当最后一个节点已经出来的时候，后面的节点都应该没有子节点
                return False
        if not left and right:  # case1
            return False

        if left:
            queue.append(left)
        if right:
            queue.append(right)
        else:
            is_last = True
    return True
