package com.birdwatcher.model;

public class Bird {
	private String species_name;
	private String extracted_text;
	private String wikipedia_link;
	public String getSpecies_name() {
		return species_name;
	}
	public void setSpecies_name(String species_name) {
		this.species_name = species_name;
	}
	public String getExtracted_text() {
		return extracted_text;
	}
	public void setExtracted_text(String extracted_text) {
		this.extracted_text = extracted_text;
	}
	public String getWikipedia_link() {
		return wikipedia_link;
	}
	public void setWikipedia_link(String wikipedia_link) {
		this.wikipedia_link = wikipedia_link;
	}
}
