# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T09:56:02.798918+00:00`
- Price records: `672`
- Market context records: `8398`
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

- `news_risk_high->unknown_24h` score `6252.5618` n `52` status `ready` deltaP `37.6202` edge `520.8381` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `7.4211` n `52` status `ready` deltaP `26.5244` edge `0.5013` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.9339` n `52` status `ready` deltaP `21.2805` edge `0.1335` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.6592` n `52` status `ready` deltaP `22.1037` edge `0.0933` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `1.9268` n `52` status `ready` deltaP `8.7594` edge `0.258` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.6927` n `52` status `ready` deltaP `13.0585` edge `0.0974` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.6182` n `52` status `ready` deltaP `11.4118` edge `0.0985` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.4307` n `52` status `ready` deltaP `17.0263` edge `0.2091` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.6622` n `52` status `ready` deltaP `6.5666` edge `0.0582` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.2732` n `52` status `ready` deltaP `4.8941` edge `0.019` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.0953` n `52` status `ready` deltaP `5.6426` edge `0.0027` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.2216` n `52` status `ready` deltaP `2.3492` edge `0.0062` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4762` n `52` status `ready` deltaP `4.3504` edge `0.0057` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.0627` n `52` status `ready` deltaP `-7.6693` edge `-0.0422` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.7319` n `52` status `ready` deltaP `-27.5508` edge `-0.0618` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-7.9063` n `52` status `ready` deltaP `-30.5422` edge `-0.1782` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-8.6878` n `52` status `ready` deltaP `-28.1895` edge `-0.2053` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-12.1766` n `52` status `ready` deltaP `-10.1763` edge `-0.3529` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.3239` n `52` status `ready` deltaP `-25.2938` edge `-0.3081` maxDD `-28.0214`
- `news_risk_high->equity_24h` score `-34.6571` n `52` status `ready` deltaP `-23.2105` edge `-0.9458` maxDD `-127.0042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
