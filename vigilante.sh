#!/bin/bash

# Configuración
LOG_FILE="/var/log/auth.log"
PYTHON_SCRIPT="/home/tecnico/ai_log_watcher/analizador.py"
VENV_PATH="/home/tecnico/ai_log_watcher/venv/bin/python"
COOLDOWN=600 # 10 minutos en segundos
ULTIMA_CONSULTA=0

echo "🛡️ Vigilante inteligente activado (Cooldown: $COOLDOWN seg)..."

sudo tail -n 0 -f $LOG_FILE | while read LINE
do
    if [[ "$LINE" == *"Failed password"* ]]; then
        AHORA=$(date +%s)
        TIEMPO_PASADO=$((AHORA - ULTIMA_CONSULTA))

        if [ $TIEMPO_PASADO -ge $COOLDOWN ]; then
            echo "⚠️ Ataque detectado. Consultando a la IA..."
            $VENV_PATH $PYTHON_SCRIPT "$LINE"
            ULTIMA_CONSULTA=$AHORA
        else
            SEGUNDOS_RESTANTES=$((COOLDOWN - TIEMPO_PASADO))
            echo "⏳ Ataque ignorado (en enfriamiento). Faltan $SEGUNDOS_RESTANTES seg para volver a usar la IA."
        fi
    fi
done
