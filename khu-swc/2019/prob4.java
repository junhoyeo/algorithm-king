import java.io.*;
import java.util.*;
import java.util.stream.*;

class Main {
    public static <T> List<List<T>> split(List<T> list, int chunk) {
        List<List<T>> res = new ArrayList<>(chunk);
        int size = list.size();
        int chunkSize = (int) Math.ceil(((double) size) / chunk);
        int leftElements = size;
        int i = 0;
        while (i < size && chunk != 0) {
            res.add(list.subList(i, i + chunkSize));
            i += chunkSize;
            leftElements -= chunkSize;
            chunkSize = (int) Math.ceil(((double) leftElements) / --chunk);
        }
        return res;
    }

	public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        int num = Arrays.stream(line.split("\\s"))
        .map(String::trim).mapToInt(Integer::parseInt).toArray()[0];


        line = br.readLine();
        int[] array = Arrays.stream(line.split("\\s"))
            .map(String::trim).mapToInt(Integer::parseInt).toArray();

        List<Integer> arr = IntStream.of(array).boxed().collect(Collectors.toList());
        List<List<Integer>> chunks = split(arr, num);
        List<Integer> res = new ArrayList<Integer>();
        for (List<Integer> chunk : chunks) {
            // System.out.println(chunk.toString());
            res.add(Collections.min(chunk));
        }
        System.out.println(Collections.max(res));
	}
}
