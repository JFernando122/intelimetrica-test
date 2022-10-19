from marshmallow import Schema, fields, ValidationError

def validateRating(value):
  if value < 0 or value > 4 or not isinstance(value, int):
    raise ValidationError('Rating must be an integer between 0 and 4')

class RestuarantValidation(Schema):
  rating = fields.Integer(required=True, validate=validateRating, strict=True)
  name = fields.Str(required=True)
  site = fields.Url(required=True)
  email = fields.Email(required=True)
  phone = fields.Str(required=True)
  street = fields.Str(required=True)
  city = fields.Str(required=True)
  state = fields.Str(required=True)
  lat = fields.Float(required=True)
  lng = fields.Float(required=True)

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