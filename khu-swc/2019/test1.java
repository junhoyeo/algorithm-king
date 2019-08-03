import java.io.*;

class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        String[] words = input.split("\\s");
        Integer res = 0;

        for (String wo : words) {
            if (wo.isEmpty())
                continue;
            res++;
        }
        System.out.println(res);
    }
}
