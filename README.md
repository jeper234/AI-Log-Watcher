# AI-Log-Watcher: Monitorización de Seguridad con Gemini 2.0

## 📖 Descripción
Este proyecto es un sistema de detección de intrusiones (IDS) ligero diseñado para servidores Ubuntu. Utiliza un script en **Bash** para vigilar los logs del sistema en tiempo real y un script en **Python** que integra la IA de **Google Gemini** para analizar ataques de fuerza bruta.

## 🚀 Flujo de Trabajo
1. **Monitorización:** `vigilante.sh` emplea `tail -f` sobre `/var/log/auth.log` filtrando intentos fallidos de SSH.
2. **Análisis:** Al detectar un evento, el script Python invoca la API de Gemini 2.0 Flash.
3. **Respuesta:** La IA desglosa el ataque y propone reglas de `iptables` o configuraciones de `fail2ban`.

## 🛠️ Tecnologías
- **SO:** Ubuntu Server
- **Lenguajes:** Bash & Python 3.12
- **IA:** Google Generative AI (Gemini 2.0 Flash)
- **Seguridad:** Gestión de logs (auth.log) y permisos de Linux

## 🔧 Instalación y Uso
1. Clona el repositorio.
2. Crea un entorno virtual e instala las dependencias:
   ```bash
   pip install -r requirements.txt

## 🔧 Configuración
Para proteger la integridad del sistema, la API Key se gestiona como variable de entorno:
```bash
export GEMINI_API_KEY="tu_clave_de_google_cloud"   

## Resultados de la Simulación 

**1. Captura del evento en la terminal:**
```bash
(venv) tecnico@srv-log-ia:~/ai_log_watcher$ sudo ./vigilante.sh
[sudo] password for tecnico:
🛡️ Vigilante inteligente activado (Cooldown: 600 seg)...
⚠️ Ataque detectado. Consultando a la IA...
/home/tecnico/ai_log_watcher/analizador.py:1: FutureWarning:

All support for the `google.generativeai` package has ended. It will no longer be receiving
updates or bug fixes. Please switch to the `google.genai` package as soon as possible.
See README for more details:

https://github.com/google-gemini/deprecated-generative-ai-python/blob/main/README.md

  import google.generativeai as genai
🔍 Consultando al experto de guardia...

✅ INFORME DE SEGURIDAD:
De acuerdo, analicemos este log de seguridad y cómo bloquear el origen del ataque.

**Análisis del Log:**

*   **Fecha y Hora:** `2026-02-07T13:13:07.840784+00:00` - Indica la fecha y hora en que se generó el evento (7 de febrero de 2026, 13:13:07 UTC).
*   **Host:** `srv-log-ia` - El nombre del servidor donde se produjo el evento.
*   **Proceso:** `sshd[1563]` - El proceso `sshd` (Servidor SSH) con el ID de proceso 1563 generó el log.
*   **Mensaje:** `Failed password for invalid user tesnico from 192.168.40.1 port 55389 ssh2` - Este es el mensaje clave:
    *   `Failed password`: Indica un intento fallido de inicio de sesión.
    *   `invalid user tesnico`: Se intentó iniciar sesión con un usuario no válido o inexistente llamado "tesnico".  Esto es una señal de escaneo de usuarios comunes.
    *   `from 192.168.40.1`: La dirección IP del atacante es 192.168.40.1.
    *   `port 55389`: El puerto de origen del atacante.
    *   `ssh2`: El protocolo SSH utilizado (versión 2).

**Conclusión Inicial:**

Este log indica un intento de inicio de sesión fallido a través de SSH con un usuario inválido, proveniente de la dirección IP 192.168.40.1.  Esto sugiere un ataque de fuerza bruta o un escaneo en busca de nombres de usuario vulnerables.  Es una actividad maliciosa.```
