# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T18:37:24.842248+00:00`
- Price records: `672`
- Market context records: `3101`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6921`

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

- `market_context_high->crypto_alt_24h` score `16.5284` n `83` status `ready` deltaP `13.9432` edge `2.5571` maxDD `-33.816`
- `market_context_high->commodity_24h` score `15.1167` n `83` status `ready` deltaP `45.233` edge `1.001` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `14.8124` n `83` status `ready` deltaP `23.0945` edge `1.1292` maxDD `-1.9039`
- `market_context_high->index_24h` score `10.5605` n `83` status `ready` deltaP `31.9695` edge `0.9161` maxDD `-15.6019`
- `market_context_high->equity_24h` score `7.3865` n `83` status `ready` deltaP `18.1058` edge `1.363` maxDD `-36.9377`
- `market_context_high->commodity_4h` score `3.0557` n `117` status `ready` deltaP `18.2015` edge `0.1791` maxDD `-1.9973`
- `market_context_high->unknown_4h` score `0.6004` n `117` status `ready` deltaP `6.1106` edge `0.0855` maxDD `-3.7631`
- `market_context_high->commodity_1h` score `-0.071` n `120` status `ready` deltaP `1.3872` edge `0.0271` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.4699` n `120` status `ready` deltaP `4.4461` edge `0.0164` maxDD `-4.5023`
- `market_context_high->fx_24h` score `-0.6231` n `83` status `ready` deltaP `3.5601` edge `-0.0029` maxDD `-0.4876`
- `market_context_high->fx_1h` score `-0.6854` n `120` status `ready` deltaP `-7.2006` edge `-0.0026` maxDD `-0.3147`
- `market_context_high->crypto_alt_1h` score `-0.8302` n `120` status `ready` deltaP `3.0788` edge `0.086` maxDD `-14.7034`
- `market_context_high->equity_1h` score `-1.3331` n `120` status `ready` deltaP `-3.0339` edge `-0.0021` maxDD `-8.8863`
- `market_context_high->fx_4h` score `-1.3623` n `117` status `ready` deltaP `-12.8232` edge `-0.0048` maxDD `-1.0829`
- `market_context_high->index_4h` score `-1.3863` n `117` status `ready` deltaP `10.3464` edge `0.0442` maxDD `-17.6057`
- `market_context_high->crypto_major_1h` score `-2.2625` n `120` status `ready` deltaP `-1.2974` edge `0.0464` maxDD `-15.1032`
- `market_context_high->metal_1h` score `-2.424` n `120` status `ready` deltaP `-7.4751` edge `-0.0128` maxDD `-7.4828`
- `market_context_high->unknown_1h` score `-2.7046` n `120` status `ready` deltaP `3.3084` edge `-0.063` maxDD `-12.7554`
- `market_context_high->crypto_alt_4h` score `-3.8135` n `117` status `ready` deltaP `12.8947` edge `0.2296` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-4.1327` n `117` status `ready` deltaP `5.4631` edge `-0.0383` maxDD `-36.5699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
