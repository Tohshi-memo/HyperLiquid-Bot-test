# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T01:22:16.385390+00:00`
- Price records: `672`
- Market context records: `1070`
- Flow alert records: `4984`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8669`

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

- `market_context_high->crypto_major_24h` score `15.7542` n `167` status `ready` deltaP `34.6956` edge `1.1279` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `5.3734` n `167` status `ready` deltaP `11.9221` edge `0.4917` maxDD `-9.5387`
- `market_context_high->equity_24h` score `4.721` n `167` status `ready` deltaP `13.6315` edge `0.3522` maxDD `-3.6396`
- `market_context_high->index_24h` score `4.0381` n `167` status `ready` deltaP `14.1613` edge `0.2729` maxDD `-2.1308`
- `market_context_high->metal_24h` score `3.7497` n `167` status `ready` deltaP `-3.5268` edge `0.5027` maxDD `-6.3373`
- `market_context_high->equity_4h` score `1.0678` n `169` status `ready` deltaP `6.1814` edge `0.1266` maxDD `-3.6396`
- `market_context_high->index_4h` score `0.4647` n `169` status `ready` deltaP `4.7293` edge `0.0755` maxDD `-2.1308`
- `market_context_high->crypto_major_4h` score `0.443` n `169` status `ready` deltaP `10.9729` edge `0.1402` maxDD `-7.1146`
- `market_context_high->index_1h` score `0.1833` n `170` status `ready` deltaP `6.0672` edge `0.0195` maxDD `-1.5741`
- `market_context_high->fx_1h` score `-0.0671` n `170` status `ready` deltaP `5.5301` edge `0.0001` maxDD `-0.3124`
- `market_context_high->crypto_major_1h` score `-0.1266` n `170` status `ready` deltaP `8.193` edge `0.0272` maxDD `-5.3898`
- `market_context_high->equity_1h` score `-0.2448` n `170` status `ready` deltaP `1.1905` edge `0.0377` maxDD `-3.6162`
- `market_context_high->metal_1h` score `-0.4444` n `170` status `ready` deltaP `5.627` edge `-0.0185` maxDD `-3.4119`
- `market_context_high->fx_4h` score `-0.7169` n `169` status `ready` deltaP `0.8154` edge `0.0023` maxDD `-1.6381`
- `market_context_high->crypto_alt_1h` score `-0.8494` n `170` status `ready` deltaP `2.3864` edge `0.0219` maxDD `-5.3538`
- `market_context_high->commodity_1h` score `-0.9422` n `170` status `ready` deltaP `-0.9951` edge `0.0089` maxDD `-3.7959`
- `market_context_high->crypto_alt_4h` score `-1.2138` n `169` status `ready` deltaP `4.7671` edge `0.1175` maxDD `-13.0347`
- `market_context_high->metal_4h` score `-2.1642` n `169` status `ready` deltaP `2.6609` edge `-0.0998` maxDD `-9.2991`
- `market_context_high->commodity_4h` score `-2.7174` n `169` status `ready` deltaP `-8.0585` edge `0.0221` maxDD `-13.0076`
- `market_context_high->fx_24h` score `-3.05` n `167` status `ready` deltaP `5.6122` edge `-0.0208` maxDD `-19.2774`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
