from abc import ABC, abstractmethod
from settings import db_path
import sqlite3


class BaseModel(ABC):
    def __init__(self, id=None) -> None:
        self.id = id
        self.__isValid = True

    @property
    def isValid(self):
        return self.__isValid

    @isValid.setter
    def isValid(self, isValid):
        self.__isValid = isValid

    @abstractmethod
    def print():
        pass

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @classmethod
    @abstractmethod
    def objects():
        pass

    @classmethod
    @abstractmethod
    def get_by_id(Id):
        pass


class Countries(BaseModel):
    table = 'Countries'

    def __init__(self, name, Id=None) -> None:
        super().__init__(Id)
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            self.__name = ''
            self.__isValid = False

    def print():
        pass

    def save(self):
        if self.isValid:
            try:
                with sqlite3.connect(db_path) as conn:
                    cursor = conn.cursor()
                    try:
                        if self.id is None:
                            # insert, create new object (row)
                            cursor.execute(f'''
                                INSERT INTO {Countries.table} ('name')
                                VALUES ('{self.name}')
                            ''')
                            self.id = cursor.lastrowid
                        else:
                            # update existing row
                            conn.execute(f'''
                                UPDATE {Countries.table} set name  = '{self.name}' where Id = {self.id}
                            ''')

                            conn.commit()
                    except:
                        
                        print('Saqlashda xatolik bo\'ldi')
                        conn.rollback()
                return True
            except:
                print('Bog\'lanishda xatolik')
        else:
            return False

    def delete(self):
        try:
            with sqlite3.connect(db_path) as conn:
                cursor = conn.cursor()
                query = f"""
                Delete From  {Countries.table} where Id = {self.id}
                """
                cursor.execute(query)
                conn.commit()
        except:
            print('Bog\'lanishda xatolik')

    def objects():
        try:
            with sqlite3.connect(db_path) as conn:
                cursor = conn.cursor()
                query = f"""
                Select *From  {Countries.table}
                """
                for row in cursor.execute(query):
                    yield Countries(row[1], row[0])
        except:
            print('Bog\'lanishda xatolik')




    def get_by_id(id):
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            query = f"""
                Select *From  {Countries.table}
                Where Id={id}
                """
            res = cursor.execute(query).fetchone()
            if res is not None:
                return Countries(res[1], res[0])
            else:
                return None

    def __str__(self):
        return f'{self.name}'


class Team(BaseModel):
    table = 'Team'

    def __init__(self, name, Countries_Id, id=None) -> None:
        super().__init__(id)
        self.name = name
        self.Countries_Id = Countries_Id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            self.__name = ''
            self.__isValid = False
    @property
    def Countries_Id(self):
        return self.__Countries_Id

    @Countries_Id.setter
    def Countries_Id(self, Countries_Id):
        if isinstance(Countries_Id, int) and Countries.get_by_id(Countries_Id) is not None:
            self.__Countries_Id = Countries_Id
        else:
            self.__Countries_Id = None
            self.__isValid = False

    @property
    def Countries(self):
        return Countries.get_by_id(self.Countries_Id)

    def print():
        pass

    def save(self):
        if self.isValid:
            try:
                with sqlite3.connect(db_path) as conn:
                    cursor = conn.cursor()
                    try:
                        if self.id is None:
                            # insert, create new object (row)
                            cursor.execute(f'''
                                INSERT INTO {Team.table} ('name', Countries_Id)
                                VALUES ('{self.name}', {self.Countries_Id})
                            ''')
                            self.id = cursor.lastrowid
                        else:
                            # update existing row

                            conn.execute(f'''
                                UPDATE {Team.table} set name = '{self.name}', Countries_Id={self.Countries_Id} where Id = {self.id}
                            ''')

                            conn.commit()
                    except:
                        print('Saqlashda xatolik bo\'ldi')
                        conn.rollback()
                return True
            except:
                print('Bog\'lanishda xatolik')
        else:
            return False

    def delete(self):
        try:
            with sqlite3.connect(db_path) as conn:
                cursor = conn.cursor()
                query = f"""
                Delete From  {Team.table} where Id = {self.id}
                """
                cursor.execute(query)
                conn.commit()
        except:
            raise
            print('Bog\'lanishda xatolik')

    def objects():
        try:
            print(db_path)
            with sqlite3.connect(db_path) as conn:
                cursor = conn.cursor()
                query = f"""
                Select *From  {Team.table}
                """
                for row in cursor.execute(query):
                    yield Team(row[1], row[2], row[0])
        except:
            raise
            print('Bog\'lanishda xatolik')

    def get_by_id(id):
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            query = f"""
                Select *From {Team.table}
                Where Id={id}
                """
            res = cursor.execute(query).fetchone()
            if res is not None:
                return Team(res[1], res[2], res[0])
            else:
                return None        
        

    def __str__(self):
        return f'{self.Countries}\t | {self.name}'



