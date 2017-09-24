package com.birdwatcher;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class UserController
{
    public List<UserDetails> userDetailsList = new ArrayList<UserDetails>();
    
    public UserController()
    {
        userDetailsList.add(new UserDetails("Vishakha", "vishakhaisawesome"));
        userDetailsList.add(new UserDetails("Chitransh", "chitranshisnot"));
    }
    @RequestMapping(value="/userdetails",method=RequestMethod.GET,produces="application/json")
    public List<UserDetails> GetUserdetails()
    {
        return userDetailsList;
    }
    
    @RequestMapping(value="/user",consumes = MediaType.APPLICATION_JSON_VALUE, method = RequestMethod.POST)
    public List<UserDetails> ProcessUser(@RequestBody UserDetails userDetails)
    {
        boolean nameExist = false;
        
        for(UserDetails ud : userDetailsList)
        {
            if(ud.getName().equals(userDetails.getName()))
            {
                nameExist = true;
                ud.setDepartment(userDetails.getDepartment());
                break;
            }
        }
        if(!nameExist)
        {
            userDetailsList.add(userDetails);
        }
        
        return userDetailsList;
    }
    
    @RequestMapping(value="/deleteuser",consumes = MediaType.APPLICATION_JSON_VALUE, method = RequestMethod.DELETE)
    public ResponseEntity DeleteUser(@RequestBody UserDetails userDetails)
    {
        Iterator<UserDetails> it = userDetailsList.iterator();
        while(it.hasNext())
        {
            UserDetails ud = (UserDetails) it.next();
            if(ud.getName().equals(userDetails.getName()))
                it.remove();
        }
        return new ResponseEntity(HttpStatus.OK);
    }
}