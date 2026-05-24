# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T12:10:34.428637+00:00`
- Price records: `672`
- Market context records: `1735`
- Flow alert records: `6897`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8838`

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

- `market_context_high->metal_24h` score `6.9334` n `152` status `ready` deltaP `25.6624` edge `0.6493` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `5.7735` n `196` status `ready` deltaP `20.3615` edge `0.522` maxDD `-9.1295`
- `market_context_high->unknown_24h` score `5.0181` n `152` status `ready` deltaP `16.3221` edge `0.8414` maxDD `-35.8966`
- `market_context_high->index_24h` score `4.2717` n `152` status `ready` deltaP `18.1525` edge `0.3578` maxDD `-4.1604`
- `market_context_high->crypto_major_4h` score `4.2266` n `196` status `ready` deltaP `21.9574` edge `0.4464` maxDD `-10.9117`
- `market_context_high->unknown_4h` score `3.0675` n `196` status `ready` deltaP `13.6417` edge `0.3918` maxDD `-11.1695`
- `market_context_high->equity_4h` score `2.9705` n `196` status `ready` deltaP `15.9594` edge `0.2506` maxDD `-5.0894`
- `market_context_high->equity_24h` score `2.463` n `152` status `ready` deltaP `16.5589` edge `0.5847` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.7369` n `196` status `ready` deltaP `7.4209` edge `0.1143` maxDD `-4.1892`
- `market_context_high->index_4h` score `0.6259` n `196` status `ready` deltaP `9.5788` edge `0.0972` maxDD `-3.7119`
- `market_context_high->crypto_alt_24h` score `0.3454` n `152` status `ready` deltaP `21.9291` edge `1.0635` maxDD `-88.8062`
- `market_context_high->crypto_major_1h` score `0.1873` n `196` status `ready` deltaP `4.7477` edge `0.0913` maxDD `-3.9211`
- `market_context_high->crypto_major_24h` score `0.1857` n `152` status `ready` deltaP `20.6792` edge `0.7362` maxDD `-62.3533`
- `market_context_high->equity_1h` score `0.0466` n `196` status `ready` deltaP `4.9707` edge `0.0516` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.3437` n `196` status `ready` deltaP `2.4197` edge `0.0184` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.3574` n `196` status `ready` deltaP `11.5294` edge `0.1465` maxDD `-12.5349`
- `market_context_high->metal_1h` score `-0.5533` n `196` status `ready` deltaP `5.4962` edge `0.026` maxDD `-6.3532`
- `market_context_high->fx_1h` score `-0.649` n `196` status `ready` deltaP `-2.8168` edge `-0.0012` maxDD `-0.3914`
- `market_context_high->fx_24h` score `-0.7179` n `152` status `ready` deltaP `5.8027` edge `0.0064` maxDD `-1.3925`
- `market_context_high->unknown_1h` score `-1.5312` n `196` status `ready` deltaP `1.2373` edge `0.0111` maxDD `-7.7558`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
