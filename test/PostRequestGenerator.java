import org.apache.http.client.HttpClient;
import java.io.File;
import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.HttpVersion;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.mime.MultipartEntity;
import org.apache.http.entity.mime.content.ContentBody;
import org.apache.http.entity.mime.content.FileBody;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.params.CoreProtocolPNames;
import org.apache.http.util.EntityUtils;

public class PostRequestGenerator {
	
	public String sendPostRequest(String pathtofile) throws Exception {
		HttpClient httpclient = new DefaultHttpClient();
	    httpclient.getParams().setParameter(CoreProtocolPNames.PROTOCOL_VERSION, HttpVersion.HTTP_1_1);

	    HttpPost httppost = new HttpPost("http://localhost/imageOpener.py");
	    File file = new File(pathtofile);

	    MultipartEntity mpEntity = new MultipartEntity();
	    mpEntity.addPart("File", new FileBody(file));
	    httppost.setEntity(mpEntity);
	    


	    httppost.setEntity(mpEntity);
	    HttpResponse response = null;
	    System.out.println("executing request " + httppost.getRequestLine());
	    boolean connection = false;
	    while(connection == false) {
	    	try {
	    		response = httpclient.execute(httppost);
	    		connection = true;
	    	}
	    	catch(Exception e) {
	    		connection = false;
	    		Thread.sleep(10);
	    	}
	    		
	    }
	    
	    HttpEntity resEntity = response.getEntity();
	    String jsonstring = null;
	    System.out.println(response.getStatusLine());
	    if (resEntity != null) {
	      jsonstring = (EntityUtils.toString(resEntity));
	    }
	    if (resEntity != null) {
	      resEntity.consumeContent();
	    }

	    httpclient.getConnectionManager().shutdown();
	    return jsonstring;
	}
	
	public static void main(String[] args) throws Exception {
	    PostRequestGenerator ts = new PostRequestGenerator();
	    ts.sendPostRequest("/home/chitransh/Documents/Projects/birds/TestData/blue-winged-warbler.jpg");
	  }
	}