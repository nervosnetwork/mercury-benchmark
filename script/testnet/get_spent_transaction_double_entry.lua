wrk.method = "POST"
wrk.body   = "{\"jsonrpc\":\"2.0\",\"method\":\"get_spent_transaction\",\"params\":[{\"outpoint\":{\"tx_hash\":\"baea5058401c63e1eaaf33ef9155afaf6c57be038e8599f1d4e59fb24b63e512\",\"index\":\"0\"},\"view_type\":\"TransactionView\"}],\"id\":100}"
wrk.headers["Content-Type"] = "application/json"