# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T06:07:26.986947+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `9714`

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

- `market_context_high->unknown_24h` score `547.6689` n `66` status `ready` deltaP `2.4263` edge `45.6229` maxDD `0.0`
- `news_risk_high->equity_24h` score `42.5426` n `52` status `ready` deltaP `47.1971` edge `3.3012` maxDD `-3.6503`
- `market_context_high->equity_24h` score `38.0509` n `66` status `ready` deltaP `42.4768` edge `3.0419` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `30.112` n `66` status `ready` deltaP `57.8121` edge `2.2316` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `22.0785` n `52` status `ready` deltaP `44.1574` edge `2.6947` maxDD `-10.014`
- `news_risk_high->equity_4h` score `11.8513` n `52` status `ready` deltaP `38.6898` edge `0.8427` maxDD `-7.0416`
- `market_context_high->index_24h` score `7.4955` n `66` status `ready` deltaP `44.5906` edge `0.3365` maxDD `-0.0653`
- `news_risk_high->commodity_24h` score `7.2768` n `52` status `ready` deltaP `49.74` edge `0.2748` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `7.0258` n `52` status `ready` deltaP `15.2713` edge `1.2495` maxDD `-29.0448`
- `news_risk_high->index_24h` score `6.186` n `52` status `ready` deltaP `40.6279` edge `0.275` maxDD `-0.4279`
- `market_context_high->metal_24h` score `5.8999` n `66` status `ready` deltaP `55.7324` edge `0.474` maxDD `-3.7989`
- `news_risk_high->crypto_major_4h` score `5.1007` n `52` status `ready` deltaP `21.107` edge `0.4331` maxDD `-9.2335`
- `news_risk_high->metal_4h` score `5.0118` n `52` status `ready` deltaP `45.747` edge `0.1503` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `3.7749` n `52` status `ready` deltaP `19.9793` edge `0.2444` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.3319` n `52` status `ready` deltaP `30.5409` edge `0.0994` maxDD `-0.3611`
- `news_risk_high->crypto_alt_4h` score `2.9044` n `52` status `ready` deltaP `27.1806` edge `0.3503` maxDD `-10.0648`
- `market_context_high->crypto_major_24h` score `2.7305` n `66` status `ready` deltaP `12.6306` edge `1.1759` maxDD `-76.2717`
- `news_risk_high->index_4h` score `2.4071` n `52` status `ready` deltaP `24.4673` edge `0.0811` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `2.2131` n `52` status `ready` deltaP `25.3454` edge `0.0409` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3422` n `52` status `ready` deltaP `17.9065` edge `0.0226` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
