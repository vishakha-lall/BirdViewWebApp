package com.birdwatcher.controller;

import java.util.ArrayList;
import java.util.List;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

import com.birdwatcher.model.User;
import com.birdwatcher.model.UserDirectory;

@Controller
public class MainController {
    @SuppressWarnings("null")
	@RequestMapping(value="/",method = RequestMethod.GET)
    public void initialiseUsers(){
    	System.out.println("Inside main Controller");
    	UserDirectory users = new UserDirectory();
    	users.initiateUserDirectory();
    	System.out.println("Users initialised");
    }
}
