package Editrans;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.URL;
import java.net.URLConnection;

public class EdiTrans {


	public static void main(String[] args) throws IOException {
		
		//Declaración de las variables a utilizar en el programa
		int numero_justificantes=150;
		String palabra_a_buscar="Justificante: <strong>";
		URL test = new URL("https://www2.agenciatributaria.gob.es/L/inwinvoc/es.aeat.dit.adu.adht.editran.NumRefEditran?mod=347");
		String inputLine;
		
		//Obtenemos el código fuente de la página, y mediante una expresión regular nos quedaremos con los dígitos necesarios del Editrans
		for (int i=1; i<=numero_justificantes;i++) {
		URLConnection uc = test.openConnection();
		uc.addRequestProperty("User-Agent", "Mozilla/4.0");
		BufferedReader in = new BufferedReader(new InputStreamReader(uc
				.getInputStream()));
		while ((inputLine = in.readLine()) != null) {
				if (inputLine.contains(palabra_a_buscar)){
					String numero =inputLine.substring(inputLine.indexOf("g>")+2,inputLine.indexOf("g>")+16).replace(" ","");
					System.out.println(numero);
				}
		}

		in.close();

		}


	}

}
