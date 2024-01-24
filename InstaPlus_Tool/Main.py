from InstaPlus import InstaPlus


UserName='ABCDEFGH' #Instagram UserName Here
UserID='5645455645' #Enter Your Instagram UserID Here


cl = InstaPlus(UserName,UserID)
cl.appStatus()
cl.SignUp()
cl.GetFollowList()
