# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T07:52:26.530674+00:00`
- Price records: `672`
- Market context records: `6583`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9808`

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

- `market_context_high->unknown_24h` score `5.232` n `151` status `ready` deltaP `8.1346` edge `0.7118` maxDD `-15.0689`
- `market_context_high->unknown_1h` score `1.9884` n `210` status `ready` deltaP `-5.4291` edge `0.292` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `1.3037` n `151` status `ready` deltaP `13.4646` edge `0.2057` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.3604` n `210` status `ready` deltaP `0.7086` edge `-0.0002` maxDD `-0.7249`
- `market_context_high->crypto_major_1h` score `-0.4134` n `210` status `ready` deltaP `7.0473` edge `0.0266` maxDD `-6.7936`
- `market_context_high->index_1h` score `-0.5537` n `210` status `ready` deltaP `-0.3807` edge `0.0035` maxDD `-0.7564`
- `market_context_high->commodity_1h` score `-0.5783` n `210` status `ready` deltaP `-0.2595` edge `-0.0041` maxDD `-2.1314`
- `market_context_high->crypto_alt_1h` score `-0.5835` n `210` status `ready` deltaP `5.1426` edge `0.0222` maxDD `-5.8368`
- `market_context_high->index_4h` score `-0.9113` n `210` status `ready` deltaP `9.142` edge `0.0102` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-1.1453` n `210` status `ready` deltaP `2.2313` edge `0.0007` maxDD `-4.2147`
- `market_context_high->commodity_4h` score `-1.3088` n `210` status `ready` deltaP `-1.279` edge `-0.0098` maxDD `-5.6246`
- `market_context_high->metal_1h` score `-1.3614` n `210` status `ready` deltaP `-4.4753` edge `-0.0029` maxDD `-2.1239`
- `market_context_high->unknown_4h` score `-1.6353` n `210` status `ready` deltaP `-16.4561` edge `0.214` maxDD `-10.5788`
- `market_context_high->fx_4h` score `-1.7377` n `210` status `ready` deltaP `0.2293` edge `-0.0031` maxDD `-3.3635`
- `market_context_high->crypto_major_4h` score `-1.7739` n `210` status `ready` deltaP `7.4289` edge `0.0545` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-2.0517` n `210` status `ready` deltaP `4.4759` edge `0.0473` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.1525` n `210` status `ready` deltaP `-1.5012` edge `0.0201` maxDD `-5.2172`
- `market_context_high->metal_24h` score `-2.8885` n `151` status `ready` deltaP `4.128` edge `0.0768` maxDD `-7.6025`
- `market_context_high->fx_24h` score `-3.726` n `151` status `ready` deltaP `-3.2701` edge `-0.0024` maxDD `-9.2795`
- `market_context_high->index_24h` score `-4.6468` n `151` status `ready` deltaP `-0.6496` edge `-0.0119` maxDD `-12.3471`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
