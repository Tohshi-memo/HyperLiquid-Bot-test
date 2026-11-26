# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T16:37:35.434400+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3407`

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

- `news_risk_high->unknown_1h` score `3224.1768` n `31` status `ready` deltaP `2.0813` edge `268.6851` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3217.4674` n `31` status `ready` deltaP `3.7864` edge `268.1027` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `32.2261` n `31` status `ready` deltaP `41.1458` edge `2.4112` maxDD `0.0`
- `news_risk_high->equity_24h` score `30.3146` n `31` status `ready` deltaP `40.2778` edge `2.2577` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `26.0673` n `31` status `ready` deltaP `40.4514` edge `1.9026` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `10.3831` n `31` status `ready` deltaP `25.6933` edge `0.781` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `9.6319` n `31` status `ready` deltaP `37.682` edge `0.5995` maxDD `-2.178`
- `news_risk_high->metal_24h` score `7.5031` n `31` status `ready` deltaP `26.8258` edge `0.4739` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `6.7894` n `31` status `ready` deltaP `18.7598` edge `0.8871` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.2209` n `31` status `ready` deltaP `41.6667` edge `0.1573` maxDD `0.0`
- `news_risk_high->fx_24h` score `4.7575` n `31` status `ready` deltaP `39.6282` edge `0.1451` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.5838` n `31` status `ready` deltaP `20.4365` edge `0.1811` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.2778` n `31` status `ready` deltaP `36.31` edge `0.0571` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7225` n `31` status `ready` deltaP `32.4416` edge `0.0191` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4299` n `31` status `ready` deltaP `9.5615` edge `0.2939` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.1661` n `31` status `ready` deltaP `12.2561` edge `0.2317` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.4207` n `31` status `ready` deltaP `28.2354` edge `0.0218` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.9094` n `31` status `ready` deltaP `14.644` edge `0.0747` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.3293` n `31` status `ready` deltaP `11.1133` edge `0.0079` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.4419` n `31` status `ready` deltaP `-2.6608` edge `0.0071` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
