wrk.method = "POST"
wrk.body   = "{\"jsonrpc\":\"2.0\",\"method\":\"query_generic_transactions\",\"params\":[{\"address\":{\"KeyAddress\":\"ckt1qyqg6y6utyjqhc3znvv7as97tgqxkd9nkr9ssuxft0\"},\"udt_hashes\":[\"0xf21e7350fa9518ed3cbb008e0e8c941d7e01a12181931d5608aa366ee22228bd\"]}],\"id\":100}"
wrk.headers["Content-Type"] = "application/json"
