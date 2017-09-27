package com.birdwatcher.controller;

import java.util.ArrayList;
import java.util.List;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

import com.birdwatcher.model.User;

@Controller
public class MainController {
	
	@SuppressWarnings("null")
	public List<User> createDirectory()
	{
		List<User> users = new ArrayList<User>(2);
		User vishakha = new User();
		vishakha.setUsername("Vishakha");
		vishakha.setEmail("vishakha@mnit.ac.in");
		vishakha.setPassword("awesome");
		users.add(vishakha);
		User chitransh = new User();
		chitransh.setUsername("Chitransh");
		chitransh.setEmail("chitransh@mnit.ac.in");
		chitransh.setPassword("notsoawesome");
		users.add(chitransh);
		return users;
	}

    @RequestMapping(value="/",method = RequestMethod.GET)
    public void initialiseUsers(){
    	System.out.println("Inside main Controller");
    	List<User> registeredUsers = null;
    	if (registeredUsers == null) {
    		registeredUsers=createDirectory();
        	System.out.println("Users initialised");
    	}
    }
}
