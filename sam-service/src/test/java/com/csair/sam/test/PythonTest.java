package com.csair.sam.test;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class PythonTest {

	public static void main(String[] args) {

		String resultString = null;
		String pyPath = "D:\\workspace\\eclipse\\web\\sam\\sam-service\\src\\test\\resources\\python\\GetFlightInfo.py"; // python文件路径
		String[] pythonStr = new String[] { "D:\\software\\python\\python.exe", pyPath }; // 设定命令行
		String result = "";
		try {
			Process proc = Runtime.getRuntime().exec(pythonStr); // 执行py文件			
			BufferedReader in = new BufferedReader(new InputStreamReader(proc.getInputStream(), "utf-8"));
			BufferedReader bufrError = new BufferedReader(new InputStreamReader(proc.getErrorStream(), "UTF-8"));
			String line = null;			
			while ((line = in.readLine()) != null) {
				//System.out.println(line);
				result += line;
			}
			String error = null;
	        while ((error = bufrError.readLine()) != null) {
	        	result +=error;
	        }
	        bufrError.close();
			in.close();
			proc.waitFor();
			System.out.println(result);
		} catch (Exception e) {
			e.printStackTrace();
		}

	}

}
