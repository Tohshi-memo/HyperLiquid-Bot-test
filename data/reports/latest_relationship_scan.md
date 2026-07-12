# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T18:52:27.254906+00:00`
- Price records: `672`
- Market context records: `6529`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `7866`

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

- `news_risk_high->crypto_alt_24h` score `13.3735` n `32` status `ready` deltaP `36.211` edge `0.8878` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.5844` n `32` status `ready` deltaP `54.4194` edge `0.1859` maxDD `0.0`
- `market_context_high->unknown_24h` score `6.2587` n `144` status `ready` deltaP `11.8934` edge `0.7723` maxDD `-15.0689`
- `news_risk_high->crypto_major_24h` score `4.8691` n `32` status `ready` deltaP `20.911` edge `0.5628` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `3.6987` n `38` status `ready` deltaP `39.1688` edge `0.0517` maxDD `-0.0345`
- `market_context_high->unknown_1h` score `2.334` n `189` status `ready` deltaP `-5.535` edge `0.3215` maxDD `-3.2083`
- `news_risk_high->commodity_24h` score `2.0752` n `32` status `ready` deltaP `22.6766` edge `0.0423` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `1.7784` n `38` status `ready` deltaP `22.3133` edge `0.0175` maxDD `-0.1113`
- `market_context_high->commodity_24h` score `1.6562` n `144` status `ready` deltaP `14.6905` edge `0.2269` maxDD `-5.2791`
- `market_context_high->index_4h` score `0.7005` n `178` status `ready` deltaP `14.5365` edge `0.0291` maxDD `-0.4108`
- `news_risk_high->crypto_major_1h` score `0.5956` n `38` status `ready` deltaP `5.3498` edge `0.0944` maxDD `-2.6299`
- `market_context_high->crypto_alt_4h` score `0.4456` n `178` status `ready` deltaP `11.1006` edge `0.1185` maxDD `-6.7632`
- `news_risk_high->crypto_alt_1h` score `0.1023` n `38` status `ready` deltaP `1.8831` edge `0.0515` maxDD `-2.0756`
- `news_risk_high->index_24h` score `-0.2506` n `32` status `ready` deltaP `7.5498` edge `0.0047` maxDD `-2.3058`
- `market_context_high->crypto_major_4h` score `-0.3834` n `178` status `ready` deltaP `13.0344` edge `0.093` maxDD `-12.6576`
- `market_context_high->equity_4h` score `-0.3894` n `178` status `ready` deltaP `9.2937` edge `0.058` maxDD `-8.2573`
- `market_context_high->commodity_1h` score `-0.4357` n `189` status `ready` deltaP `2.0325` edge `-0.0011` maxDD `-2.1314`
- `market_context_high->fx_1h` score `-0.4695` n `189` status `ready` deltaP `-1.1343` edge `-0.0019` maxDD `-0.7249`
- `market_context_high->crypto_major_1h` score `-0.562` n `189` status `ready` deltaP `6.1853` edge `0.0133` maxDD `-6.7936`
- `market_context_high->unknown_4h` score `-0.6016` n `178` status `ready` deltaP `-20.1853` edge `0.325` maxDD `-10.5788`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
