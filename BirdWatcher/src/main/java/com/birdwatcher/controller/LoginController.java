package com.birdwatcher.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

import com.birdwatcher.model.UserDTO;

@Controller
@RequestMapping(value="/login")
public class LoginController {
	@RequestMapping(value="/authenticate",method = RequestMethod.POST)
	@ResponseBody
    public String authenticate(@RequestBody UserDTO activeUser){
		System.out.println("Inside login Controller authenticate");
		String username=activeUser.getUsername();
		String password=activeUser.getPassword();
		if(username.equals("vishakha")) {
			if(password.equals("awesome")) {
				return "success";
			}else {
				return "failure";
			}
		}else {
			return "failure";
		}	
    }
}
