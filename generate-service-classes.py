import operator
import re
from os import path

from fastems import services


def _project_dir(file):
    return path.join(path.dirname(path.abspath(__file__)), file)


def generate_methods(service):
    methods = []

    print('Building %s Zeep Client' % service)
    client, history = services.build_client(service)

    for service in client.wsdl.services.values():
        for port in service.ports.values():
            operations = sorted(
                port.binding._operations.values(),
                key=operator.attrgetter('name'))

            for operation in operations:
                m = re.match(r'([a-zA-Z]+)\((.+)\)', str(operation))
# TODO: fix the generation of methods with no parameters
                if m:
                    param_def = m.group(2).split(', ')
                    methods.append({
                        'method_name': m.group(1),
                        'params': ', '.join([p.split(': ')[0] for p in param_def]),
                        'param_def': param_def
                    })
    return methods


class_template_file = _project_dir('fastems/services/py_templates/class.tmpl')
method_template_file = _project_dir('fastems/services/py_templates/method.tmpl')

if __name__ == '__main__':
    for service in services.__all__:
        service_class = _project_dir('fastems/services/%s.py' % service)

        methods = generate_methods(service)
        # print(methods)

        print('Creating %s' % service_class)
        with open(class_template_file, 'r') as class_template, \
            open(method_template_file, 'r') as method_template, \
            open(service_class, 'w') as new_class:

            method_str = method_template.read()

            new_class.write(class_template.read().format(service_name=service))
            new_class.write('\n')

            for method in methods:
                print('[%s] Adding %s()' % (service, method['method_name']))
                new_class.write(method_str.format(**method))

            new_class.write('\n')

        print('Done!\n')
