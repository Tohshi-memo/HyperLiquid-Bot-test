# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T14:52:25.903843+00:00`
- Price records: `672`
- Market context records: `8420`
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

- `news_risk_high->unknown_24h` score `6252.9704` n `52` status `ready` deltaP `41.0924` edge `520.849` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.0224` n `52` status `ready` deltaP `24.0854` edge `0.401` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.3415` n `52` status `ready` deltaP `19.3344` edge `0.0971` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.2247` n `52` status `ready` deltaP `19.2073` edge `0.0764` maxDD `-0.191`
- `news_risk_high->crypto_alt_1h` score `1.5716` n `52` status `ready` deltaP `12.31` edge `0.0923` maxDD `-1.1388`
- `news_risk_high->crypto_major_4h` score `1.4181` n `52` status `ready` deltaP `5.863` edge `0.2121` maxDD `-2.8833`
- `news_risk_high->crypto_major_1h` score `1.4132` n `52` status `ready` deltaP `10.2142` edge `0.0894` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.1435` n `52` status `ready` deltaP `14.8922` edge `0.1865` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.2361` n `52` status `ready` deltaP `3.6703` edge `0.042` maxDD `-0.7433`
- `news_risk_high->fx_1h` score `0.1421` n `52` status `ready` deltaP `6.2414` edge `0.0047` maxDD `-0.2475`
- `news_risk_high->index_1h` score `0.0527` n `52` status `ready` deltaP `2.948` edge `0.0136` maxDD `-0.3089`
- `news_risk_high->metal_1h` score `-0.3822` n `52` status `ready` deltaP `0.8522` edge `0.0028` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4433` n `52` status `ready` deltaP `4.5028` edge `0.0089` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-1.9309` n `52` status `ready` deltaP `-6.322` edge `-0.0402` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.7493` n `52` status `ready` deltaP `-27.7244` edge `-0.0621` maxDD `-5.2413`
- `news_risk_high->commodity_4h` score `-8.3039` n `52` status `ready` deltaP `-25.4456` edge `-0.1916` maxDD `-13.1269`
- `news_risk_high->metal_24h` score `-8.5153` n `52` status `ready` deltaP `-34.0144` edge `-0.2058` maxDD `-10.8302`
- `news_risk_high->commodity_24h` score `-12.4607` n `52` status `ready` deltaP `-11.9124` edge `-0.365` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.505` n `52` status `ready` deltaP `-26.1619` edge `-0.3174` maxDD `-28.0214`
- `news_risk_high->equity_24h` score `-35.2444` n `52` status `ready` deltaP `-24.2521` edge `-0.9878` maxDD `-127.0042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
