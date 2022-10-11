// I am Already solve that in Python But I study about DSA of C it is Same As Python So I am Posting of that Code 

struct ListNode* middleNode(struct ListNode* head){
    struct ListNode* hare = head;   
    // 2X Faster 
    struct ListNode* tort = head;  
    // 1X faster
    
    while (hare != NULL)
	{
		if (hare->next != NULL)
		{
			hare = hare->next->next;
			tort = tort->next;
		}
		else hare = hare->next;
	}

	return tort;
}

// --HappyCode--
