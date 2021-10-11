import boto3

sqs = boto3.resource('sqs')

# Retrieving a queue by its name
#queue = sqs.get_queue_by_name(QueueName='standard-queue')
queue = sqs.get_queue_by_name(QueueName='queue.fifo')

# Create a new message
#Sending 1-20
for number in range(1, 21):
    print(f"Sending {number}")
    response = queue.send_message(MessageBody=str(number), MessageGroupId="reqGroup", MessageDeduplicationId = str(number))

    # The response is not a resource, but gives you a message ID and MD5
    print("MessageId created: {0}".format(response.get('MessageId')))
    print("MD5 created: {0}".format(response.get('MD5OfMessageBody')))
