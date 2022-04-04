def paginate(data, pagenum, pagesize):
    num_pages = len(data) // pagesize
    rem_data = len(data) % pagesize
    if rem_data != 0:
        num_pages += 1
    if pagenum <= num_pages:
        data_end = pagenum * pagesize
        data_start = data_end - pagesize
        items = data[data_start:data_end]
        pagination = {"current_item_count": len(items), "current_page_number": pagenum, "pagination_size": pagesize,
                      "total_item_count": len(data), "total_page_count": num_pages}
        return {"items": items, "pagination": pagination}
    else:
        return None
