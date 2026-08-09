# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T12:07:27.866251+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9825`

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

- `market_context_high->equity_24h` score `3.84` n `103` status `ready` deltaP `4.5729` edge `0.5955` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.548` n `103` status `ready` deltaP `11.3437` edge `0.1943` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.0807` n `143` status `ready` deltaP `14.1374` edge `0.0631` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.7797` n `143` status `ready` deltaP `10.6916` edge `0.028` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.7325` n `103` status `ready` deltaP `21.4013` edge `0.0379` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.5218` n `103` status `ready` deltaP `8.4058` edge `0.164` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.3337` n `143` status `ready` deltaP `3.8462` edge `-0.0039` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.3668` n `143` status `ready` deltaP `-0.4951` edge `-0.0048` maxDD `-0.7809`
- `market_context_high->fx_4h` score `-0.5053` n `143` status `ready` deltaP `5.523` edge `-0.0036` maxDD `-1.6928`
- `market_context_high->metal_1h` score `-0.6565` n `143` status `ready` deltaP `-4.2889` edge `-0.006` maxDD `-0.9664`
- `market_context_high->index_4h` score `-0.7588` n `143` status `ready` deltaP `0.7612` edge `-0.0078` maxDD `-1.1743`
- `market_context_high->equity_1h` score `-0.8725` n `143` status `ready` deltaP `0.2618` edge `0.0084` maxDD `-4.6286`
- `market_context_high->metal_4h` score `-0.9575` n `143` status `ready` deltaP `-0.7462` edge `-0.0169` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-1.8317` n `143` status `ready` deltaP `-9.5348` edge `-0.0249` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.3679` n `143` status `ready` deltaP `0.1056` edge `-0.0643` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.0908` n `143` status `ready` deltaP `-10.2383` edge `-0.0571` maxDD `-7.2436`
- `market_context_high->crypto_alt_4h` score `-3.5209` n `143` status `ready` deltaP `-6.2948` edge `-0.0858` maxDD `-6.585`
- `market_context_high->crypto_major_24h` score `-3.7089` n `103` status `ready` deltaP `3.4419` edge `-0.0826` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-5.7399` n `103` status `ready` deltaP `-15.9183` edge `-0.2279` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-7.7346` n `143` status `ready` deltaP `-5.1956` edge `-0.5652` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
