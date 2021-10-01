class StockSpanner {
    Stack<int[]> stack;
    
    public StockSpanner() {
        stack = new Stack();
    }
    
    public int next(int price) {
        int span = 1;
        while (!stack.isEmpty() && stack.peek()[0] <= price) {
            int[] curr = stack.pop();
            span += curr[1];
        }
        stack.push(new int[] {price, span});
        return span;
    }
}