# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T20:37:55.379258+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6818`

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

- `market_context_high->unknown_1h` score `337.7905` n `50` status `ready` deltaP `8.479` edge `28.0976` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `286.4056` n `50` status `ready` deltaP `6.8598` edge `23.8214` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `20.2156` n `100` status `ready` deltaP `35.8472` edge `1.4666` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `10.2721` n `50` status `ready` deltaP `33.2153` edge `0.7762` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `7.2511` n `50` status `ready` deltaP `18.9146` edge `0.5485` maxDD `-3.294`
- `market_context_high->crypto_alt_24h` score `5.6679` n `50` status `ready` deltaP `11.8472` edge `0.5643` maxDD `-11.6768`
- `market_context_high->crypto_alt_4h` score `5.0414` n `50` status `ready` deltaP `16.3415` edge `0.4405` maxDD `-7.6792`
- `news_risk_high->crypto_major_24h` score `4.6515` n `100` status `ready` deltaP `19.2153` edge `0.5749` maxDD `-15.8971`
- `market_context_high->equity_24h` score `3.8473` n `50` status `ready` deltaP `19.0417` edge `0.5525` maxDD `-11.8957`
- `news_risk_high->equity_4h` score `3.304` n `113` status `ready` deltaP `27.6347` edge `0.1607` maxDD `-2.9013`
- `market_context_high->fx_4h` score `3.1428` n `50` status `ready` deltaP `35.128` edge `0.0412` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `3.0131` n `50` status `ready` deltaP `14.4491` edge `0.1998` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `2.9278` n `50` status `ready` deltaP `13.4551` edge `0.2206` maxDD `-3.6387`
- `news_risk_high->equity_24h` score `2.766` n `100` status `ready` deltaP `20.0417` edge `0.4559` maxDD `-9.4579`
- `news_risk_high->index_24h` score `2.2096` n `100` status `ready` deltaP `22.7917` edge `0.08` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `2.0892` n `100` status `ready` deltaP `24.0972` edge `0.2346` maxDD `-2.192`
- `market_context_high->fx_1h` score `1.5142` n `50` status `ready` deltaP `21.0898` edge `0.012` maxDD `-0.113`
- `news_risk_high->commodity_24h` score `1.1134` n `100` status `ready` deltaP `20.2431` edge `0.1037` maxDD `-6.6698`
- `market_context_high->index_24h` score `0.9065` n `50` status `ready` deltaP `14.7917` edge `0.0747` maxDD `-1.2338`
- `news_risk_high->equity_1h` score `0.4973` n `113` status `ready` deltaP `7.3194` edge `0.0463` maxDD `-0.9592`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
