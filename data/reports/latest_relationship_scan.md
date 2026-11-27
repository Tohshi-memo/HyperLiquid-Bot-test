# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T19:52:38.688598+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `2886`

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

- `news_risk_high->unknown_1h` score `3285.4693` n `31` status `ready` deltaP `1.6322` edge `273.7958` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3182.8857` n `31` status `ready` deltaP `3.3191` edge `265.224` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `16.5019` n `31` status `ready` deltaP `25.8232` edge `1.203` maxDD `0.0`
- `news_risk_high->equity_24h` score `12.5117` n `31` status `ready` deltaP `23.9168` edge `0.8832` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `12.0715` n `31` status `ready` deltaP `25.8232` edge `0.8338` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.1138` n `31` status `ready` deltaP `20.8916` edge `0.6239` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `5.4041` n `31` status `ready` deltaP `29.6853` edge `0.3005` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `5.0082` n `31` status `ready` deltaP `13.6495` edge `0.6928` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.6574` n `31` status `ready` deltaP `38.6762` edge `0.1431` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.752` n `31` status `ready` deltaP `12.1877` edge `0.2589` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.339` n `31` status `ready` deltaP `28.9243` edge `0.0281` maxDD `-0.4146`
- `news_risk_high->index_24h` score `2.2208` n `31` status `ready` deltaP `24.6101` edge `0.021` maxDD `0.0`
- `news_risk_high->index_1h` score `2.2205` n `31` status `ready` deltaP `27.3518` edge `0.0112` maxDD `-0.0136`
- `news_risk_high->equity_1h` score `2.1339` n `31` status `ready` deltaP `14.7479` edge `0.0982` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `1.8297` n `31` status `ready` deltaP `5.819` edge `0.2419` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.6267` n `31` status `ready` deltaP `8.3639` edge `0.1885` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1333` n `31` status `ready` deltaP `24.6426` edge `0.0089` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.4543` n `31` status `ready` deltaP `10.7281` edge `0.0265` maxDD `-0.5151`
- `news_risk_high->metal_4h` score `0.3734` n `31` status `ready` deltaP `11.6708` edge `0.0258` maxDD `-0.7918`
- `news_risk_high->commodity_1h` score `-0.3052` n `31` status `ready` deltaP `-1.6129` edge `0.0115` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
