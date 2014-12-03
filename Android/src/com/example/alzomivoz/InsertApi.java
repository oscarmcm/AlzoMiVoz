package com.example.alzomivoz;

import java.io.File;

import org.apache.http.HttpResponse;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.util.EntityUtils;
import org.json.JSONObject;

import android.os.AsyncTask;
import android.util.Log;

public class InsertApi extends AsyncTask<String, Integer, Boolean> {

	protected Boolean doInBackground(String... params) {
		
		boolean resul = true;
		HttpClient httpClient = new DefaultHttpClient();
		HttpPost post = new HttpPost(
				"http://alzomivoz.herokuapp.com/denuncia/api/v1/posts/?format=json");
		post.setHeader("content-type", "application/json");
		
		try {
			// Construimos el objeto cliente en formato JSON
			JSONObject dato = new JSONObject();
			
			dato.put("titulo", params[0]);
			//dato.put("imagen", params[1]);
			dato.put("autor", params[1]);
			dato.put("lugar", params[2]);
			StringEntity entity = new StringEntity(dato.toString());
			post.setEntity(entity);

			HttpResponse resp = httpClient.execute(post);
			String respStr = EntityUtils.toString(resp.getEntity());

			if (!respStr.equals("true"))
				resul = false;
		} catch (Exception ex) {
			Log.e("ServicioRest", "Error!", ex);
			resul = false;
		}

		return resul;
	}

	protected void onPostExecute(Boolean result) {

		if (result) {
			System.out.println("Insertado OK.");
		}
	}	
}