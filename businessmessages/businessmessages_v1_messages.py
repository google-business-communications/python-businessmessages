"""Generated message classes for businessmessages version v1.

"""
# NOTE: This file is autogenerated and should not be edited by hand.

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding


package = 'businessmessages'


class BusinessMessagesCardContent(_messages.Message):
  r"""Card content.

  Fields:
    description: Optional. Description of the card. Maximum 2000 characters.
    media: Optional. Media to include in the card.
    suggestions: Optional. List of suggestions to include in the card. Maximum
      4 suggestions.
    title: Optional. Title of the card. Maximum 200 characters.
  """

  description = _messages.StringField(1)
  media = _messages.MessageField('BusinessMessagesMedia', 2)
  suggestions = _messages.MessageField('BusinessMessagesSuggestion', 3, repeated=True)
  title = _messages.StringField(4)


class BusinessMessagesCarouselCard(_messages.Message):
  r"""Carousel of cards.

  Enums:
    CardWidthValueValuesEnum: The width of the cards in the carousel.

  Fields:
    cardContents: The list of contents for each card in the carousel. A
      carousel can have a minimum of 2 cards and a maximum 10 cards.
    cardWidth: The width of the cards in the carousel.
  """

  class CardWidthValueValuesEnum(_messages.Enum):
    r"""The width of the cards in the carousel.

    Values:
      CARD_WIDTH_UNSPECIFIED: Not specified
      SMALL: 120 DP. Can't include tall media.
      MEDIUM: 232 DP.
    """
    CARD_WIDTH_UNSPECIFIED = 0
    SMALL = 1
    MEDIUM = 2

  cardContents = _messages.MessageField('BusinessMessagesCardContent', 1, repeated=True)
  cardWidth = _messages.EnumField('CardWidthValueValuesEnum', 2)


class BusinessMessagesContentInfo(_messages.Message):
  r"""Message containing the content information.

  Fields:
    altText: Text describing the details about the media for accessibility
      purposes.
    fileUrl: Publicly reachable URL of the file. The platform determines the
      MIME type of the file from the content-type field in the HTTP headers
      when the platform fetches the file. The content-type field must be
      present and accurate in the HTTP response from the URL.  Maximum 5 MB.
      Supported content types: image/jpeg, image/jpg, image/png
    forceRefresh: If set, the platform fetches the file and thumbnail from the
      specified URLs, even if the platform has cached copies of the file
      (and/or of the thumbnail).
    thumbnailUrl: Optional. Publicly reachable URL of the thumbnail.  If you
      don't provide a thumbnail URL, the platform displays a blank placeholder
      thumbnail until the user's device downloads the file.  Maximum 25 KB.
      Supported content types: image/jpeg, image/jpg, image/png
  """

  altText = _messages.StringField(1)
  fileUrl = _messages.StringField(2)
  forceRefresh = _messages.BooleanField(3)
  thumbnailUrl = _messages.StringField(4)


class BusinessMessagesDialAction(_messages.Message):
  r"""Opens the user's default dialer app with the specified phone number
  filled in.

  Fields:
    phoneNumber: Required. The specified phone number, in [RFC
      3966](https://tools.ietf.org/html/rfc3966) format. For example,
      "+1-201-555-0123".
  """

  phoneNumber = _messages.StringField(1)


class BusinessMessagesEvent(_messages.Message):
  r"""An event in a conversation between an agent and a user.

  Enums:
    EventTypeValueValuesEnum: The type of the event.

  Fields:
    eventType: The type of the event.
    name: The name of the event, as set by Business Messages. Resolves to
      "conversations/{conversationId}/events/{eventId}", where
      {conversationId} is the unique ID for the conversation and {eventId} is
      the unique ID for the event.
    representative: Details about the representative (human or chatbot) that
      sent the event.
  """

  class EventTypeValueValuesEnum(_messages.Enum):
    r"""The type of the event.

    Values:
      EVENT_TYPE_UNSPECIFIED: Not specified.
      TYPING_STARTED: The representative is typing.
      TYPING_STOPPED: The representative stopped typing.
      REPRESENTATIVE_JOINED: The representative joined the conversation.
      REPRESENTATIVE_LEFT: The representative left the conversation.
    """
    EVENT_TYPE_UNSPECIFIED = 0
    TYPING_STARTED = 1
    TYPING_STOPPED = 2
    REPRESENTATIVE_JOINED = 3
    REPRESENTATIVE_LEFT = 4

  eventType = _messages.EnumField('EventTypeValueValuesEnum', 1)
  name = _messages.StringField(2)
  representative = _messages.MessageField('BusinessMessagesRepresentative', 3)


class BusinessMessagesLiveAgentRequest(_messages.Message):
  r"""When tapped, sends a request for a live agent to join the conversation.
  """



