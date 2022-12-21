//product of two numbers only when both numbers are grater than zero.
public class Main
{
	public static void main(String[] args) 
	{
		static Scanner sc=new Scanner(System.in);
        static int B=sc.nextInt();
        static int H=sc.nextInt();
        static boolean flag=true;
        static{
                try
                {
                    if( B<=0 || H<=0)
                    {
                        flag=false;
                        throw new Exception("Breadth and height must be positive");
                    }
                    else
                    {
                        if(flag)
                        {
                            System.out.printl(B*H);
                        }
                    }
                    
                }
                catch(Exception e)
                {
                    System.out.println(e);
                    
                }
            
        }
	}
}
