# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-14T07:33:22.289412+00:00`
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

- `market_context_high->unknown_24h` score `449.6069` n `75` status `ready` deltaP `2.1944` edge `37.4667` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `37.3448` n `53` status `ready` deltaP `35.9244` edge `2.9432` maxDD `-3.6503`
- `market_context_high->equity_24h` score `29.1111` n `75` status `ready` deltaP `30.4652` edge `2.377` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `16.6362` n `75` status `ready` deltaP `47.5834` edge `1.3206` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `15.5815` n `53` status `ready` deltaP `42.0434` edge `1.9139` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.3178` n `53` status `ready` deltaP `36.8499` edge `0.8105` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `6.6066` n `53` status `ready` deltaP `44.6181` edge `0.2531` maxDD `0.0`
- `market_context_high->index_24h` score `5.906` n `75` status `ready` deltaP `34.9375` edge `0.2684` maxDD `-0.0653`
- `news_risk_high->index_24h` score `5.225` n `53` status `ready` deltaP `32.95` edge `0.2461` maxDD `-0.4279`
- `news_risk_high->metal_4h` score `5.0391` n `53` status `ready` deltaP `47.7681` edge `0.1391` maxDD `-1.0104`
- `market_context_high->metal_24h` score `4.3259` n `75` status `ready` deltaP `41.3334` edge `0.3682` maxDD `-3.7989`
- `news_risk_high->crypto_major_4h` score `4.231` n `53` status `ready` deltaP `22.1152` edge `0.3539` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.5517` n `53` status `ready` deltaP `18.464` edge `0.2359` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.1213` n `53` status `ready` deltaP `28.3882` edge `0.0962` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.2326` n `53` status `ready` deltaP `26.0394` edge `0.0379` maxDD `-0.3692`
- `news_risk_high->index_4h` score `2.2187` n `53` status `ready` deltaP `22.7278` edge `0.077` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `2.1003` n `53` status `ready` deltaP `26.1936` edge `0.2585` maxDD `-10.1088`
- `news_risk_high->crypto_alt_24h` score `1.6077` n `53` status `ready` deltaP `14.4261` edge `0.5605` maxDD `-29.0448`
- `news_risk_high->index_1h` score `1.2502` n `53` status `ready` deltaP `16.8766` edge `0.0218` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.7655` n `53` status `ready` deltaP `17.8934` edge `0.0768` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
