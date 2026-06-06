# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T23:22:26.157831+00:00`
- Price records: `672`
- Market context records: `3122`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7027`

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

- `market_context_high->commodity_24h` score `14.4854` n `100` status `ready` deltaP `47.0764` edge `0.9361` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `12.2482` n `100` status `ready` deltaP `21.7917` edge `0.9242` maxDD `-1.9039`
- `market_context_high->crypto_alt_24h` score `11.6032` n `100` status `ready` deltaP `10.5556` edge `2.3248` maxDD `-63.9403`
- `market_context_high->index_24h` score `6.6089` n `100` status `ready` deltaP `32.0764` edge `0.8889` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.6948` n `100` status `ready` deltaP `12.1875` edge `1.3119` maxDD `-51.6338`
- `market_context_high->commodity_4h` score `3.0133` n `126` status `ready` deltaP `18.721` edge `0.1721` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `-0.0514` n `138` status `ready` deltaP `1.8268` edge `0.0258` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.4603` n `138` status `ready` deltaP `4.2697` edge `0.0188` maxDD `-4.5023`
- `market_context_high->fx_24h` score `-0.5207` n `100` status `ready` deltaP `4.5556` edge `-0.001` maxDD `-0.4876`
- `market_context_high->crypto_alt_1h` score `-0.7451` n `138` status `ready` deltaP `3.3954` edge `0.0948` maxDD `-14.7034`
- `market_context_high->equity_1h` score `-1.0253` n `138` status `ready` deltaP `0.8743` edge `0.0113` maxDD `-8.8863`
- `market_context_high->fx_1h` score `-1.1446` n `138` status `ready` deltaP `-10.9715` edge `-0.0057` maxDD `-0.7651`
- `market_context_high->index_4h` score `-1.3044` n `126` status `ready` deltaP `11.2006` edge `0.049` maxDD `-17.6057`
- `market_context_high->fx_4h` score `-1.4365` n `126` status `ready` deltaP `-13.8599` edge `-0.0074` maxDD `-1.0829`
- `market_context_high->crypto_major_1h` score `-2.0292` n `138` status `ready` deltaP `0.0889` edge `0.0566` maxDD `-15.1032`
- `market_context_high->metal_1h` score `-2.2494` n `138` status `ready` deltaP `-6.2527` edge `-0.0064` maxDD `-7.4828`
- `market_context_high->unknown_4h` score `-2.3647` n `126` status `ready` deltaP `1.96` edge `0.0121` maxDD `-14.7778`
- `market_context_high->unknown_1h` score `-3.0316` n `138` status `ready` deltaP `1.6055` edge `-0.0607` maxDD `-14.2111`
- `market_context_high->crypto_alt_4h` score `-3.654` n `126` status `ready` deltaP `14.2083` edge `0.2413` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-3.7865` n `126` status `ready` deltaP `8.0575` edge `-0.0086` maxDD `-36.7784`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
