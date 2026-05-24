# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T10:52:14.989408+00:00`
- Price records: `672`
- Market context records: `1728`
- Flow alert records: `6881`
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

- `market_context_high->metal_24h` score `6.8048` n `147` status `ready` deltaP `25.7503` edge `0.638` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `5.8605` n `196` status `ready` deltaP `20.8188` edge `0.5262` maxDD `-9.1295`
- `market_context_high->unknown_24h` score `5.5315` n `147` status `ready` deltaP `16.6949` edge `0.8817` maxDD `-35.8966`
- `market_context_high->crypto_major_4h` score `4.374` n `196` status `ready` deltaP `22.7196` edge `0.4536` maxDD `-10.9117`
- `market_context_high->index_24h` score `4.1305` n `147` status `ready` deltaP `17.8271` edge `0.3482` maxDD `-4.1604`
- `market_context_high->unknown_4h` score `3.0809` n `196` status `ready` deltaP `13.7941` edge `0.3919` maxDD `-11.1695`
- `market_context_high->equity_4h` score `3.0019` n `196` status `ready` deltaP `16.1119` edge `0.2522` maxDD `-5.0894`
- `market_context_high->equity_24h` score `2.0777` n `147` status `ready` deltaP `16.6631` edge `0.5519` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.7716` n `196` status `ready` deltaP `7.7203` edge `0.1152` maxDD `-4.1892`
- `market_context_high->index_4h` score `0.5565` n `196` status `ready` deltaP `8.8166` edge `0.0965` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.2244` n `196` status `ready` deltaP `5.0471` edge `0.0924` maxDD `-3.9211`
- `market_context_high->crypto_alt_24h` score `0.1466` n `147` status `ready` deltaP `22.3689` edge `1.044` maxDD `-88.8062`
- `market_context_high->equity_1h` score `0.0359` n `196` status `ready` deltaP `4.821` edge `0.0517` maxDD `-2.8014`
- `market_context_high->metal_4h` score `-0.3392` n `196` status `ready` deltaP `11.8343` edge `0.1468` maxDD `-12.5349`
- `market_context_high->index_1h` score `-0.3689` n `196` status `ready` deltaP `2.1203` edge `0.0183` maxDD `-1.7205`
- `market_context_high->crypto_major_24h` score `-0.5668` n `147` status `ready` deltaP `20.9178` edge `0.6719` maxDD `-62.3533`
- `market_context_high->metal_1h` score `-0.5697` n `196` status `ready` deltaP `5.1968` edge `0.0259` maxDD `-6.3532`
- `market_context_high->fx_1h` score `-0.6404` n `196` status `ready` deltaP `-2.6671` edge `-0.0011` maxDD `-0.3914`
- `market_context_high->fx_24h` score `-0.7566` n `147` status `ready` deltaP `5.288` edge `0.0066` maxDD `-1.3925`
- `market_context_high->unknown_1h` score `-1.4377` n `196` status `ready` deltaP `1.9858` edge `0.0139` maxDD `-7.7558`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
