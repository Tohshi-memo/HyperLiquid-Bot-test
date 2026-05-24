# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T12:37:14.949936+00:00`
- Price records: `672`
- Market context records: `1737`
- Flow alert records: `6903`
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

- `market_context_high->metal_24h` score `6.9907` n `153` status `ready` deltaP `25.8538` edge `0.6528` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `5.7831` n `196` status `ready` deltaP `20.3615` edge `0.5228` maxDD `-9.1295`
- `market_context_high->unknown_24h` score `4.875` n `153` status `ready` deltaP `16.1235` edge `0.8308` maxDD `-35.8966`
- `market_context_high->index_24h` score `4.3017` n `153` status `ready` deltaP `18.3471` edge `0.359` maxDD `-4.1604`
- `market_context_high->crypto_major_4h` score `4.1891` n `196` status `ready` deltaP `21.6526` edge `0.4453` maxDD `-10.9117`
- `market_context_high->unknown_4h` score `3.0795` n `196` status `ready` deltaP `13.6417` edge `0.3928` maxDD `-11.1695`
- `market_context_high->equity_4h` score `2.9645` n `196` status `ready` deltaP `15.9594` edge `0.2501` maxDD `-5.0894`
- `market_context_high->equity_24h` score `2.5629` n `153` status `ready` deltaP `16.7726` edge `0.5916` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.7513` n `196` status `ready` deltaP `7.4209` edge `0.1155` maxDD `-4.1892`
- `market_context_high->index_4h` score `0.6539` n `196` status `ready` deltaP `9.8837` edge `0.0975` maxDD `-3.7119`
- `market_context_high->crypto_alt_24h` score `0.311` n `153` status `ready` deltaP `21.7238` edge `1.062` maxDD `-88.8062`
- `market_context_high->crypto_major_24h` score `0.2943` n `153` status `ready` deltaP `20.5208` edge `0.7463` maxDD `-62.3533`
- `market_context_high->crypto_major_1h` score `0.2268` n `196` status `ready` deltaP `5.0471` edge `0.0926` maxDD `-3.9211`
- `market_context_high->equity_1h` score `0.0478` n `196` status `ready` deltaP `4.9707` edge `0.0517` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.3329` n `196` status `ready` deltaP `2.5694` edge `0.0183` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.3384` n `196` status `ready` deltaP `11.8343` edge `0.1469` maxDD `-12.5349`
- `market_context_high->metal_1h` score `-0.5362` n `196` status `ready` deltaP `5.7956` edge `0.0262` maxDD `-6.3532`
- `market_context_high->fx_1h` score `-0.6482` n `196` status `ready` deltaP `-2.8168` edge `-0.0011` maxDD `-0.3914`
- `market_context_high->fx_24h` score `-0.7095` n `153` status `ready` deltaP `5.9378` edge `0.0062` maxDD `-1.3925`
- `market_context_high->unknown_1h` score `-1.5623` n `196` status `ready` deltaP `0.9379` edge `0.0105` maxDD `-7.7558`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
