import logging
import os, sys
import time

format_string="[%(asctime)s: %(levelname)s, %(module)s : %(message)s]"

log_dir="LOG"
file_name=time.strftime('%m_%d_%Y_%H_%S')
file_path=os.path.join(os.getcwd(),log_dir, file_name)
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(level=logging.INFO, format=format_string, handlers=[
    logging.FileHandler(file_path),
    logging.StreamHandler(sys.stdout)
])

logger=logging.getLogger("credit_card_fraud_logger")