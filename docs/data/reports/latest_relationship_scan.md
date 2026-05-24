# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T07:07:16.482335+00:00`
- Price records: `672`
- Market context records: `1711`
- Flow alert records: `6834`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8834`

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

- `market_context_high->metal_24h` score `6.8772` n `138` status `ready` deltaP `25.5905` edge `0.6451` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `6.39` n `196` status `ready` deltaP `22.0384` edge `0.5622` maxDD `-9.1295`
- `market_context_high->crypto_major_4h` score `4.651` n `196` status `ready` deltaP `23.4818` edge `0.4716` maxDD `-10.9117`
- `market_context_high->index_24h` score `3.9317` n `138` status `ready` deltaP `16.8422` edge `0.3382` maxDD `-4.1604`
- `market_context_high->equity_4h` score `3.1141` n `196` status `ready` deltaP `16.5692` edge `0.2585` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.5126` n `138` status `ready` deltaP `15.6737` edge `0.5114` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.9492` n `196` status `ready` deltaP `8.0197` edge `0.128` maxDD `-4.1892`
- `market_context_high->crypto_alt_24h` score `0.6204` n `138` status `ready` deltaP `24.1212` edge `1.0718` maxDD `-88.8062`
- `market_context_high->index_4h` score `0.584` n `196` status `ready` deltaP `8.6642` edge `0.0998` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.3048` n `196` status `ready` deltaP `5.3465` edge `0.0971` maxDD `-3.9211`
- `market_context_high->equity_1h` score `0.0683` n `196` status `ready` deltaP `4.6713` edge `0.0554` maxDD `-2.8014`
- `market_context_high->metal_4h` score `-0.1261` n `196` status `ready` deltaP `13.0538` edge `0.166` maxDD `-12.5349`
- `market_context_high->index_1h` score `-0.4443` n `196` status `ready` deltaP `0.9227` edge `0.02` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.4512` n `196` status `ready` deltaP `6.095` edge `0.0351` maxDD `-6.3532`
- `market_context_high->fx_1h` score `-0.6622` n `196` status `ready` deltaP `-3.1162` edge `-0.0009` maxDD `-0.3914`
- `market_context_high->fx_24h` score `-0.7926` n `138` status `ready` deltaP `4.6136` edge `0.0081` maxDD `-1.3925`
- `market_context_high->crypto_major_24h` score `-0.9065` n `138` status `ready` deltaP `22.2707` edge `0.5939` maxDD `-62.3533`
- `market_context_high->fx_4h` score `-1.7718` n `196` status `ready` deltaP `-6.8193` edge `-0.0093` maxDD `-1.4313`
- `market_context_high->commodity_1h` score `-2.0095` n `196` status `ready` deltaP `0.333` edge `-0.0144` maxDD `-14.9691`
- `market_context_high->unknown_1h` score `-11.3413` n `196` status `ready` deltaP `1.6864` edge `-0.8094` maxDD `-7.7558`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
