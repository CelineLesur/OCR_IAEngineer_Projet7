import logging
from opencensus.ext.azure.log_exporter import AzureLogHandler
from azure.monitor.opentelemetry import configure_azure_monitor
import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()
INSTRUMENTATION_KEY = os.getenv("APPLICATION_INSIGHTS_CONNECTION_STRING")

if not INSTRUMENTATION_KEY:
    print("❗ Erreur : Clé d'instrumentation non trouvée.")
else:
    print("✅ Clé d'instrumentation détectée.")

# Configurer les logs généraux
logging.basicConfig(level=logging.INFO)

# Configurer Application Insights
try:
    # Utilisez configure_azure_monitor pour gérer les logs
    configure_azure_monitor(
        connection_string=INSTRUMENTATION_KEY,
        logger_name="insight-ocr-p7"
    )
    print("✅ Azure Monitor configuré avec succès.")
except Exception as e:
    print(f"❗ Erreur lors de la configuration d'Azure Monitor : {e}")

# Configurer le logger
logger = logging.getLogger("insight-ocr-p7")
logger.setLevel(logging.INFO)

# Vérifier si des handlers existent
if not logger.handlers:
    try:
        azure_handler = AzureLogHandler(connection_string=INSTRUMENTATION_KEY)
        azure_handler.setLevel(logging.INFO)
        logger.addHandler(azure_handler)
        print("✅ AzureLogHandler ajouté avec succès.")
    except Exception as e:
        print(f"❗ Erreur lors de l'ajout du AzureLogHandler: {e}")

# Gestion des feedbacks
def log_feedback(feedback, tweet):
    print(f"log_feedback appelé")
    if feedback == "negative":
        logger.warning(f"Feedback négatif reçu: {tweet}")
    else:
        logger.info(f"Feedback positif reçu: {tweet}")

# def send_alert_email():
#     logger.info("📧 Envoi d'un email d'alerte (simulation).")
#     # Simuler un envoi d'email via un service d'emailing comme SendGrid ou SMTP