# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-14T06:07:34.962978+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10428`

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

- `market_context_high->unknown_24h` score `437.4461` n `75` status `ready` deltaP `2.1944` edge `36.4533` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `36.9689` n `53` status `ready` deltaP `35.23` edge `2.9165` maxDD `-3.6503`
- `market_context_high->equity_24h` score `28.7352` n `75` status `ready` deltaP `29.7708` edge `2.3503` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `16.5774` n `75` status `ready` deltaP `47.5834` edge `1.3157` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `15.424` n `53` status `ready` deltaP `42.0434` edge `1.8937` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.3032` n `53` status `ready` deltaP `36.6975` edge `0.8103` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `6.4885` n `53` status `ready` deltaP `43.5764` edge `0.2502` maxDD `0.0`
- `market_context_high->index_24h` score `5.7927` n `75` status `ready` deltaP `33.8959` edge `0.2659` maxDD `-0.0653`
- `news_risk_high->index_24h` score `5.1117` n `53` status `ready` deltaP `31.9084` edge `0.2436` maxDD `-0.4279`
- `news_risk_high->metal_4h` score `5.0769` n `53` status `ready` deltaP `48.2254` edge `0.1392` maxDD `-1.0104`
- `market_context_high->metal_24h` score `4.2963` n `75` status `ready` deltaP `41.3334` edge `0.3644` maxDD `-3.7989`
- `news_risk_high->crypto_major_4h` score `4.2204` n `53` status `ready` deltaP `22.2676` edge `0.352` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.5792` n `53` status `ready` deltaP `18.7634` edge `0.2362` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.0641` n `53` status `ready` deltaP `27.7784` edge `0.0955` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.2937` n `53` status `ready` deltaP `26.7879` edge `0.038` maxDD `-0.3692`
- `news_risk_high->index_4h` score `2.1931` n `53` status `ready` deltaP `22.4229` edge `0.0769` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `2.1144` n `53` status `ready` deltaP `26.346` edge `0.2593` maxDD `-10.1088`
- `news_risk_high->crypto_alt_24h` score `1.5695` n `53` status `ready` deltaP `14.4261` edge `0.5556` maxDD `-29.0448`
- `news_risk_high->index_1h` score `1.225` n `53` status `ready` deltaP `16.5772` edge `0.0217` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.7286` n `53` status `ready` deltaP `17.8934` edge `0.0793` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
