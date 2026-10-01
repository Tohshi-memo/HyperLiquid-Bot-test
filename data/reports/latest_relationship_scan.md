# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T12:08:04.244676+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7070`

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

- `market_context_high->unknown_1h` score `324.5787` n `50` status `ready` deltaP `7.5808` edge `27.0026` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `280.7896` n `50` status `ready` deltaP `6.8598` edge `23.3534` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.647` n `119` status `ready` deltaP `31.3054` edge `1.4495` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `8.9637` n `50` status `ready` deltaP `30.0903` edge `0.688` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `6.9895` n `50` status `ready` deltaP `18.9146` edge `0.5267` maxDD `-3.294`
- `news_risk_high->equity_24h` score `5.3984` n `119` status `ready` deltaP `21.8939` edge `0.5388` maxDD `-9.4579`
- `news_risk_high->equity_4h` score `4.5052` n `123` status `ready` deltaP `29.7764` edge `0.2258` maxDD `-1.2436`
- `market_context_high->crypto_alt_4h` score `4.3279` n `50` status `ready` deltaP `14.8171` edge `0.3912` maxDD `-7.6792`
- `news_risk_high->crypto_major_24h` score `3.6539` n `119` status `ready` deltaP `21.1995` edge `0.6425` maxDD `-15.8971`
- `market_context_high->equity_24h` score `3.6075` n `50` status `ready` deltaP `16.7847` edge `0.5368` maxDD `-11.8957`
- `market_context_high->fx_4h` score `2.9862` n `50` status `ready` deltaP `33.7561` edge `0.0373` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `2.8583` n `50` status `ready` deltaP `14.4491` edge `0.1869` maxDD `-2.2692`
- `market_context_high->crypto_alt_24h` score `2.7494` n `50` status `ready` deltaP `6.9861` edge `0.3535` maxDD `-11.6768`
- `market_context_high->crypto_alt_1h` score `2.6028` n `50` status `ready` deltaP `12.4072` edge `0.2005` maxDD `-3.6387`
- `news_risk_high->index_24h` score `2.496` n `119` status `ready` deltaP `24.0473` edge `0.0955` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `2.2839` n `119` status `ready` deltaP `26.9418` edge `0.2406` maxDD `-2.192`
- `news_risk_high->crypto_alt_4h` score `2.257` n `123` status `ready` deltaP `10.6708` edge `0.3176` maxDD `-10.7193`
- `market_context_high->fx_1h` score `1.4316` n `50` status `ready` deltaP `20.1916` edge `0.0111` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.876` n `132` status `ready` deltaP `8.229` edge `0.0718` maxDD `-0.9592`
- `market_context_high->index_24h` score `0.7034` n `50` status `ready` deltaP `12.5347` edge `0.0637` maxDD `-1.2338`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
