class SoftwareFJException(Exception):
    """Clase base global para todas las excepciones de Software FJ."""
    def __init__(self, mensaje: str = "Error en el sistema Software FJ.", codigo_error: int = 400):
        super().__init__(mensaje)
        self.codigo_error = codigo_error
        self.mensaje = mensaje

    def __str__(self):
        return f"[Error {self.codigo_error}] {self.mensaje}"


class CostoInvalidoException(SoftwareFJException):
    """Se lanza cuando se intenta asignar un costo negativo o fuera de rango."""
    def __init__(self, mensaje: str = "El costo base del servicio no puede ser menor a cero."):
        super().__init__(mensaje, codigo_error=401)


class CapacidadExcedidaException(SoftwareFJException):
    """Se lanza si se intenta agendar una sala con más personas de las permitidas."""
    def __init__(self, capacidad_max=None, personas_intentadas=None, mensaje: str = None):
        if mensaje is not None:
            texto = mensaje
        elif isinstance(capacidad_max, str) and personas_intentadas is None:
            texto = capacidad_max
        elif capacidad_max is not None and personas_intentadas is not None:
            texto = (
                f"Error: Capacidad excedida. Máximo {capacidad_max} personas, "
                f"intentó registrar {personas_intentadas}."
            )
        else:
            texto = "Error: Se ha excedido la capacidad máxima permitida."
        super().__init__(texto, codigo_error=402)


class IdentificadorDuplicadoException(SoftwareFJException):
    """Se lanza si se intenta registrar un ID de cliente o servicio que ya existe."""
    def __init__(self, id_duplicado: str = "desconocido"):
        if "ya se encuentra" in str(id_duplicado) or "duplicado" in str(id_duplicado).lower():
            mensaje = str(id_duplicado)
        else:
            mensaje = f"El identificador '{id_duplicado}' ya se encuentra registrado en el sistema."
        super().__init__(mensaje, codigo_error=403)


class RecursoNoEncontradoException(SoftwareFJException):
    """Se lanza cuando no se encuentra un cliente, servicio o reserva por su ID."""
    def __init__(self, entidad: str = "Recurso", identificador: str = ""):
        detalle = f" con ID '{identificador}'" if identificador else ""
        mensaje = f"{entidad}{detalle} no fue encontrado en el sistema."
        super().__init__(mensaje, codigo_error=404)


class ReservaInvalidaException(SoftwareFJException):
    """Se lanza cuando una reserva presenta fechas inválidas, conflictos de horario o datos incompletos."""
    def __init__(self, mensaje: str = "Los datos o el horario de la reserva no son válidos."):
        super().__init__(mensaje, codigo_error=405)

