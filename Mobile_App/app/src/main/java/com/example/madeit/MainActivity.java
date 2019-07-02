package com.example.madeit;


import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

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

import static android.provider.AlarmClock.EXTRA_MESSAGE;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        final Button Madeit = findViewById(R.id.MadeIt);
        Madeit.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {

                //todo: make method to gather the json info

                String message = "Info we want to send";

                Log.i("Info", message);

                Toast.makeText(MainActivity.this, "The button works!", Toast.LENGTH_SHORT).show();
            }
        });
        //todo: create method to update app database as to who they can send messages to.

        //todo: create structures to send data to aws service.
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        MenuInflater inflater = getMenuInflater();
        inflater.inflate(R.menu.drop_menu, menu);

        return true;
    }

    //todo: create settings menu and seperate settings screen
    @Override
    public boolean onOptionsItemSelected(@NonNull MenuItem item) {
        switch (item.getItemId()) {
            case R.id.settings:
                Intent intent = new Intent(this, SettingsActivity.class);
                startActivity(intent);
                Toast.makeText(this, "Settings Menu", Toast.LENGTH_SHORT).show();
                return true;

            case R.id.item2:
                Intent intent2 = new Intent(this, LoginActivity.class);
                startActivity(intent2);
                Toast.makeText(this, "Login", Toast.LENGTH_SHORT).show();
                return true;

            case R.id.item3:
                Toast.makeText(this, "Item 3", Toast.LENGTH_SHORT).show();
                return true;

            case R.id.sub_item1:
                Toast.makeText(this, "Sub 1", Toast.LENGTH_SHORT).show();
                return true;

            case R.id.sub_item2:
                Toast.makeText(this, "Sub 2", Toast.LENGTH_SHORT).show();
                return true;

        }

        return super.onOptionsItemSelected(item);
    }
}
