# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T20:39:48.169724+00:00`
- Price records: `672`
- Market context records: `8338`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5886`

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

- `news_risk_high->unknown_24h` score `6250.9615` n `52` status `ready` deltaP `35.016` edge `520.7221` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `7.0042` n `52` status `ready` deltaP `25.1524` edge `0.4757` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.9076` n `52` status `ready` deltaP `20.6817` edge `0.1353` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.5383` n `52` status `ready` deltaP `21.3415` edge `0.0883` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.0782` n `52` status `ready` deltaP `9.8264` edge `0.2703` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.8689` n `52` status `ready` deltaP `13.9567` edge `0.1061` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.725` n `52` status `ready` deltaP `11.5615` edge `0.1064` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.5902` n `52` status `ready` deltaP `17.4836` edge `0.2265` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.8328` n `52` status `ready` deltaP `7.6337` edge `0.0653` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.296` n `52` status `ready` deltaP `5.0438` edge `0.0199` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.1203` n `52` status `ready` deltaP `6.0917` edge `0.0029` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1353` n `52` status `ready` deltaP `2.948` edge `0.0094` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.447` n `52` status `ready` deltaP `4.8077` edge `0.0064` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.3191` n `52` status `ready` deltaP `-10.2142` edge `-0.0466` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.0606` n `52` status `ready` deltaP `-20.7799` edge `-0.051` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-6.2779` n `52` status `ready` deltaP `-23.5977` edge `-0.0888` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-9.1903` n `52` status `ready` deltaP `-32.6102` edge `-0.2177` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-11.8852` n `52` status `ready` deltaP `-9.3082` edge `-0.3344` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.1679` n `52` status `ready` deltaP `-24.0785` edge `-0.3032` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-34.3359` n `52` status `ready` deltaP `-16.6399` edge `-1.2979` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
