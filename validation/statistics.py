from marshmallow import ValidationError, Schema, fields

def positive(value):
  if value < 0:
    raise ValidationError('radius must be positive')

class StatsValidation(Schema):
  latitude = fields.Float(required=True)
  longitude = fields.Float(required=True)
  radius = fields.Float(required=True, validate=positive)

  def proccessErrorMessage(self, error):
    errorMessage = ''
    for field in error.messages.keys():
      msg = error.messages[field][0]
      if error.messages[field][0].startswith('Missing'):
        msg = 'Missing field "%s".' % field
      elif error.messages[field][0].startswith('Not a valid'):
        msg = '"%s" must be a valid %s' % (field, error.messages[field][0].split(' ')[-1])
      elif error.messages[field][0].startswith('Unknown'):
        msg = 'Unknown field "%s"' % field
      errorMessage = errorMessage + '\n' +msg
      return errorMessage