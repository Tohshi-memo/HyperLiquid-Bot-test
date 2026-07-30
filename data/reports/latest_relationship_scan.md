# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T16:22:30.425152+00:00`
- Price records: `672`
- Market context records: `8427`
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

- `news_risk_high->unknown_24h` score `6254.2003` n `52` status `ready` deltaP `41.9605` edge `520.9457` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.532` n `52` status `ready` deltaP `23.4756` edge `0.3642` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.3103` n `52` status `ready` deltaP `19.1847` edge `0.0955` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.1304` n `52` status `ready` deltaP `18.5976` edge `0.0726` maxDD `-0.191`
- `news_risk_high->crypto_alt_1h` score `1.5907` n `52` status `ready` deltaP `12.6094` edge `0.0919` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.3053` n `52` status `ready` deltaP `9.4657` edge `0.0854` maxDD `-1.1783`
- `news_risk_high->crypto_major_4h` score `1.2817` n `52` status `ready` deltaP `4.9484` edge `0.2007` maxDD `-2.8833`
- `news_risk_high->crypto_alt_4h` score `1.0327` n `52` status `ready` deltaP `13.9775` edge `0.1784` maxDD `-5.8012`
- `news_risk_high->fx_1h` score `0.1491` n `52` status `ready` deltaP `6.3911` edge `0.0046` maxDD `-0.2475`
- `news_risk_high->metal_4h` score `0.1404` n `52` status `ready` deltaP `2.9081` edge `0.0391` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.0371` n `52` status `ready` deltaP `2.7983` edge `0.0133` maxDD `-0.3089`
- `news_risk_high->fx_4h` score `-0.3834` n `52` status `ready` deltaP `5.265` edge `0.0115` maxDD `-0.6604`
- `news_risk_high->metal_1h` score `-0.423` n `52` status `ready` deltaP `0.5528` edge `0.0014` maxDD `-0.5599`
- `news_risk_high->commodity_1h` score `-1.9465` n `52` status `ready` deltaP `-6.4717` edge `-0.0405` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.7277` n `52` status `ready` deltaP `-27.7244` edge `-0.0603` maxDD `-5.2413`
- `news_risk_high->commodity_4h` score `-8.3815` n `52` status `ready` deltaP `-26.0553` edge `-0.194` maxDD `-13.1269`
- `news_risk_high->metal_24h` score `-8.6752` n `52` status `ready` deltaP `-34.7088` edge `-0.2145` maxDD `-10.8302`
- `news_risk_high->commodity_24h` score `-12.5516` n `52` status `ready` deltaP `-12.4332` edge `-0.3691` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.6843` n `52` status `ready` deltaP `-27.2035` edge `-0.3254` maxDD `-28.0214`
- `news_risk_high->equity_24h` score `-36.2253` n `52` status `ready` deltaP `-25.2938` edge `-1.0626` maxDD `-127.0042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
