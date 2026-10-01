# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T11:52:33.617214+00:00`
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

- `market_context_high->unknown_1h` score `324.5499` n `50` status `ready` deltaP `7.5808` edge `27.0002` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `280.8616` n `50` status `ready` deltaP `6.8598` edge `23.3594` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.9019` n `120` status `ready` deltaP `31.1458` edge `1.4718` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `8.8857` n `50` status `ready` deltaP `30.0903` edge `0.6815` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `6.9739` n `50` status `ready` deltaP `18.9146` edge `0.5254` maxDD `-3.294`
- `news_risk_high->equity_24h` score `5.5592` n `120` status `ready` deltaP `22.118` edge `0.5507` maxDD `-9.4579`
- `news_risk_high->equity_4h` score `4.51` n `123` status `ready` deltaP `29.7764` edge `0.2262` maxDD `-1.2436`
- `market_context_high->crypto_alt_4h` score `4.2581` n `50` status `ready` deltaP `14.6646` edge `0.3864` maxDD `-7.6792`
- `news_risk_high->crypto_major_24h` score `3.8442` n `120` status `ready` deltaP `21.4236` edge `0.6654` maxDD `-15.8971`
- `market_context_high->equity_24h` score `3.5888` n `50` status `ready` deltaP `16.7847` edge `0.5344` maxDD `-11.8957`
- `market_context_high->fx_4h` score `2.9728` n `50` status `ready` deltaP `33.6037` edge `0.0372` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `2.8535` n `50` status `ready` deltaP `14.4491` edge `0.1865` maxDD `-2.2692`
- `market_context_high->crypto_alt_24h` score `2.5987` n `50` status `ready` deltaP `6.8125` edge `0.3421` maxDD `-11.6768`
- `market_context_high->crypto_alt_1h` score `2.5932` n `50` status `ready` deltaP `12.4072` edge `0.1997` maxDD `-3.6387`
- `news_risk_high->crypto_alt_4h` score `2.5594` n `123` status `ready` deltaP `11.3313` edge `0.3384` maxDD `-10.7193`
- `news_risk_high->index_24h` score `2.5276` n `120` status `ready` deltaP `24.2014` edge `0.0971` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `2.2999` n `120` status `ready` deltaP `27.0833` edge `0.2417` maxDD `-2.192`
- `market_context_high->fx_1h` score `1.4328` n `50` status `ready` deltaP `20.1916` edge `0.0112` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.8808` n `133` status `ready` deltaP `8.3641` edge `0.0713` maxDD `-0.9592`
- `market_context_high->index_24h` score `0.7026` n `50` status `ready` deltaP `12.5347` edge `0.0636` maxDD `-1.2338`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
