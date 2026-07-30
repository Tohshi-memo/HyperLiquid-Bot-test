# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T13:52:27.596135+00:00`
- Price records: `672`
- Market context records: `8415`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5742`

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

- `news_risk_high->unknown_24h` score `6252.8933` n `52` status `ready` deltaP `40.398` edge `520.8472` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.425` n `52` status `ready` deltaP `24.5427` edge `0.4315` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.5154` n `52` status `ready` deltaP `19.6338` edge `0.1096` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.3069` n `52` status `ready` deltaP `19.6646` edge `0.0802` maxDD `-0.191`
- `news_risk_high->crypto_alt_1h` score `1.5896` n `52` status `ready` deltaP `12.31` edge `0.0938` maxDD `-1.1388`
- `news_risk_high->crypto_major_4h` score `1.5037` n `52` status `ready` deltaP `6.4728` edge `0.219` maxDD `-2.8833`
- `news_risk_high->crypto_major_1h` score `1.4779` n `52` status `ready` deltaP `10.6633` edge `0.0918` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.2189` n `52` status `ready` deltaP `15.5019` edge `0.1921` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.3029` n `52` status `ready` deltaP `4.28` edge `0.0435` maxDD `-0.7433`
- `news_risk_high->fx_1h` score `0.1358` n `52` status `ready` deltaP `6.2414` edge `0.0039` maxDD `-0.2475`
- `news_risk_high->index_1h` score `0.1066` n `52` status `ready` deltaP `3.3971` edge `0.0151` maxDD `-0.3089`
- `news_risk_high->metal_1h` score `-0.3654` n `52` status `ready` deltaP `1.0019` edge `0.0032` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4653` n `52` status `ready` deltaP `4.3504` edge `0.0071` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-1.9237` n `52` status `ready` deltaP `-6.322` edge `-0.0396` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.7661` n `52` status `ready` deltaP `-27.7244` edge `-0.0635` maxDD `-5.2413`
- `news_risk_high->commodity_4h` score `-8.3475` n `52` status `ready` deltaP `-25.7505` edge `-0.1932` maxDD `-13.1269`
- `news_risk_high->metal_24h` score `-8.3853` n `52` status `ready` deltaP `-33.32` edge `-0.1996` maxDD `-10.8302`
- `news_risk_high->index_24h` score `-12.3894` n `52` status `ready` deltaP `-25.4674` edge `-0.3124` maxDD `-28.0214`
- `news_risk_high->commodity_24h` score `-12.4499` n `52` status `ready` deltaP `-11.9124` edge `-0.3641` maxDD `-33.8515`
- `news_risk_high->equity_24h` score `-34.7004` n `52` status `ready` deltaP `-23.5577` edge `-0.9471` maxDD `-127.0042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
