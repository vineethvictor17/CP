class Solution {
     void reverse(char[] str,int i,int j){
            for(;i<j;i++,j--){
                char temp=str[i];
                str[i]=str[j];
                str[j]=temp;
            }
     }
         
    public String reverseWords(String s) {
        if(s==null || s.length()==0)
            return s;
        
        char[] str=s.toCharArray();
        int i=0;
        int j=0;
        while(j<=str.length ){
            if(j == str.length || str[j] == ' '){
            reverse(str,i,j-1);
            i=j+1;
            }
              j++;
        }
      
       
            
        
         return new String(str);
        
    }
}
