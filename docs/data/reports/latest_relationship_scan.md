# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T12:07:26.614841+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14754`

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

- `market_context_high->unknown_1h` score `1.0004` n `145` status `ready` deltaP `7.4975` edge `0.0561` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.2469` n `135` status `ready` deltaP `18.5693` edge `-0.0593` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.073` n `135` status `ready` deltaP `7.4729` edge `0.0098` maxDD `-0.3539`
- `market_context_high->index_1h` score `0.0241` n `145` status `ready` deltaP `7.7225` edge `0.0047` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.0225` n `145` status `ready` deltaP `4.2154` edge `0.0049` maxDD `-0.2043`
- `market_context_high->metal_4h` score `-0.2818` n `135` status `ready` deltaP `6.4295` edge `-0.0174` maxDD `-1.5942`
- `market_context_high->metal_1h` score `-0.3062` n `145` status `ready` deltaP `1.1253` edge `-0.0049` maxDD `-0.6822`
- `market_context_high->equity_1h` score `-0.3531` n `145` status `ready` deltaP `4.3382` edge `0.0328` maxDD `-5.2257`
- `market_context_high->index_4h` score `-0.5471` n `135` status `ready` deltaP `3.3333` edge `0.0112` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.689` n `135` status `ready` deltaP `-1.1709` edge `0.0045` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.8982` n `145` status `ready` deltaP `-6.6694` edge `-0.0016` maxDD `-1.1941`
- `market_context_high->equity_4h` score `-1.6734` n `135` status `ready` deltaP `-0.4991` edge `0.0693` maxDD `-16.1079`
- `market_context_high->crypto_alt_4h` score `-1.6862` n `135` status `ready` deltaP `5.1265` edge `-0.0477` maxDD `-5.4926`
- `market_context_high->fx_24h` score `-1.8842` n `121` status `ready` deltaP `-0.6643` edge `0.0084` maxDD `-2.2121`
- `market_context_high->commodity_24h` score `-1.92` n `121` status `ready` deltaP `-5.1409` edge `0.0576` maxDD `-4.666`
- `market_context_high->crypto_alt_1h` score `-2.3624` n `145` status `ready` deltaP `-2.2486` edge `-0.0324` maxDD `-7.9582`
- `market_context_high->crypto_major_1h` score `-3.4018` n `145` status `ready` deltaP `-4.7718` edge `-0.1058` maxDD `-7.6697`
- `market_context_high->index_24h` score `-4.4535` n `121` status `ready` deltaP `-8.0248` edge `-0.046` maxDD `-20.3839`
- `market_context_high->crypto_major_4h` score `-5.4175` n `135` status `ready` deltaP `-1.0829` edge `-0.3178` maxDD `-5.1148`
- `market_context_high->metal_24h` score `-5.4193` n `121` status `ready` deltaP `-24.0732` edge `-0.2035` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
