class SoftwareFJException(Exception):
    """Clase base global para todas las excepciones de Software FJ."""
    def __init__(self, mensaje: str, codigo_error: int):
        super().__init__(mensaje)
        self.codigo_error = codigo_error
        self.mensaje = mensaje

class CostoInvalidoException(SoftwareFJException):
    """Se lanza cuando se intenta asignar un costo negativo o fuera de rango."""
    def __init__(self, mensaje: str = "El costo base del servicio no puede ser menor a cero."):
        super().__init__(mensaje, codigo_error=401)

class CapacidadExcedidaException(SoftwareFJException):
    """Se lanza si se intenta agendar una sala con más personas de las permitidas."""
    def __init__(self, capacidad_max: int, personas_intentadas: int):
        mensaje = f"Error: Capacidad excedida. Máximo {capacidad_max} personas, intentó registrar {personas_intentadas}."
        super().__init__(mensaje, codigo_error=402)

class IdentificadorDuplicadoException(SoftwareFJException):
    """Se lanza si se intenta registrar un ID de cliente o servicio que ya existe."""
    def __init__(self, id_duplicado: str):
        mensaje = f"El identificador '{id_duplicado}' ya se encuentra registrado en el sistema."
        super().__init__(mensaje, codigo_error=403)
