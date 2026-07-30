# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T21:52:27.811429+00:00`
- Price records: `672`
- Market context records: `8450`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5785`

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

- `news_risk_high->unknown_24h` score `6260.7161` n `52` status `ready` deltaP `44.0438` edge `521.4748` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `4.8873` n `52` status `ready` deltaP `22.2561` edge `0.3186` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.9345` n `59` status `ready` deltaP `20.882` edge `0.1362` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.0204` n `52` status `ready` deltaP `17.9878` edge `0.0675` maxDD `-0.191`
- `news_risk_high->crypto_alt_1h` score `1.6789` n `59` status `ready` deltaP `13.5618` edge `0.0929` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.1416` n `59` status `ready` deltaP `8.4238` edge `0.0787` maxDD `-1.1783`
- `news_risk_high->crypto_major_4h` score `1.0777` n `52` status `ready` deltaP `3.5764` edge `0.1837` maxDD `-2.8833`
- `news_risk_high->crypto_alt_4h` score `0.877` n `52` status `ready` deltaP `12.4531` edge `0.1686` maxDD `-5.8012`
- `news_risk_high->fx_1h` score `0.599` n `59` status `ready` deltaP `10.6211` edge `0.0072` maxDD `-0.2475`
- `news_risk_high->index_1h` score `0.449` n `59` status `ready` deltaP `6.9268` edge `0.0201` maxDD `-0.3089`
- `news_risk_high->metal_4h` score `-0.0912` n `52` status `ready` deltaP `1.0788` edge `0.032` maxDD `-0.7433`
- `news_risk_high->metal_1h` score `-0.1024` n `59` status `ready` deltaP `3.7349` edge `0.0069` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.3377` n `52` status `ready` deltaP `5.8748` edge `0.0133` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-1.5151` n `59` status `ready` deltaP `-2.3394` edge `-0.0321` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.6293` n `52` status `ready` deltaP `-27.7244` edge `-0.0521` maxDD `-5.2413`
- `news_risk_high->commodity_4h` score `-8.448` n `52` status `ready` deltaP `-26.5126` edge `-0.1965` maxDD `-13.1269`
- `news_risk_high->metal_24h` score `-9.019` n `52` status `ready` deltaP `-35.7505` edge `-0.2362` maxDD `-10.8302`
- `news_risk_high->commodity_24h` score `-12.7798` n `52` status `ready` deltaP `-12.7804` edge `-0.3858` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-13.435` n `52` status `ready` deltaP `-31.023` edge `-0.3625` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-39.0581` n `52` status `ready` deltaP `-26.3621` edge `-1.6266` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