class BusinessMessagesMedia(_messages.Message):
  r"""A media file within a rich card.

  Enums:
    HeightValueValuesEnum: The height of the media within a rich card.

  Fields:
    contentInfo: Information about a file, including the URL of the file and
      the URL of the file's thumbnail.
    height: The height of the media within a rich card.
  """

  class HeightValueValuesEnum(_messages.Enum):
    r"""The height of the media within a rich card.

    Values:
      HEIGHT_UNSPECIFIED: Not specified.
      SHORT: 112 DP.
      MEDIUM: 168 DP.
      TALL: 264 DP. Not available for rich card carousels when the card width
        is set to SMALL.
    """
    HEIGHT_UNSPECIFIED = 0
    SHORT = 1
    MEDIUM = 2
    TALL = 3

  contentInfo = _messages.MessageField('BusinessMessagesContentInfo', 1)
  height = _messages.EnumField('HeightValueValuesEnum', 2)


class BusinessMessagesMessage(_messages.Message):
  r"""A message in a conversation between an agent and a user.

  Fields:
    fallback: Optional. Fallback text that displays if the user's device
      doesn't support the message type or content.
    messageId: The unique identifier of the message, assigned by the agent. If
      a message attempts to use the same `messageId` as a previous message,
      Business Messages returns an `ALREADY_EXISTS` error.
    name: The name of the message, as set by Business Messages. Resolves to
      "conversations/{conversationId}/messages/{messageId}", where
      {conversationId} is the unique ID for the conversation and {messageId}
      is the unique ID for the message.
    representative: Details about the representative (human or chatbot) that
      sent the message.
    richCard: Rich Card message.
    suggestions: A list of suggested replies that appear as a list of
      suggestion chips following the associated message. Maximum 13
      suggestions.  The chips only display when the associated message is the
      most recent message within the conversation (including both agent and
      user messages). The user can tap a suggested reply to send the text
      reply to the agent.
    text: Text message.
  """

  fallback = _messages.StringField(1)
  messageId = _messages.StringField(2)
  name = _messages.StringField(3)
  representative = _messages.MessageField('BusinessMessagesRepresentative', 4)
  richCard = _messages.MessageField('BusinessMessagesRichCard', 5)
  suggestions = _messages.MessageField('BusinessMessagesSuggestion', 6, repeated=True)
  text = _messages.StringField(7)


class BusinessMessagesOpenUrlAction(_messages.Message):
  r"""Opens the specified URL.

  Fields:
    url: URL
  """

  url = _messages.StringField(1)


class BusinessMessagesRepresentative(_messages.Message):
  r"""Details about the representative (human or chatbot) that sent the
  message.

  Enums:
    RepresentativeTypeValueValuesEnum: Required. The type of representative.

  Fields:
    avatarImage: Optional. The representative's avatar image, as a publicly
      available URL. Displays as a circle.  Images must be 1024x1024 px and
      have a maximum files size of 50 KB.
    displayName: Optional. Name of the representative.
    representativeType: Required. The type of representative.
  """

  class RepresentativeTypeValueValuesEnum(_messages.Enum):
    r"""Required. The type of representative.

    Values:
      REPRESENTATIVE_TYPE_UNSPECIFIED: Unspecified representative type.
      BOT: Bot representative.
      HUMAN: Human representative.
    """
    REPRESENTATIVE_TYPE_UNSPECIFIED = 0
    BOT = 1
    HUMAN = 2

  avatarImage = _messages.StringField(1)
  displayName = _messages.StringField(2)
  representativeType = _messages.EnumField('RepresentativeTypeValueValuesEnum', 3)


class BusinessMessagesRichCard(_messages.Message):
  r"""A standalone rich card or a carousel of rich cards sent from the agent
  to the user.

  Fields:
    carouselCard: Carousel of cards.
    standaloneCard: Standalone card.
  """

  carouselCard = _messages.MessageField('BusinessMessagesCarouselCard', 1)
  standaloneCard = _messages.MessageField('BusinessMessagesStandaloneCard', 2)


class BusinessMessagesStandaloneCard(_messages.Message):
  r"""Standalone card.

  Fields:
    cardContent: Card content.
  """

  cardContent = _messages.MessageField('BusinessMessagesCardContent', 1)


class BusinessMessagesSuggestedAction(_messages.Message):
  r"""When tapped, initiates the corresponding native action on the device.

  Fields:
    dialAction: Opens the user's default dialer app.
    openUrlAction: Opens the specified URL.
    postbackData: The string that the agent receives when a user taps the
      suggested action.
    text: Text that is shown in the suggested action. Maximum 25 characters.
  """

  dialAction = _messages.MessageField('BusinessMessagesDialAction', 1)
  openUrlAction = _messages.MessageField('BusinessMessagesOpenUrlAction', 2)
  postbackData = _messages.StringField(3)
  text = _messages.StringField(4)


