from InstaPlus import InstaPlus


UserName='ABCDEFGH' #Instagram UserName Here
UserID='49078425082' #Enter Your Instagram UserID Here


cl = InstaPlus(UserName,UserID)
cl.appStatus()
cl.SignUp()
cl.GetFollowList()