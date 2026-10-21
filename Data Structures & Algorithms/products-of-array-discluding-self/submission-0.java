class Solution {
    public int[] productExceptSelf(int[] nums) {
         ArrayList<Integer> answer = new ArrayList<>();

        for (int i =0; i < nums.length;i++){
            int productSum = Math.multiplyExact(productLeft(nums,i),productRight(nums,i));

            answer.add(productSum);
        }

        int[] product = new int[answer.size()];
        for (int i = 0; i < answer.size(); i++) {
            product[i] = answer.get(i); // Unboxing Integer to int
        }

        return product;
    }

 public static int productLeft (int[] num, int k){

        int product =1;
        for (int i =k; i > 0; i--){
            int value = num[i-1];
            product = Math.multiplyExact(product,value);
        }

        return product;
    }


    public static int productRight (int[] num, int k){

        int product =1;
        for (int i =k; i < num.length -1; i++){
            int value = num[i+1];
            product = Math.multiplyExact(product,value);
        }
        return product;
    }























}  
