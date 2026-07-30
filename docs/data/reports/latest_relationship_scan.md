# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T14:07:33.311438+00:00`
- Price records: `672`
- Market context records: `8416`
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

- `news_risk_high->unknown_24h` score `6252.9155` n `52` status `ready` deltaP `40.5716` edge `520.8479` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.353` n `52` status `ready` deltaP `24.5427` edge `0.4255` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.4974` n `52` status `ready` deltaP `19.6338` edge `0.1081` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.2985` n `52` status `ready` deltaP `19.6646` edge `0.0795` maxDD `-0.191`
- `news_risk_high->crypto_alt_1h` score `1.5884` n `52` status `ready` deltaP `12.31` edge `0.0937` maxDD `-1.1388`
- `news_risk_high->crypto_major_4h` score `1.4864` n `52` status `ready` deltaP `6.3203` edge `0.2178` maxDD `-2.8833`
- `news_risk_high->crypto_major_1h` score `1.4635` n `52` status `ready` deltaP `10.5136` edge `0.0916` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.2047` n `52` status `ready` deltaP `15.3495` edge `0.1913` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.2871` n `52` status `ready` deltaP `4.1276` edge `0.0432` maxDD `-0.7433`
- `news_risk_high->fx_1h` score `0.139` n `52` status `ready` deltaP `6.2414` edge `0.0043` maxDD `-0.2475`
- `news_risk_high->index_1h` score `0.1054` n `52` status `ready` deltaP `3.3971` edge `0.015` maxDD `-0.3089`
- `news_risk_high->metal_1h` score `-0.3678` n `52` status `ready` deltaP `1.0019` edge `0.003` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4614` n `52` status `ready` deltaP `4.3504` edge `0.0076` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-1.9237` n `52` status `ready` deltaP `-6.322` edge `-0.0396` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.7625` n `52` status `ready` deltaP `-27.7244` edge `-0.0632` maxDD `-5.2413`
- `news_risk_high->commodity_4h` score `-8.3281` n `52` status `ready` deltaP `-25.598` edge `-0.1926` maxDD `-13.1269`
- `news_risk_high->metal_24h` score `-8.4184` n `52` status `ready` deltaP `-33.4936` edge `-0.2012` maxDD `-10.8302`
- `news_risk_high->index_24h` score `-12.4105` n `52` status `ready` deltaP `-25.641` edge `-0.313` maxDD `-28.0214`
- `news_risk_high->commodity_24h` score `-12.4499` n `52` status `ready` deltaP `-11.9124` edge `-0.3641` maxDD `-33.8515`
- `news_risk_high->equity_24h` score `-34.7743` n `52` status `ready` deltaP `-23.7313` edge `-0.9521` maxDD `-127.0042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
