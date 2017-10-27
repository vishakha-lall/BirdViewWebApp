package com.birdwatcher.model;

public class BirdResult {
	String result;
	Bird[] tuples =new Bird[5];
	public String getResult() {
		return result;
	}
	public void setResult(String result) {
		this.result = result;
	}
	public Bird[] getTuples() {
		return tuples;
	}
	public void setTuples(Bird[] tuples) {
		this.tuples = tuples;
	}
}
