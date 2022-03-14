import requests
import asyncio
import time
from typing import List


ISBNS = [
    9780007355143,
    9780008108298,
    9780547249643,
    9781405882583,
    9780316095860,
    9780930289232,
    9780486415871,
    9780765350381,
    9789898559425,
    9781944529024,
    9780765376671,
    9781400079988,
    9781438114026,
    9780393066258,
]


def print_book_info(index: int, isbn: str):
    """Our example of a syncronous request we want to parallelize"""
    url = "https://www.googleapis.com/books/v1/volumes"
    response = requests.get(f"{url}?q=isbn:{isbn}").json()
    title = response["items"][0]["volumeInfo"]["title"]
    print(f"{index}: {title}")


def sync_main(isbns: List[str] = ISBNS):
    """Sync version for printing all isbns"""
    for index, isbn in enumerate(isbns):
        print_book_info(index, isbn)


async def async_main_long(isbns: List[str] = ISBNS):
    for index, isbn in enumerate(isbns):
        await asyncio.get_event_loop().run_in_executor(
            None, print_book_info, index, isbn
        )


async def async_main_multi_line_loop(isbns: List[str] = ISBNS):
    for index in range(0, len(isbns), 2):
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, print_book_info, index, isbns[index])
        if index + 1 < len(isbns):
            await loop.run_in_executor(
                None, print_book_info, index + 1, isbns[index + 1]
            )


async def async_main_sep_tasks(isbns: List[str] = ISBNS):
    loop = asyncio.get_event_loop()
    tasks = [
        loop.run_in_executor(None, print_book_info, index, isbn)
        for index, isbn in enumerate(isbns)
    ]
    await asyncio.gather(*tasks)


# ------------------


def time_sync(func):
    """Time calls for parameterless syncronous functions"""
    start = time.time()
    func()
    end = time.time()
    return end - start


def time_async(func):
    loop = asyncio.get_event_loop()
    start = time.time()
    loop.run_until_complete(func())
    end = time.time()
    return end - start


# ---------------------


def main():
    funcs_to_time = [
        (sync_main, "sync"),
        (async_main_long, "async"),
        (async_main_multi_line_loop, "async"),
        (async_main_sep_tasks, "async"),
    ]
    timings = [
        time_sync(f) if ftype == "sync" else time_async(f) for f, ftype in funcs_to_time
    ]
    print("\n\n\n")
    for ((func, _), time_taken) in zip(funcs_to_time, timings):
        print(f"{func.__name__:30s} took {time_taken:.3f} seconds")


if __name__ == "__main__":
    main()
