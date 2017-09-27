package com.birdwatcher.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

import com.birdwatcher.model.User;
import com.birdwatcher.model.UserDTO;

@Controller
@RequestMapping(value="/signup")
public class SignupController {
	@RequestMapping(method = RequestMethod.POST)
	@ResponseBody
    public String registerUser(@RequestBody User activeUser){
		System.out.println("Inside signup Controller");
		String username=activeUser.getUsername();
		String email=activeUser.getEmail();
		String password=activeUser.getPassword();
		System.out.println(username);
		return "success";
    }
}
