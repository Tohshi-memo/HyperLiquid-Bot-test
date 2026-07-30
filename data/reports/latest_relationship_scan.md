# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T22:07:42.318038+00:00`
- Price records: `672`
- Market context records: `8452`
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

- `news_risk_high->unknown_24h` score `6261.0029` n `52` status `ready` deltaP `44.0438` edge `521.4987` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `4.8415` n `52` status `ready` deltaP `22.1037` edge `0.3158` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `3.0045` n `60` status `ready` deltaP `21.1278` edge `0.1404` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.0034` n `52` status `ready` deltaP `17.8354` edge `0.0671` maxDD `-0.191`
- `news_risk_high->crypto_alt_1h` score `1.7417` n `60` status `ready` deltaP `14.0619` edge `0.0948` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.203` n `60` status `ready` deltaP `8.9521` edge `0.0803` maxDD `-1.1783`
- `news_risk_high->crypto_major_4h` score `1.0667` n `52` status `ready` deltaP `3.424` edge `0.1833` maxDD `-2.8833`
- `news_risk_high->crypto_alt_4h` score `0.8652` n `52` status `ready` deltaP `12.3007` edge `0.1681` maxDD `-5.8012`
- `news_risk_high->fx_1h` score `0.6447` n `60` status `ready` deltaP `11.1776` edge `0.0073` maxDD `-0.2475`
- `news_risk_high->index_1h` score `0.4973` n `60` status `ready` deltaP `7.4551` edge `0.0206` maxDD `-0.3089`
- `news_risk_high->metal_1h` score `-0.0591` n `60` status `ready` deltaP `4.2914` edge `0.0068` maxDD `-0.5599`
- `news_risk_high->metal_4h` score `-0.1082` n `52` status `ready` deltaP `0.9264` edge `0.0316` maxDD `-0.7433`
- `news_risk_high->fx_4h` score `-0.3471` n `52` status `ready` deltaP `5.7223` edge `0.0131` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-1.4417` n `60` status `ready` deltaP `-1.5569` edge `-0.0312` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.6245` n `52` status `ready` deltaP `-27.7244` edge `-0.0517` maxDD `-5.2413`
- `news_risk_high->commodity_4h` score `-8.4504` n `52` status `ready` deltaP `-26.5126` edge `-0.1967` maxDD `-13.1269`
- `news_risk_high->metal_24h` score `-9.0473` n `52` status `ready` deltaP `-35.9241` edge `-0.2374` maxDD `-10.8302`
- `news_risk_high->commodity_24h` score `-12.7846` n `52` status `ready` deltaP `-12.7804` edge `-0.3862` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-13.4789` n `52` status `ready` deltaP `-31.1966` edge `-0.365` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-39.1332` n `52` status `ready` deltaP `-26.5357` edge `-1.6317` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
