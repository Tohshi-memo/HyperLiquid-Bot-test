# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T20:37:31.445107+00:00`
- Price records: `672`
- Market context records: `8549`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5925`

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

- `news_risk_high->unknown_24h` score `5436.2793` n `58` status `ready` deltaP `41.8881` edge `452.7861` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.5577` n `64` status `ready` deltaP `20.0457` edge `0.3892` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.8989` n `64` status `ready` deltaP `15.4345` edge `0.0744` maxDD `-0.191`
- `market_context_high->crypto_alt_4h` score `1.8968` n `62` status `ready` deltaP `13.3605` edge `0.1647` maxDD `-5.323`
- `news_risk_high->equity_1h` score `1.7049` n `64` status `ready` deltaP `16.1022` edge `0.0824` maxDD `-2.4803`
- `news_risk_high->crypto_major_4h` score `0.9832` n `64` status `ready` deltaP `6.2881` edge `0.1617` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.6419` n `64` status `ready` deltaP `12.9573` edge `0.1351` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.4789` n `64` status `ready` deltaP `8.4113` edge `0.058` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3625` n `64` status `ready` deltaP `6.9143` edge `0.0516` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.0706` n `64` status `ready` deltaP `4.9869` edge `0.0039` maxDD `-0.2475`
- `news_risk_high->index_1h` score `0.0044` n `64` status `ready` deltaP `3.6209` edge `0.0081` maxDD `-0.5338`
- `news_risk_high->metal_4h` score `-0.0483` n `64` status `ready` deltaP `1.5625` edge `0.031` maxDD `-0.8085`
- `news_risk_high->fx_4h` score `-0.0829` n `64` status `ready` deltaP `10.2515` edge `0.0205` maxDD `-0.6604`
- `news_risk_high->metal_1h` score `-0.1623` n `64` status `ready` deltaP `2.9566` edge `0.0071` maxDD `-0.5599`
- `market_context_high->fx_4h` score `-0.2512` n `62` status `ready` deltaP `7.0761` edge `0.0115` maxDD `-1.3685`
- `market_context_high->commodity_1h` score `-0.2779` n `62` status `ready` deltaP `4.3075` edge `-0.0018` maxDD `-2.0038`
- `market_context_high->fx_1h` score `-0.2941` n `62` status `ready` deltaP `1.9123` edge `-0.0002` maxDD `-0.6874`
- `market_context_high->crypto_alt_1h` score `-0.4979` n `62` status `ready` deltaP `-2.627` edge `0.0164` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.7764` n `62` status `ready` deltaP `0.6471` edge `-0.0161` maxDD `-1.5667`
- `market_context_high->commodity_4h` score `-0.9519` n `62` status `ready` deltaP `2.0604` edge `0.0157` maxDD `-5.4508`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
