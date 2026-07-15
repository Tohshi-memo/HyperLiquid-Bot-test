# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T05:07:27.059790+00:00`
- Price records: `672`
- Market context records: `6784`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11716`

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

- `market_context_high->unknown_24h` score `0.8953` n `176` status `ready` deltaP `-1.1995` edge `0.498` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `0.0585` n `176` status `ready` deltaP `8.144` edge `0.1374` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.1176` n `182` status `ready` deltaP `7.0968` edge `0.0236` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.3235` n `182` status `ready` deltaP `4.4499` edge `0.0198` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.3582` n `182` status `ready` deltaP `0.2977` edge `0.0006` maxDD `-0.5468`
- `market_context_high->index_1h` score `-0.624` n `182` status `ready` deltaP `-1.3473` edge `0.0004` maxDD `-0.7136`
- `market_context_high->commodity_1h` score `-0.6673` n `182` status `ready` deltaP `-1.1466` edge `-0.0096` maxDD `-2.1314`
- `market_context_high->metal_1h` score `-0.7204` n `182` status `ready` deltaP `-5.3465` edge `-0.0042` maxDD `-1.2017`
- `market_context_high->equity_1h` score `-1.2023` n `182` status `ready` deltaP `2.7012` edge `-0.0155` maxDD `-3.8827`
- `market_context_high->fx_4h` score `-1.3094` n `176` status `ready` deltaP `6.0144` edge `-0.0016` maxDD `-2.1765`
- `market_context_high->index_4h` score `-1.3114` n `176` status `ready` deltaP `5.3769` edge `-0.016` maxDD `-5.7046`
- `market_context_high->commodity_4h` score `-1.505` n `176` status `ready` deltaP `-3.1458` edge `-0.023` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.5926` n `182` status `ready` deltaP `-5.5965` edge `-0.0053` maxDD `-3.2083`
- `market_context_high->metal_4h` score `-2.5991` n `176` status `ready` deltaP `-5.7096` edge `-0.0091` maxDD `-5.2172`
- `market_context_high->crypto_major_4h` score `-2.8985` n `176` status `ready` deltaP `2.2866` edge `-0.0554` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-3.0` n `176` status `ready` deltaP `1.1502` edge `-0.0521` maxDD `-19.2145`
- `market_context_high->unknown_4h` score `-3.2583` n `176` status `ready` deltaP `-13.8858` edge `0.0576` maxDD `-10.2579`
- `market_context_high->equity_4h` score `-4.3176` n `176` status `ready` deltaP `2.245` edge `-0.1416` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-4.4483` n `176` status `ready` deltaP `-9.2645` edge `-0.0053` maxDD `-5.6237`
- `market_context_high->metal_24h` score `-9.0334` n `176` status `ready` deltaP `-17.2822` edge `-0.1944` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
