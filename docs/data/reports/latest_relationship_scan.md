# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T13:07:25.031221+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11734`

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

- `market_context_high->unknown_24h` score `275.8455` n `86` status `ready` deltaP `6.4979` edge `22.9579` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `103.9857` n `86` status `ready` deltaP `7.3136` edge `8.6615` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `27.3671` n `53` status `ready` deltaP `21.0486` edge `2.2109` maxDD `-3.6503`
- `market_context_high->equity_24h` score `16.5204` n `86` status `ready` deltaP `16.8142` edge `1.4058` maxDD `-7.6288`
- `news_risk_high->crypto_major_24h` score `11.1729` n `53` status `ready` deltaP `36.8969` edge `1.383` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `10.6864` n `53` status `ready` deltaP `33.9536` edge `0.7772` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `7.3174` n `53` status `ready` deltaP `42.3875` edge `0.3272` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `6.0149` n `86` status `ready` deltaP `36.5494` edge `0.961` maxDD `-27.3483`
- `market_context_high->metal_24h` score `5.5226` n `86` status `ready` deltaP `36.8834` edge `0.2602` maxDD `-0.6695`
- `news_risk_high->metal_4h` score `4.5962` n `53` status `ready` deltaP `43.9571` edge `0.1276` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `3.6712` n `53` status `ready` deltaP `21.6579` edge `0.3103` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.619` n `53` status `ready` deltaP `18.0149` edge `0.2445` maxDD `-3.7082`
- `news_risk_high->index_24h` score `3.5145` n `53` status `ready` deltaP `19.129` edge `0.1957` maxDD `-0.4279`
- `market_context_high->index_24h` score `3.3467` n `86` status `ready` deltaP `18.8219` edge `0.176` maxDD `-1.1406`
- `news_risk_high->commodity_4h` score `3.0447` n `53` status `ready` deltaP `26.7114` edge `0.101` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.1894` n `53` status `ready` deltaP `25.8897` edge `0.0353` maxDD `-0.3692`
- `news_risk_high->index_4h` score `2.0592` n `53` status `ready` deltaP `19.9839` edge `0.082` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.9553` n `53` status `ready` deltaP `25.4314` edge `0.245` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.3281` n `53` status `ready` deltaP `17.4754` edge `0.0243` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.7886` n `53` status `ready` deltaP `18.9413` edge `0.08` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
