# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T12:22:29.902184+00:00`
- Price records: `672`
- Market context records: `8409`
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

- `news_risk_high->unknown_24h` score `6252.7631` n `52` status `ready` deltaP `39.3563` edge `520.8433` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.8072` n `52` status `ready` deltaP `25.0` edge `0.4603` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.6845` n `52` status `ready` deltaP `20.0829` edge `0.1207` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.4377` n `52` status `ready` deltaP `20.5793` edge `0.085` maxDD `-0.191`
- `news_risk_high->crypto_alt_1h` score `1.6447` n `52` status `ready` deltaP `12.6094` edge `0.0964` maxDD `-1.1388`
- `news_risk_high->crypto_major_4h` score `1.6431` n `52` status `ready` deltaP `7.235` edge `0.2318` maxDD `-2.8833`
- `news_risk_high->crypto_major_1h` score `1.5571` n `52` status `ready` deltaP `10.9627` edge `0.0964` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.2807` n `52` status `ready` deltaP `15.8068` edge `0.198` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.4035` n `52` status `ready` deltaP `5.0422` edge `0.0468` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.163` n `52` status `ready` deltaP `3.8462` edge `0.0168` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.1062` n `52` status `ready` deltaP `5.7923` edge `0.0031` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.3235` n `52` status `ready` deltaP `1.3013` edge `0.0047` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4746` n `52` status `ready` deltaP `4.3504` edge `0.0059` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-1.9429` n `52` status `ready` deltaP `-6.4717` edge `-0.0402` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.7637` n `52` status `ready` deltaP `-27.7244` edge `-0.0633` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-8.2084` n `52` status `ready` deltaP `-32.2783` edge `-0.1918` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-8.4638` n `52` status `ready` deltaP `-26.6651` edge `-0.1968` maxDD `-13.1269`
- `news_risk_high->index_24h` score `-12.3467` n `52` status `ready` deltaP `-25.2938` edge `-0.31` maxDD `-28.0214`
- `news_risk_high->commodity_24h` score `-12.4168` n `52` status `ready` deltaP `-11.7388` edge `-0.3625` maxDD `-33.8515`
- `news_risk_high->equity_24h` score `-34.5587` n `52` status `ready` deltaP `-23.2105` edge `-0.9376` maxDD `-127.0042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
