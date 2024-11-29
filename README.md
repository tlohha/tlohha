package com.example.wastemanagementapp;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import java.io.OutputStreamWriter;
import java.net.HttpURLConnection;
import java.net.URL;

public class MainActivity extends AppCompatActivity {
@Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

// Initialize UI components
        EditText userIdEditText = findViewById(R.id.userIdEditText);
        EditText wasteTypeEditText = findViewById(R.id.wasteTypeEditText);
        Button submitButton = findViewById(R.id.submitButton);

// Set button click listener
        submitButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String userId = userIdEditText.getText().toString();
                String wasteType = wasteTypeEditText.getText().toString();

   if (userId.isEmpty() || wasteType.isEmpty()) {
                    Toast.makeText(MainActivity.this, "All fields are required", Toast.LENGTH_SHORT).show();
                } else {
                    sendRequestToServer(userId, wasteType);
                }
            }
        });
    }

  // Function to send data to the backend API
    private void sendRequestToServer(String userId, String wasteType) {
        new Thread(() -> {
            try {
                // API URL
                URL url = new URL("http://your-backend-url.com/api/create_request/");  // Replace with your backend URL

   // Open connection
     HttpURLConnection connection = (HttpURLConnection) url.openConnection();
         connection.setRequestMethod("POST");
         connection.setRequestProperty("Content-Type", "application/json");
            connection.setDoOutput(true);

  // Prepare JSON payload
  String jsonPayload = "{ \"user_id\": \"" + userId + "\", \"waste_type\": \"" + wasteType + "\" }";

   // Send the JSON payload
  OutputStreamWriter writer = new OutputStreamWriter(connection.getOutputStream());
  writer.write(jsonPayload);
  writer.flush();
  writer.close();

   // Get the response code
  int responseCode = connection.getResponseCode();
   if (responseCode == HttpURLConnection.HTTP_OK) {
   runOnUiThread(() -> Toast.makeText(MainActivity.this, "Request Sent Successfully!", Toast.LENGTH_SHORT).show());
   } else {
   runOnUiThread(() -> Toast.makeText(MainActivity.this, "Failed to send request!", Toast.LENGTH_SHORT).show());
   }

  connection.disconnect();
  } catch (Exception e) {
  e.printStackTrace();
runOnUiThread(() -> Toast.makeText(MainActivity.this, "Error: " + e.getMessage(), Toast.LENGTH_SHORT).show());
            }
        }).start();
    }
}
