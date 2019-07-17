
# TODO: use AIY API to do the vision stuff.
# Training a new model:
# https://www.hackster.io/dvillevald/transfer-learning-model-on-google-aiy-vision-kit-1aa600

#const KNOWN_PEOPLE_FILE = `${__dirname}/models/faces.json`;
#const KNOWN_PEOPLE = require(KNOWN_PEOPLE_FILE);
#const KNOWN_OBJECTS_FILE = `${__dirname}/models/faces.json`;
#const KNOWN_OBJECTS = require(KNOWN_OBJECTS_FILE);

class Result(object) :
  def __init__(self, success, answer=None, obj_type=None) :
    self.success = success
    self.answer = answer
    self.obj_type = obj_type

class Looker(object) :
  def __init__(self) :
    self.model = None
  def identify_it(self, obj_type) :
    #if obj_type == 'object' :
    #  return Result(True, answer="table", obj_type=obj_type)
    return Result(False, obj_type=obj_type)
    #return json.dumps({'success': True, 'answer':'Nick', 'what': 'person'})
