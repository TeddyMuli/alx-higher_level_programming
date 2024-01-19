#!/usr/bin/python3
"""Defines the class model"""
import json
import csv
import turtle


class Base:
    """The base declaration
    Atrributes:
        __nb_objects (int): The number of instantiated Bases"""
    __nb_objects = 0

    def __init__(self, id=None):
        """The constructor
        Args:
            id(int): The identity of the new base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation of list_dictionaryies"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is None or list_objs == []:
        #save an empty list
            list_objs = []
        #create a list of dictionaries
        list_dicts = []
        for obj in list_objs:
            list_dicts.append(obj.to_dictionary())
        #convert the list of dictionaries to a JSON string
        json_string = Base.to_json_string(list_dicts)
        #write the JSON string to a file
        with open(cls.__name__ + ".json", "w") as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)
    
    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        #must use def update(self, *args, **kwargs)
        dummy.update(**dictionary)
        return dummy
    
    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        try:
            with open(cls.__name__ + ".json", "r") as f:
                json_string = f.read()
        except:
            return []
        list_dicts = cls.from_json_string(json_string)
        list_instances = []
        for dict in list_dicts:
            list_instances.append(cls.create(**dict))
        return list_instances
    
    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes in CSV"""
        if list_objs is None or list_objs == []:
            list_objs = []
        list_dicts = []
        for object in list_objs:
            list_dicts.append(object.to_dictionary())
        with open(cls.__name__ + ".csv", "w") as f:
            if cls.__name__ == "Rectangle":
                fieldnames = ["id", "width", "height", "x", "y"]
            elif cls.__name__ == "Square":
                fieldnames = ["id", "size", "x", "y"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(list_dicts)

    @classmethod
    def load_from_file_csv(cls):
        """deserializes in CSV"""
        try:
            with open(cls.__name__ + ".csv", "r") as f:
                reader = csv.DictReader(f)
                list_dicts = []
                for row in reader:
                    for key, value in row.items():
                        row[key] = int(value)
                    list_dicts.append(row)
        except:
            return []
        list_instances = []
        for dict in list_dicts:
            list_instances.append(cls.create(**dict))
        return list_instances
    
    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws the Rectangles and Squares using the turtle module"""
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.color("#ffffff")
        turt.shape("turtle")
        turt.pensize(3)
        turt.speed(10)
        for rect in list_rectangles:
            turt.penup()
            turt.setpos(rect.x, rect.y)
            turt.pendown()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
        for square in list_squares:
            turt.penup()
            turt.setpos(square.x, square.y)
            turt.pendown()
            for i in range(4):
                turt.forward(square.size)
                turt.left(90)
        turt.hideturtle()
        turtle.done()
    