# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-14T07:22:27.878863+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10464`

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

- `market_context_high->unknown_24h` score `447.6329` n `75` status `ready` deltaP `2.1944` edge `37.3022` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `37.2733` n `53` status `ready` deltaP `35.7508` edge `2.9384` maxDD `-3.6503`
- `market_context_high->equity_24h` score `29.0397` n `75` status `ready` deltaP `30.2916` edge `2.3722` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `16.6122` n `75` status `ready` deltaP `47.5834` edge `1.3186` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `15.5511` n `53` status `ready` deltaP `42.0434` edge `1.91` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.3178` n `53` status `ready` deltaP `36.8499` edge `0.8105` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `6.588` n `53` status `ready` deltaP `44.4444` edge `0.2527` maxDD `0.0`
- `market_context_high->index_24h` score `5.8861` n `75` status `ready` deltaP `34.7639` edge `0.2679` maxDD `-0.0653`
- `news_risk_high->index_24h` score `5.2051` n `53` status `ready` deltaP `32.7764` edge `0.2456` maxDD `-0.4279`
- `news_risk_high->metal_4h` score `5.0513` n `53` status `ready` deltaP `47.9205` edge `0.1391` maxDD `-1.0104`
- `market_context_high->metal_24h` score `4.3212` n `75` status `ready` deltaP `41.3334` edge `0.3676` maxDD `-3.7989`
- `news_risk_high->crypto_major_4h` score `4.2528` n `53` status `ready` deltaP `22.2676` edge `0.3547` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.5373` n `53` status `ready` deltaP `18.3143` edge `0.2357` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.1201` n `53` status `ready` deltaP `28.3882` edge `0.0961` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.2445` n `53` status `ready` deltaP `26.1891` edge `0.0379` maxDD `-0.3692`
- `news_risk_high->index_4h` score `2.2187` n `53` status `ready` deltaP `22.7278` edge `0.077` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `2.1018` n `53` status `ready` deltaP `26.1936` edge `0.2587` maxDD `-10.1088`
- `news_risk_high->crypto_alt_24h` score `1.5921` n `53` status `ready` deltaP `14.4261` edge `0.5585` maxDD `-29.0448`
- `news_risk_high->index_1h` score `1.2382` n `53` status `ready` deltaP `16.7269` edge `0.0218` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.7492` n `53` status `ready` deltaP `17.7437` edge `0.0757` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
