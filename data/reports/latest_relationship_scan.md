# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-14T08:07:30.633416+00:00`
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

- `market_context_high->unknown_24h` score `453.7865` n `75` status `ready` deltaP `2.1944` edge `37.815` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `37.4854` n `53` status `ready` deltaP `36.2717` edge `2.9526` maxDD `-3.6503`
- `market_context_high->equity_24h` score `29.2517` n `75` status `ready` deltaP `30.8125` edge `2.3864` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `16.6818` n `75` status `ready` deltaP `47.5834` edge `1.3244` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `15.6408` n `53` status `ready` deltaP `42.0434` edge `1.9215` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.3166` n `53` status `ready` deltaP `36.8499` edge `0.8104` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `6.644` n `53` status `ready` deltaP `44.9653` edge `0.2539` maxDD `0.0`
- `market_context_high->index_24h` score `5.9434` n `75` status `ready` deltaP `35.2848` edge `0.2692` maxDD `-0.0653`
- `news_risk_high->index_24h` score `5.2624` n `53` status `ready` deltaP `33.2973` edge `0.2469` maxDD `-0.4279`
- `news_risk_high->metal_4h` score `5.0379` n `53` status `ready` deltaP `47.7681` edge `0.139` maxDD `-1.0104`
- `market_context_high->metal_24h` score `4.3353` n `75` status `ready` deltaP `41.3334` edge `0.3694` maxDD `-3.7989`
- `news_risk_high->crypto_major_4h` score `4.191` n `53` status `ready` deltaP `21.8103` edge `0.3526` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.5685` n `53` status `ready` deltaP `18.6137` edge `0.2363` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.1225` n `53` status `ready` deltaP `28.3882` edge `0.0963` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.2326` n `53` status `ready` deltaP `26.0394` edge `0.0379` maxDD `-0.3692`
- `news_risk_high->index_4h` score `2.2065` n `53` status `ready` deltaP `22.5754` edge `0.077` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `2.0948` n `53` status `ready` deltaP `26.1936` edge `0.2578` maxDD `-10.1088`
- `news_risk_high->crypto_alt_24h` score `1.6373` n `53` status `ready` deltaP `14.4261` edge `0.5643` maxDD `-29.0448`
- `news_risk_high->index_1h` score `1.2622` n `53` status `ready` deltaP `17.0263` edge `0.0218` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.7827` n `53` status `ready` deltaP `18.0431` edge `0.078` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
