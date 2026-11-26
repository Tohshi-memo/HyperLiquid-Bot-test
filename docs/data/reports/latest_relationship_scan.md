# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T15:07:29.278699+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3491`

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

- `news_risk_high->unknown_1h` score `3223.0632` n `31` status `ready` deltaP `1.7819` edge `268.5943` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3219.6055` n `31` status `ready` deltaP `3.4815` edge `268.2829` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `33.5106` n `31` status `ready` deltaP `42.1875` edge `2.5113` maxDD `0.0`
- `news_risk_high->equity_24h` score `32.2508` n `31` status `ready` deltaP `41.3194` edge `2.4121` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `27.4802` n `31` status `ready` deltaP `41.4931` edge `2.0134` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `10.3723` n `31` status `ready` deltaP `25.6933` edge `0.7801` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `9.8827` n `31` status `ready` deltaP `37.682` edge `0.6204` maxDD `-2.178`
- `news_risk_high->metal_24h` score `7.9068` n `31` status `ready` deltaP `27.8674` edge `0.5006` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `6.7925` n `31` status `ready` deltaP `18.7598` edge `0.8875` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.4711` n `31` status `ready` deltaP `42.7083` edge `0.1712` maxDD `0.0`
- `news_risk_high->fx_24h` score `4.8366` n `31` status `ready` deltaP `40.4962` edge `0.1459` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.675` n `31` status `ready` deltaP `20.5862` edge `0.1877` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.3018` n `31` status `ready` deltaP `36.31` edge `0.0591` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.756` n `31` status `ready` deltaP `32.741` edge `0.0199` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4462` n `31` status `ready` deltaP `9.7112` edge `0.295` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.2097` n `31` status `ready` deltaP `12.5555` edge `0.2353` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.4145` n `31` status `ready` deltaP `28.0857` edge `0.022` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.9418` n `31` status `ready` deltaP `15.1013` edge `0.0758` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.3932` n `31` status `ready` deltaP `12.0279` edge `0.01` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.4383` n `31` status `ready` deltaP `-2.6608` edge `0.0074` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
