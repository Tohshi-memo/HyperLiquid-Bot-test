# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-22T10:37:29.400678+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `40`

- Symbol pattern count: `4008`

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

- `market_context_high->unknown_1h` score `12053.8627` n `106` status `ready` deltaP `-0.0933` edge `1004.509` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `7541.4051` n `106` status `ready` deltaP `-2.4218` edge `628.4971` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1530.436` n `30` status `ready` deltaP `4.5608` edge `127.5235` maxDD `-0.7389`
- `news_risk_high->equity_1h` score `3.8997` n `30` status `ready` deltaP `18.9122` edge `0.2176` maxDD `-0.163`
- `news_risk_high->index_1h` score `2.6266` n `30` status `ready` deltaP `30.7485` edge `0.0224` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4407` n `30` status `ready` deltaP `7.7146` edge `0.3076` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.9877` n `30` status `ready` deltaP `6.9661` edge `0.2441` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.4664` n `30` status `ready` deltaP `27.6746` edge `0.0314` maxDD `-0.2315`
- `news_risk_high->commodity_1h` score `-0.0469` n `30` status `ready` deltaP `1.6467` edge `0.0113` maxDD `-0.0947`
- `market_context_high->metal_1h` score `-0.3293` n `106` status `ready` deltaP `2.4545` edge `0.0079` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.4311` n `106` status `ready` deltaP `1.6919` edge `0.0015` maxDD `-1.2295`
- `market_context_high->fx_1h` score `-1.1137` n `106` status `ready` deltaP `-7.2789` edge `-0.0013` maxDD `-0.4384`
- `market_context_high->fx_4h` score `-1.51` n `106` status `ready` deltaP `-0.0115` edge `0.0037` maxDD `-1.444`
- `news_risk_high->fx_1h` score `-1.8227` n `30` status `ready` deltaP `-15.9581` edge `-0.0019` maxDD `-0.1548`
- `market_context_high->crypto_major_1h` score `-1.8589` n `106` status `ready` deltaP `2.9347` edge `-0.0469` maxDD `-13.8788`
- `market_context_high->equity_1h` score `-2.0167` n `106` status `ready` deltaP `6.0191` edge `-0.0106` maxDD `-13.1399`
- `market_context_high->metal_4h` score `-2.0933` n `106` status `ready` deltaP `1.5416` edge `-0.0041` maxDD `-10.1161`
- `market_context_high->commodity_1h` score `-2.544` n `106` status `ready` deltaP `-11.5608` edge `-0.0274` maxDD `-4.2689`
- `market_context_high->index_4h` score `-3.4606` n `106` status `ready` deltaP `-13.9323` edge `-0.0322` maxDD `-7.0639`
- `market_context_high->crypto_alt_1h` score `-3.7704` n `106` status `ready` deltaP `-5.361` edge `-0.0674` maxDD `-13.8848`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
