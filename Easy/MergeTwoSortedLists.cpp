/*
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by
splicing together the nodes of the first two lists.

** Return the head of the merged linked list **

Example 1:
    Input: list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]

Example 2:
    Input: list1 = [], list2 = []
    Output: []

Example 3:
    Input: list1 = [], list2 = [0]
    Output: [0]
*/

 // Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};


class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* curr1 = list1;
        ListNode* curr2 = list2;
        ListNode* front = list1;
        if (list1 == nullptr) {
            return list2;
        }
        else if (list2 == nullptr) {
            return list1;
        }
        if (curr1->val > curr2->val) {
            curr1 = list2;
            curr2 = list1;
            front = list2;
        }
        while (curr1 != nullptr) {
            if (curr2 == nullptr) {
                break;
            }
            if(curr1->next == nullptr) {
                curr1->next = curr2;
                break;
            }
            else if (curr1->next->val >= curr2->val) {
                ListNode* curr = curr2->next;
                curr2->next = curr1->next;
                curr1->next = curr2;
                curr2 = curr;
                curr1 = curr1->next;
            }
            else {
                curr1 = curr1->next;
            }
        }
        return front;
    }
};