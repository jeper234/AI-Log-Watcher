import google.generativeai as genai
import sys

# Configuración limpia
API_KEY = "TU_API_KEY_AQUI"
genai.configure(api_key=API_KEY)

# Usamos el modelo más estable del Free Tier
model = genai.GenerativeModel('gemini-2.0-flash')

def analizar():
    # Línea de prueba estática para no fallar
    log_line = sys.argv[1] if len(sys.argv) > 1 else "Error de prueba"
    
    print(f"📡 Enviando solicitud única a Google...")
    try:
        response = model.generate_content(
            f"Brevemente, analiza este log de seguridad: {log_line}"
        )
        print("\n✅ RESPUESTA:")
        print(response.text)
    except Exception as e:
        print(f"\n❌ Error de cuota o conexión. Espera un poco más. \nDetalle: {e}")

if __name__ == "__main__":
    analizar()
