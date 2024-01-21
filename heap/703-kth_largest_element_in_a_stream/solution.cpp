class KthLargest {
// Solution explaination:
// Same as the python solution, but wanted to try implementing the same in cpp

public:
    int k;
    priority_queue <int, vector<int>, greater<int>> pq;
    KthLargest(int k, vector<int>& nums) {
        this->k = k;
        for (int i : nums) {
            add(i);
        }
    }
    
    int add(int val) {
        if (this->pq.size() < this->k) {
            this->pq.push(val);
            return this->pq.top();
        }
        if (val > this->pq.top()) {
            this->pq.pop();
            this->pq.push(val);
        }
        return this->pq.top();
    }
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */