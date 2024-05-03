import boto3

# Connect to DynamoDB
def connect_to_dynamodb():
    print("Connecting to DynamoDB...")
    try:
        dynamodb = boto3.resource('dynamodb')
        print("Connected to DynamoDB successfully!")
        return dynamodb
    except Exception as e:
        print(f"Error connecting to DynamoDB: {e}")
        return None

# Main function
if __name__ == "__main__":
    # Connect to DynamoDB
    dynamodb = connect_to_dynamodb()
    if dynamodb:
        # Perform DynamoDB operations
        try:
            # Example: list all tables
            print("Listing DynamoDB tables:")
            for table in dynamodb.tables.all():
                print(table.name)
        except Exception as e:
            print(f"Error performing DynamoDB operations: {e}")
