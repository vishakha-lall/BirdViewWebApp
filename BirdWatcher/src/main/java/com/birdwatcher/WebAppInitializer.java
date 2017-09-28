package com.birdwatcher;

import javax.annotation.Resource;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;

import com.birdwatcher.storage.StorageService;

@SpringBootApplication
@Configuration
@EnableAutoConfiguration
@ComponentScan("com.birdwatcher")
public class WebAppInitializer{
	
	@Resource
	StorageService storageService; 
	
    public static void main(String[] args) throws Exception{
        SpringApplication.run(WebAppInitializer.class, args);
    }
    
    public void run(String... args) throws Exception {
   		storageService.deleteAll();
   		storageService.init();
   	}
}

