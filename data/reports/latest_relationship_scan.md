# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-26T10:07:24.618539+00:00`
- Price records: `672`
- Market context records: `7974`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11787`

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

- `market_context_high->equity_24h` score `16.2388` n `82` status `ready` deltaP `24.2124` edge `1.326` maxDD `-6.0681`
- `market_context_high->metal_24h` score `8.09` n `82` status `ready` deltaP `35.8752` edge `0.435` maxDD `0.0`
- `market_context_high->equity_4h` score `6.6185` n `95` status `ready` deltaP `25.9381` edge `0.4679` maxDD `-5.1426`
- `market_context_high->commodity_24h` score `3.9368` n `82` status `ready` deltaP `28.4002` edge `0.292` maxDD `-6.5945`
- `market_context_high->index_4h` score `2.7336` n `95` status `ready` deltaP `28.4532` edge `0.0741` maxDD `-0.8791`
- `market_context_high->metal_4h` score `2.5875` n `95` status `ready` deltaP `23.1691` edge `0.1234` maxDD `-0.979`
- `market_context_high->equity_1h` score `1.7324` n `102` status `ready` deltaP `14.6441` edge `0.1285` maxDD `-4.2072`
- `market_context_high->index_24h` score `1.1262` n `82` status `ready` deltaP `8.7018` edge `0.1534` maxDD `-1.3621`
- `market_context_high->fx_24h` score `1.1128` n `82` status `ready` deltaP `24.9746` edge `0.035` maxDD `-3.0343`
- `market_context_high->index_1h` score `1.0891` n `102` status `ready` deltaP `16.8257` edge `0.0216` maxDD `-0.7743`
- `market_context_high->crypto_alt_4h` score `1.0749` n `95` status `ready` deltaP `9.209` edge `0.1399` maxDD `-3.9374`
- `market_context_high->crypto_major_4h` score `0.866` n `95` status `ready` deltaP `9.9712` edge `0.1775` maxDD `-6.7444`
- `market_context_high->metal_1h` score `0.7423` n `102` status `ready` deltaP `10.6346` edge `0.0288` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.6005` n `102` status `ready` deltaP `11.4653` edge `0.0416` maxDD `-1.6171`
- `market_context_high->crypto_alt_1h` score `-0.0726` n `102` status `ready` deltaP `0.0675` edge `0.0335` maxDD `-1.4603`
- `market_context_high->fx_1h` score `-0.2315` n `102` status `ready` deltaP `0.8921` edge `0.0011` maxDD `-0.2715`
- `market_context_high->fx_4h` score `-0.638` n `95` status `ready` deltaP `2.6999` edge `0.0036` maxDD `-0.9813`
- `market_context_high->commodity_1h` score `-0.751` n `102` status `ready` deltaP `0.6094` edge `-0.0049` maxDD `-1.9395`
- `market_context_high->commodity_4h` score `-0.7963` n `95` status `ready` deltaP `2.5071` edge `0.0106` maxDD `-3.1604`
- `market_context_high->unknown_1h` score `-1.9863` n `102` status `ready` deltaP `6.1671` edge `-0.1643` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
