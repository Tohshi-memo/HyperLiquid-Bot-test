# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T12:25:29.749142+00:00`
- Price records: `672`
- Market context records: `8302`
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

- `news_risk_high->unknown_24h` score `5951.8826` n `54` status `ready` deltaP `35.4745` edge `495.7958` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.8371` n `54` status `ready` deltaP `25.1637` edge `0.4617` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.8963` n `54` status `ready` deltaP `20.9304` edge `0.1327` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.5672` n `54` status `ready` deltaP `21.6576` edge `0.0886` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.0328` n `54` status `ready` deltaP `9.8691` edge `0.2642` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.8927` n `54` status `ready` deltaP `14.8536` edge `0.1021` maxDD `-1.1388`
- `news_risk_high->crypto_alt_4h` score `1.62` n `54` status `ready` deltaP `18.1459` edge `0.2259` maxDD `-5.8012`
- `news_risk_high->crypto_major_1h` score `1.5634` n `54` status `ready` deltaP `10.6066` edge `0.0993` maxDD `-1.1783`
- `news_risk_high->metal_4h` score `1.1946` n `54` status `ready` deltaP `10.8062` edge `0.0743` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.3441` n `54` status `ready` deltaP `5.7053` edge `0.0195` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.1596` n `54` status `ready` deltaP `6.8474` edge `0.0029` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.0353` n `54` status `ready` deltaP `3.7037` edge `0.0127` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.5134` n `54` status `ready` deltaP `3.5456` edge `0.0063` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.1444` n `54` status `ready` deltaP `-8.8102` edge `-0.0414` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.044` n `54` status `ready` deltaP `-20.544` edge `-0.049` maxDD `-5.4165`
- `news_risk_high->metal_24h` score `-5.8561` n `54` status `ready` deltaP `-22.1644` edge `-0.0632` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-8.8196` n `54` status `ready` deltaP `-30.9621` edge `-0.1978` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-10.8314` n `54` status `ready` deltaP `-5.9606` edge `-0.2689` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-11.8939` n `54` status `ready` deltaP `-22.8588` edge `-0.2885` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-32.2522` n `54` status `ready` deltaP `-13.0787` edge `-1.148` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
