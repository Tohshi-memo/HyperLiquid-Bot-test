# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T09:00:29.304382+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8841`

## Conditions

- `news_risk_high`: News Risk is elevated.
- `macro_risk_high`: Macro Risk is elevated.
- `risk_on_high`: Risk-On score is elevated.
- `market_context_high`: Market Context is supportive.
- `polymarket_volume_spike`: Polymarket 24h volume z-score is elevated.
- `flow_alert_high`: Flow Alert score is elevated.
- `news_and_polymarket`: News Risk and Polymarket volume spike happen together.
- `risk_on_and_context`: Risk-On and Market Context are both supportive.
- `macro_and_flow`: Macro Risk and Flow Alert are elevated together.

## Top Patterns

- `market_context_high->equity_24h` score `3.7512` n `103` status `ready` deltaP `4.5729` edge `0.5881` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.6711` n `103` status `ready` deltaP `12.7326` edge `0.1953` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.173` n `143` status `ready` deltaP `15.0521` edge `0.0647` maxDD `-2.7169`
- `market_context_high->fx_24h` score `0.7774` n `103` status `ready` deltaP `21.575` edge `0.0425` maxDD `-1.9329`
- `market_context_high->commodity_1h` score `0.7749` n `143` status `ready` deltaP `10.6916` edge `0.0276` maxDD `-0.7439`
- `market_context_high->index_24h` score `0.5618` n `103` status `ready` deltaP `9.1002` edge `0.1645` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.2954` n `143` status `ready` deltaP `4.2953` edge `-0.0037` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.4143` n `143` status `ready` deltaP `-1.3933` edge `-0.0049` maxDD `-0.7809`
- `market_context_high->fx_4h` score `-0.4603` n `143` status `ready` deltaP `5.9803` edge `-0.0029` maxDD `-1.6928`
- `market_context_high->metal_1h` score `-0.6815` n `143` status `ready` deltaP `-4.738` edge `-0.0062` maxDD `-0.9664`
- `market_context_high->index_4h` score `-0.8904` n `143` status `ready` deltaP `-0.7632` edge `-0.0086` maxDD `-1.1743`
- `market_context_high->equity_1h` score `-0.9013` n `143` status `ready` deltaP `-0.0376` edge `0.008` maxDD `-4.6286`
- `market_context_high->metal_4h` score `-0.9575` n `143` status `ready` deltaP `-0.7462` edge `-0.0169` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-1.8916` n `143` status `ready` deltaP `-10.1336` edge `-0.0259` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.527` n `143` status `ready` deltaP `-1.4188` edge `-0.0674` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.0872` n `143` status `ready` deltaP `-10.2383` edge `-0.0568` maxDD `-7.2436`
- `market_context_high->crypto_major_24h` score `-3.3275` n `103` status `ready` deltaP `5.5253` edge `-0.0647` maxDD `-14.2873`
- `market_context_high->crypto_alt_4h` score `-3.5523` n `143` status `ready` deltaP `-6.4473` edge `-0.0874` maxDD `-6.585`
- `market_context_high->crypto_alt_24h` score `-5.0837` n `103` status `ready` deltaP `-13.835` edge `-0.1871` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-7.8113` n `143` status `ready` deltaP `-5.7944` edge `-0.5676` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
