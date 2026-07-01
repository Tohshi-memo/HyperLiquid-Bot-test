# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T16:22:26.758410+00:00`
- Price records: `672`
- Market context records: `5368`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11510`

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

- `market_context_high->unknown_24h` score `9.5389` n `176` status `ready` deltaP `17.0296` edge `0.6944` maxDD `-0.3748`
- `market_context_high->crypto_major_24h` score `5.2298` n `176` status `ready` deltaP `22.2065` edge `0.7418` maxDD `-29.6555`
- `market_context_high->equity_24h` score `3.0836` n `176` status `ready` deltaP `14.3624` edge `0.7241` maxDD `-40.0306`
- `market_context_high->crypto_major_4h` score `2.4643` n `200` status `ready` deltaP `13.2012` edge `0.3466` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `1.8879` n `200` status `ready` deltaP `9.6768` edge `0.2569` maxDD `-9.46`
- `market_context_high->equity_4h` score `1.1846` n `200` status `ready` deltaP `8.2927` edge `0.2073` maxDD `-7.4425`
- `market_context_high->index_24h` score `0.3369` n `176` status `ready` deltaP `17.0613` edge `0.0947` maxDD `-9.0959`
- `market_context_high->equity_1h` score `0.058` n `205` status `ready` deltaP `5.8135` edge `0.0626` maxDD `-5.0555`
- `market_context_high->fx_24h` score `-0.0131` n `176` status `ready` deltaP `8.3017` edge `0.0331` maxDD `-0.8294`
- `market_context_high->index_1h` score `-0.1253` n `205` status `ready` deltaP `4.0792` edge `0.0117` maxDD `-0.9472`
- `market_context_high->crypto_major_1h` score `-0.1789` n `205` status `ready` deltaP `3.576` edge `0.0858` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `-0.241` n `205` status `ready` deltaP `1.1808` edge `0.0682` maxDD `-5.0257`
- `market_context_high->fx_1h` score `-0.4166` n `205` status `ready` deltaP `-0.5046` edge `-0.0011` maxDD `-0.5823`
- `market_context_high->metal_1h` score `-0.5765` n `205` status `ready` deltaP `1.0311` edge `0.0126` maxDD `-2.0682`
- `market_context_high->index_4h` score `-1.021` n `200` status `ready` deltaP `4.5427` edge `0.0226` maxDD `-2.704`
- `market_context_high->fx_4h` score `-1.0764` n `200` status `ready` deltaP `1.6829` edge `0.002` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.4891` n `205` status `ready` deltaP `-3.4701` edge `-0.0065` maxDD `-3.5563`
- `market_context_high->unknown_4h` score `-1.5203` n `200` status `ready` deltaP `7.4329` edge `-0.0578` maxDD `-6.1421`
- `market_context_high->metal_4h` score `-2.7389` n `200` status `ready` deltaP `-8.128` edge `-0.0445` maxDD `-12.8631`
- `market_context_high->crypto_alt_24h` score `-3.4809` n `176` status `ready` deltaP `12.8315` edge `0.3379` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
