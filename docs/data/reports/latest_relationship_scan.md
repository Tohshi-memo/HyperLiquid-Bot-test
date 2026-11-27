# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T11:52:24.022805+00:00`
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

- `news_risk_high->unknown_1h` score `3250.0189` n `31` status `ready` deltaP `1.4825` edge `270.8426` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3194.935` n `31` status `ready` deltaP `3.7864` edge `266.225` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `17.6957` n `31` status `ready` deltaP `27.9514` edge `1.2883` maxDD `0.0`
- `news_risk_high->equity_24h` score `15.7364` n `31` status `ready` deltaP `27.4306` edge `1.1285` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `13.0543` n `31` status `ready` deltaP `27.0833` edge `0.9073` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.3343` n `31` status `ready` deltaP `20.6628` edge `0.6438` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `6.3345` n `31` status `ready` deltaP `30.3649` edge `0.3735` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `5.2396` n `31` status `ready` deltaP `13.1196` edge `0.726` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `4.6358` n `31` status `ready` deltaP `38.5865` edge `0.1419` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `4.5608` n `31` status `ready` deltaP `15.3674` edge `0.3051` maxDD `-0.1986`
- `news_risk_high->index_24h` score `2.8738` n `31` status `ready` deltaP `28.9931` edge `0.0462` maxDD `0.0`
- `news_risk_high->index_4h` score `2.5702` n `31` status `ready` deltaP `30.06` edge `0.0398` maxDD `-0.4146`
- `news_risk_high->equity_1h` score `2.5177` n `31` status `ready` deltaP `15.7958` edge `0.1232` maxDD `-0.1621`
- `news_risk_high->index_1h` score `2.3571` n `31` status `ready` deltaP `28.5494` edge `0.0146` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `1.9638` n `31` status `ready` deltaP `5.9687` edge `0.2581` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.7935` n `31` status `ready` deltaP `9.4118` edge `0.2029` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1527` n `31` status `ready` deltaP `24.942` edge `0.0094` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.3248` n `31` status `ready` deltaP `11.2903` edge `0.0221` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `0.0412` n `31` status `ready` deltaP `6.9974` edge `-0.0016` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.5701` n `31` status `ready` deltaP `-4.0081` edge `0.0054` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
