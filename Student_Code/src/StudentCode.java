import java.util.Map;

public class StudentCode {


    public static String student_entrypoint(Double Measured_Bandwidth, Double Previous_Throughput, Map Buffer_Occupancy, Map Available_Bitrates, Double Video_Time, Map Chunk, Double Rebuffering_Time, String Preferred_Bitrate){
        System.out.println("I was called!");
        return "5000000";
    }

}
