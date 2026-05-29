# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T12:07:21.761207+00:00`
- Price records: `672`
- Market context records: `2243`
- Flow alert records: `8349`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9203`

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

- `news_risk_high->crypto_alt_24h` score `25.5706` n `39` status `ready` deltaP `55.4621` edge `1.82` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `16.2179` n `39` status `ready` deltaP `45.3526` edge `1.0931` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.3001` n `39` status `ready` deltaP `36.3248` edge `1.0643` maxDD `-2.1831`
- `market_context_high->crypto_alt_4h` score `12.3591` n `131` status `ready` deltaP `33.504` edge `0.9002` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.1952` n `131` status `ready` deltaP `39.7691` edge `0.7208` maxDD `-1.9063`
- `news_risk_high->unknown_24h` score `9.898` n `39` status `ready` deltaP `36.3649` edge `0.605` maxDD `-1.4744`
- `news_risk_high->crypto_major_24h` score `8.7647` n `39` status `ready` deltaP `23.4375` edge `1.0255` maxDD `-3.3119`
- `market_context_high->unknown_24h` score `8.2396` n `120` status `ready` deltaP `28.9931` edge `0.6202` maxDD `-8.4815`
- `market_context_high->unknown_4h` score `6.0508` n `131` status `ready` deltaP `23.2824` edge `0.3944` maxDD `-1.6306`
- `market_context_high->crypto_major_24h` score `5.9787` n `120` status `ready` deltaP `17.6041` edge `1.0384` maxDD `-25.1408`
- `market_context_high->index_4h` score `4.1581` n `131` status `ready` deltaP `31.5409` edge `0.1736` maxDD `-0.3228`
- `market_context_high->equity_4h` score `4.0433` n `131` status `ready` deltaP `23.7595` edge `0.2454` maxDD `-2.3484`
- `news_risk_high->commodity_4h` score `3.913` n `43` status `ready` deltaP `33.2246` edge `0.3473` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.4682` n `39` status `ready` deltaP `35.0828` edge `0.0736` maxDD `-0.1442`
- `news_risk_high->index_24h` score `3.3185` n `39` status `ready` deltaP `12.5134` edge `0.235` maxDD `-1.3507`
- `market_context_high->index_24h` score `3.2078` n `120` status `ready` deltaP `13.0903` edge `0.2318` maxDD `-1.4737`
- `market_context_high->crypto_alt_1h` score `2.6323` n `143` status `ready` deltaP `15.1847` edge `0.2045` maxDD `-4.9097`
- `market_context_high->crypto_major_1h` score `2.5134` n `143` status `ready` deltaP `14.0855` edge `0.1746` maxDD `-2.0579`
- `market_context_high->equity_24h` score `2.4913` n `120` status `ready` deltaP `20.5556` edge `0.2418` maxDD `-8.3649`
- `news_risk_high->fx_4h` score `2.15` n `43` status `ready` deltaP `27.2794` edge `0.0157` maxDD `-0.1382`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
