# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T22:52:24.179186+00:00`
- Price records: `672`
- Market context records: `8455`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5828`

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

- `news_risk_high->unknown_24h` score `6261.8729` n `52` status `ready` deltaP `44.0438` edge `521.5712` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.6604` n `55` status `ready` deltaP `23.0099` edge `0.378` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.9662` n `60` status `ready` deltaP `20.8284` edge `0.1392` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.1491` n `55` status `ready` deltaP `18.7416` edge `0.0732` maxDD `-0.191`
- `news_risk_high->crypto_alt_1h` score `1.6938` n `60` status `ready` deltaP `13.6128` edge `0.0938` maxDD `-1.1388`
- `news_risk_high->crypto_major_4h` score `1.2083` n `55` status `ready` deltaP `5.4268` edge `0.1881` maxDD `-2.8833`
- `news_risk_high->crypto_major_1h` score `1.1766` n `60` status `ready` deltaP `8.8024` edge `0.0791` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `0.9934` n `55` status `ready` deltaP `13.9413` edge `0.1736` maxDD `-5.8012`
- `news_risk_high->fx_1h` score `0.6435` n `60` status `ready` deltaP `11.1776` edge `0.0072` maxDD `-0.2475`
- `news_risk_high->index_1h` score `0.4685` n `60` status `ready` deltaP `7.1557` edge `0.0202` maxDD `-0.3089`
- `news_risk_high->metal_4h` score `0.0567` n `55` status `ready` deltaP `2.6719` edge `0.0337` maxDD `-0.7433`
- `news_risk_high->metal_1h` score `-0.0842` n `60` status `ready` deltaP `3.992` edge `0.0067` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.1839` n `55` status `ready` deltaP `8.4118` edge `0.0161` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-1.4692` n `60` status `ready` deltaP `-1.8563` edge `-0.0315` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.6101` n `52` status `ready` deltaP `-27.7244` edge `-0.0505` maxDD `-5.2413`
- `news_risk_high->commodity_4h` score `-7.9054` n `55` status `ready` deltaP `-22.0399` edge `-0.1811` maxDD `-13.1269`
- `news_risk_high->metal_24h` score `-9.111` n `52` status `ready` deltaP `-36.2713` edge `-0.2404` maxDD `-10.8302`
- `news_risk_high->commodity_24h` score `-12.8152` n `52` status `ready` deltaP `-12.954` edge `-0.3876` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-13.6082` n `52` status `ready` deltaP `-31.7174` edge `-0.3723` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-39.3597` n `52` status `ready` deltaP `-27.0566` edge `-1.6471` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
