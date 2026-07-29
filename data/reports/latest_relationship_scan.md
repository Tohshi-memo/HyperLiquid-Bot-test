# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T21:22:26.097605+00:00`
- Price records: `672`
- Market context records: `8341`
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

- `news_risk_high->unknown_24h` score `6250.9891` n `52` status `ready` deltaP `35.016` edge `520.7244` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `7.1728` n `52` status `ready` deltaP `25.6098` edge `0.4867` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `3.006` n `52` status `ready` deltaP `21.1308` edge `0.1405` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.6001` n `52` status `ready` deltaP `21.7988` edge `0.0904` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.1449` n `52` status `ready` deltaP `10.2838` edge `0.2758` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.942` n `52` status `ready` deltaP `14.4058` edge `0.1092` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.7645` n `52` status `ready` deltaP `11.8609` edge `0.1077` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.6553` n `52` status `ready` deltaP `17.9409` edge `0.2318` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.7854` n `52` status `ready` deltaP `7.1764` edge `0.0644` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.3115` n `52` status `ready` deltaP `5.1935` edge `0.0202` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.1039` n `52` status `ready` deltaP `5.7923` edge `0.0028` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1497` n `52` status `ready` deltaP `2.7983` edge `0.0092` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4659` n `52` status `ready` deltaP `4.5028` edge `0.006` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.3047` n `52` status `ready` deltaP `-10.0645` edge `-0.0464` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.1083` n `52` status `ready` deltaP `-21.3008` edge `-0.0515` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-6.3796` n `52` status `ready` deltaP `-24.1186` edge `-0.0938` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-9.1783` n `52` status `ready` deltaP `-32.6102` edge `-0.2167` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-11.914` n `52` status `ready` deltaP `-9.3082` edge `-0.3368` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.1355` n `52` status `ready` deltaP `-24.0785` edge `-0.3005` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-34.3671` n `52` status `ready` deltaP `-16.6399` edge `-1.3005` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
