# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T09:22:30.658167+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4854`

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

- `market_context_high->unknown_1h` score `340.8743` n `50` status `ready` deltaP `10.2754` edge `28.3426` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `287.6519` n `50` status `ready` deltaP `9.2988` edge `23.909` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `14.8379` n `69` status `ready` deltaP `39.6361` edge `0.9932` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `10.7349` n `50` status `ready` deltaP `35.8194` edge `0.7974` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `10.1169` n `69` status `ready` deltaP `36.4432` edge `0.6486` maxDD `-2.8784`
- `market_context_high->crypto_alt_24h` score `9.0069` n `50` status `ready` deltaP `16.5347` edge `0.8113` maxDD `-11.6768`
- `market_context_high->crypto_major_4h` score `6.9985` n `50` status `ready` deltaP `17.5427` edge `0.5366` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.9673` n `50` status `ready` deltaP `15.5793` edge `0.4394` maxDD `-7.6792`
- `news_risk_high->crypto_alt_4h` score `4.3792` n `98` status `ready` deltaP `17.0079` edge `0.3859` maxDD `-6.4152`
- `market_context_high->fx_4h` score `2.9383` n `50` status `ready` deltaP `32.8415` edge `0.0394` maxDD `-0.0791`
- `market_context_high->crypto_alt_1h` score `2.8977` n `50` status `ready` deltaP `13.9042` edge `0.2151` maxDD `-3.6387`
- `market_context_high->crypto_major_1h` score `2.85` n `50` status `ready` deltaP `13.8503` edge `0.1902` maxDD `-2.2692`
- `market_context_high->equity_24h` score `2.79` n `50` status `ready` deltaP `13.1389` edge `0.4563` maxDD `-11.8957`
- `news_risk_high->equity_4h` score `2.4475` n `98` status `ready` deltaP `23.6343` edge `0.116` maxDD `-2.9013`
- `news_risk_high->crypto_major_24h` score `1.6664` n `69` status `ready` deltaP `7.4426` edge `0.4794` maxDD `-15.8971`
- `market_context_high->fx_1h` score `1.4903` n `50` status `ready` deltaP `20.7904` edge `0.012` maxDD `-0.113`
- `news_risk_high->metal_24h` score `1.0828` n `69` status `ready` deltaP `9.7826` edge `0.201` maxDD `-2.192`
- `news_risk_high->crypto_alt_1h` score `0.9699` n `110` status `ready` deltaP `6.086` edge `0.0965` maxDD `-2.4998`
- `market_context_high->index_24h` score `0.9665` n `50` status `ready` deltaP `15.6597` edge `0.0766` maxDD `-1.2338`
- `news_risk_high->crypto_major_4h` score `0.7146` n `98` status `ready` deltaP `9.7468` edge `0.2576` maxDD `-10.477`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