class Players(BaseModel):
    table = 'Players'


    def __init__(self, Name, Age, Goals, Speed, Team_Id, id=None):
        super().__init__(id)
        self.Name = Name
        self.Age = Age
        self.Goals = Goals
        self.Speed = Speed
        self.Team_Id = Team_Id

    @property
    def Name(self):
        return self.__Name

    @Name.setter
    def Name(self, Name):
        if isinstance(Name, str):
            self.__Name = Name
        else:
            self.__Name = ''
            self.__isValid = False

    @property
    def Age(self):
        return self.__Age

    @Age.setter
    def Age(self, Age):
        if isinstance(Age, int):
            self.__Age = Age
        else:
            self.__Age = ''
            self.__isValid = False

    @property
    def Goals(self):
        return self.__Goals

    @Goals.setter
    def Goals(self, Goals):
        if isinstance(Goals, int):
            self.__Goals = Goals
        else:
            self.__Goals = ''
            self.__isValid = False

    @property
    def Speed(self):
        return self.__Speed

    @Speed.setter
    def Speed(self, Speed):
        if isinstance(Speed, int):
            self.__Speed = Speed
        else:
            self.__Speed = ''
            self.__isValid = False
            raise

    @property
    def Team_Id(self):
        return self.__Team_Id
    
    @Team_Id.setter
    def Team_Id(self, Team_Id):
        if isinstance(Team_Id, int) and Team.get_by_id(Team_Id) is not None:
            self.__Team_Id = Team_Id
        else:
            self.__Team_Id = 0
            self.__isValid = False
    @property
    def Team(self):
        return Team.get_by_id(self.Team_Id)



    def del_by_id(id):
        try:
            with sqlite3.connect(db_path) as conn:
                cursor = conn.cursor()
                query = f"""
                Delete From  {Players.table} where Id = {id}
                """
                cursor.execute(query)
                conn.commit()
        except:
            print('Bog\'lanishda xatolik')
 
    def save(self):
        if self.isValid:
            try:
                with sqlite3.connect(db_path) as conn:
                    cursor = conn.cursor()
                    try:
                        if self.id is None:
                            # insert, create new object (row)
                            cursor.execute(f'''
                                INSERT INTO {Players.table} ('Name', Age,Goals,Speed,Team_Id)
                                VALUES ('{self.Name}',{self.Age},{self.Goals},{self.Speed},{self.Team_Id})
                            ''')
                            self.id = cursor.lastrowid
                        else:
                            # update existing row
                            conn.execute(f'''
                                UPDATE {Players.table} set Name = '{self.Name}',Age = {self.Age},Goals = {self.Goals},Speed = {self.Speed},Team_Id={self.Team_Id} where Id = {self.id}
                            ''')

                            conn.commit()
                    except:
                        print('Saqlashda xatolik bo\'ldi')
                        conn.rollback()
                return True
            except:
                print('Bog\'lanishda xatolik')
                print('hello001')
        else:
            return False

    def delete(self):
        try:
            with sqlite3.connect(db_path) as conn:
                cursor = conn.cursor()
                query = f"""
                Delete From  {Players.table} where Id = {self.id}
                """
                cursor.execute(query)
                conn.commit()
        except:
            print('Bog\'lanishda xatolik')
            print('hello002')

    def objects():
        try:
            print(db_path)
            with sqlite3.connect(db_path) as conn:
                cursor = conn.cursor()
                query = f"""
                Select *From  {Players.table}
                """
                for row in cursor.execute(query):
                    yield Players(row[1], row[2], row[3], row[4], row[5], row[0])
        except:
            print('Bog\'lanishda xatolik')
            print('hello003')

    def get_by_id(id):
       pass
    def print():
       pass
