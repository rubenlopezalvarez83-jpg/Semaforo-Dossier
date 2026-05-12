# Lista de preguntas del cuestionario del semáforo
# Cada pregunta tiene:
#   - pr:          número de pregunta
#   - texto:       lo que verá el ciudadano
#   - valor_si:    puntos si responde SÍ (señal clara de riesgo)
#   - valor_nose:  puntos si responde NO ESTOY SEGURO (señal dudosa)
#   - valor_no:    puntos si responde NO (sin riesgo)
# La suma de todos los valor_si es exactamente 100

PREGUNTAS = [
    {
        "pr": 1,
        "texto": "¿Le han contactado por un canal no oficial como SMS, WhatsApp o email desconocido?",
        "valor_si":    5,
        "valor_nose":  2,
        "valor_no":    0
    },
    {
        "pr": 2,
        "texto": "¿Le han pedido que actúe con urgencia o que dispone de muy poco tiempo para responder?",
        "valor_si":    8,
        "valor_nose":  4,
        "valor_no":    0
    },
    {
        "pr": 3,
        "texto": "¿Le han solicitado un código de verificación que le ha llegado por SMS?",
        "valor_si":   14,
        "valor_nose":  7,
        "valor_no":    0
    },
    {
        "pr": 4,
        "texto": "¿Le han pedido sus credenciales bancarias, contraseña o número de tarjeta?",
        "valor_si":   14,
        "valor_nose":  7,
        "valor_no":    0
    },
    {
        "pr": 5,
        "texto": "¿Quién le contacta dice ser su banco, la policía, Hacienda u otro organismo oficial?",
        "valor_si":    8,
        "valor_nose":  4,
        "valor_no":    0
    },
    {
        "pr": 6,
        "texto": "¿Le han pedido que mantenga la conversación en secreto o que no consulte con nadie?",
        "valor_si":   12,
        "valor_nose":  6,
        "valor_no":    0
    },
    {
        "pr": 7,
        "texto": "¿Le han enviado un enlace para que acceda a una página web y meta sus datos?",
        "valor_si":   11,
        "valor_nose":  5,
        "valor_no":    0
    },
    {
        "pr": 8,
        "texto": "¿Le han pedido que realice una transferencia a una cuenta que no conoce?",
        "valor_si":   14,
        "valor_nose":  7,
        "valor_no":    0
    },
    {
        "pr": 9,
        "texto": "¿El tono de la comunicación es amenazante o le advierte de consecuencias graves?",
        "valor_si":    8,
        "valor_nose":  4,
        "valor_no":    0
    },
    {
        "pr": 10,
        "texto": "¿Ha notado errores ortográficos o un lenguaje poco natural en el mensaje recibido?",
        "valor_si":    6,
        "valor_nose":  3,
        "valor_no":    0
    },
]

# Puntuación máxima posible = 100 (suma de todos los valor_si)
PUNTUACION_MAXIMA = 100

# Umbrales — directamente en puntos sobre 100, sin conversión necesaria
UMBRAL_VERDE    = 40   # menos de 40 → semáforo verde   (riesgo bajo)
UMBRAL_AMARILLO = 60   # entre 40 y 60 → semáforo amarillo (riesgo medio)
                       # más de 60 → semáforo rojo      (riesgo alto)