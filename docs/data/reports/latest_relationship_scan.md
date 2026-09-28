# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T18:22:32.025352+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7808`

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

- `news_risk_high->unknown_24h` score `2675.7372` n `139` status `ready` deltaP `1.2153` edge `222.97` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `8.7121` n `139` status `ready` deltaP `24.2544` edge `0.9595` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `5.5137` n `139` status `ready` deltaP `23.8521` edge `0.5561` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `5.501` n `139` status `ready` deltaP `20.3799` edge `0.766` maxDD `-26.1424`
- `news_risk_high->index_24h` score `3.1312` n `139` status `ready` deltaP `29.4839` edge `0.1339` maxDD `-2.2287`
- `news_risk_high->equity_4h` score `2.4082` n `139` status `ready` deltaP `25.8017` edge `0.1896` maxDD `-9.2079`
- `news_risk_high->metal_24h` score `2.0768` n `139` status `ready` deltaP `21.8638` edge `0.2128` maxDD `-6.8392`
- `news_risk_high->crypto_alt_4h` score `0.7149` n `139` status `ready` deltaP `7.4311` edge `0.276` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.5008` n `139` status `ready` deltaP `6.4188` edge `0.09` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.49` n `139` status `ready` deltaP `7.2546` edge `0.0586` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4431` n `139` status `ready` deltaP `8.6019` edge `0.0086` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.1649` n `139` status `ready` deltaP `6.658` edge `0.0272` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.5579` n `139` status `ready` deltaP `1.0414` edge `0.0095` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.6706` n `139` status `ready` deltaP `-0.1519` edge `0.0433` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.1804` n `139` status `ready` deltaP `-9.1178` edge `-0.0025` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.2231` n `139` status `ready` deltaP `9.982` edge `-0.002` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.4809` n `139` status `ready` deltaP `-9.9184` edge `0.0257` maxDD `-3.6214`
- `news_risk_high->crypto_major_4h` score `-1.8922` n `139` status `ready` deltaP `-5.7006` edge `0.0669` maxDD `-13.719`
- `news_risk_high->commodity_1h` score `-2.0123` n `139` status `ready` deltaP `-11.7165` edge `-0.0124` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-3.8755` n `139` status `ready` deltaP `-11.4746` edge `-0.0046` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
