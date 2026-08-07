# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T13:52:28.278798+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11740`

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

- `market_context_high->commodity_4h` score `0.9732` n `115` status `ready` deltaP `12.3489` edge `0.0834` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.9093` n `110` status `ready` deltaP `2.5361` edge `0.1498` maxDD `-2.2743`
- `market_context_high->commodity_1h` score `0.7879` n `121` status `ready` deltaP `10.9294` edge `0.0344` maxDD `-1.3282`
- `market_context_high->fx_24h` score `0.5475` n `110` status `ready` deltaP `21.1018` edge `0.0486` maxDD `-4.1933`
- `market_context_high->fx_1h` score `0.0894` n `121` status `ready` deltaP `8.528` edge `-0.0028` maxDD `-1.0616`
- `market_context_high->fx_4h` score `-0.1896` n `115` status `ready` deltaP `8.6386` edge `0.0041` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.4598` n `121` status `ready` deltaP `-1.5205` edge `-0.006` maxDD `-1.4247`
- `market_context_high->index_1h` score `-0.5839` n `121` status `ready` deltaP `-1.8978` edge `-0.0088` maxDD `-1.6054`
- `market_context_high->crypto_alt_1h` score `-0.8538` n `121` status `ready` deltaP `-3.8563` edge `-0.0154` maxDD `-2.8016`
- `market_context_high->index_24h` score `-1.1126` n `110` status `ready` deltaP `0.4189` edge `0.084` maxDD `-6.3605`
- `market_context_high->equity_1h` score `-1.213` n `121` status `ready` deltaP `3.5941` edge `-0.023` maxDD `-10.5179`
- `market_context_high->metal_4h` score `-1.301` n `115` status `ready` deltaP `-1.128` edge `-0.0077` maxDD `-2.4558`
- `market_context_high->index_4h` score `-1.5583` n `115` status `ready` deltaP `-6.6569` edge `-0.031` maxDD `-4.6193`
- `market_context_high->crypto_major_1h` score `-1.5666` n `121` status `ready` deltaP `-4.6952` edge `-0.0365` maxDD `-7.3107`
- `market_context_high->crypto_alt_4h` score `-2.0525` n `115` status `ready` deltaP `0.6667` edge `-0.0365` maxDD `-5.7857`
- `market_context_high->crypto_alt_24h` score `-3.7272` n `110` status `ready` deltaP `-10.0789` edge `-0.0991` maxDD `-4.5445`
- `market_context_high->commodity_24h` score `-6.2513` n `110` status `ready` deltaP `10.2853` edge `0.0065` maxDD `-52.7876`
- `market_context_high->equity_4h` score `-6.2575` n `115` status `ready` deltaP `-1.315` edge `-0.2646` maxDD `-34.9766`
- `market_context_high->crypto_major_24h` score `-7.428` n `110` status `ready` deltaP `-8.0968` edge `-0.3347` maxDD `-33.7567`
- `market_context_high->crypto_major_4h` score `-7.5147` n `115` status `ready` deltaP `-7.3463` edge `-0.1787` maxDD `-25.5505`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
