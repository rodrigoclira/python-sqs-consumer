import boto3

sqs = boto3.resource('sqs')

#queue = sqs.get_queue_by_name(QueueName='standard-queue')
queue = sqs.get_queue_by_name(QueueName='queue.fifo')

while 1:
    messages = queue.receive_messages(WaitTimeSeconds=5, MaxNumberOfMessages=5)

    if messages:
        print("Receiveing a new bunch of messages...")
        for message in messages:
            print("Message received: {0}".format(message.body))
            #message.delete()
    else:
        print("No messages available")
