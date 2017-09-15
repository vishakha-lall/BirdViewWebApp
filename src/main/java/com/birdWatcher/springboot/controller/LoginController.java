package com.birdWatcher.springboot.controller;

import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.stereotype.Controller;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

import com.birdWatcher.springboot.DTO.LoginUserDTO;

@RestController
@EnableAutoConfiguration
public class LoginController {

	@RequestMapping(value="/login",method=RequestMethod.GET)
	public @ResponseBody String printDetails(@RequestParam LoginUserDTO loginUserInstance){
		System.out.print(loginUserInstance.getUsername());
		System.out.print(loginUserInstance.getPassword());
		return null;
	}
	
}
