# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T09:45:32.781018+00:00`
- Price records: `672`
- Market context records: `1723`
- Flow alert records: `6866`
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

- `market_context_high->metal_24h` score `6.657` n `143` status `ready` deltaP `25.5826` edge `0.6268` maxDD `-12.7414`
- `market_context_high->unknown_24h` score `5.9902` n `143` status `ready` deltaP `16.9683` edge `0.9181` maxDD `-35.8966`
- `market_context_high->crypto_alt_4h` score `5.9511` n `196` status `ready` deltaP `21.2762` edge `0.5307` maxDD `-9.1295`
- `market_context_high->crypto_major_4h` score `4.4682` n `196` status `ready` deltaP `23.1769` edge `0.4584` maxDD `-10.9117`
- `market_context_high->index_24h` score `3.9324` n `143` status `ready` deltaP `17.2563` edge `0.3355` maxDD `-4.1604`
- `market_context_high->unknown_4h` score `3.0437` n `196` status `ready` deltaP `13.7941` edge `0.3888` maxDD `-11.1695`
- `market_context_high->equity_4h` score `3.0189` n `196` status `ready` deltaP `16.2643` edge `0.2526` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.654` n `143` status `ready` deltaP `16.0162` edge `0.5209` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.7333` n `196` status `ready` deltaP `7.4209` edge `0.114` maxDD `-4.1892`
- `market_context_high->index_4h` score `0.536` n `196` status `ready` deltaP `8.6642` edge `0.0958` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.1777` n `196` status `ready` deltaP `4.7477` edge `0.0905` maxDD `-3.9211`
- `market_context_high->equity_1h` score `0.0227` n `196` status `ready` deltaP `4.6713` edge `0.0516` maxDD `-2.8014`
- `market_context_high->crypto_alt_24h` score `-0.031` n `143` status `ready` deltaP `22.6995` edge `1.027` maxDD `-88.8062`
- `market_context_high->metal_4h` score `-0.3377` n `196` status `ready` deltaP `11.8343` edge `0.147` maxDD `-12.5349`
- `market_context_high->index_1h` score `-0.4228` n `196` status `ready` deltaP `1.5215` edge `0.0178` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.5533` n `196` status `ready` deltaP `5.4962` edge `0.026` maxDD `-6.3532`
- `market_context_high->fx_1h` score `-0.6646` n `196` status `ready` deltaP `-3.1162` edge `-0.0012` maxDD `-0.3914`
- `market_context_high->fx_24h` score `-0.7868` n `143` status `ready` deltaP `4.8504` edge `0.007` maxDD `-1.3925`
- `market_context_high->crypto_major_24h` score `-0.7915` n `143` status `ready` deltaP `21.077` edge `0.6166` maxDD `-62.3533`
- `market_context_high->unknown_1h` score `-1.4797` n `196` status `ready` deltaP `1.8361` edge `0.0114` maxDD `-7.7558`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
