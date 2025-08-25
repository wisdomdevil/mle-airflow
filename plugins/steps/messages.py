from airflow.providers.telegram.hooks.telegram import TelegramHook

def send_telegram_failure_message(context): # на вход принимаем словарь с контекстными переменными
    hook = TelegramHook(token='8370947549:AAEsjqbnwOPAlYXVoof-wFOfmrpsBCEqxmw', chat_id='-1002706215104')
    dag = context['dag'].dag_id
    run_id = context['run_id']
    
    message = f'Исполнение DAG {dag} с id={run_id} прошло неудачно' # определение текста сообщения
    hook.send_message({
        'chat_id': '-1002706215104',
        'text': message
    }) # отправление сообщения 

def send_telegram_success_message(context): # на вход принимаем словарь с контекстными переменными
    hook = TelegramHook(token='8370947549:AAEsjqbnwOPAlYXVoof-wFOfmrpsBCEqxmw', chat_id='-1002706215104')
    dag = context['dag'].dag_id
    run_id = context['run_id']
    
    message = f'Исполнение DAG {dag} с id={run_id} прошло успешно!' # определение текста сообщения
    hook.send_message({
        'chat_id': '-1002706215104',
        'text': message
    }) # отправление сообщения 