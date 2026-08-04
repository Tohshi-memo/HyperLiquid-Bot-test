# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T17:52:43.216531+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9856`

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

- `market_context_high->unknown_24h` score `26.6277` n `60` status `ready` deltaP `21.25` edge `2.0816` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.3951` n `89` status `ready` deltaP `0.9351` edge `0.5429` maxDD `-3.6303`
- `market_context_high->crypto_alt_24h` score `2.6202` n `60` status `ready` deltaP `17.6736` edge `0.1936` maxDD `-2.7795`
- `market_context_high->commodity_4h` score `1.2554` n `89` status `ready` deltaP `15.6823` edge `0.0847` maxDD `-2.7703`
- `market_context_high->commodity_24h` score `0.3381` n `60` status `ready` deltaP `20.4166` edge `0.1542` maxDD `-15.091`
- `market_context_high->commodity_1h` score `0.2006` n `90` status `ready` deltaP `5.1929` edge `0.0237` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.1746` n `90` status `ready` deltaP `7.9042` edge `-0.0033` maxDD `-0.7878`
- `market_context_high->fx_4h` score `0.1548` n `89` status `ready` deltaP `14.677` edge `0.008` maxDD `-1.8797`
- `market_context_high->fx_24h` score `-0.3901` n `60` status `ready` deltaP `7.5694` edge `0.0376` maxDD `-4.3126`
- `market_context_high->index_1h` score `-0.5386` n `90` status `ready` deltaP `0.4425` edge `-0.0186` maxDD `-1.6054`
- `market_context_high->metal_1h` score `-0.5784` n `90` status `ready` deltaP `-2.2056` edge `-0.01` maxDD `-1.6224`
- `market_context_high->crypto_alt_1h` score `-0.7172` n `90` status `ready` deltaP `-2.159` edge `-0.0065` maxDD `-3.0178`
- `market_context_high->metal_4h` score `-0.7399` n `89` status `ready` deltaP `2.7474` edge `0.0103` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-0.8533` n `89` status `ready` deltaP `4.3334` edge `0.0007` maxDD `-5.7857`
- `market_context_high->metal_24h` score `-0.8688` n `60` status `ready` deltaP `-12.9514` edge `0.0918` maxDD `-2.6802`
- `market_context_high->equity_1h` score `-1.7445` n `90` status `ready` deltaP `4.2016` edge `-0.0981` maxDD `-10.619`
- `market_context_high->index_4h` score `-1.9992` n `89` status `ready` deltaP `-11.6505` edge `-0.0532` maxDD `-4.7021`
- `market_context_high->index_24h` score `-3.4584` n `60` status `ready` deltaP `-16.875` edge `-0.1114` maxDD `-7.8922`
- `market_context_high->unknown_1h` score `-3.4792` n `90` status `ready` deltaP `2.1989` edge `-0.2599` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.4871` n `90` status `ready` deltaP `-12.3087` edge `-0.0712` maxDD `-7.6533`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
