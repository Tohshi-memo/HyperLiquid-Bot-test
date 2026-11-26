# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T17:07:29.656031+00:00`
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

- `news_risk_high->unknown_1h` score `3224.2596` n `31` status `ready` deltaP `2.231` edge `268.691` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3217.5756` n `31` status `ready` deltaP `3.9388` edge `268.1107` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `31.8227` n `31` status `ready` deltaP `40.7986` edge `2.3799` maxDD `0.0`
- `news_risk_high->equity_24h` score `29.6916` n `31` status `ready` deltaP `39.9306` edge `2.2081` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `25.6315` n `31` status `ready` deltaP `40.1042` edge `1.8686` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `10.4049` n `31` status `ready` deltaP `25.8457` edge `0.7818` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `9.5803` n `31` status `ready` deltaP `37.682` edge `0.5952` maxDD `-2.178`
- `news_risk_high->metal_24h` score `7.3757` n `31` status `ready` deltaP `26.4785` edge `0.4656` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `6.7941` n `31` status `ready` deltaP `18.7598` edge `0.8877` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.1416` n `31` status `ready` deltaP `41.3194` edge `0.153` maxDD `0.0`
- `news_risk_high->fx_24h` score `4.7714` n `31` status `ready` deltaP `39.8018` edge `0.1451` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.5742` n `31` status `ready` deltaP `20.4365` edge `0.1803` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.2742` n `31` status `ready` deltaP `36.31` edge `0.0568` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7357` n `31` status `ready` deltaP `32.5913` edge `0.0192` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4424` n `31` status `ready` deltaP `9.5615` edge `0.2955` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.1668` n `31` status `ready` deltaP `12.2561` edge `0.2318` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.4301` n `31` status `ready` deltaP `28.3851` edge `0.022` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.8992` n `31` status `ready` deltaP `14.4915` edge `0.0744` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.338` n `31` status `ready` deltaP `11.2657` edge `0.008` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.4095` n `31` status `ready` deltaP `-2.3614` edge `0.0078` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
