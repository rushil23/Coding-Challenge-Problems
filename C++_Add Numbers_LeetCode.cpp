/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    int r,sum;
    void addRemaining(ListNode* l, ListNode* rem, int r){
        cout<<"\nAdd Remaining"<<endl;
        while (rem!=NULL){
            sum = rem->val+r;
            cout<<sum;
            ListNode* n = new ListNode(sum%10);
            l->next=n;
            l=l->next;
            rem = rem->next;
            r= sum / 10;
        }
        if (r>0){
            ListNode* n = new ListNode(r);
            l->next=n;
        }
        
    }
    
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        
        ListNode* lh = new ListNode(0);
        ListNode* l=lh;
        int status = 0;
        
        cout<<sum<<" "<<l1->val<<l2->val<<r;
        sum = l1->val+l2->val+r;
        l->val = sum % 10;
        cout<<"\n"<<sum/10;
        r = sum / 10;
        
        l1=l1->next;
        l2=l2->next;
        
        while (true){
            
            if (l1 == NULL && l2 == NULL) {
                if (r>0){
                    ListNode* n = new ListNode(r);
                    l->next = n;
                }
                break;
            }
            else if (l1==NULL) {

                status = 1;
                break;
            }
            
            else if (l2==NULL) {
        
                status = 2;
                break;
            }
            
            sum = l1->val+l2->val+r;
            cout<<"SUM: "<<sum<<endl;
            ListNode* n = new ListNode(sum % 10);
            r = sum / 10;
            l->next=n;
            l=l->next;
            
            l1 = l1->next;
            l2 = l2->next;
        }
        
        if (status==1) addRemaining(l,l2,r);
        if (status==2) addRemaining(l,l1,r);
        
        return lh;
        
    }
};
