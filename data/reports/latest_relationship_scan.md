# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-14T08:37:22.384115+00:00`
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

- `market_context_high->unknown_24h` score `457.8809` n `75` status `ready` deltaP `2.1944` edge `38.1562` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `37.6152` n `53` status `ready` deltaP `36.6189` edge `2.9611` maxDD `-3.6503`
- `market_context_high->equity_24h` score `29.3815` n `75` status `ready` deltaP `31.1597` edge `2.3949` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `16.7178` n `75` status `ready` deltaP `47.5834` edge `1.3274` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `15.6962` n `53` status `ready` deltaP `42.0434` edge `1.9286` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.3142` n `53` status `ready` deltaP `36.8499` edge `0.8102` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `6.6826` n `53` status `ready` deltaP `45.3125` edge `0.2548` maxDD `0.0`
- `market_context_high->index_24h` score `5.982` n `75` status `ready` deltaP `35.632` edge `0.2701` maxDD `-0.0653`
- `news_risk_high->index_24h` score `5.301` n `53` status `ready` deltaP `33.6445` edge `0.2478` maxDD `-0.4279`
- `news_risk_high->metal_4h` score `5.0123` n `53` status `ready` deltaP `47.4632` edge `0.1389` maxDD `-1.0104`
- `market_context_high->metal_24h` score `4.3423` n `75` status `ready` deltaP `41.3334` edge `0.3703` maxDD `-3.7989`
- `news_risk_high->crypto_major_4h` score `4.1716` n `53` status `ready` deltaP `21.6579` edge `0.352` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.5697` n `53` status `ready` deltaP `18.6137` edge `0.2364` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.1237` n `53` status `ready` deltaP `28.3882` edge `0.0964` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.2326` n `53` status `ready` deltaP `26.0394` edge `0.0379` maxDD `-0.3692`
- `news_risk_high->index_4h` score `2.1943` n `53` status `ready` deltaP `22.4229` edge `0.077` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `2.0948` n `53` status `ready` deltaP `26.1936` edge `0.2578` maxDD `-10.1088`
- `news_risk_high->crypto_alt_24h` score `1.6607` n `53` status `ready` deltaP `14.4261` edge `0.5673` maxDD `-29.0448`
- `news_risk_high->index_1h` score `1.2622` n `53` status `ready` deltaP `17.0263` edge `0.0218` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.7707` n `53` status `ready` deltaP `18.3425` edge `0.0817` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
