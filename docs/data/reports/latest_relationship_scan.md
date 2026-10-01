# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T23:22:27.193912+00:00`
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

- `market_context_high->unknown_1h` score `338.556` n `50` status `ready` deltaP `9.3772` edge `28.1554` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `287.086` n `50` status `ready` deltaP `7.7744` edge `23.872` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.9049` n `89` status `ready` deltaP `36.9889` edge `1.4331` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `10.6961` n `50` status `ready` deltaP `35.125` edge `0.7988` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `7.3199` n `50` status `ready` deltaP `19.2195` edge `0.5522` maxDD `-3.294`
- `market_context_high->crypto_alt_24h` score `6.3958` n `50` status `ready` deltaP `13.2361` edge `0.6157` maxDD `-11.6768`
- `market_context_high->crypto_alt_4h` score `5.0742` n `50` status `ready` deltaP `16.6463` edge `0.4412` maxDD `-7.6792`
- `news_risk_high->crypto_major_24h` score `4.0018` n `89` status `ready` deltaP `17.1699` edge `0.5344` maxDD `-15.8971`
- `market_context_high->equity_24h` score `3.7085` n `50` status `ready` deltaP `19.0417` edge `0.5347` maxDD `-11.8957`
- `market_context_high->crypto_major_1h` score `3.0623` n `50` status `ready` deltaP `14.8982` edge `0.2009` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `3.0309` n `50` status `ready` deltaP `14.2036` edge `0.2242` maxDD `-3.6387`
- `market_context_high->fx_4h` score `2.9992` n `50` status `ready` deltaP `33.6037` edge `0.0394` maxDD `-0.0791`
- `news_risk_high->equity_4h` score `2.9828` n `102` status `ready` deltaP `25.8399` edge `0.1459` maxDD `-2.9013`
- `news_risk_high->equity_24h` score `2.3765` n `89` status `ready` deltaP `16.2102` edge `0.4315` maxDD `-9.4579`
- `news_risk_high->metal_24h` score `1.8001` n `89` status `ready` deltaP `20.0979` edge `0.2242` maxDD `-2.192`
- `news_risk_high->index_24h` score `1.7377` n `89` status `ready` deltaP `20.0726` edge `0.0588` maxDD `-0.4916`
- `news_risk_high->commodity_24h` score `1.5893` n `89` status `ready` deltaP `25.749` edge `0.1445` maxDD `-3.9922`
- `news_risk_high->crypto_alt_4h` score `1.5602` n `102` status `ready` deltaP `7.4306` edge `0.2317` maxDD `-7.7645`
- `market_context_high->fx_1h` score `1.5154` n `50` status `ready` deltaP `21.0898` edge `0.0121` maxDD `-0.113`
- `market_context_high->index_24h` score `0.9151` n `50` status `ready` deltaP `14.7917` edge `0.0758` maxDD `-1.2338`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
