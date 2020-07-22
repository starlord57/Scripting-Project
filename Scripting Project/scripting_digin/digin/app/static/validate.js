function validate() 
{
	cname = document.getElementById('cname');
	pwd = document.getElementById("cpassword");
	cpwd = document.getElementById("password");
	if (cpwd.value != pwd.value) 
	{
		alert("Both Passwords must match!");
	}
}
