package com.birdwatcher.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;


@Controller
public class ResultController {
	@RequestMapping(value="/result",method = RequestMethod.POST)
	@ResponseBody
    public String result(@RequestBody String bird){
		return bird;
	}
}