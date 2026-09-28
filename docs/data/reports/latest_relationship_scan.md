# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T17:52:31.936150+00:00`
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

- `news_risk_high->unknown_24h` score `2676.7164` n `139` status `ready` deltaP `1.2153` edge `223.0516` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `8.466` n `139` status `ready` deltaP `23.9071` edge `0.9413` maxDD `-29.2814`
- `news_risk_high->crypto_major_24h` score `5.3665` n `139` status `ready` deltaP `20.0327` edge `0.7571` maxDD `-26.1424`
- `news_risk_high->equity_24h` score `5.3275` n `139` status `ready` deltaP `23.5049` edge `0.5429` maxDD `-11.1179`
- `news_risk_high->index_24h` score `3.0866` n `139` status `ready` deltaP `29.1367` edge `0.1325` maxDD `-2.2287`
- `news_risk_high->equity_4h` score `2.379` n `139` status `ready` deltaP `25.4968` edge `0.1892` maxDD `-9.2079`
- `news_risk_high->metal_24h` score `1.9998` n `139` status `ready` deltaP `21.5166` edge `0.2087` maxDD `-6.8392`
- `news_risk_high->crypto_alt_4h` score `0.7077` n `139` status `ready` deltaP `7.4311` edge `0.2754` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.5367` n `139` status `ready` deltaP `6.5685` edge `0.092` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.4792` n `139` status `ready` deltaP `7.1049` edge `0.0587` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4431` n `139` status `ready` deltaP `8.6019` edge `0.0086` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.1649` n `139` status `ready` deltaP `6.658` edge `0.0272` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.5699` n `139` status `ready` deltaP `0.8917` edge `0.0095` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.676` n `139` status `ready` deltaP `-0.3016` edge `0.0436` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.1882` n `139` status `ready` deltaP `-9.2675` edge `-0.0025` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.2064` n `139` status `ready` deltaP `10.2869` edge `-0.0019` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.4904` n `139` status `ready` deltaP `-10.0708` edge `0.0255` maxDD `-3.6214`
- `news_risk_high->crypto_major_4h` score `-1.9125` n `139` status `ready` deltaP `-5.7006` edge `0.0643` maxDD `-13.719`
- `news_risk_high->commodity_1h` score `-2.0053` n `139` status `ready` deltaP `-11.5668` edge `-0.0125` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-3.8827` n `139` status `ready` deltaP `-11.4746` edge `-0.0052` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
