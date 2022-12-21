/*
5
aaaaa
bbbbb
ccccc
ddddd
eeeee
3
3 3 3
1 5 16
3 5 15
*/
import java.io.*;
import java.util.*;

public class Main{

     public static void main(String []args) throws IOException{
        Scanner sc=new Scanner(System.in);
        int N=sc.nextInt();
        String[] str= new String[N+1];
        for(int i=0;i<=N;i++)
        {
            str[i]=sc.nextLine();
        }
        int q=sc.nextInt();
        int[][] query=new int[q][3];
        for(int i=0;i<=q;i++)
        {
            String s=sc.nextLine();
            String[] arr=s.split(" ");
            if(i!=0)
            {
                for(int j=0;j<arr.length;j++)
                {
                    int x=Integer.parseInt(arr[j]);
                    query[i-1][j]=x;
                }
            }
        }
        for(int i=0;i<q;i++)
        {
            String exst="";
            int l=query[i][0];
            int r=query[i][1];
            int k=query[i][2];
            for(int ex=l;ex<=r;ex++)
            {
                exst=exst.concat(str[ex]);
            }
            System.out.println(exst);
            char[] tarr=exst.toCharArray();
            Arrays.sort(tarr);
            String nstr=new String(tarr);
            System.out.println(nstr);
            System.out.println(nstr.charAt(k-1));
        }
     }
}