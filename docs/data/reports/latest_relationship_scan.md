# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T13:37:34.497849+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2572`

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

- `market_context_high->unknown_1h` score `12696.2158` n `103` status `ready` deltaP `0.2529` edge `1058.0361` maxDD `-0.9174`
- `market_context_high->unknown_4h` score `7931.1264` n `103` status `ready` deltaP `-0.2975` edge `660.9576` maxDD `-0.6067`
- `market_context_high->crypto_major_24h` score `25.1118` n `89` status `ready` deltaP `45.9114` edge `1.8459` maxDD `-2.746`
- `market_context_high->crypto_alt_24h` score `11.6171` n `89` status `ready` deltaP `23.7671` edge `1.4702` maxDD `-7.4749`
- `market_context_high->crypto_major_4h` score `1.8213` n `103` status `ready` deltaP `3.5342` edge `0.4101` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `1.154` n `103` status `ready` deltaP `4.2964` edge `0.2751` maxDD `-12.9396`
- `market_context_high->metal_4h` score `0.4195` n `103` status `ready` deltaP `17.9922` edge `0.044` maxDD `-5.9858`
- `market_context_high->metal_24h` score `0.301` n `89` status `ready` deltaP `18.3482` edge `0.2116` maxDD `-14.7068`
- `market_context_high->metal_1h` score `-0.1592` n `103` status `ready` deltaP `4.7497` edge `0.0144` maxDD `-2.6517`
- `market_context_high->crypto_major_1h` score `-0.3146` n `103` status `ready` deltaP `3.7018` edge `0.0831` maxDD `-7.1826`
- `market_context_high->index_1h` score `-0.4291` n `103` status `ready` deltaP `0.9389` edge `0.0041` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-0.6763` n `103` status `ready` deltaP `-1.0799` edge `0.0427` maxDD `-5.4428`
- `market_context_high->index_4h` score `-1.2754` n `103` status `ready` deltaP `-3.9116` edge `-0.0031` maxDD `-4.7471`
- `market_context_high->fx_1h` score `-1.4329` n `103` status `ready` deltaP `-9.6637` edge `-0.0005` maxDD `-0.3584`
- `market_context_high->equity_1h` score `-1.8851` n `103` status `ready` deltaP `3.8515` edge `0.0001` maxDD `-10.9626`
- `market_context_high->fx_4h` score `-2.3687` n `103` status `ready` deltaP `-14.6963` edge `-0.0037` maxDD `-1.8272`
- `market_context_high->commodity_1h` score `-2.4378` n `103` status `ready` deltaP `-10.0401` edge `-0.0284` maxDD `-3.9584`
- `market_context_high->fx_24h` score `-6.9184` n `89` status `ready` deltaP `-21.1084` edge `-0.0085` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-8.2649` n `103` status `ready` deltaP `-30.1578` edge `-0.1258` maxDD `-14.9509`
- `market_context_high->equity_4h` score `-9.4985` n `103` status `ready` deltaP `-8.3812` edge `-0.0647` maxDD `-43.344`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
