package algorithm;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class Solution {

	/*
	 * write a method to replace all spaces in string with %20,The string is
	 * given in characters array, you can assume it has encough space for
	 * replacement and you are given the true length of string
	 * 
	 * @param string: An array of Char
	 * 
	 * @param length: The true length of the string
	 * 
	 * @return: The true length of new string
	 */
	public int replaceBlank(char[] string, int length) {
		int count = 0;
		// count the space
		for (int i = 0; i < length - 1; i++) {
			if (string[i] == ' ') {
				count++;
			}
		}

		int idx = length - 1 + 2 * count;
		for (int i = length - 1; i >= 0; i--) {
			if (string[i] == ' ') {
				string[idx] = '0';
				string[idx - 1] = '2';
				string[idx - 2] = '%';
				idx -= 3;
			} else {
				string[idx] = string[i];
				idx -= 1;
			}
		}
		return string.length;
	}

	/*
	 * Given n points on a 2D plane, find the maximum number of points that lie
	 * on the same straight line.
	 * 
	 * Definition for a point. 
	 * class Point { 
	 * 		int x; int y; 
	 * 		Point() { x = 0; y =0; 
	 * 		} 
	 * 		Point(int a, int b) { x = a; y = b; } 
	 * }
	 */
	public int maxPoints(Point[] points) {
		if (points.length == 0 || points == null) {
			return 0;
		}
		int maxPoints = 0;
		for (int i = 0; i < points.length - 1; i++) {
			double ratio = 0.0;
			int samePointNum = 0;
			int localMaxPoints = 1;
			HashMap<Double, Integer> map = new HashMap<Double, Integer>();
			for (int j = i + 1; j < points.length; j++) {
				if (points[i].x == points[j].x && points[i].y == points[j].y) {
					samePointNum++;
					continue;
				} else if(points[i].x == points[j].x){
					ratio = Integer.MAX_VALUE;
				} else if (points[i].y == points[j].y){
					ratio = 0;
				} else {
					ratio = (points[j].y - points[i].y) / (points[j].x - points[i].x);
				}
				if(map.containsKey(ratio)) {
					map.put(ratio, map.get(ratio) + 1);
				} else {
					map.put(ratio, 1);
				}
			}
			for(int value : map.values()) {
				localMaxPoints = localMaxPoints > value ? localMaxPoints : value;
			}
			localMaxPoints += samePointNum;
			maxPoints = maxPoints > localMaxPoints ? maxPoints : localMaxPoints;
		}
        return maxPoints;
    }
	
	/* 
	 * Given a dictionary, find all of the longest words in the dictionary
	 * 
     * @param dictionary: an array of strings
     * @return: an arraylist of strings
     */
	public ArrayList<String> longestWords(String[] dictionary) {
        // write your code here
		if (dictionary == null || dictionary.length == 0) 
			return null;
		int maxLength = 0;
		ArrayList<String> longestStrings = new ArrayList<String>();
		for (int i = 0; i < dictionary.length; i++) {
			int length = dictionary[i].length();
			if (maxLength < length) {
				maxLength = length;
				longestStrings.clear();
				longestStrings.add(dictionary[i]);
			} else if (maxLength == length) {
				longestStrings.add(dictionary[i]);
			} else {
				continue;
			}
		}
		return longestStrings;
    }
	
	/* 
	 * Given two strings s1 and s2 of the same length, 
	 * determine if s2 is a scrambled string of s1.
	 * 
	 * @param s1 A string
     * @param s2 Another string
     * @return whether s2 is a scrambled string of s1
     * 
	 */
	public boolean isScramble(String s1, String s2) {
        // Write your code here
		if (s1 == null || s2 == null) {
			return false;
		}
		for (int i = 0; i < s1.length(); i++) {
			if (s1.charAt(i) == s2.charAt(i)) {
				continue;
			} else {
				if(i != s1.length() - 1 && i != s2.length() - 1){
					if(s1.charAt(i) == s2.charAt(i+1) && s1.charAt(i + 1) == s2.charAt(i)){
						
						i += 1;
						continue;
					} else {
						return false;
					}
				} else {
					return false;
				}
			}
		}
		return true;
    }


}

class Point { 
	 int x; int y; 
	 Point() { 
		 x = 0; 
		 y =0; 
	 } 
	 Point(int a, int b) { 
		 x = a; 
		 y = b; 
	} 
}
