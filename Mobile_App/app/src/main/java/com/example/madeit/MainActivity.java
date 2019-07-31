package com.example.madeit;


import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.app.NotificationChannel;
import android.app.NotificationManager;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.net.wifi.WifiInfo;
import android.net.wifi.WifiManager;
import android.os.AsyncTask;
import android.os.Build;
import android.os.Bundle;
import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.NotificationCompat;
import androidx.core.app.NotificationManagerCompat;
import androidx.preference.Preference;
import androidx.preference.PreferenceManager;

import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.example.madeit.ui.login.LoginActivity;
import com.google.gson.JsonElement;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.lang.reflect.Array;
import java.net.Socket;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Calendar;
import java.util.Scanner;
import java.util.concurrent.TimeUnit;

import static android.provider.AlarmClock.EXTRA_MESSAGE;

public class MainActivity extends AppCompatActivity {

    Menu menu;
    SharedPreferences prefs;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        createNotificationChannel();

        final NotificationCompat.Builder builder = new NotificationCompat.Builder(this, "Noice")
                .setSmallIcon(R.drawable.ic_airport_shuttle_black_24dp)
                .setContentTitle("MadeIt")
                .setContentText("Much longer text that cannot fit one line...")
                .setStyle(new NotificationCompat.BigTextStyle()
                        .bigText("Much longer text that cannot fit one line..."))
                .setPriority(NotificationCompat.PRIORITY_DEFAULT);

        //check internet connection and get mac address
        final String address;
        WifiManager manager = (WifiManager) getApplicationContext().getSystemService(Context.WIFI_SERVICE);
        WifiInfo info = manager.getConnectionInfo();
        address = info.getMacAddress();
        //todo: flash error message to screen
        //**************
        prefs = PreferenceManager.getDefaultSharedPreferences(this);
        final Button Madeit = findViewById(R.id.MadeIt);
        Madeit.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {

                if (Madeit.getText() == getText(R.string.Login_Signup)) {

                    Intent intent2 = new Intent(MainActivity.this, LoginActivity.class);
                    intent2.putExtra("info", 0);
                    startActivityForResult(intent2, 1);

                } else {

                    //todo: make method to gather the json info

                    @SuppressLint("StaticFieldLeak") AsyncTask task = new AsyncTask() {
                        @Override
                        protected Void doInBackground(Object[] objects) {
                            JSONObject postData1 = new JSONObject();
                            JSONObject postData2 = new JSONObject();
                            try {
                                ////todo: pull from account info
                                postData1.put("FirstName", "Mike");
                                postData1.put("LastName", "Hunt");
                                postData1.put("UserName", "mmoore97");
                                postData1.put("Email", "mmoore97");
                                postData1.put("Password", "passwd");
                                postData1.put("Friends", "");
                                //todo: pull message from custom list
                                //todo: edit who will get message
                                postData1.put("connection", address);
                                postData1.put("timestamp", Calendar.getInstance().getTime().toString());

                                postData2.put("Handle", "1");
                                postData2.put("UserInfo", postData1.toString());
                                postData2.put("FriendEmail", "test@testmail.com");
                                String[] friends = {"test2@testmail.com", "test3@testmail.com"};
                                postData2.put("FriendEmailList", Arrays.toString(friends));
                                postData2.put("MadeItMessage", "ImDead");

                                Log.i("JSON", postData2.toString());

                                // startConnection("ec2-3-80-254-191.compute-1.amazonaws.com", 8080);
                                startConnection(prefs.getString("ip_config", "not_set"),
                                        Integer.parseInt(prefs.getString("port_config", "-1")));
                                sendMessage(postData2.toString());

                            } catch (JSONException e) {
                                e.printStackTrace();
                            } catch (IOException e) {
                                e.printStackTrace();
                            }
                            return null;
                        }
                    };


                    task.execute();

                    String message = "Info we want to send";

                    Log.i("Info", message);

                    // Toast.makeText(MainActivity.this, "MadeIt", Toast.LENGTH_SHORT).show();

                    NotificationManagerCompat notificationManager = NotificationManagerCompat.from(MainActivity.this);

                    // notificationId is a unique int for each notification that you must define
                    notificationManager.notify(24, builder.build());

                }
            }
        });
        //todo: create method to update app database as to who they can send messages to.

        //todo: create structures to send data to aws service.
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        MenuInflater inflater = getMenuInflater();
        inflater.inflate(R.menu.drop_menu, menu);

        this.menu = menu;

        return true;
    }


    @Override
    public boolean onOptionsItemSelected(@NonNull MenuItem item) {
        switch (item.getItemId()) {
            case R.id.settings:
                Intent intent = new Intent(this, SettingsActivity.class);
                startActivity(intent);
                return true;

            case R.id.custom_responses:
                updateMenuTitles();
                return true;

            case R.id.response1:
                Toast.makeText(this, getText(R.string.response_1), Toast.LENGTH_SHORT).show();
                return true;

            case R.id.response2:
                Toast.makeText(this, getText(R.string.response_2), Toast.LENGTH_SHORT).show();
                return true;

            case R.id.response3:
                Toast.makeText(this,  getText(R.string.response_3), Toast.LENGTH_SHORT).show();
                return true;

            case R.id.response4:
                Toast.makeText(this, getText(R.string.response_4), Toast.LENGTH_SHORT).show();
                return true;

            case R.id.response5:
                Toast.makeText(this, getText(R.string.response_5), Toast.LENGTH_SHORT).show();
                return true;
        }

        return super.onOptionsItemSelected(item);
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        if (requestCode == 1) {

            if (resultCode == RESULT_OK) {
                Button madeIt = findViewById(R.id.MadeIt);
                madeIt.setText(getText(R.string.MadeIT_Button));
            }
        }
    }
    private Socket clientSocket;
    private PrintWriter out;
    private BufferedReader in;

    public void startConnection(String ip, int port) throws IOException {
        clientSocket = new Socket(ip, port);
        out = new PrintWriter(clientSocket.getOutputStream(), true);
        in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
    }

    public String sendMessage(String msg) throws IOException {
        out.println(msg);
        String resp = in.readLine();
        return resp;
    }

    public void stopConnection() throws IOException {
        in.close();
        out.close();
        clientSocket.close();
    }

    private void updateMenuTitles() {

        MenuItem item1 = menu.findItem(R.id.response1);
        item1.setTitle(prefs.getString("response_1", "Empty"));
        MenuItem item2 = menu.findItem(R.id.response2);
        item2.setTitle(prefs.getString("response_2", "Empty"));
        MenuItem item3 = menu.findItem(R.id.response3);
        item3.setTitle(prefs.getString("response_3", "Empty"));
        MenuItem item4 = menu.findItem(R.id.response4);
        item4.setTitle(prefs.getString("response_4", "Empty"));
        MenuItem item5 = menu.findItem(R.id.response5);
        item5.setTitle(prefs.getString("response_5", "Empty"));
    }

    private void createNotificationChannel() {
        // Create the NotificationChannel, but only on API 26+ because
        // the NotificationChannel class is new and not in the support library
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            CharSequence name = "hey";
            String description = "dude";
            int importance = NotificationManager.IMPORTANCE_DEFAULT;
            NotificationChannel channel = new NotificationChannel("Noice", name, importance);
            channel.setDescription(description);
            // Register the channel with the system; you can't change the importance
            // or other notification behaviors after this
            NotificationManager notificationManager = getSystemService(NotificationManager.class);
            notificationManager.createNotificationChannel(channel);
        }
    }


}
