import os
import sys  # <--- ¡Asegúrate de tener ambos!
import google.generativeai as genai

# Cargamos la clave desde el sistema (Seguridad)
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ Error: Configura la variable GEMINI_API_KEY")
    sys.exit(1)

genai.configure(api_key=api_key)
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
