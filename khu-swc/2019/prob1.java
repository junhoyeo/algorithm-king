import java.io.*;
import java.util.Scanner;

class Main {
    public static int reverse(int value) {
        int resultNumber = 0;
        for (int i = value; i !=0; i /= 10) {
            resultNumber = resultNumber * 10 + i % 10;
        }
        return resultNumber;
    }

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		Scanner scn = new Scanner(System.in);
        int x = scn.nextInt();
        int y = scn.nextInt();
        System.out.println(Math.abs((x + y) - (reverse(x) + reverse(y))));
	}
}
