package com.example.alzomivoz;

import java.io.File;
import java.io.IOException;

import org.apache.http.entity.mime.MultipartEntity;

import android.app.Activity;
import android.app.ProgressDialog;
import android.content.ContentValues;
import android.content.Intent;
import android.database.Cursor;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.net.Uri;
import android.os.AsyncTask;
import android.os.Bundle;
import android.provider.MediaStore;
import android.util.Log;
import android.view.Display;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageButton;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends Activity {

	final static int RESULT_LOAD_IMAGE = 1;

	Uri imageUri = null;
	static TextView imageDetails = null;
	public static ImageView showImg = null;
	MainActivity CameraActivity = null;

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
		CameraActivity = this;

		final EditText title = (EditText) findViewById(R.id.etTitle);
		final EditText author = (EditText) findViewById(R.id.etAuthor);
		final EditText site = (EditText) findViewById(R.id.etLugar);
		
		showImg = (ImageView) findViewById(R.id.showImg);
		
		final ImageButton photo = (ImageButton) findViewById(R.id.btPhoto);
		final Button send = (Button) findViewById(R.id.btSend);

		photo.setOnClickListener(new View.OnClickListener() {
			public void onClick(View v) {
				Intent i = new Intent(
						Intent.ACTION_PICK,
						android.provider.MediaStore.Images.Media.EXTERNAL_CONTENT_URI);
				startActivityForResult(i, RESULT_LOAD_IMAGE);

			}
		});
		
		send.setOnClickListener(new View.OnClickListener() {
			@Override
			public void onClick(View v) {
				String titulo = title.getText().toString();
				String autor = author.getText().toString();
				String lugar = site.getText().toString();
				if (titulo.matches("") || lugar.matches("")) {
					Toast.makeText(getApplicationContext(), "Complete el Formulario", Toast.LENGTH_LONG).show();
				}				
				else {
					InsertApi tarea = new InsertApi();
					tarea.execute(titulo, autor, lugar);
					Toast.makeText(getApplicationContext(), "Denuncia reportada", Toast.LENGTH_LONG).show();
				}
			}
		});

	}
	
	@Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
    	super.onActivityResult(requestCode, resultCode, data);
    	
		if (requestCode == RESULT_LOAD_IMAGE && resultCode == RESULT_OK && null != data) {
			Uri selectedImage = data.getData();
			String[] filePathColumn = { MediaStore.Images.Media.DATA };

			Cursor cursor = getContentResolver().query(selectedImage,
					filePathColumn, null, null, null);
			cursor.moveToFirst();

			int columnIndex = cursor.getColumnIndex(filePathColumn[0]);
			String picturePath = cursor.getString(columnIndex);
			cursor.close();
			
			showImg.setImageBitmap(BitmapFactory.decodeFile(picturePath));
			
			MultipartEntity entity = new MultipartEntity();
		
		}
    
    
    }

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		getMenuInflater().inflate(R.menu.main, menu);
		return true;
	}

	@Override
	public boolean onOptionsItemSelected(MenuItem item) {
		int id = item.getItemId();
		if (id == R.id.action_settings) {
			return true;
		}
		return super.onOptionsItemSelected(item);
	}

}
