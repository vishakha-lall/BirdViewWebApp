package com.birdwatcher.model;

import java.util.ArrayList;
import java.util.List;

public class UserDirectory {
	private static List <User> userDirectory = new ArrayList<User>();
	public List<User> initiateUserDirectory(){
		User newUser1 = new User();
		newUser1.setUsername("vishakha");
		newUser1.setPassword("awesome");
		newUser1.setEmail("vishakha@mnit.ac.in");
		userDirectory.add(newUser1);
		User newUser2 = new User();
		newUser2.setUsername("chitransh");
		newUser2.setPassword("notawesome");
		newUser2.setEmail("chitransh@mnit.ac.in");
		userDirectory.add(newUser2);
		return userDirectory;
	}
	public List<User> addNewUser(String username, String password, String email){
		User newUser = new User();
		newUser.setUsername(username);
		newUser.setPassword(password);
		newUser.setEmail(email);
		userDirectory.add(newUser);
		return userDirectory;
	}
	public String checkUser(String username, String password){
		for(User u:userDirectory) {
			if(u.getUsername().equals(username)) {
				if(u.getPassword().equals(password)) {
					return "success";
				}
			}
		}
		return "failure";
	}
	public User findUser(String username){
		for(User u:userDirectory) {
			if(u.getUsername().equals(username)) {
				return u;
			}
		}
		return null;
	}
	public List<User> getUserDirectory() {
		return userDirectory;
	}
	public void setUserDirectory(List<User> userDirectory) {
		this.userDirectory = userDirectory;
	}
}
