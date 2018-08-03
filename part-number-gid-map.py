import utils
import fastems


plans = fastems.get_all_process_plans()

part_number_gids = [{'part_number': plan['Name'],'gid': plan['Id']} for plan in plans]

utils.pretty_print_json(part_number_gids)
