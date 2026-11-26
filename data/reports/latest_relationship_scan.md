# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T17:22:28.262454+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3419`

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

- `news_risk_high->unknown_1h` score `3224.2656` n `31` status `ready` deltaP `2.231` edge `268.6915` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3217.6514` n `31` status `ready` deltaP `4.0913` edge `268.116` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `31.6276` n `31` status `ready` deltaP `40.625` edge `2.3648` maxDD `0.0`
- `news_risk_high->equity_24h` score `29.4078` n `31` status `ready` deltaP `39.7569` edge `2.1856` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `25.4352` n `31` status `ready` deltaP `39.9306` edge `1.8534` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `10.4025` n `31` status `ready` deltaP `25.8457` edge `0.7816` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `9.5323` n `31` status `ready` deltaP `37.682` edge `0.5912` maxDD `-2.178`
- `news_risk_high->metal_24h` score `7.3186` n `31` status `ready` deltaP `26.3049` edge `0.462` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `6.7855` n `31` status `ready` deltaP `18.7598` edge `0.8866` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.1049` n `31` status `ready` deltaP `41.1458` edge `0.1511` maxDD `0.0`
- `news_risk_high->fx_24h` score `4.7865` n `31` status `ready` deltaP `39.9754` edge `0.1452` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.5646` n `31` status `ready` deltaP `20.4365` edge `0.1795` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.2718` n `31` status `ready` deltaP `36.31` edge `0.0566` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7345` n `31` status `ready` deltaP `32.5913` edge `0.0191` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4509` n `31` status `ready` deltaP `9.5615` edge `0.2966` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.1816` n `31` status `ready` deltaP `12.4058` edge `0.2327` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.4301` n `31` status `ready` deltaP `28.3851` edge `0.022` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.8961` n `31` status `ready` deltaP `14.4915` edge `0.074` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.3293` n `31` status `ready` deltaP `11.1133` edge `0.0079` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.3939` n `31` status `ready` deltaP `-2.2117` edge `0.0081` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
