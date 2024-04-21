import uuid

class Initializer(object):
    class_attribute = 'Class attribute'

    def __init__(self):
        self.ID = uuid.uuid4()

    def execute(self):
        print(f'Execute {self.ID} {Initializer.class_attribute}')

class MyClass:
    class_attribute = 10

    def __init__(self, instance_attribute):
        self.instance_attribute = instance_attribute


if __name__ == '__main__':
    objet1 = Initializer()
    objet1.execute()

    objet2 = Initializer()
    objet2.execute()

    # Accès à l'attribut de classe via la classe
    print(MyClass.class_attribute)  # Sortie: 10

    # Accès à l'attribut de classe via une instance
    obj1 = MyClass(20)
    print(obj1.class_attribute)  # Sortie: 10

    # Modification de l'attribut de classe via la classe
    MyClass.class_attribute = 30
    print(MyClass.class_attribute)  # Sortie: 30
    print(obj1.class_attribute)  # Sortie: 30 (la modification est propagée à toutes les instances)

    # Modification de l'attribut de classe via une instance
    obj1.class_attribute = 40
    print(MyClass.class_attribute)  # Sortie: 30 (la classe n'est pas affectée)
    print(obj1.class_attribute)  # Sortie: 40 (une nouvelle variable d'instance est créée)

    # Création d'une nouvelle instance
    obj2 = MyClass(50)
    print(obj2.class_attribute)  # Sortie: 30 (la valeur partagée par toutes les instances est toujours 30)

    MyClass.class_attribute = 10
    print(obj1.class_attribute)
    print(obj2.class_attribute)
