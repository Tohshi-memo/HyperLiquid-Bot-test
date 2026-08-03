# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T05:52:25.849750+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5935`

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

- `news_risk_high->unknown_24h` score `1704.3671` n `39` status `ready` deltaP `20.1255` edge `141.9385` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `13.3407` n `40` status `ready` deltaP `51.4583` edge `0.8084` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `11.0442` n `40` status `ready` deltaP `51.3194` edge `0.591` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `0.9891` n `39` status `ready` deltaP `-3.8736` edge `0.229` maxDD `-3.4427`
- `news_risk_high->commodity_1h` score `0.6644` n `39` status `ready` deltaP `16.3481` edge `-0.001` maxDD `-0.8244`
- `news_risk_high->index_4h` score `0.5078` n `39` status `ready` deltaP `3.9713` edge `0.0539` maxDD `-0.3783`
- `market_context_high->commodity_1h` score `0.3595` n `47` status `ready` deltaP `7.5646` edge `0.0331` maxDD `-1.3282`
- `market_context_high->commodity_4h` score `0.3122` n `47` status `ready` deltaP `5.0338` edge `0.0911` maxDD `-2.7703`
- `market_context_high->fx_4h` score `0.0596` n `47` status `ready` deltaP `14.1801` edge `-0.0039` maxDD `-1.8531`
- `market_context_high->fx_1h` score `0.0157` n `47` status `ready` deltaP `7.4149` edge `-0.0085` maxDD `-0.7804`
- `news_risk_high->metal_1h` score `-0.0713` n `39` status `ready` deltaP `2.6486` edge `0.0052` maxDD `-0.5599`
- `market_context_high->crypto_alt_4h` score `-0.2165` n `47` status `ready` deltaP `2.2963` edge `0.0475` maxDD `-4.9116`
- `news_risk_high->fx_24h` score `-0.3192` n `39` status `ready` deltaP `6.2366` edge `0.0318` maxDD `-2.8111`
- `news_risk_high->fx_1h` score `-0.3271` n `39` status `ready` deltaP `-1.7504` edge `0.002` maxDD `-0.2475`
- `news_risk_high->metal_4h` score `-0.4635` n `39` status `ready` deltaP `0.6723` edge `-0.008` maxDD `-0.8085`
- `news_risk_high->crypto_alt_1h` score `-0.492` n `39` status `ready` deltaP `2.7791` edge `-0.0134` maxDD `-3.1233`
- `news_risk_high->fx_4h` score `-0.5426` n `39` status `ready` deltaP `-1.4228` edge `0.027` maxDD `-0.6326`
- `news_risk_high->commodity_4h` score `-0.6088` n `39` status `ready` deltaP `4.8155` edge `-0.043` maxDD `-3.0389`
- `news_risk_high->index_1h` score `-0.6364` n `39` status `ready` deltaP `-2.7791` edge `-0.0022` maxDD `-0.5845`
- `market_context_high->fx_24h` score `-0.6839` n `40` status `ready` deltaP `0.6597` edge `0.0366` maxDD `-2.506`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
