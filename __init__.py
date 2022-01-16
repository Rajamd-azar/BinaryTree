import BinTree

if __name__ == '__main__':
    mlist = input('Enter the list of value: ').split()
    mlist = [int(value) for value in mlist]

    btree = BinTree.BTree()
    for value in mlist:
        btree.add(value)
    
    print('Binary Sorted List: ',end='')
    btree.inorder()
