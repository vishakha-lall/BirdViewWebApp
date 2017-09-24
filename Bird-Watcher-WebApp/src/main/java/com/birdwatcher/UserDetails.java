package com.birdwatcher;

import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlAttribute;
import javax.xml.bind.annotation.XmlRootElement;

@XmlRootElement
@XmlAccessorType(XmlAccessType.FIELD)
public class UserDetails
{
    @XmlAttribute
    private String name;
    @XmlAttribute
    private String department;
    public UserDetails()
    {
        super();
    }
    public UserDetails(String name, String department)
    {
        super();
        this.name = name;
        this.department = department;
    }
    public String getName()
    {
        return name;
    }
    public void setName(String name)
    {
        this.name = name;
    }
    public String getDepartment()
    {
        return department;
    }
    public void setDepartment(String department)
    {
        this.department = department;
    }
    @Override
    public String toString()
    {
        return "UserDetails [name=" + name + ", department=" + department + "]";
    }
}