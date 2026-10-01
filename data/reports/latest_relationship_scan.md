# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T12:37:34.202752+00:00`
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

- `market_context_high->unknown_1h` score `325.2267` n `50` status `ready` deltaP `7.5808` edge `27.0566` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `280.9588` n `50` status `ready` deltaP `6.8598` edge `23.3675` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.2501` n `117` status `ready` deltaP `31.6239` edge `1.4143` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `9.1324` n `50` status `ready` deltaP `30.2639` edge `0.7009` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `7.0519` n `50` status `ready` deltaP `18.9146` edge `0.5319` maxDD `-3.294`
- `news_risk_high->equity_24h` score `5.1019` n `117` status `ready` deltaP `21.6079` edge `0.516` maxDD `-9.4579`
- `market_context_high->crypto_alt_4h` score `4.4927` n `50` status `ready` deltaP `15.122` edge `0.4029` maxDD `-7.6792`
- `news_risk_high->equity_4h` score `4.3828` n `123` status `ready` deltaP `29.7764` edge `0.2156` maxDD `-1.2436`
- `market_context_high->equity_24h` score `3.6587` n `50` status `ready` deltaP `16.9583` edge `0.5422` maxDD `-11.8957`
- `news_risk_high->crypto_major_24h` score `3.3512` n `117` status `ready` deltaP `20.9135` edge `0.6056` maxDD `-15.8971`
- `market_context_high->crypto_alt_24h` score `3.0399` n `50` status `ready` deltaP `7.3333` edge `0.3754` maxDD `-11.6768`
- `market_context_high->fx_4h` score `2.9996` n `50` status `ready` deltaP `33.9085` edge `0.0374` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `2.8859` n `50` status `ready` deltaP `14.4491` edge `0.1892` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `2.6591` n `50` status `ready` deltaP `12.5569` edge `0.2042` maxDD `-3.6387`
- `news_risk_high->index_24h` score `2.4396` n `117` status `ready` deltaP `23.7313` edge `0.0929` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `2.2461` n `117` status `ready` deltaP `26.4691` edge `0.2389` maxDD `-2.192`
- `news_risk_high->crypto_alt_4h` score `1.5405` n `123` status `ready` deltaP `9.3496` edge `0.2667` maxDD `-10.7193`
- `market_context_high->fx_1h` score `1.4316` n `50` status `ready` deltaP `20.1916` edge `0.0111` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.8753` n `130` status `ready` deltaP `8.5652` edge `0.0695` maxDD `-0.9592`
- `market_context_high->index_24h` score `0.7073` n `50` status `ready` deltaP `12.5347` edge `0.0642` maxDD `-1.2338`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
