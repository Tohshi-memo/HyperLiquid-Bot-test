# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T16:22:43.182498+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9839`

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

- `market_context_high->unknown_24h` score `30.3082` n `54` status `ready` deltaP `22.1064` edge `2.3826` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.2175` n `89` status `ready` deltaP `0.0205` edge `0.5342` maxDD `-3.6303`
- `market_context_high->crypto_alt_24h` score `4.4888` n `54` status `ready` deltaP `25.6365` edge `0.2575` maxDD `-1.6806`
- `market_context_high->commodity_24h` score `2.375` n `54` status `ready` deltaP `26.9676` edge `0.2641` maxDD `-8.4846`
- `market_context_high->commodity_4h` score `1.1343` n `89` status `ready` deltaP `14.7677` edge `0.0807` maxDD `-2.7703`
- `market_context_high->commodity_1h` score `0.2172` n `89` status `ready` deltaP `5.5053` edge `0.023` maxDD `-1.3282`
- `market_context_high->fx_4h` score `0.2063` n `89` status `ready` deltaP `15.5916` edge `0.0085` maxDD `-1.8797`
- `market_context_high->fx_1h` score `0.1865` n `89` status `ready` deltaP `8.0536` edge `-0.0033` maxDD `-0.7878`
- `market_context_high->index_1h` score `-0.5127` n `89` status `ready` deltaP `0.8663` edge `-0.0181` maxDD `-1.6054`
- `market_context_high->metal_1h` score `-0.5683` n `89` status `ready` deltaP `-1.9814` edge `-0.0102` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.6681` n `89` status `ready` deltaP `3.662` edge `0.0134` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-0.8209` n `89` status `ready` deltaP `4.7907` edge `0.0018` maxDD `-5.7857`
- `market_context_high->fx_24h` score `-1.049` n `54` status `ready` deltaP `1.3889` edge `0.0239` maxDD `-4.3126`
- `market_context_high->crypto_alt_1h` score `-1.0954` n `89` status `ready` deltaP `-2.1345` edge `-0.006` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.7247` n `89` status `ready` deltaP `4.3884` edge `-0.0968` maxDD `-10.619`
- `market_context_high->metal_24h` score `-1.8518` n `54` status `ready` deltaP `-17.6505` edge `-0.0029` maxDD `-2.6802`
- `market_context_high->index_4h` score `-1.9197` n `89` status `ready` deltaP `-10.7358` edge `-0.0491` maxDD `-4.7021`
- `market_context_high->unknown_1h` score `-3.4206` n `89` status `ready` deltaP `2.661` edge `-0.2581` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.4797` n `89` status `ready` deltaP `-12.3966` edge `-0.07` maxDD `-7.6533`
- `market_context_high->index_24h` score `-4.2553` n `54` status `ready` deltaP `-21.7593` edge `-0.181` maxDD `-7.8922`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
