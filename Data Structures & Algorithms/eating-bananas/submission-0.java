class Solution {
    public int minEatingSpeed(int[] piles, int h) {
         Arrays.sort(piles);
        int left = 1;
        int right = piles[piles.length-1];
        int minSpeed = right;


        while (left <= right){
            int mid = (left + right)/2;
            int hours =0;

            for (int p:piles ){
                hours += (p + mid - 1) / mid;
            }

            if (hours <= h){
                minSpeed = Math.min(minSpeed,mid);
                right = mid -1;
            } else {
                left = mid+1;
            }
        }


        return minSpeed;
    }
}
