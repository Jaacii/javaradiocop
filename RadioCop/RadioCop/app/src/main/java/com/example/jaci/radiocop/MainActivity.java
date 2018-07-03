package com.example.jaci.radiocop;


import android.support.annotation.NonNull;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.ImageButton;
import android.widget.Toast;

import org.eclipse.paho.client.mqttv3.MqttClient;
import org.eclipse.paho.android.service.MqttAndroidClient;
import org.eclipse.paho.client.mqttv3.IMqttActionListener;
import org.eclipse.paho.client.mqttv3.IMqttToken;
import org.eclipse.paho.client.mqttv3.MqttException;
import org.eclipse.paho.client.mqttv3.persist.MemoryPersistence;



public class MainActivity extends AppCompatActivity implements View.OnClickListener
{

    boolean radioplaying = false;
    private static WebView webview ;
    String url = "http://192.168.0.192:8081";
    String url2 ="https://www.google.com/search?q=androidstudio+layout+&ie=utf-8&oe=utf-8&client=firefox-b-ab";
    private MqttAndroidClient client;
    private final MemoryPersistence persistence = new MemoryPersistence();
    //String brokerurl = "broker.mqttdashboard.com"
    //String topic = "haw/dmi/mt/its/ss18"
    boolean connected = false;
    String topic = "haw/dmi/mt/its/ss18/radiocop";
    MqttAndroidClient clientt;

    @Override
    protected void onCreate (Bundle savedInstanceState){
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);



        //MQTT CONNECT start

        String clientId = MqttClient.generateClientId();//"clientId-2EgBVg0z70"; //MqttClient.generateClientId();
         clientt =
                new MqttAndroidClient(MainActivity.this, "tcp://broker.mqttdashboard.com:1883",
                        clientId, persistence);



        try {
            IMqttToken token = clientt.connect();
            token.setActionCallback(new IMqttActionListener() {
                @Override
                public void onSuccess(IMqttToken asyncActionToken) {
                   Toast.makeText(MainActivity.this, "connected", Toast.LENGTH_LONG).show();

                }

                @Override
                public void onFailure(IMqttToken asyncActionToken, Throwable exception) {
                    Toast.makeText(MainActivity.this, "not connected", Toast.LENGTH_LONG).show();


                }
            });
        } catch (MqttException e) {
            e.printStackTrace();
        }



        ////MQTT end



        // BUTTON + WEBVIEW INIT
        ImageButton radiobtn = (ImageButton)findViewById(R.id.radiobtn);
        radiobtn.setOnClickListener(this);

        ImageButton videobtn = (ImageButton)findViewById(R.id.videobtn);
        videobtn.setOnClickListener(this);

        ImageButton forward =(ImageButton) findViewById(R.id.forward);
        ImageButton backward =(ImageButton) findViewById(R.id.backward);
        ImageButton left =(ImageButton) findViewById(R.id.left);
        ImageButton right =(ImageButton) findViewById(R.id.right);
        ImageButton stop =(ImageButton) findViewById(R.id.stop);
        ImageButton camR =(ImageButton) findViewById(R.id.CamR);
        ImageButton camL =(ImageButton) findViewById(R.id.CamL);





        //Video/ LIVESTREAM START       falls webview nicht klappt
        /*Uri uri = Uri.parse("192:168:0:192.8081");
        VideoView videoView = findViewById(R.id.videoView);
        videoView.setVideoURI(uri);

        videoView.start();*/
        webview =(WebView) findViewById(R.id.webview);
        webview();

    }





    public void webview() {
        //WebView init
        webview.setWebViewClient(new WebViewClient());
        webview.getSettings().getJavaScriptEnabled();
        webview.loadUrl(url);
    }




    //BUTTON ONCLICK
    @Override
    public void onClick(View v) {
        switch (v.getId()) {
            case R.id.radiobtn:
                radiotoggled();
                break;


            case R.id.videobtn:
                videoaction();

                break;




            case R.id.forward:
                //FORWARD

                    publishMessage(clientt, "forward", 1, topic );

                break;

            case R.id.backward:
                //BACKWARD
                publishMessage(clientt, "back", 1, topic );
                break;

            case R.id.left:
                //LEFT
                publishMessage(clientt, "links", 1, topic );

                break;

            case R.id.stop:
                //STOP

                    publishMessage(clientt, "stop", 1, topic );

                break;

            case R.id.right:
                //RIGHT

                    publishMessage(clientt, "rechts", 1, topic );

                break;
            case R.id.CamL:
                //CAMERA LEFT

                    publishMessage(clientt, "CamL", 1, topic );

                break;
            case R.id.CamR:
                //CAMERA RIGHT

                    publishMessage(clientt, "CamR", 1, topic );

                break;

        }
    }

    public void publishMessage(@NonNull MqttAndroidClient client,@NonNull String msg, int qos, @NonNull String topic) {

        String message = msg;
        byte[] encodedPayload = new byte[0];
        try {
           // encodedPayload = payload.getBytes("UTF-8");
           // MqttMessage message = new MqttMessage(encodedPayload);
            client.publish(topic, message.getBytes(),qos,false);
        } catch (MqttException e) {
            e.printStackTrace();
        }
    }


    public void videoaction() {
        //reload url
        webview.loadUrl(url);
    }


    public void radiotoggled() {
        if (!radioplaying) {
            radioplaying = true;
            publishMessage(clientt, "radioAn", 1, topic );


        } else {
            radioplaying = false;
            publishMessage(clientt, "RadioAus", 1, topic );
        }
    }


}
