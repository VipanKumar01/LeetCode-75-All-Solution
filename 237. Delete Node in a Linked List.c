// Name = Vipan Kumar
// User Name = @VipanKumar01



void deleteNode(struct ListNode* node) {
    
    node->val=node->next->val;
    node->next=node->next->next;
    
    return node;
}

// --HappyCode--
