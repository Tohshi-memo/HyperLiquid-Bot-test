# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-14T09:07:30.898866+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10224`

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

- `market_context_high->unknown_24h` score `462.1037` n `75` status `ready` deltaP `2.1944` edge `38.5081` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `37.7299` n `53` status `ready` deltaP `36.7925` edge `2.9695` maxDD `-3.6503`
- `market_context_high->equity_24h` score `29.4962` n `75` status `ready` deltaP `31.3333` edge `2.4033` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `16.761` n `75` status `ready` deltaP `47.5834` edge `1.331` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `15.7578` n `53` status `ready` deltaP `42.0434` edge `1.9365` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.2838` n `53` status `ready` deltaP `36.5451` edge `0.8097` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `6.7248` n `53` status `ready` deltaP `45.6597` edge `0.256` maxDD `0.0`
- `market_context_high->index_24h` score `6.0193` n `75` status `ready` deltaP `35.9792` edge `0.2709` maxDD `-0.0653`
- `news_risk_high->index_24h` score `5.3384` n `53` status `ready` deltaP `33.9917` edge `0.2486` maxDD `-0.4279`
- `news_risk_high->metal_4h` score `4.9855` n `53` status `ready` deltaP `47.1584` edge `0.1387` maxDD `-1.0104`
- `market_context_high->metal_24h` score `4.3509` n `75` status `ready` deltaP `41.3334` edge `0.3714` maxDD `-3.7989`
- `news_risk_high->crypto_major_4h` score `4.1498` n `53` status `ready` deltaP `21.5054` edge `0.3512` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.5888` n `53` status `ready` deltaP `18.7634` edge `0.237` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.1249` n `53` status `ready` deltaP `28.3882` edge `0.0965` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.2206` n `53` status `ready` deltaP `25.8897` edge `0.0379` maxDD `-0.3692`
- `news_risk_high->index_4h` score `2.1687` n `53` status `ready` deltaP `22.118` edge `0.0769` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `2.0956` n `53` status `ready` deltaP `26.1936` edge `0.2579` maxDD `-10.1088`
- `news_risk_high->crypto_alt_24h` score `1.6888` n `53` status `ready` deltaP `14.4261` edge `0.5709` maxDD `-29.0448`
- `news_risk_high->index_1h` score `1.2634` n `53` status `ready` deltaP `17.0263` edge `0.0219` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.7793` n `53` status `ready` deltaP `18.4922` edge `0.0818` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
