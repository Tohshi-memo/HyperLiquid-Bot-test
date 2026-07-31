# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T00:22:28.988974+00:00`
- Price records: `672`
- Market context records: `8462`
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

- `news_risk_high->unknown_24h` score `6263.6141` n `52` status `ready` deltaP `44.0438` edge `521.7163` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.9826` n `58` status `ready` deltaP `23.3179` edge `0.4028` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.9021` n `61` status `ready` deltaP `20.6121` edge `0.1353` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.1581` n `58` status `ready` deltaP `19.0496` edge `0.0719` maxDD `-0.191`
- `news_risk_high->crypto_alt_1h` score `1.5649` n `61` status `ready` deltaP `12.4521` edge `0.0908` maxDD `-1.1388`
- `news_risk_high->crypto_major_4h` score `1.3032` n `58` status `ready` deltaP `7.3434` edge `0.1875` maxDD `-2.8833`
- `news_risk_high->crypto_major_1h` score `1.2004` n `61` status `ready` deltaP `9.1587` edge `0.0787` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.1514` n `58` status `ready` deltaP `15.9745` edge `0.1803` maxDD `-5.8012`
- `news_risk_high->fx_1h` score `0.5107` n `61` status `ready` deltaP `9.6225` edge `0.0065` maxDD `-0.2475`
- `news_risk_high->index_1h` score `0.4886` n `61` status `ready` deltaP `7.512` edge `0.0195` maxDD `-0.3089`
- `news_risk_high->metal_1h` score `-0.0392` n `61` status `ready` deltaP `4.5254` edge `0.0069` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.0785` n `58` status `ready` deltaP `10.3186` edge `0.0169` maxDD `-0.6604`
- `news_risk_high->metal_4h` score `-0.1348` n `58` status `ready` deltaP `0.8936` edge `0.0296` maxDD `-0.7433`
- `news_risk_high->commodity_1h` score `-1.4983` n `61` status `ready` deltaP `-2.2946` edge `-0.031` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.5861` n `52` status `ready` deltaP `-27.7244` edge `-0.0485` maxDD `-5.2413`
- `news_risk_high->commodity_4h` score `-7.4048` n `58` status `ready` deltaP `-18.0772` edge `-0.1658` maxDD `-13.1269`
- `news_risk_high->metal_24h` score `-9.1964` n `52` status `ready` deltaP `-36.6186` edge `-0.2452` maxDD `-10.8302`
- `news_risk_high->commodity_24h` score `-12.8675` n `52` status `ready` deltaP `-13.1277` edge `-0.3908` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-13.8631` n `52` status `ready` deltaP `-32.7591` edge `-0.3866` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-39.7802` n `52` status `ready` deltaP `-28.0982` edge `-1.6752` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
