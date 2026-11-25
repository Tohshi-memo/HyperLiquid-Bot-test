# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T22:52:27.050565+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3696`

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

- `market_context_high->unknown_1h` score `32152.2458` n `45` status `ready` deltaP `1.4171` edge `2679.3538` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21824.1262` n `45` status `ready` deltaP `1.958` edge `1818.678` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `917.2909` n `31` status `ready` deltaP `1.6322` edge `76.4476` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `571.1787` n `31` status `ready` deltaP `3.1766` edge `47.5827` maxDD `-0.1191`
- `news_risk_high->unknown_24h` score `288.3205` n `31` status `ready` deltaP `6.0764` edge `23.9862` maxDD `0.0`
- `news_risk_high->equity_24h` score `45.9147` n `31` status `ready` deltaP `52.0833` edge `3.479` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `42.0807` n `31` status `ready` deltaP `53.2986` edge `3.1514` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `37.5246` n `31` status `ready` deltaP `52.7778` edge `2.7752` maxDD `0.0`
- `news_risk_high->metal_24h` score `11.5948` n `31` status `ready` deltaP `39.1521` edge `0.7327` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.8843` n `31` status `ready` deltaP `26.3031` edge `0.8187` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `10.4469` n `31` status `ready` deltaP `37.8344` edge `0.6664` maxDD `-2.178`
- `news_risk_high->index_24h` score `7.4619` n `31` status `ready` deltaP `53.2986` edge `0.2665` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `6.7096` n `31` status `ready` deltaP `17.5403` edge `0.885` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `5.2726` n `31` status `ready` deltaP `44.8365` edge `0.1533` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.6715` n `31` status `ready` deltaP `19.9874` edge `0.1914` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.3512` n `31` status `ready` deltaP `36.4625` edge `0.0622` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6734` n `31` status `ready` deltaP `31.6931` edge `0.02` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4594` n `31` status `ready` deltaP `10.1603` edge `0.2937` maxDD `-1.6897`
- `market_context_high->fx_4h` score `2.3303` n `45` status `ready` deltaP `28.8685` edge `0.0302` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.2635` n `31` status `ready` deltaP `12.8549` edge `0.2402` maxDD `-1.5232`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
