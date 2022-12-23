# Tapni Application Backend 


## About database models 
there are total  5 models  and business logic   
1. **connections** models is for adding people 
2. **profiles** models is for user profies
3. **social** models is for social links 
4. **products** models is for product items 
5. **user** models is for user auth and much more

## End Point 

``` bash


POST - >  status code success = 201 or error = 400
  {
            "profile",
            "peroson_name",
            "Email",
            "phone_number",
            "job_title",
            "company_name",
            "Add_note"       
 } 


 GET -> status 200
 {
            "profile",
            "peroson_name",
            "Email",
            "phone_number",
            "job_title",
            "company_name",
            "Add_note"   


 }


```
