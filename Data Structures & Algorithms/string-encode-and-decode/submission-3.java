class Solution {

    public String encode(List<String> strs) {
 StringBuilder encoded = new StringBuilder();

        for (int i =0; i < strs.size(); i ++){
            encoded.append(strs.get(i)).append('~');
        }

        return encoded.toString();
    }

    public List<String> decode(String str) {
    List<String> decoded = new ArrayList<>();
            StringBuilder word = new StringBuilder();
            for (int i =0; i < str.length(); i++){

                char c = str.charAt(i);
                if (c != '~'){
                    word.append(c);
                } else {
                    decoded.add(word.toString());
                    word = new StringBuilder();
                }
            }




            return decoded;
    }
}
