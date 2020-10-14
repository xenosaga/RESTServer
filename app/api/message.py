
def GetTimeMenu(title):
#   {
#       "type" : "template",
#       "altText" : "This is datetime picker",
#       "template" : {
#           "type" : "confirm",
#           "text" : "Select time",
#           "actions" : [
#               {
#                   "type" : "datetimepicker",
#                   "label" : "DateTime",
#                   "data" : "line_uid",
#                   "mode" : "datetime",
#                   "initial" : "2020-10-14t00:00",
#                   "max" : "2020-10-21t00:00",
#                   "min" : "2020-10-14t00:00"
#               }
#           ]
#       }
#   }

    __action = {}
    __action['type'] = 'datetimepicker'
    __action['label'] = "DateTime"
    __action['data'] = title
    __action['mode'] = 'datetime'
    __action['initial'] = '2020-10-14t00:00'
    __action['max'] = '2020-10-21t00:00'
    __action['min'] = '2020-10-14t00:00'

    _template = {}
    _template['type'] = 'confirm'
    _template['text'] = 'Select time'
    _template['actions'] = __action

    TimeMenuTemp = {}
    TimeMenuTemp['type'] = 'template'
    TimeMenuTemp['altText'] = 'This is datetime picker'
    TimeMenuTemp['template'] = _template

    return TimeMenuTemp