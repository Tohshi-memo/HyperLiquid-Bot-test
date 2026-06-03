# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T19:37:34.879044+00:00`
- Price records: `672`
- Market context records: `2794`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9237`

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

- `market_context_high->unknown_24h` score `3.016` n `142` status `ready` deltaP `5.2058` edge `0.2631` maxDD `-1.7175`
- `market_context_high->crypto_alt_24h` score `1.9757` n `142` status `ready` deltaP `2.702` edge `0.5383` maxDD `-22.6673`
- `market_context_high->unknown_4h` score `0.8846` n `142` status `ready` deltaP `6.338` edge `0.1368` maxDD `-3.7602`
- `market_context_high->commodity_24h` score `0.5785` n `142` status `ready` deltaP `11.0377` edge `0.284` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.331` n `142` status `ready` deltaP `13.4533` edge `0.0369` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.017` n `142` status `ready` deltaP `4.3308` edge `0.0428` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.0898` n `142` status `ready` deltaP `4.198` edge `0.0099` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.5383` n `142` status `ready` deltaP `-0.5376` edge `0.0031` maxDD `-0.2164`
- `market_context_high->metal_1h` score `-0.6232` n `142` status `ready` deltaP `0.5819` edge `0.0008` maxDD `-3.0996`
- `market_context_high->commodity_1h` score `-0.6826` n `142` status `ready` deltaP `-0.7316` edge `-0.0073` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.7147` n `142` status `ready` deltaP `4.7968` edge `0.0524` maxDD `-10.747`
- `market_context_high->crypto_major_1h` score `-0.8975` n `142` status `ready` deltaP `4.0757` edge `0.0447` maxDD `-9.622`
- `market_context_high->equity_1h` score `-0.9675` n `142` status `ready` deltaP `-2.5997` edge `0.02` maxDD `-2.6634`
- `market_context_high->fx_4h` score `-1.1447` n `142` status `ready` deltaP `-3.753` edge `0.0075` maxDD `-0.5631`
- `market_context_high->equity_4h` score `-1.1826` n `142` status `ready` deltaP `2.2673` edge `0.0243` maxDD `-5.7037`
- `market_context_high->crypto_alt_4h` score `-1.4149` n `142` status `ready` deltaP `14.1854` edge `0.2216` maxDD `-28.7261`
- `market_context_high->fx_24h` score `-1.5341` n `142` status `ready` deltaP `-2.7533` edge `-0.0223` maxDD `-0.6418`
- `market_context_high->commodity_4h` score `-1.66` n `142` status `ready` deltaP `-0.6012` edge `-0.0168` maxDD `-10.0279`
- `market_context_high->metal_4h` score `-2.06` n `142` status `ready` deltaP `-0.0086` edge `-0.009` maxDD `-11.4038`
- `market_context_high->crypto_major_4h` score `-2.4387` n `142` status `ready` deltaP `5.7347` edge `0.1397` maxDD `-32.2466`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
