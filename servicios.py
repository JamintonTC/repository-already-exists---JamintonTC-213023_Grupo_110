from abc import ABC, abstractmethod

class Servicio(ABC):
    """
    Clase abstracta que representa la base de todos los servicios 
    ofrecidos por Software FJ. Implementa Abstracción y Encapsulación.
    """
    def __init__(self, id_servicio: str, nombre: str, costo_base: float):
        self._id_servicio = id_servicio  # Atributo protegido
        self._nombre = nombre            # Atributo protegido
        self._costo_base = costo_base    # Atributo protegido

    # Getters y Setters para demostrar Encapsulación
    @property
    def id_servicio(self):
        return self._id_servicio

    @property
    def nombre(self):
        return self._nombre

    @property
    def costo_base(self):
        return self._costo_base

    @costo_base.setter
    def costo_base(self, nuevo_costo: float):
        if nuevo_costo < 0:
            raise ValueError("El costo base no puede ser negativo.")
        self._costo_base = nuevo_costo

    @abstractmethod
    def calcular_costo(self, **kwargs) -> float:
        """Método abstracto para calcular el costo total (Polimorfismo)"""
        pass

    @abstractmethod
    def obtener_descripcion(self) -> str:
        """Método abstracto para describir el servicio (Polimorfismo)"""
        pass


class ReservaSala(Servicio):
    """Clase derivada para el servicio de Reserva de Salas"""
    def __init__(self, id_servicio: str, nombre: str, costo_base: float, capacidad: int):
        super().__init__(id_servicio, nombre, costo_base)
        self.capacidad = capacidad

    def calcular_costo(self, horas: int = 1, tiene_descuento: bool = False) -> float:
        # Sobrecarga simulada mediante parámetros opcionales
        costo_total = self._costo_base * horas
        if tiene_descuento:
            costo_total *= 0.90  # 10% de descuento
        return costo_total

    def obtener_descripcion(self) -> str:
        return f"Servicio: {self._nombre} [Sala]. Capacidad máxima: {self.capacidad} personas."


class AlquilerEquipo(Servicio):
    """Clase derivada para el servicio de Alquiler de Equipos"""
    def __init__(self, id_servicio: str, nombre: str, costo_base: float, tipo_equipo: str):
        super().__init__(id_servicio, nombre, costo_base)
        self.tipo_equipo = tipo_equipo

    def calcular_costo(self, dias: int = 1, incluye_seguro: bool = False) -> float:
        costo_total = self._costo_base * dias
        if incluye_seguro:
            costo_total += 15000.0  # Costo fijo adicional por seguro empresarial
        return costo_total

    def obtener_descripcion(self) -> str:
        return f"Servicio: {self._nombre} [Equipo]. Tipo: {self.tipo_equipo}."

class AsesoriaEspecializada(Servicio):
    """Clase derivada para el servicio de Asesorías Especializadas"""
    def __init__(self, id_servicio: str, nombre: str, costo_base: float, area: str):
        super().__init__(id_servicio, nombre, costo_base)
        self.area = area

    def calcular_costo(self, sesiones: int = 1, aplica_iva: bool = True) -> float:
        costo_total = self._costo_base * sesiones
        if aplica_iva:
            costo_total *= 1.19  # IVA del 19% en Colombia
        return costo_total

    def obtener_descripcion(self) -> str:
        return f"Servicio: {self._nombre} [Asesoría]. Área experta: {self.area}."
