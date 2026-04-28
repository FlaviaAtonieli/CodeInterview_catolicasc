# prev -> Nó anterior
# curr -> Nó atual
# next_node -> Guarda o próximo nó antes de perder a referência

class Solution(object):
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


## TEST 01
print('Teste 01:')

head = ListNode(1,
        ListNode(2,
        ListNode(3,
        ListNode(4,
        ListNode(5)))))

print('Lista original:')
print('1, 2, 3, 4, 5')

sol = Solution()
new_head = sol.reverseList(head)

result = []
curr = new_head

while curr:
    result.append(str(curr.val))
    curr = curr.next

print('Lista invertida:')
print(', '.join(result))


## TEST 02
print('\nTeste 02:')

head = ListNode(1,
        ListNode(1,
        ListNode(2,
        ListNode(3,
        ListNode(4,
        ListNode(4,
        ListNode(5)))))))

print('Lista original:')
print('1, 1, 2, 3, 4, 4, 5')

sol = Solution()
new_head = sol.reverseList(head)

result = []
curr = new_head

while curr:
    result.append(str(curr.val))
    curr = curr.next

print('Lista invertida:')
print(', '.join(result))
