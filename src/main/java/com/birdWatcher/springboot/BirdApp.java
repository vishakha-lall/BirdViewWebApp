package com.birdWatcher.springboot;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.context.annotation.ComponentScan;


@EnableAutoConfiguration
@ComponentScan("com.birdWatcher.springboot")

public class BirdApp {

	public static void main(String[] args) {
		SpringApplication.run(BirdApp.class, args);
	}
}
