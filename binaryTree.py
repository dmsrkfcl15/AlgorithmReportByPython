class Node:
    def __init__(self, value):
        self.value = value
    value = None
    left = None
    right = None
    parent = None

def treeInsert(node, value):
    if node == None:
        return Node(value)
    else:
        if node.value > value:
            node.left = treeInsert(node.left, value)
            node.left.parent = node
        else:
            node.right = treeInsert(node.right, value)
            node.right.parent = node
        return node
    
def treeSearch(node, value):
    if node == None:
        return False
    elif node.value == value:
        return node
    elif node.value < value:
        return treeSearch(node.right, value)
    elif node.value > value:
        return treeSearch(node.left, value)

def treeDelete(deleteNode, parentNode, rootNode):
    if parentNode == None: #삭제하려는 노드가 루트 노드인 경우
        rootNode = None
    
    if parentNode.left == deleteNode:
        parentNode.left = deleteForNode(deleteNode)
        if parentNode.left != None:
            parentNode.left.parent = parentNode
    else:
        parentNode.right = deleteForNode(deleteNode)
        if parentNode.right != None:
            parentNode.right.parent = parentNode 
           

def deleteForNode(deleteNode):
    if deleteNode.left == None and deleteNode.right == None:
        return None
    elif deleteNode.left == None and deleteNode.right != None:
        return deleteNode.right
    elif deleteNode.left != None and deleteNode.right == None:
        return deleteNode.left
    else:
        s = deleteNode.right
        while s.left != None:
            s = s.left

        #오른쪽 서브 트리에서 가장 작은 원소가 들어있는 노드의 부모와 자녀를 연결
        if s.right != None:
            s.right.parent = s.parent 
        s.parent.left = s.right 

        #오른쪽 서브 트리에서 가장 작은 원소가 들어있는 노드를 deleteNode의 위치로 이동
        s.left, s.right = deleteNode.left, deleteNode.right 
        return s



#테스트
rootNode = None
for i in [32, 12, 9, 11, 47, 38, 62, 51]:#리스트에 있는 숫자를 삽입
    rootNode = treeInsert(rootNode, i)

    #           32
    #     12          47
    #  9          38      62  
    #    11             51

result = treeSearch(rootNode, 55) #없는 숫자를 검색할 경우 False 출력
print("55 검색:", result)
if result != False:
    print("55 검색 value값 확인:", result.value)

result = treeSearch(rootNode, 47) #있는 숫자를 검색할 경우 해당 Node객체 정보 출력
print("47 검색:", result)
if result != False:
    print("있는 숫자 검색 후 value값 확인:", result.value) #벨류값이 같은지 확인

result = treeSearch(rootNode, 9)
print("9 검색:", result)
if result != False:
    print("있는 숫자 검색 후 value값 확인:", result.value)

result = treeSearch(rootNode, 11)
print("11 검색:", result)
if result != False:
    print("있는 숫자 검색 후 value값 확인:", result.value)

result = treeSearch(rootNode, 47)#자식 노드가 2개인 경우 삭제되는지 확인
print("삭제 노드:", result.value, "부모 노드:", result.parent.value)
treeDelete(result, result.parent, rootNode)
result = treeSearch(rootNode, 47)
print("삭제 후 47 검색:", result)
if result != False:
    print(result.value)

result = treeSearch(rootNode, 9)#자식 노드가 1개인 경우 삭제되는지 확인
print("삭제 노드:", result.value, "부모 노드:", result.parent.value)
treeDelete(result, result.parent, rootNode)
result = treeSearch(rootNode, 9)
print("삭제 후 9 검색:", result)
if result != False:
    print(result.value)

result = treeSearch(rootNode, 11)#자식 노드가 0개인 경우 삭제되는지 확인
print("삭제 노드:", result.value, "부모 노드:", result.parent.value)
treeDelete(result, result.parent, rootNode)
result = treeSearch(rootNode, 11)
print("삭제 후 11 검색:", result)
if result != False:
    print(result.value)


