# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T11:22:16.518330+00:00`
- Price records: `672`
- Market context records: `1731`
- Flow alert records: `6887`
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

- `market_context_high->metal_24h` score `6.8533` n `149` status `ready` deltaP `25.6508` edge `0.6427` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `5.8195` n `196` status `ready` deltaP `20.6664` edge `0.5238` maxDD `-9.1295`
- `market_context_high->unknown_24h` score `5.3243` n `149` status `ready` deltaP `16.5498` edge `0.8654` maxDD `-35.8966`
- `market_context_high->crypto_major_4h` score `4.31` n `196` status `ready` deltaP `22.4147` edge `0.4503` maxDD `-10.9117`
- `market_context_high->index_24h` score `4.2088` n `149` status `ready` deltaP `18.1011` edge `0.3529` maxDD `-4.1604`
- `market_context_high->unknown_4h` score `3.0833` n `196` status `ready` deltaP `13.7941` edge `0.3921` maxDD `-11.1695`
- `market_context_high->equity_4h` score `2.9971` n `196` status `ready` deltaP `16.1119` edge `0.2518` maxDD `-5.0894`
- `market_context_high->equity_24h` score `2.2381` n `149` status `ready` deltaP `16.6276` edge `0.5655` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.7333` n `196` status `ready` deltaP `7.4209` edge `0.114` maxDD `-4.1892`
- `market_context_high->index_4h` score `0.5845` n `196` status `ready` deltaP `9.1215` edge `0.0968` maxDD `-3.7119`
- `market_context_high->crypto_alt_24h` score `0.2156` n `149` status `ready` deltaP `22.1964` edge `1.0509` maxDD `-88.8062`
- `market_context_high->crypto_major_1h` score `0.1909` n `196` status `ready` deltaP `4.7477` edge `0.0916` maxDD `-3.9211`
- `market_context_high->equity_1h` score `0.0466` n `196` status `ready` deltaP `4.9707` edge `0.0516` maxDD `-2.8014`
- `market_context_high->crypto_major_24h` score `-0.2632` n `149` status `ready` deltaP `20.8275` edge `0.6978` maxDD `-62.3533`
- `market_context_high->index_1h` score `-0.3557` n `196` status `ready` deltaP `2.27` edge `0.0184` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.3574` n `196` status `ready` deltaP `11.5294` edge `0.1465` maxDD `-12.5349`
- `market_context_high->metal_1h` score `-0.5689` n `196` status `ready` deltaP `5.1968` edge `0.026` maxDD `-6.3532`
- `market_context_high->fx_1h` score `-0.6404` n `196` status `ready` deltaP `-2.6671` edge `-0.0011` maxDD `-0.3914`
- `market_context_high->fx_24h` score `-0.741` n `149` status `ready` deltaP `5.4981` edge `0.0065` maxDD `-1.3925`
- `market_context_high->unknown_1h` score `-1.4761` n `196` status `ready` deltaP `1.6864` edge `0.0127` maxDD `-7.7558`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
