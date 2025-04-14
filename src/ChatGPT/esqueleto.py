import sys
import openai
import time
import os  # Importa el módulo os para manejar variables de entorno

# Obtén la clave de API desde una variable de entorno
API_KEY = os.getenv("OPENAI_API_KEY")

# Verifica si la clave fue cargada correctamente
if API_KEY is None:
    print("Error: La clave de la API de OpenAI no se encontró en las variables de entorno.")
    sys.exit(1)

openai.api_key = API_KEY

def main():
    """
    Función principal que maneja el ciclo de entrada del usuario, 
    realiza las consultas a la API de OpenAI y muestra las respuestas.
    """
    last_query = None

    while True:
        try:
            if last_query:
                print(f"Última consulta: {last_query}")

            user_input = input("Ingrese su consulta o presione 'flecha arriba' para editar la última consulta: ").strip()

            if not user_input and last_query:
                user_input = last_query
            elif not user_input:
                print("Error: No hay ninguna consulta anterior para editar.")
                continue

            print(f"You: {user_input}")

            retries = 0
            max_retries = 5
            while retries < max_retries:
                try:
                    response = openai.ChatCompletion.create(
                        model="gpt-4",
                        messages=[
                            {"role": "system", "content": "Eres un asistente útil."},
                            {"role": "user", "content": user_input}
                        ],
                        temperature=0.7
                    )

                    choices = response.get('choices', [])
                    if choices:
                        reply = choices[0].get('message', {}).get('content', '').strip()
                        print(f"chatGPT: {reply}")
                        last_query = user_input
                        break
                    else:
                        print("Error: No se recibió una respuesta válida de la API.")
                        break

                except openai.error.RateLimitError:
                    retries += 1
                    print(f"Error de límite de tasa. Intentando nuevamente... ({retries}/{max_retries})")
                    time.sleep(2)  # Espera 2 segundos antes de intentar de nuevo
                except openai.error.OpenAIError as e:
                    print(f"Error con la API de OpenAI: {e}")
                    break
                except Exception as e:
                    print(f"Error desconocido: {e}")
                    break

        except Exception as e:
            print(f"Error al aceptar la consulta del usuario: {e}")
            continue

if __name__ == "__main__":
    main()
