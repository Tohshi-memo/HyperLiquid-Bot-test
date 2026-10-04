# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T18:52:30.601899+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5058`

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

- `market_context_high->unknown_1h` score `96.788` n `97` status `ready` deltaP `-0.3102` edge `8.1092` maxDD `-0.9839`
- `market_context_high->unknown_4h` score `78.5486` n `97` status `ready` deltaP `2.7564` edge `6.5585` maxDD `-0.4928`
- `news_risk_high->crypto_major_4h` score `10.5275` n `65` status `ready` deltaP `37.2772` edge `0.6491` maxDD `-0.6258`
- `market_context_high->crypto_major_24h` score `9.1604` n `46` status `ready` deltaP `30.4498` edge `0.6256` maxDD `-4.5519`
- `market_context_high->crypto_alt_24h` score `8.9157` n `46` status `ready` deltaP `24.0112` edge `0.7102` maxDD `-8.1838`
- `news_risk_high->crypto_alt_4h` score `7.487` n `65` status `ready` deltaP `24.6646` edge `0.5939` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `7.1339` n `65` status `ready` deltaP `21.4504` edge `0.4615` maxDD `-0.1344`
- `market_context_high->crypto_major_4h` score `4.861` n `97` status `ready` deltaP `21.2582` edge `0.3337` maxDD `-3.294`
- `news_risk_high->index_24h` score `3.8357` n `65` status `ready` deltaP `26.7361` edge `0.1414` maxDD `0.0`
- `news_risk_high->equity_4h` score `3.8004` n `65` status `ready` deltaP `25.6074` edge `0.207` maxDD `-2.881`
- `news_risk_high->index_4h` score `3.2805` n `65` status `ready` deltaP `35.8771` edge `0.0604` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.8945` n `65` status `ready` deltaP `12.4113` edge `0.194` maxDD `-1.5096`
- `news_risk_high->metal_4h` score `2.6574` n `65` status `ready` deltaP `23.1942` edge `0.1084` maxDD `-0.993`
- `news_risk_high->index_1h` score `2.1836` n `65` status `ready` deltaP `26.8148` edge `0.0182` maxDD `-0.1997`
- `market_context_high->crypto_major_1h` score `2.156` n `97` status `ready` deltaP `15.3297` edge `0.1225` maxDD `-2.2692`
- `news_risk_high->crypto_alt_1h` score `1.6721` n `65` status `ready` deltaP `6.0663` edge `0.1508` maxDD `-2.4854`
- `market_context_high->crypto_alt_4h` score `1.6002` n `97` status `ready` deltaP `6.5203` edge `0.2688` maxDD `-7.6465`
- `market_context_high->fx_4h` score `1.3946` n `97` status `ready` deltaP `24.9733` edge `0.0254` maxDD `-0.3868`
- `market_context_high->fx_24h` score `1.3646` n `46` status `ready` deltaP `25.536` edge `0.1065` maxDD `-1.8102`
- `market_context_high->fx_1h` score `0.9636` n `97` status `ready` deltaP `15.0163` edge `0.0066` maxDD `-0.113`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
