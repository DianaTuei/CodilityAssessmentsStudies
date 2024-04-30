def function(arrayofusers, targetid):
    unread_messages = []
    read_messages = []

    for user in arrayofusers:
        if user["id"] == targetid:
            for message in user["messages"]:
                if not message["read"]:
                    unread_messages.append(message)
                else:
                    read_messages.append(message)
    
    # Sort unread messages before read messages and sort both by msg_id
    sorted_messages = sorted(unread_messages, key=lambda x: x.get("msg_id", 0)) + sorted(read_messages, key=lambda x: x.get("msg_id", 0))

    for message in sorted_messages:
        print(message)
    
    return sorted_messages

# Provided users array
users = [
    {
        "id": 30,
        "username": "Ruth.Nduta",
        "email": "ruthnduta891@gmail.com",
        "messages": [
            {"msg_id": 45, "read": False, "user_id": 30},
            {"msg_id": 30, "read": True, "user_id": 30},
            {"msg_id": 112, "read": False, "user_id": 30}
        ]
    },
    {
        "id": 31,
        "username": "Pascaline.Chumba",
        "email": "pjerono56@gmail.com",
        "messages": []
    },
    {
        "id": 45,
        "username": "Josephbill",
        "email": "josephbill00@gmail.com",
        "messages": [
            {"msg_id": 31, "read": True, "user_id": 45}
        ]
    },
    {
        "id": 26,
        "username": "Simon.Thuo",
        "email": "simonthuo85@gmail.com",
        "messages": []
    },
    {
        "id": 112,
        "username": "Christine.Kiage",
        "email": "christinekiage@gmail.com",
        "messages": [
            {"msg_id": 45, "read": False, "user_id": 27},
            {"msg_id": 3, "read": False, "user_id": 27},
            {"msg_id": 112, "read": False, "user_id": 27}
        ]
    }
]

# Target user ID
target_user_id = 30

sorted_messages = function(users, target_user_id)
