package com.csair.sam.test;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class PythonTest {

	public static void main(String[] args) {

		String resultString = null;
		String pyPath = "python/GetFlightInfo.py"; // python文件路径
		String[] pythonStr = new String[] { "python", pyPath }; // 设定命令行
		try {
			Process proc = Runtime.getRuntime().exec(pythonStr); // 执行py文件
			BufferedReader in = new BufferedReader(new InputStreamReader(proc.getInputStream()));
			String line = null;
			while ((line = in.readLine()) != null) {
				System.out.println(line);
			}
			in.close();
			proc.waitFor();
		} catch (Exception e) {
			e.printStackTrace();
		}

	}

}
