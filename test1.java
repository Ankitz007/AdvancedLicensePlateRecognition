import java.io.*;
 
class test1{
public static void main(String a[]){
try{
Process p = Runtime.getRuntime().exec("bash run.sh -i samples/test -o /home/ankitz/Desktop/output -c /home/ankitz/Desktop/output/res.csv");
BufferedReader in = new BufferedReader(new InputStreamReader(p.getInputStream()));
String ret = new String();
while((ret=in.readLine())!=null){
   System.out.println(ret);
}
//System.out.println("value is : "+ret);
}catch(Exception e){}
}
}
