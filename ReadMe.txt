# Sistema de reservas para un Motel

El software "MotelGestor" es una potente herramienta programada en Python que facilita la gestión integral de reservas,
informes y facturas para un motel. Diseñado para optimizar la eficiencia operativa, este sistema permite a los propietarios
y administradores llevar un control preciso de todas las operaciones diarias.

Características destacadas:
    Gestión de Reservas: Permite realizar y gestionar reservas de habitaciones de manera fácil y rápida, evitando conflictos de disponibilidad.
    Informes Detallados: Genera informes personalizados con datos relevantes sobre ocupación, ingresos y estadísticas, para una toma de decisiones informada.
    Facturación Automatizada: Agiliza el proceso de facturación mediante la generación automática de facturas y recibos para los clientes.
    Seguridad y Confidencialidad: Garantiza la protección de la información con un sistema de acceso seguro y restricciones de usuarios.

Con el software "MotelGestor", administrar un motel se convierte en una tarea sencilla y organizada, mejorando la experiencia tanto para el personal como para los clientes.
Simplifica la gestión diaria y proporciona una visión integral de las operaciones para lograr un motel más rentable y exitoso.


## Estructura del Proyecto

Bases de datos:
    * Tabla de usuarios
    nombre = udb.cipher
    divisor = "|"
    [linea][0] = Usuario
    [linea][1] = Contraseña

    * Tabla de cuartos
    nombre = rooms.cipher
    divisor_día = "/": 7 días
    divisor_hora = "|": 24 horas
    [dia][hora][0-24] = 0 : Ocupado
    [dia][hora][0-24] = 1 : Disponible