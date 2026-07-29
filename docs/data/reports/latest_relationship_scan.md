# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T14:22:33.256162+00:00`
- Price records: `672`
- Market context records: `8310`
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

- `news_risk_high->unknown_24h` score `6250.955` n `52` status `ready` deltaP `35.1896` edge `520.7204` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.631` n `52` status `ready` deltaP `25.1524` edge `0.4446` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.76` n `52` status `ready` deltaP `20.6817` edge `0.123` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.5135` n `52` status `ready` deltaP `21.6463` edge `0.0842` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.0171` n `52` status `ready` deltaP `9.5216` edge `0.2645` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.7886` n `52` status `ready` deltaP `13.6573` edge `0.1014` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.623` n `52` status `ready` deltaP `11.1124` edge `0.1009` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.6054` n `52` status `ready` deltaP `17.9409` edge `0.2254` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `1.2095` n `52` status `ready` deltaP `10.3776` edge `0.0784` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.236` n `52` status `ready` deltaP `4.7444` edge `0.0169` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.1615` n `52` status `ready` deltaP `6.8402` edge `0.0032` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `0.024` n `52` status `ready` deltaP `4.445` edge `0.0127` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4676` n `52` status `ready` deltaP `4.3504` edge `0.0068` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.2711` n `52` status `ready` deltaP `-9.7651` edge `-0.0456` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.0009` n `52` status `ready` deltaP `-20.2591` edge `-0.0495` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-5.6589` n `52` status `ready` deltaP `-21.5144` edge `-0.0511` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-9.1934` n `52` status `ready` deltaP `-33.22` edge `-0.2139` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-11.7244` n `52` status `ready` deltaP `-9.3082` edge `-0.321` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.1852` n `52` status `ready` deltaP `-23.9049` edge `-0.3058` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-33.3078` n `52` status `ready` deltaP `-14.9038` edge `-1.2238` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
