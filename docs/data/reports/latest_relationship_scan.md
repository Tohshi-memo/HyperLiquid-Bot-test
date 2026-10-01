# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T22:37:29.946114+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6574`

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

- `market_context_high->unknown_1h` score `338.2669` n `50` status `ready` deltaP `9.0778` edge `28.1333` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `286.9102` n `50` status `ready` deltaP `7.3171` edge `23.8604` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `20.2207` n `92` status `ready` deltaP `36.5414` edge `1.4624` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `10.5405` n `50` status `ready` deltaP `34.6042` edge `0.7893` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `7.3235` n `50` status `ready` deltaP `19.2195` edge `0.5525` maxDD `-3.294`
- `market_context_high->crypto_alt_24h` score `6.1093` n `50` status `ready` deltaP `12.7153` edge `0.5953` maxDD `-11.6768`
- `market_context_high->crypto_alt_4h` score `5.097` n `50` status `ready` deltaP `16.6463` edge `0.4431` maxDD `-7.6792`
- `news_risk_high->crypto_major_24h` score `4.366` n `92` status `ready` deltaP `17.8216` edge `0.5604` maxDD `-15.8971`
- `market_context_high->equity_24h` score `3.7436` n `50` status `ready` deltaP `19.0417` edge `0.5392` maxDD `-11.8957`
- `news_risk_high->equity_4h` score `3.0849` n `105` status `ready` deltaP `26.4561` edge `0.1503` maxDD `-2.9013`
- `market_context_high->crypto_major_1h` score `3.0419` n `50` status `ready` deltaP `14.7485` edge `0.2002` maxDD `-2.2692`
- `market_context_high->fx_4h` score `3.0308` n `50` status `ready` deltaP `33.9085` edge `0.04` maxDD `-0.0791`
- `market_context_high->crypto_alt_1h` score `3.0069` n `50` status `ready` deltaP `14.0539` edge `0.2232` maxDD `-3.6387`
- `news_risk_high->equity_24h` score `2.4894` n `92` status `ready` deltaP `17.346` edge `0.4384` maxDD `-9.4579`
- `news_risk_high->metal_24h` score `1.9002` n `92` status `ready` deltaP `21.5731` edge `0.2272` maxDD `-2.192`
- `news_risk_high->index_24h` score `1.8814` n `92` status `ready` deltaP `20.8787` edge `0.0654` maxDD `-0.4916`
- `market_context_high->fx_1h` score `1.5023` n `50` status `ready` deltaP `20.9401` edge `0.012` maxDD `-0.113`
- `news_risk_high->commodity_24h` score `1.428` n `92` status `ready` deltaP `24.0716` edge `0.135` maxDD `-3.9922`
- `market_context_high->index_24h` score `0.9112` n `50` status `ready` deltaP `14.7917` edge `0.0753` maxDD `-1.2338`
- `news_risk_high->crypto_alt_4h` score `0.6133` n `105` status `ready` deltaP `5.6939` edge `0.2029` maxDD `-10.1798`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
