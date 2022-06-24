import java.io.FileWriter;
import java.io.IOException;

public class Main {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		try {
			FileWriter RandoOutput = new FileWriter ("Randomizer.json");
			RandoOutput.write("Penis");
			RandoOutput.close();
			System.out.println("Success!");
	} catch (IOException e) {
		System.out.println("An error occurred.");
		e.printStackTrace();
	}
}
}
