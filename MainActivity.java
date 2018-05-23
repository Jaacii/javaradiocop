package com.example.jaci.javaradiocop;

import android.hardware.SensorManager;
import android.media.AudioManager;

import android.media.MediaPlayer;
import android.net.Uri;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.VideoView;
import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.widget.TextView;
import android.webkit.WebView;


public class MainActivity extends AppCompatActivity implements View.OnClickListener{

    boolean radioplaying = false;
    private TextView xText, yText, zText;
    private SensorManager SM;
    private Sensor mySensor;
    private Button radiobtn, forward, backward, stop, left, right;



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
// RADIO BUTTON INIT
        Button radiobtn = findViewById(R.id.radiobtn);
        radiobtn.setOnClickListener(this);

//Video/ LIVESTREAM START
        Uri uri = Uri.parse("http://abhiandroid-8fb4.kxcdn.com/ui/wp-content/uploads/2016/04/videoviewtestingvideo.mp4");
        VideoView videoView = findViewById(R.id.videoView) ;
        videoView.setVideoURI(uri);

        videoView.start();
		
		String test ="http://abhiandroid-8fb4.kxcdn.com/ui/wp-content/uploads/2016/04/videoviewtestingvideo.mp4";
		String url ="192.168.0.192:8081";
		WebView view = (WebView) this.findViewById(R.id.webview);
		view.getSettings().setJavaScriptEnabled(true);
		view.loadUrl(url);


//SensorManager init
        SM = (SensorManager)getSystemService(SENSOR_SERVICE);
        mySensor = SM.getDefaultSensor(Sensor.TYPE_ACCELEROMETER);
        SM.registerListener(this, mySensor, SensorManager.SENSOR_DELAY_NORMAL);


        xText = (TextView)findViewById(R.id.xText);
        yText = (TextView)findViewById(R.id.yText);
        zText = (TextView)findViewById(R.id.zText);

//Impromovement init  //später mit joystick ersetzen
        forward = (Button)findViewById(R.id.forward);
        left = (Button)findViewById(R.id.left);
        right = (Button)findViewById(R.id.right);
        stop = (Button)findViewById(R.id.stop);
        backward = (Button)findViewById(R.id.backward);

        forward.setOnClickListener(this);
        left.setOnClickListener(this);
        right.setOnClickListener(this);
        stop.setOnClickListener(this);
        backward.setOnClickListener(this);





    }
//KAMERA // accelerator
    @Override
    public void onAccuracyChanged (Sensor sensor, int accuracy) {
        //not in use
    }

    @Override
    public void onSensorChanged (SensorEvent event) {
        xText.setText("X: " + event.values[0]);
        yText.setText(" Y: " + event.values[1]);
        zText.setText(" Z: " + event.values[2]);

        //Hier Anbindung an CamMovement setzen für movement.



        //ViewVideo??

    }

//BUTTON  RADIO + MOVEMENT IMPRO  onlick
    @Override
    public void onClick (View v) {
    {
        switch (v.getId()) {
            case R.id.radiobtn:
               //RADIO

                //radio
                String url = "https://www.youtube.com/watch?v=EqPtz5qN7HM";
                MediaPlayer mediaPlayer = new MediaPlayer();
                mediaPlayer.setAudioStreamType(AudioManager.STREAM_MUSIC);
                mediaPlayer.setDataSource(url);
                mediaPlayer.prepare();
                //vermutlich nicht ideal das prepare etc hier zu haben

                if (radioplaying == false) {
                    radioplaying = true;
                    mediaPlayer.start();
                    //radio anschalten  RADIO KLASSE ODER PI
                } else {
                    radioplaying = false;
                    mediaPlayer.stop();
                    //radio ausschalten RADIO KLASSE ODER PI
                }



                break;


            case R.id.forward:
                //FORWARD

                break;

            case R.id.backward:
                //BACKWARD

                break;

            case R.id.left:
                //LEFT

                break;

            case R.id.stop:
                //STOP

                break;

            case R.id.right:
                //RIGHT

                break;



        }


    }

//wenns klappt späteres besseres MOVEMENT
    @Override
    public void onJoystickMoved (float xPercent, float yPercent, int  id) {
     /*   Log.d("Main Method", "X percent: " + xPercent + " Y percent: " + yPercent);

        switch(id){
            case R.id.joystickRight:
                Log.d("Right Joystick", "X percent: " + xPercent  " Y percent:: " + yPercent);
                break;
            case R.id.joystickLeft:
                Log.d("Left Joystick", "X percent: " + xPercent + " Y percent: " + yPercent);
                break;
        }*/


    }

}

}
