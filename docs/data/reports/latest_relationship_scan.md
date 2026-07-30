# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T21:22:33.765356+00:00`
- Price records: `672`
- Market context records: `8448`
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

- `news_risk_high->unknown_24h` score `6260.1497` n `52` status `ready` deltaP `44.0438` edge `521.4276` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `4.9801` n `52` status `ready` deltaP `22.561` edge `0.3243` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.8897` n `58` status `ready` deltaP `20.7723` edge `0.1332` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.0568` n `52` status `ready` deltaP `18.2927` edge `0.0685` maxDD `-0.191`
- `news_risk_high->crypto_alt_1h` score `1.8039` n `58` status `ready` deltaP `14.6139` edge `0.0963` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.2618` n `58` status `ready` deltaP `9.5963` edge `0.0809` maxDD `-1.1783`
- `news_risk_high->crypto_major_4h` score `1.0942` n `52` status `ready` deltaP `3.7289` edge `0.1848` maxDD `-2.8833`
- `news_risk_high->crypto_alt_4h` score `0.899` n `52` status `ready` deltaP `12.6056` edge `0.1704` maxDD `-5.8012`
- `news_risk_high->fx_1h` score `0.6713` n `58` status `ready` deltaP `11.465` edge `0.0076` maxDD `-0.2475`
- `news_risk_high->index_1h` score `0.4025` n `58` status `ready` deltaP `6.3752` edge `0.0199` maxDD `-0.3089`
- `news_risk_high->metal_4h` score `-0.0608` n `52` status `ready` deltaP `1.3837` edge `0.0325` maxDD `-0.7433`
- `news_risk_high->metal_1h` score `-0.1537` n `58` status `ready` deltaP `3.1541` edge `0.0065` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.3187` n `52` status `ready` deltaP `6.1797` edge `0.0137` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-1.6054` n `58` status `ready` deltaP `-3.3038` edge `-0.0332` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.6389` n `52` status `ready` deltaP `-27.7244` edge `-0.0529` maxDD `-5.2413`
- `news_risk_high->commodity_4h` score `-8.4335` n `52` status `ready` deltaP `-26.3602` edge `-0.1963` maxDD `-13.1269`
- `news_risk_high->metal_24h` score `-8.96` n `52` status `ready` deltaP `-35.4033` edge `-0.2336` maxDD `-10.8302`
- `news_risk_high->commodity_24h` score `-12.7762` n `52` status `ready` deltaP `-12.7804` edge `-0.3855` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-13.3401` n `52` status `ready` deltaP `-30.6758` edge `-0.3569` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-38.9007` n `52` status `ready` deltaP `-26.0149` edge `-1.6158` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
