# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T02:52:28.457606+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5104`

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

- `market_context_high->unknown_4h` score `27.6081` n `113` status `ready` deltaP `-1.6634` edge `2.3453` maxDD `-1.016`
- `market_context_high->fx_24h` score `0.0394` n `98` status `ready` deltaP `20.1425` edge `0.028` maxDD `-1.2451`
- `market_context_high->metal_24h` score `0.037` n `98` status `ready` deltaP `21.2656` edge `0.13` maxDD `-7.3625`
- `market_context_high->fx_4h` score `-0.0767` n `113` status `ready` deltaP `6.849` edge `0.0078` maxDD `-0.4545`
- `market_context_high->fx_1h` score `-0.1495` n `116` status `ready` deltaP `2.2094` edge `0.0016` maxDD `-0.173`
- `market_context_high->commodity_1h` score `-0.4813` n `116` status `ready` deltaP `-0.1858` edge `0.0112` maxDD `-1.0053`
- `market_context_high->commodity_4h` score `-0.6062` n `113` status `ready` deltaP `0.5058` edge `0.0418` maxDD `-1.165`
- `market_context_high->metal_1h` score `-0.6522` n `116` status `ready` deltaP `4.491` edge `-0.0051` maxDD `-1.6682`
- `market_context_high->index_24h` score `-0.7889` n `98` status `ready` deltaP `10.4237` edge `-0.0424` maxDD `-4.925`
- `market_context_high->index_1h` score `-1.0801` n `116` status `ready` deltaP `-2.7772` edge `-0.0063` maxDD `-1.2155`
- `market_context_high->metal_4h` score `-2.006` n `113` status `ready` deltaP `3.5466` edge `-0.0198` maxDD `-5.3474`
- `market_context_high->crypto_major_1h` score `-2.1287` n `116` status `ready` deltaP `2.772` edge `-0.0378` maxDD `-9.3126`
- `market_context_high->index_4h` score `-2.1498` n `113` status `ready` deltaP `-7.7676` edge `-0.0364` maxDD `-4.3282`
- `market_context_high->crypto_major_24h` score `-2.9265` n `98` status `ready` deltaP `1.1515` edge `-0.0315` maxDD `-12.9372`
- `market_context_high->crypto_alt_1h` score `-3.5068` n `116` status `ready` deltaP `-1.6571` edge `-0.0704` maxDD `-12.1963`
- `market_context_high->equity_1h` score `-3.92` n `116` status `ready` deltaP `-1.1305` edge `-0.0918` maxDD `-12.1865`
- `market_context_high->commodity_24h` score `-4.4964` n `98` status `ready` deltaP `-13.981` edge `-0.101` maxDD `-14.9141`
- `market_context_high->equity_24h` score `-7.3975` n `98` status `ready` deltaP `-1.9097` edge `-0.4073` maxDD `-36.6024`
- `market_context_high->crypto_major_4h` score `-10.0532` n `113` status `ready` deltaP `-12.7428` edge `-0.253` maxDD `-32.9851`
- `market_context_high->crypto_alt_24h` score `-10.1798` n `98` status `ready` deltaP `-9.662` edge `-0.3869` maxDD `-58.9699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
