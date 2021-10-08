wrk.method = "POST"
wrk.body   = "{\"jsonrpc\":\"2.0\",\"method\":\"get_spent_transaction\",\"params\":[{\"outpoint\":{\"tx_hash\":\"0x6ed4024a1958c716b03b263cbfdeba1bfa70de673e5186a4f9bd5372641171c3\",\"index\":\"0x1\"},\"structure_type\":\"DoubleEntry\"}],\"id\":100}"
wrk.headers["Content-Type"] = "application/json"
