from neo4j import GraphDatabase, Driver
import json

URI = "neo4j+s://6f5270e8.databases.neo4j.io"
AUTH = ("ole_andreas.jensen@hotmail.com", "zRaR1f3SAqAMIgBAVJ9Th3z5u_1wLiZjAoan2arpmrA")

def get_connection() -> Driver:
    driver = GraphDatabase.driver(URI, auth=AUTH)
    driver.verify_connectivity()
    return driver

def node_to_json(node):
    return dict(node.items())

def findAllCars():
    with get_connection().session() as session:
        cars = session.run("MATCH (a:Car) RETURN a;")
        nodes_json = [node_to_json(record["a"]) for record in cars]
        print(nodes_json)
        return nodes_json

def findCarByReg(reg):
    with get_connection().session() as session:
        cars = session.run("MATCH (a:Car) WHERE a.reg=$reg RETURN a;", reg=reg)
        nodes_json = [node_to_json(record["a"]) for record in cars]
        print(nodes_json)
        return nodes_json

def save_car(make, model, reg, year, capacity):
    with get_connection().session() as session:
        cars = session.run(
            "MERGE (a:Car {make: $make, model: $model, reg: $reg, year: $year, capacity: $capacity}) RETURN a;",
            make=make, model=model, reg=reg, year=year, capacity=capacity
        )
        nodes_json = [node_to_json(record["a"]) for record in cars]
        print(nodes_json)
        return nodes_json

def update_car(make, model, reg, year, capacity):
    with get_connection().session() as session:
        cars = session.run(
            "MATCH (a:Car {reg: $reg}) SET a.make=$make, a.model=$model, a.year=$year, a.capacity=$capacity RETURN a;",
            reg=reg, make=make, model=model, year=year, capacity=capacity
        )
        nodes_json = [node_to_json(record["a"]) for record in cars]
        print(nodes_json)
        return nodes_json

def delete_car(reg):
    with get_connection().session() as session:
        session.run("MATCH (a:Car {reg: $reg}) DELETE a;", reg=reg)