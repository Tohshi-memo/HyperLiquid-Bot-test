# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T06:52:27.227072+00:00`
- Price records: `672`
- Market context records: `8171`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11746`

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

- `news_risk_high->unknown_24h` score `8672.7082` n `40` status `ready` deltaP `37.1528` edge `722.478` maxDD `0.0`
- `market_context_high->equity_24h` score `18.8075` n `59` status `ready` deltaP `44.2532` edge `1.3633` maxDD `-4.9489`
- `market_context_high->equity_4h` score `9.2428` n `60` status `ready` deltaP `38.1606` edge `0.5393` maxDD `-0.5442`
- `news_risk_high->equity_4h` score `9.2161` n `43` status `ready` deltaP `34.866` edge `0.5561` maxDD `-0.6428`
- `market_context_high->metal_24h` score `8.0747` n `59` status `ready` deltaP `42.0139` edge `0.3928` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `5.5607` n `43` status `ready` deltaP `20.7956` edge `0.3853` maxDD `-2.1767`
- `market_context_high->index_4h` score `4.0563` n `60` status `ready` deltaP `36.9309` edge `0.0961` maxDD `-0.0092`
- `market_context_high->equity_1h` score `3.5025` n `60` status `ready` deltaP `20.489` edge `0.1756` maxDD `-0.6254`
- `news_risk_high->equity_1h` score `3.3124` n `49` status `ready` deltaP `24.7067` edge `0.1422` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.9708` n `43` status `ready` deltaP `24.9929` edge `0.1` maxDD `-0.191`
- `news_risk_high->metal_4h` score `1.854` n `43` status `ready` deltaP `17.0235` edge `0.0878` maxDD `-0.7433`
- `market_context_high->index_24h` score `1.8035` n `59` status `ready` deltaP `16.9109` edge `0.1855` maxDD `-1.3621`
- `market_context_high->index_1h` score `1.7855` n `60` status `ready` deltaP `20.5988` edge `0.0253` maxDD `-0.1069`
- `news_risk_high->crypto_major_1h` score `1.6901` n `49` status `ready` deltaP `10.586` edge `0.11` maxDD `-1.1783`
- `market_context_high->metal_4h` score `1.5963` n `60` status `ready` deltaP `20.5894` edge `0.058` maxDD `-0.979`
- `news_risk_high->crypto_alt_1h` score `1.4791` n `49` status `ready` deltaP `11.4842` edge `0.0901` maxDD `-1.1388`
- `news_risk_high->crypto_alt_4h` score `1.173` n `43` status `ready` deltaP `12.8651` edge `0.2038` maxDD `-5.8012`
- `market_context_high->commodity_24h` score `0.9158` n `59` status `ready` deltaP `26.948` edge `0.2263` maxDD `-15.7497`
- `market_context_high->fx_24h` score `0.8984` n `59` status `ready` deltaP `19.9858` edge `0.0523` maxDD `-0.6283`
- `news_risk_high->index_1h` score `0.5406` n `49` status `ready` deltaP `7.7417` edge `0.0223` maxDD `-0.3089`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
