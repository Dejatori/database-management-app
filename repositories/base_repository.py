# Esse archivo contiene la implementación de un repositorio base que puede ser utilizado para crear repositorios específicos para cada modelo del banco de datos.
from flask_sqlalchemy import SQLAlchemy
from typing import TypeVar, Generic, Type, List, Optional

# Definimos un tipo genérico T
T = TypeVar('T')

# Definimos la clase BaseRepository que recibe un tipo genérico T
class BaseRepository(Generic[T]):
    """
    Clase base para repositorios que maneja operaciones CRUD para un modelo específico.

    Atributos:
        db (SQLAlchemy): Instancia de SQLAlchemy para manejar la base de datos.
        model (Type[T]): Modelo de la base de datos para el cual se crea el repositorio.
    """

    def __init__(self, db: SQLAlchemy, model: Type[T]):
        """
        Inicializa el repositorio con una instancia de SQLAlchemy y un modelo.

        Args:
            db (SQLAlchemy): Instancia de SQLAlchemy.
            model (Type[T]): Modelo de la base de datos.
        """
        self.db = db
        self.model = model

    def get_all(self) -> List[T]:
        """
        Obtiene todos los registros de la tabla.

        Returns:
            List[T]: Lista de todos los registros del modelo.
        """
        return self.model.query.all()

    def get_by_id(self, id: int) -> Optional[T]:
        """
        Obtiene un registro por su id.

        Args:
            id (int): Identificador del registro.

        Returns:
            Optional[T]: El registro encontrado o None si no existe.
        """
        return self.db.session.get(self.model, id)

    def create(self, **kwargs) -> T:
        """
        Crea un nuevo registro.

        Args:
            **kwargs: Atributos del modelo a crear.

        Returns:
            T: La instancia del modelo creada.
        """
        instance = self.model(**kwargs)
        self.db.session.add(instance)
        self.db.session.commit()
        return instance

    def update(self, id: int, **kwargs) -> Optional[T]:
        """
        Actualiza un registro.

        Args:
            id (int): Identificador del registro a actualizar.
            **kwargs: Atributos del modelo a actualizar.

        Returns:
            Optional[T]: La instancia del modelo actualizada o None si no existe.
        """
        instance = self.get_by_id(id)
        if instance:
            for key, value in kwargs.items():
                setattr(instance, key, value)
            self.db.session.commit()
        return instance

    def delete(self, id: int) -> bool:
        """
        Elimina un registro.

        Args:
            id (int): Identificador del registro a eliminar.

        Returns:
            bool: True si el registro fue eliminado, False si no existe.
        """
        instance = self.get_by_id(id)
        if instance:
            self.db.session.delete(instance)
            self.db.session.commit()
            return True
        return False