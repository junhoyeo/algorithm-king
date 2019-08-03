import java.io.*;
import java.util.HashMap;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        char[] keys = { '1', 'I', 'l', '|' };
        HashMap<Character, Integer> counts = new HashMap<Character, Integer>();
        for (Character k : keys) {
            counts.put(k, 0);
        }
        Character temp;
        for (int i = 0; i < input.length(); i++) {
            temp = input.charAt(i);
            for (Character k : keys) {
                if (k == temp) {
                    counts.put(k, counts.get(k) + 1);
                }
            }
        }
        for (Character k : keys) {
            System.out.println(counts.get(k));
        }
    }
}
