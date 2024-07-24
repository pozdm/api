
def sorted_dict(d: dict) -> dict:
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=True))


def return_json(start_result: dict, end_result: dict) -> dict:
    keys = set()
    delta = dict()

    if isinstance(start_result, dict) and isinstance(end_result, dict):
        keys.update(start_result.keys())
        keys.update(end_result.keys())

        for key in keys:
            if key not in start_result:
                delta[key] = end_result[key]
            elif key not in end_result:
                delta[key] = -start_result[key]
            else:
                delta[key] = end_result[key] - start_result[key]

    return {
        "result_for_start_day": sorted_dict(start_result),
        "result_for_end_day": sorted_dict(end_result),
        "delta": sorted_dict(delta)
    }
