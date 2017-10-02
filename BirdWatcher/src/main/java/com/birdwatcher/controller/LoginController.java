package com.birdwatcher.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

import com.birdwatcher.model.User;
import com.birdwatcher.model.UserDTO;
import com.birdwatcher.model.UserDirectory;

@Controller
@RequestMapping(value="/login")
public class LoginController {
	@RequestMapping(value="/authenticate",method = RequestMethod.POST)
	@ResponseBody
    public String authenticate(@RequestBody UserDTO activeUser){
		System.out.println("Inside login Controller authenticate");
		String username=activeUser.getUsername();
		String password=activeUser.getPassword();
		UserDirectory users = new UserDirectory();
		if(users.checkUser(username, password).equals("success")) {
			User active =new User();
			active=users.findUser(username);
			return "success";
		}
		else {
			return "failure";
		}
    }
}
