import operator
import re

import services
from services import build_client

class_template_file = './py_templates/class.tmpl'
method_template_file = './py_templates/method.tmpl'


def generate_methods(service):
    methods = []

    print('Building %s Zeep Client' % service)
    client, history = build_client(service)

    for service in client.wsdl.services.values():
        for port in service.ports.values():
            operations = sorted(
                port.binding._operations.values(),
                key=operator.attrgetter('name'))

            for operation in operations:
                m = re.match(r'([a-zA-Z]+)\((.+)?\)', str(operation))

                if m:
                    param_def = ''
                    params = ''
                    comma = ''

                    if m.group(2):
                        param_def = m.group(2).split(', ')
                        params = ', '.join([p.split(': ')[0] for p in param_def])

                        comma = ', '

                    methods.append({
                        'method_name': m.group(1),
                        'comma': comma,
                        'params': params,
                        'param_def': param_def
                    })
    return methods


for service in services.__all__:
    service_class_file = './%s.py' % service
    methods = generate_methods(service)
    # print(methods)

    print('Creating %s' % service_class_file)
    with open(class_template_file, 'r') as class_template, \
            open(method_template_file, 'r') as method_template, \
            open(service_class_file, 'w') as new_class:

        method_str = method_template.read()

        new_class.write(class_template.read().format(service_name=service))
        new_class.write('\n')

        for method in methods:
            print('[%s] Adding %s()' % (service, method['method_name']))
            new_class.write(method_str.format(**method))

        new_class.write('\n')

    print('Done!\n')
