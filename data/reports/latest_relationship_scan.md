# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T18:37:28.765901+00:00`
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

- `market_context_high->unknown_24h` score `25.0299` n `63` status `ready` deltaP `20.8085` edge `1.9514` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.4569` n `89` status `ready` deltaP `1.3925` edge `0.545` maxDD `-3.6303`
- `market_context_high->crypto_alt_24h` score `1.8006` n `63` status `ready` deltaP `14.2609` edge `0.1686` maxDD `-3.4232`
- `market_context_high->commodity_4h` score `1.316` n `89` status `ready` deltaP `16.1397` edge `0.0867` maxDD `-2.7703`
- `market_context_high->commodity_1h` score `0.1862` n `90` status `ready` deltaP `5.0432` edge `0.0235` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.1746` n `90` status `ready` deltaP `7.9042` edge `-0.0033` maxDD `-0.7878`
- `market_context_high->fx_4h` score `0.1533` n `89` status `ready` deltaP `14.677` edge `0.0078` maxDD `-1.8797`
- `market_context_high->fx_24h` score `-0.093` n `63` status `ready` deltaP `10.1438` edge `0.0452` maxDD `-4.3126`
- `market_context_high->metal_24h` score `-0.4413` n `63` status `ready` deltaP `-10.491` edge `0.1302` maxDD `-2.6802`
- `market_context_high->index_1h` score `-0.5479` n `90` status `ready` deltaP `0.2928` edge `-0.0188` maxDD `-1.6054`
- `market_context_high->metal_1h` score `-0.5597` n `90` status `ready` deltaP `-1.9062` edge `-0.0096` maxDD `-1.6224`
- `market_context_high->commodity_24h` score `-0.6157` n `63` status `ready` deltaP `17.6836` edge `0.106` maxDD `-18.5593`
- `market_context_high->crypto_alt_1h` score `-0.7281` n `90` status `ready` deltaP `-2.3087` edge `-0.0069` maxDD `-3.0178`
- `market_context_high->metal_4h` score `-0.762` n `89` status `ready` deltaP `2.4425` edge `0.0095` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-0.8619` n `89` status `ready` deltaP `4.3334` edge `-0.0004` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.7305` n `90` status `ready` deltaP `4.3513` edge `-0.0973` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.0094` n `89` status `ready` deltaP `-11.6505` edge `-0.0545` maxDD `-4.7021`
- `market_context_high->index_24h` score `-3.1155` n `63` status `ready` deltaP `-14.8562` edge `-0.0809` maxDD `-7.8922`
- `market_context_high->crypto_major_1h` score `-3.4715` n `90` status `ready` deltaP `-12.159` edge `-0.0709` maxDD `-7.6533`
- `market_context_high->unknown_1h` score `-3.4768` n `90` status `ready` deltaP `2.1989` edge `-0.2597` maxDD `-1.2421`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