class BusinessMessagesSuggestedReply(_messages.Message):
  r"""When tapped, sends the text reply back to the agent.

  Fields:
    postbackData: The string that the agent receives when a user taps the
      suggested reply.
    text: Text that is shown in the suggested reply and sent to the agent when
      the user taps it. Maximum 25 characters.
  """

  postbackData = _messages.StringField(1)
  text = _messages.StringField(2)


class BusinessMessagesSuggestion(_messages.Message):
  r"""A suggestion within a chip list.

  Fields:
    action: A suggested action that initiates a native action on the device.
    liveAgentRequest: A request to have a live agent join the conversation.
    reply: A suggestion for the user to reply with specified text.
  """

  action = _messages.MessageField('BusinessMessagesSuggestedAction', 1)
  liveAgentRequest = _messages.MessageField('BusinessMessagesLiveAgentRequest', 2)
  reply = _messages.MessageField('BusinessMessagesSuggestedReply', 3)


class BusinessMessagesSurvey(_messages.Message):
  r"""A survey to measure customer satisfaction.

  Fields:
    name: The name of the survey, as set by Business Messages. Resolves to
      "conversations/{conversationId}/surveys/{surveyId}", where
      {conversationId} is the unique ID for the conversation and {surveyId} is
      the unique ID for the survey.
  """

  name = _messages.StringField(1)


class BusinessmessagesConversationsEventsCreateRequest(_messages.Message):
  r"""A BusinessmessagesConversationsEventsCreateRequest object.

  Fields:
    businessMessagesEvent: A BusinessMessagesEvent resource to be passed as
      the request body.
    eventId: The unique identifier of the event, assigned by the agent. If an
      event has the same `eventId` as a previous event in the conversation,
      Business Messages returns an `ALREADY_EXISTS` error.
    parent: Required. The conversation that contains the message. Resolves to
      "conversations/{conversationId}".
  """

  businessMessagesEvent = _messages.MessageField('BusinessMessagesEvent', 1)
  eventId = _messages.StringField(2)
  parent = _messages.StringField(3, required=True)


class BusinessmessagesConversationsMessagesCreateRequest(_messages.Message):
  r"""A BusinessmessagesConversationsMessagesCreateRequest object.

  Fields:
    businessMessagesMessage: A BusinessMessagesMessage resource to be passed
      as the request body.
    parent: Required. The conversation that contains the message. Resolves to
      "conversations/{conversationId}".
  """

  businessMessagesMessage = _messages.MessageField('BusinessMessagesMessage', 1)
  parent = _messages.StringField(2, required=True)


class BusinessmessagesConversationsSurveysCreateRequest(_messages.Message):
  r"""A BusinessmessagesConversationsSurveysCreateRequest object.

  Fields:
    businessMessagesSurvey: A BusinessMessagesSurvey resource to be passed as
      the request body.
    parent: Required. The conversation that contains the survey. Resolves to
      "conversations/{conversationId}".
    surveyId: The unique identifier of the survey, assigned by the agent. If a
      survey attempts to use the same `surveyId` as a previous survey,
      Business Messages returns an `ALREADY_EXISTS` error.
  """

  businessMessagesSurvey = _messages.MessageField('BusinessMessagesSurvey', 1)
  parent = _messages.StringField(2, required=True)
  surveyId = _messages.StringField(3)


class StandardQueryParameters(_messages.Message):
  r"""Query parameters accepted by all methods.

  Enums:
    FXgafvValueValuesEnum: V1 error format.
    AltValueValuesEnum: Data format for response.

  Fields:
    f__xgafv: V1 error format.
    access_token: OAuth access token.
    alt: Data format for response.
    callback: JSONP
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters.
    trace: A tracing token of the form "token:<tokenid>" to include in api
      requests.
    uploadType: Legacy upload protocol for media (e.g. "media", "multipart").
    upload_protocol: Upload protocol for media (e.g. "raw", "multipart").
  """

  class AltValueValuesEnum(_messages.Enum):
    r"""Data format for response.

    Values:
      json: Responses with Content-Type of application/json
      media: Media download with context-dependent Content-Type
      proto: Responses with Content-Type of application/x-protobuf
    """
    json = 0
    media = 1
    proto = 2

  class FXgafvValueValuesEnum(_messages.Enum):
    r"""V1 error format.

    Values:
      _1: v1 error format
      _2: v2 error format
    """
    _1 = 0
    _2 = 1

  f__xgafv = _messages.EnumField('FXgafvValueValuesEnum', 1)
  access_token = _messages.StringField(2)
  alt = _messages.EnumField('AltValueValuesEnum', 3, default=u'json')
  callback = _messages.StringField(4)
  fields = _messages.StringField(5)
  key = _messages.StringField(6)
  oauth_token = _messages.StringField(7)
  prettyPrint = _messages.BooleanField(8, default=True)
  quotaUser = _messages.StringField(9)
  trace = _messages.StringField(10)
  uploadType = _messages.StringField(11)
  upload_protocol = _messages.StringField(12)


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2')
