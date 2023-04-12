from django.db import models

"""
create table company(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    description VARCHAR(255),
    city VARCHAR(255),
    address VARCHAR(255)
);
"""
"""
create table vacancy(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    description VARCHAR(255),
    salary INT,
    company INT,
     FOREIGN KEY (company)  REFERENCES company (id)
);
"""

# ORM - Object Relational Mapping

class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address
        }

class Vacancy(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    salary = models.FloatField(default=255)
    company = models.ForeignKey(Company,
                                 on_delete=models.CASCADE,
                                 related_name='company')

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'salary': self.salary,
            'company': self.company
        }