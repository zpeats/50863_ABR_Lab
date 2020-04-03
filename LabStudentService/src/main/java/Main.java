import com.github.arteam.simplejsonrpc.server.JsonRpcServer;

import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;

public class Main {

    public static void main( String args[] ){
        System.out.println("hello world!");

        StudentService studentService = new StudentService();
        JsonRpcServer rpcServer = new JsonRpcServer();

        ServerSocket server = null;
        Socket socket = null;
        BufferedReader input = null;
        PrintWriter output = null;
        try {
            server = new ServerSocket(6000);
            socket = server.accept();
            System.out.println("socket made");
            output = new PrintWriter(socket.getOutputStream(), true);
            input = new BufferedReader(new InputStreamReader(socket.getInputStream()));
        }
        catch (Exception e){
            System.out.println("Error setting up socket:" + e);
            return;
        }


        System.out.println("now attempting to read from tcp socket");
        String json = "";
        String inline = null;
        while(true) {
            try {
                inline = input.readLine();
                System.out.println(inline);
            } catch (IOException e) {
                System.out.println("big frickin error" + e);
            }

            json = inline.substring(1);
            System.out.println("new json is" + json);
            String retjson = rpcServer.handle(json, studentService);

            retjson = (char) 0x1E + retjson;
            output.println(retjson);
        }

    }
}
