import com.github.arteam.simplejsonrpc.core.annotation.JsonRpcMethod;
import com.github.arteam.simplejsonrpc.core.annotation.JsonRpcParam;
import com.github.arteam.simplejsonrpc.core.annotation.JsonRpcService;

@JsonRpcService
public class StudentService {

    @JsonRpcMethod
    public String swapper(@JsonRpcParam("instring") String str){
        System.out.println("I was remotely called!");
        return "Pretend I swapped it :)";
    }
}
