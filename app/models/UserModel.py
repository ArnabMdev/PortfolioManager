class User:
    def __init__(self, user_id, user_name="",password=""):
        self.__user_id = user_id,
        self.__user_name = user_name
        self.__password = password
        
    @property
    def user_id(self):
        return self.__user_id
    
    @property
    def user_name(self):
        return self.__user_name
    
    @property
    def password(self):
        return self.__password
    
    @user_name.setter
    def user_name(self, value):
        self.__user_name = value
    
    @password.setter
    def password(self, value):
        self.__password = value
    
    def to_dict(self):
        return {
            'user_id' : self.__user_id,
            'user_name' : self.__user_name,
            'password' : self.__password
        }