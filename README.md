# [Google's Business Messages: Python Client](https://github.com/google-business-communications/python-businessmessages)

[Business Messages](https://developers.google.com/business-communications/business-messages/guides/learn) is a mobile conversational channel that combines entry points on Google Maps, Search, and brand websites to create rich, asynchronous messaging experiences.

This document contains an [API reference](https://developers.google.com/business-communications/business-messages/reference/rest), samples, and other resources useful to developing Python applications.
For additional help developing Business Messages applications, in Python and other languages, see our
[Business Messages quickstart](https://developers.google.com/business-communications/business-messages/guides/quickstarts/echo-agent)
guide.

## Documentation

The documentation for the Business Messages API can be found [here](https://developers.google.com/business-communications/business-messages/reference/rest).

## Quickstart

### Before you begin

1.  [Register with Business Messages](https://developers.google.com/business-communications/business-messages/guides/set-up/register).
1.  Once registered, follow the instructions to [enable the APIs for your project](https://developers.google.com/business-communications/business-messages/guides/set-up/register#enable-api).

### Installation

#### Mac/Linux

```
python -m venv <your-env>
source <your-env>/bin/activate
<your-env>/bin/pip install google-businessmessages
```

#### Windows

```
python -m venv <your-env>
<your-env>\Scripts\activate
<your-env>\Scripts\pip.exe install google-businessmessages
```

### Supported Python Versions

Python 3.5, 3.6 and 3.7, and 3.8 are fully supported and tested.

### Using the client library

```python
from businessmessages import businessmessages_v1_client as bm_client
from businessmessages.businessmessages_v1_messages import (
    BusinessmessagesConversationsMessagesCreateRequest,
    BusinessMessagesMessage,
    BusinessMessagesRepresentative)

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'your-service-account-key-file-location',
    scopes=['https://www.googleapis.com/auth/businessmessages'])

client = bm_client.BusinessmessagesV1(credentials=credentials)

conversation_id = 'valid-conversation-id'

message = BusinessMessagesMessage(
    messageId=str(uuid.uuid4().int),
    representative=BusinessMessagesRepresentative(
        representativeType=BusinessMessagesRepresentative.RepresentativeTypeValueValuesEnum.BOT
    ),
    text='Hello, World!')

# Create the message request
create_request = BusinessmessagesConversationsMessagesCreateRequest(
    businessMessagesMessage=message,
    parent='conversations/' + conversation_id)

# Send the message
bm_client.BusinessmessagesV1.ConversationsMessagesService(
    client=client).Create(request=create_request)
```

## Sample usage

Samples below assume a similar library initialization as shown in the [Using the client library](https://github.com/google-business-communications/python-businessmessages#using-the-client-library) section.

### Sending a text message

```python
message = BusinessMessagesMessage(
    messageId=str(uuid.uuid4().int),
    representative=BusinessMessagesRepresentative(
        representativeType=BusinessMessagesRepresentative.RepresentativeTypeValueValuesEnum.BOT
    ),
    text='Hello, World!')

# Create the message request
create_request = BusinessmessagesConversationsMessagesCreateRequest(
    businessMessagesMessage=message,
    parent='conversations/' + conversation_id)

# Send the message
bm_client.BusinessmessagesV1.ConversationsMessagesService(
    client=client).Create(request=create_request)
```

### Sending a text message with suggested replies and actions

```python
message = BusinessMessagesMessage(
    messageId=str(uuid.uuid4().int),
    representative=BusinessMessagesRepresentative(
        representativeType=BusinessMessagesRepresentative.RepresentativeTypeValueValuesEnum.BOT
    ),
    text='Hello, World!',
    suggestions=[
        BusinessMessagesSuggestion(
            reply=BusinessMessagesSuggestedReply(
                text='Sample Chip',
                postbackData='sample_chip')
            ),
        BusinessMessagesSuggestion(
            action=BusinessMessagesSuggestedAction(
                text='URL Action',
                postbackData='url_action',
                openUrlAction=BusinessMessagesOpenUrlAction(
                    url='https://www.google.com'))
            ),
        BusinessMessagesSuggestion(
            action=BusinessMessagesSuggestedAction(
                text='Dial Action',
                postbackData='dial_action',
                dialAction=BusinessMessagesDialAction(
                    phoneNumber='+12223334444'))
            ),
        ])

# Create the message request
create_request = BusinessmessagesConversationsMessagesCreateRequest(
    businessMessagesMessage=message,
    parent='conversations/' + conversation_id)

# Send the message
bm_client.BusinessmessagesV1.ConversationsMessagesService(
    client=client).Create(request=create_request)
```

### Sending a rich card

```python
message = BusinessMessagesMessage(
    messageId=str(uuid.uuid4().int),
    representative=BusinessMessagesRepresentative(
        representativeType=BusinessMessagesRepresentative.RepresentativeTypeValueValuesEnum.BOT
    ),
    richCard=BusinessMessagesRichCard(
        standaloneCard=BusinessMessagesStandaloneCard(
            cardContent=BusinessMessagesCardContent(
                title='Business Messages!!!',
                description='This is an example rich card',
                suggestions=[
                  BusinessMessagesSuggestion(
                      reply=BusinessMessagesSuggestedReply(
                          text='Sample Chip',
                          postbackData='sample_chip')
                      )
                  ],
                media=BusinessMessagesMedia(
                    height=BusinessMessagesMedia.HeightValueValuesEnum.MEDIUM,
                    contentInfo=BusinessMessagesContentInfo(
                        fileUrl='https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png',
                        forceRefresh=False
                    ))
                ))))

# Create the message request
create_request = BusinessmessagesConversationsMessagesCreateRequest(
    businessMessagesMessage=message,
    parent='conversations/' + conversation_id)

# Send the message
bm_client.BusinessmessagesV1.ConversationsMessagesService(
    client=client).Create(request=create_request)
```

### Sending a carousel

```python
message = BusinessMessagesMessage(
    messageId=str(uuid.uuid4().int),
    representative=BusinessMessagesRepresentative(
        representativeType=BusinessMessagesRepresentative.RepresentativeTypeValueValuesEnum.BOT
    ),
    richCard=BusinessMessagesRichCard(
      carouselCard=BusinessMessagesCarouselCard(
        cardWidth=BusinessMessagesCarouselCard.CardWidthValueValuesEnum.MEDIUM,
        cardContents=[
          BusinessMessagesCardContent(
              title='Card #1',
              description='The description for card #1',
              suggestions=[
                BusinessMessagesSuggestion(
                        reply=BusinessMessagesSuggestedReply(
                            text='Card #1',
                            postbackData='card_1')
                        )
              ],
              media=BusinessMessagesMedia(
                  height=BusinessMessagesMedia.HeightValueValuesEnum.MEDIUM,
                  contentInfo=BusinessMessagesContentInfo(
                      fileUrl='https://storage.googleapis.com/kitchen-sink-sample-images/cute-dog.jpg',
                      forceRefresh=False))),
          BusinessMessagesCardContent(
              title='Card #2',
              description='The description for card #2',
              suggestions=[
                BusinessMessagesSuggestion(
                        reply=BusinessMessagesSuggestedReply(
                            text='Card #2',
                            postbackData='card_2')
                        )
              ],
              media=BusinessMessagesMedia(
                  height=BusinessMessagesMedia.HeightValueValuesEnum.MEDIUM,
                  contentInfo=BusinessMessagesContentInfo(
                      fileUrl='https://storage.googleapis.com/kitchen-sink-sample-images/elephant.jpg',
                      forceRefresh=False)))
        ]
    )
))

# Create the message request
create_request = BusinessmessagesConversationsMessagesCreateRequest(
    businessMessagesMessage=message,
    parent='conversations/' + conversation_id)

# Send the message
bm_client.BusinessmessagesV1.ConversationsMessagesService(
    client=client).Create(request=create_request)
```

## Samples

See the code examples to see example usage for most API features. The samples' `README.md` has instructions for running the samples.

| Sample                      | Source Code                       |
| --------------------------- | --------------------------------- |
| Echo Bot | [source code](https://github.com/google-business-communications/bm-python-echo-bot) |


## Contributing

Contributions welcome! See the [Contributing Guide](https://github.com/google-business-communications/python-businessmessages/CONTRIBUTING.md).

## License

Apache Version 2.0

See [LICENSE](https://github.com/google-business-communications/python-businessmessages/LICENSE)
