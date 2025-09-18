import time
import json
import orjson


def benchmark(name, dumps_func, loads_func, data, iterations=1000000):  # type: ignore
    start = time.time()
    for _ in range(iterations):
        serialized = dumps_func(data)  # type: ignore
        deserialized = loads_func(serialized)  # type: ignore
    end = time.time()
    print(f"{name}: {end - start:.4f} 秒")


if __name__ == "__main__":
    test_data = {  # type: ignore
        "timestamp": 1556283673.1523004,
        "task_uuid": "0ed1a1c3-050c-4fb9-9426-a7e72d0acfc7",
        "task_level": [1, 2, 1],
        "action_status": "started",
        "action_type": "main",
        "key": "value",
        "another_key": 123,
        "and_another": ["a", "b"],
        "none_value": None,
    }

    # 測試 json
    benchmark("json", json.dumps, json.loads, test_data)

    # 測試 orjson (轉換 bytes 為 str 以公平比較)
    def orjson_dumps_wrapper(obj):  # type: ignore
        return str(orjson.dumps(obj), "utf-8")

    benchmark("orjson", orjson_dumps_wrapper, orjson.loads, test_data)
