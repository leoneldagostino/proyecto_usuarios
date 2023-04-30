class usuario:
    def __init__(self, user_name = None, password = None, id_usuario = None):
        self._user_name = user_name
        self._password = password
        self._id_usuario = id_usuario
    
    def __str__(self):
        return 'Nombre usuario: {} - contraseña: {} - ID: {} '.format(self._user_name,self._password,self._id_usuario)
        
    
    @property
    def user_name(self):
        return self._user_name
    @user_name.setter
    def user_name(self,user_name):
        self.user_name = user_name
    
       
    @property
    def password(self):
        return self._password
    @password.setter
    def password(self,password):
        self.password = password
          
       
    @property
    def id_usuario(self):
        return self._id_usuario
