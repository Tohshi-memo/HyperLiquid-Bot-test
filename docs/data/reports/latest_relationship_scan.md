# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T14:52:31.898739+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11756`

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

- `market_context_high->metal_24h` score `1.474` n `110` status `ready` deltaP `5.5046` edge `0.1604` maxDD `-2.2743`
- `market_context_high->commodity_1h` score `0.7639` n `121` status `ready` deltaP `10.9294` edge `0.0324` maxDD `-1.3282`
- `market_context_high->commodity_4h` score `0.6565` n `111` status `ready` deltaP `10.9702` edge `0.0662` maxDD `-2.7703`
- `market_context_high->fx_24h` score `0.4376` n `110` status `ready` deltaP `19.6175` edge `0.0444` maxDD `-4.1933`
- `market_context_high->fx_1h` score `0.1519` n `121` status `ready` deltaP `9.2047` edge `-0.0021` maxDD `-1.0616`
- `market_context_high->fx_4h` score `-0.2645` n `111` status `ready` deltaP `7.5877` edge `0.0015` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.4393` n `121` status `ready` deltaP `-1.5205` edge `-0.0069` maxDD `-1.1422`
- `market_context_high->index_24h` score `-0.7702` n `110` status `ready` deltaP `0.4189` edge `0.0885` maxDD `-5.7715`
- `market_context_high->crypto_alt_1h` score `-0.8271` n `121` status `ready` deltaP `-4.5331` edge `-0.0129` maxDD `-2.3669`
- `market_context_high->metal_4h` score `-0.8858` n `111` status `ready` deltaP `1.0342` edge `-0.0016` maxDD `-1.9954`
- `market_context_high->index_1h` score `-1.1147` n `121` status `ready` deltaP `-3.9281` edge `-0.0133` maxDD `-1.6054`
- `market_context_high->equity_1h` score `-1.5065` n `121` status `ready` deltaP `2.2406` edge `-0.0516` maxDD `-10.5179`
- `market_context_high->crypto_alt_4h` score `-1.6858` n `111` status `ready` deltaP `2.6409` edge `-0.0191` maxDD `-5.7857`
- `market_context_high->index_4h` score `-2.236` n `111` status `ready` deltaP `-5.3011` edge `-0.0296` maxDD `-4.3783`
- `market_context_high->crypto_major_1h` score `-2.4614` n `121` status `ready` deltaP `-5.3719` edge `-0.0396` maxDD `-7.0428`
- `market_context_high->crypto_alt_24h` score `-3.8406` n `110` status `ready` deltaP `-10.821` edge `-0.1036` maxDD `-4.5445`
- `market_context_high->crypto_major_4h` score `-4.7678` n `111` status `ready` deltaP `-6.147` edge `-0.1767` maxDD `-25.1525`
- `market_context_high->crypto_major_24h` score `-6.3172` n `110` status `ready` deltaP `-5.8704` edge `-0.2896` maxDD `-28.4934`
- `market_context_high->unknown_1h` score `-8.1648` n `121` status `ready` deltaP `0.4974` edge `-0.639` maxDD `-1.2437`
- `market_context_high->equity_4h` score `-9.1035` n `111` status `ready` deltaP `0.0632` edge `-0.2591` maxDD `-33.6624`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
