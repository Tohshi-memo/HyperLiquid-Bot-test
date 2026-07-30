# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T19:22:26.187025+00:00`
- Price records: `672`
- Market context records: `8439`
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

- `news_risk_high->unknown_24h` score `6257.8457` n `52` status `ready` deltaP `44.0438` edge `521.2356` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.1727` n `52` status `ready` deltaP `23.0183` edge `0.3373` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.3246` n `53` status `ready` deltaP `18.9442` edge `0.0983` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.1149` n `52` status `ready` deltaP `18.75` edge `0.0703` maxDD `-0.191`
- `news_risk_high->crypto_alt_1h` score `1.4048` n `53` status `ready` deltaP `11.0355` edge `0.0869` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.2488` n `53` status `ready` deltaP `9.3295` edge `0.0816` maxDD `-1.1783`
- `news_risk_high->crypto_major_4h` score `1.1374` n `52` status `ready` deltaP `4.0338` edge `0.1883` maxDD `-2.8833`
- `news_risk_high->crypto_alt_4h` score `0.9902` n `52` status `ready` deltaP `13.5202` edge `0.176` maxDD `-5.8012`
- `news_risk_high->fx_1h` score `0.2286` n `53` status `ready` deltaP `7.8607` edge `0.005` maxDD `-0.2475`
- `news_risk_high->index_1h` score `0.0266` n `53` status `ready` deltaP `2.6212` edge `0.0136` maxDD `-0.3089`
- `news_risk_high->metal_4h` score `-0.0038` n `52` status `ready` deltaP `1.841` edge `0.0342` maxDD `-0.7433`
- `news_risk_high->fx_4h` score `-0.3195` n `52` status `ready` deltaP `6.1797` edge `0.0136` maxDD `-0.6604`
- `news_risk_high->metal_1h` score `-0.4156` n `53` status `ready` deltaP `0.5254` edge `0.0022` maxDD `-0.5599`
- `news_risk_high->commodity_1h` score `-1.9536` n `53` status `ready` deltaP `-6.4852` edge `-0.041` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.6761` n `52` status `ready` deltaP `-27.7244` edge `-0.056` maxDD `-5.2413`
- `news_risk_high->commodity_4h` score `-8.5234` n `52` status `ready` deltaP `-27.2748` edge `-0.1977` maxDD `-13.1269`
- `news_risk_high->metal_24h` score `-8.7904` n `52` status `ready` deltaP `-34.7088` edge `-0.2241` maxDD `-10.8302`
- `news_risk_high->commodity_24h` score `-12.7306` n `52` status `ready` deltaP `-12.7804` edge `-0.3817` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-13.0046` n `52` status `ready` deltaP `-29.2869` edge `-0.3382` maxDD `-28.0214`
- `news_risk_high->equity_24h` score `-38.0` n `52` status `ready` deltaP `-27.3771` edge `-1.1966` maxDD `-127.0042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
