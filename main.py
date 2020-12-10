import boto3
import time


def limpa_fila(queue_name):
    queue = boto3.resource('sqs').get_queue_by_name(QueueName=queue_name)

    if queue is not None:
        count_message = queue.attributes['ApproximateNumberOfMessages']
        print('Total de mensagens a serem deletadas: {}' .format(count_message))
        url = queue.url

        client = boto3.client('sqs')
        response = client.purge_queue(QueueUrl=url)

        print('Fila limpa com sucesso')
        time.sleep(60)


def main(context, event):
    nome_fila_desejada = 'queueCipReceivablesAdjustmentAliasBankDLQ'
    limpa_fila(nome_fila_desejada)


if __name__ == "__main__":
    record = ""
    main(record, "")
