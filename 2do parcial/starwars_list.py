def obtener_personajes():
    return [
        ("Luke Skywalker", 6), ("Darth Vader", 6), ("Yoda", 6), 
        ("Boba Fett", 3), ("C-3PO", 9), ("Leia", 6), 
        ("Rey", 3), ("Kylo Ren", 3), ("Chewbacca", 7), 
        ("Han Solo", 5), ("R2-D2", 9), ("BB-8", 3)
    ]

def obtener_conexiones():
    return [
        (4, "Luke Skywalker", "Darth Vader"),
        (5, "Luke Skywalker", "Leia"),
        (3, "Luke Skywalker", "Yoda"),
        (6, "C-3PO", "R2-D2"),
        (4, "C-3PO", "Leia"),
        (5, "Han Solo", "Chewbacca"),
        (3, "Rey", "Kylo Ren"),
        (3, "Rey", "BB-8"),
        (2, "Yoda", "Darth Vader"),
        (1, "Boba Fett", "Darth Vader")
    ]