package com.birdwatcher.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.multipart.MultipartFile;

import com.birdwatcher.model.UserDTO;

@Controller
@RequestMapping(value="/upload")
public class UploadController {
	@RequestMapping(method = RequestMethod.POST)
	@ResponseBody
    public String authenticate(@RequestBody MultipartFile img){
		return img.toString();
    }
}
