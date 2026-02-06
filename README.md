# AI-Log-Watcher: Monitorización de Seguridad con Gemini 2.0

## 📖 Descripción
Este proyecto es un sistema de detección de intrusiones (IDS) ligero diseñado para servidores Ubuntu. Utiliza un script en **Bash** para vigilar los logs del sistema en tiempo real y un script en **Python** que integra la IA de **Google Gemini** para analizar ataques de fuerza bruta.

## 🚀 Cómo funciona
1. El script `vigilante.sh` monitoriza `/var/log/auth.log` buscando intentos fallidos de SSH.
2. Al detectar un ataque, extrae la línea del log y la envía a `analizador.py`.
3. La IA analiza la gravedad y sugiere medidas de mitigación inmediatas (como reglas de firewall).

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
