/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
import java.io.*;
import java.util.*;
public class Main
{
	public static void main(String[] args) throws IOException{
		System.out.println("Hello World");
		Scanner sc=new Scanner(System.in);
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		
		int n=sc.nextInt();
		int[] arr=new int[n];
		String[] s= br.readLine().trim().split(" ");
		
		sc.close();
		for(int i=0;i<n;i++)
		{
		    arr[i]=Integer.parseInt(s[i]);
		    System.out.println(arr[i]);
		}
	}
}
