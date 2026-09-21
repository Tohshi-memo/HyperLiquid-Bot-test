# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T19:22:28.234357+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10204`

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

- `market_context_high->unknown_4h` score `28.5859` n `58` status `ready` deltaP `1.6874` edge `2.3859` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `15.7736` n `101` status `ready` deltaP `3.6303` edge `1.9761` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `10.1696` n `101` status `ready` deltaP `4.0154` edge `1.3088` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `3.7131` n `101` status `ready` deltaP `17.3946` edge `0.3144` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.0717` n `101` status `ready` deltaP `19.2239` edge `0.2536` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.6215` n `101` status `ready` deltaP `15.932` edge `0.1588` maxDD `-2.058`
- `news_risk_high->commodity_24h` score `1.9625` n `101` status `ready` deltaP `27.5371` edge `0.1986` maxDD `-3.4467`
- `news_risk_high->crypto_major_1h` score `1.9093` n `101` status `ready` deltaP `17.429` edge `0.0952` maxDD `-2.8494`
- `market_context_high->equity_1h` score `0.615` n `58` status `ready` deltaP `4.362` edge `0.0475` maxDD `-0.36`
- `news_risk_high->metal_1h` score `0.4975` n `101` status `ready` deltaP `13.4004` edge `0.0123` maxDD `-0.8144`
- `market_context_high->index_1h` score `0.4813` n `58` status `ready` deltaP `8.0322` edge `0.0121` maxDD `-0.0435`
- `market_context_high->fx_1h` score `0.4097` n `58` status `ready` deltaP `9.5241` edge `0.0063` maxDD `-0.1854`
- `news_risk_high->fx_4h` score `0.3415` n `101` status `ready` deltaP `10.0126` edge `0.0253` maxDD `-0.421`
- `market_context_high->index_24h` score `0.3175` n `39` status `ready` deltaP `-5.3418` edge `0.1552` maxDD `-1.644`
- `news_risk_high->metal_4h` score `0.2783` n `101` status `ready` deltaP `14.3549` edge `0.0329` maxDD `-2.0994`
- `market_context_high->metal_1h` score `0.2195` n `58` status `ready` deltaP `4.9505` edge `0.0161` maxDD `-0.1314`
- `market_context_high->index_4h` score `0.0872` n `58` status `ready` deltaP `11.2752` edge `-0.0003` maxDD `-1.0949`
- `news_risk_high->fx_1h` score `-0.1393` n `101` status `ready` deltaP `3.8907` edge `0.0068` maxDD `-0.2147`
- `market_context_high->metal_24h` score `-0.2114` n `39` status `ready` deltaP `10.9909` edge `-0.0675` maxDD `-0.2042`
- `market_context_high->crypto_major_1h` score `-0.3756` n `58` status `ready` deltaP `-2.39` edge `0.0565` maxDD `-2.7494`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
