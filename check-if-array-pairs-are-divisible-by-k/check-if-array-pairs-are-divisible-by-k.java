class Solution {
    public boolean canArrange(int[] arr, int k) {
        
        int freq[] = new int[k];
        for(int a : arr){
            int rmd=a%k;
            if(rmd<0)
                rmd+=k;
            freq[rmd]++;
            }
        
        for(int i=1;i<k;i++)
            if(freq[i]!=freq[k-i])
                return false;
        
        return freq[0]%2==0;   
            
        
    }
   
}