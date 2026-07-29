# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T10:52:27.884899+00:00`
- Price records: `672`
- Market context records: `8295`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5892`

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

- `news_risk_high->unknown_24h` score `5950.4182` n `54` status `ready` deltaP `34.7801` edge `495.6784` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.7843` n `54` status `ready` deltaP `25.1637` edge `0.4573` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.9431` n `54` status `ready` deltaP `21.2298` edge `0.1346` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.5478` n `54` status `ready` deltaP `21.5052` edge `0.088` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `1.9762` n `54` status `ready` deltaP `9.2593` edge `0.261` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.8867` n `54` status `ready` deltaP `14.8536` edge `0.1016` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.5658` n `54` status `ready` deltaP `10.6066` edge `0.0995` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.5499` n `54` status `ready` deltaP `17.3837` edge `0.222` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `1.083` n `54` status `ready` deltaP `9.8916` edge `0.0711` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.386` n `54` status `ready` deltaP `6.1544` edge `0.02` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.1603` n `54` status `ready` deltaP `6.8474` edge `0.003` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.0533` n `54` status `ready` deltaP `3.554` edge `0.0122` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4706` n `54` status `ready` deltaP `4.3078` edge `0.0067` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.1599` n `54` status `ready` deltaP `-8.9599` edge `-0.0417` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.0404` n `54` status `ready` deltaP `-20.544` edge `-0.0487` maxDD `-5.4165`
- `news_risk_high->metal_24h` score `-5.7362` n `54` status `ready` deltaP `-21.2963` edge `-0.059` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-8.787` n `54` status `ready` deltaP `-30.8096` edge `-0.1961` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-10.9094` n `54` status `ready` deltaP `-5.9606` edge `-0.2754` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-11.9421` n `54` status `ready` deltaP `-23.206` edge `-0.2902` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-32.0021` n `54` status `ready` deltaP `-12.0371` edge `-1.1341` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
