package com.birdwatcher.controller;

import java.io.File;
import java.util.ArrayList;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.multipart.MultipartFile;

import com.birdwatcher.model.User;
import com.birdwatcher.model.UserDTO;
import com.birdwatcher.model.UserDirectory;
import com.birdwatcher.storage.StorageService;

@Controller
public class UploadController {
	@Autowired
	StorageService storageService;
	List<String> files = new ArrayList<String>();
	@RequestMapping(value="/upload",method = RequestMethod.POST)
	public @ResponseBody String upload(@RequestBody MultipartFile file){
		try {
			storageService.store(file);
			files.add(file.getOriginalFilename());
			return "success";
		} catch (Exception e) {
			return "failure";
		}
    }
}
