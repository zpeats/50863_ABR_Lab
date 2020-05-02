import java.io.BufferedReader;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.InputStreamReader;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Map;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;


public class Main {

    public static void main( String args[] ){

        int maxThreads = 50;
        int port = 6000;
        try {
            ServerSocket socket = new ServerSocket(port);
            Socket client = socket.accept();
            //start it, this method doesn't block

            BufferedReader dis = new BufferedReader(new InputStreamReader(client.getInputStream()));
            DataOutputStream dos = new DataOutputStream(client.getOutputStream());
            //System.out.println("server started!");

            while (true) {
                String message = (String)dis.readLine();

                //System.out.println(message);

                JSONParser parser = new JSONParser();

                Object obj = parser.parse(message);
                JSONObject simArgs = (JSONObject)obj;

                if((Long)simArgs.get("exit") != 0){
                    //System.out.println("requested to exit");
                    client.close();
                    return;
                }

                double m_band = ((Number)simArgs.get("Measured Bandwidth")).doubleValue();
                double prev_throughput = ((Number)simArgs.get("Previous Throughput")).doubleValue();
                Map buff_occ = (Map)simArgs.get("Buffer Occupancy");
                Map av_bitrates = (Map)simArgs.get("Available Bitrates");
                double vid_time = ((Number)simArgs.get("Video Time")).doubleValue();
                Map chunk_arg = (Map)simArgs.get("Chunk");
                double rebuf_time = ((Number)simArgs.get("Rebuffering Time")).doubleValue();
                String pref_bitrate = (String)simArgs.get("Preferred Bitrate");

                String chosen_bitrate = StudentCode.student_entrypoint(m_band,prev_throughput,buff_occ,av_bitrates,vid_time,chunk_arg,rebuf_time,pref_bitrate);

                JSONObject payload = new JSONObject();
                payload.put("bitrate", chosen_bitrate);

                //System.out.println(payload);

                String paystr = payload.toJSONString() + "\n";



                dos.writeBytes(paystr);
                dos.flush();



            }


        }
        catch (Exception e){
            System.out.println("something went wrong!" + e);
        }


    }
}
