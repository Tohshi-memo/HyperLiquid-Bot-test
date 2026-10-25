# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T22:22:29.714156+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5062`

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

- `market_context_high->unknown_4h` score `29.7285` n `113` status `ready` deltaP `-0.7487` edge `2.5159` maxDD `-1.016`
- `market_context_high->crypto_major_24h` score `0.6072` n `80` status `ready` deltaP `6.0069` edge `0.1131` maxDD `-4.5369`
- `market_context_high->fx_1h` score `-0.091` n `113` status `ready` deltaP `3.1106` edge `0.0025` maxDD `-0.1258`
- `market_context_high->fx_4h` score `-0.0974` n `113` status `ready` deltaP `6.5441` edge `0.0081` maxDD `-0.4545`
- `market_context_high->fx_24h` score `-0.357` n `80` status `ready` deltaP `13.8542` edge `0.0191` maxDD `-1.2451`
- `market_context_high->commodity_1h` score `-0.4667` n `113` status `ready` deltaP `0.1166` edge `0.0104` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.6775` n `113` status `ready` deltaP `-2.3356` edge `-0.0061` maxDD `-1.2155`
- `market_context_high->metal_1h` score `-0.6934` n `113` status `ready` deltaP `4.0353` edge `-0.0055` maxDD `-1.6682`
- `market_context_high->commodity_4h` score `-0.7733` n `113` status `ready` deltaP `-1.4759` edge `0.0336` maxDD `-1.165`
- `market_context_high->metal_24h` score `-0.8828` n `80` status `ready` deltaP `9.0972` edge `0.0932` maxDD `-7.3625`
- `market_context_high->index_24h` score `-1.1019` n `80` status `ready` deltaP `8.2292` edge `-0.0679` maxDD `-4.925`
- `market_context_high->crypto_major_1h` score `-1.3223` n `113` status `ready` deltaP `3.3967` edge `-0.0341` maxDD `-9.3126`
- `market_context_high->commodity_24h` score `-1.9637` n `80` status `ready` deltaP `-5.4861` edge `-0.0218` maxDD `-5.8041`
- `market_context_high->metal_4h` score `-2.023` n `113` status `ready` deltaP `3.3941` edge `-0.0202` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.1783` n `113` status `ready` deltaP `-8.2249` edge `-0.037` maxDD `-4.3282`
- `market_context_high->crypto_alt_1h` score `-3.1751` n `113` status `ready` deltaP `-1.4109` edge `-0.0678` maxDD `-11.3243`
- `market_context_high->equity_1h` score `-3.8943` n `113` status `ready` deltaP `-0.6889` edge `-0.0926` maxDD `-12.1865`
- `market_context_high->crypto_alt_24h` score `-6.831` n `80` status `ready` deltaP `-2.6736` edge `-0.2123` maxDD `-42.3182`
- `market_context_high->equity_24h` score `-8.2774` n `80` status `ready` deltaP `-3.4722` edge `-0.5097` maxDD `-36.6024`
- `market_context_high->crypto_major_4h` score `-10.1494` n `113` status `ready` deltaP `-13.8099` edge `-0.2539` maxDD `-32.9851`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
