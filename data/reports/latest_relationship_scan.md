# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T21:37:28.299364+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11754`

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

- `news_risk_high->unknown_24h` score `4436.3796` n `85` status `ready` deltaP `1.2153` edge `369.6902` maxDD `0.0`
- `market_context_high->unknown_1h` score `70.4803` n `45` status `ready` deltaP `10.2029` edge `5.81` maxDD `-0.0395`
- `market_context_high->crypto_major_24h` score `49.4674` n `45` status `ready` deltaP `25.0347` edge `3.9905` maxDD `-2.4756`
- `market_context_high->equity_24h` score `27.0346` n `45` status `ready` deltaP `35.2778` edge `2.0491` maxDD `-2.1786`
- `market_context_high->crypto_alt_24h` score `26.7995` n `45` status `ready` deltaP `14.9653` edge `2.1715` maxDD `-2.7051`
- `market_context_high->index_24h` score `7.412` n `45` status `ready` deltaP `30.0695` edge `0.426` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.5516` n `45` status `ready` deltaP `30.5556` edge `0.1161` maxDD `-0.2401`
- `market_context_high->index_4h` score `3.314` n `45` status `ready` deltaP `37.2357` edge `0.035` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.9134` n `45` status `ready` deltaP `18.2385` edge `0.163` maxDD `-1.3444`
- `news_risk_high->index_24h` score `2.0562` n `85` status `ready` deltaP `24.0564` edge `0.068` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `1.4139` n `85` status `ready` deltaP `30.4249` edge `0.1432` maxDD `-6.8481`
- `market_context_high->equity_1h` score `1.2092` n `45` status `ready` deltaP `13.523` edge `0.0509` maxDD `-1.5564`
- `market_context_high->crypto_major_1h` score `1.1024` n `45` status `ready` deltaP `8.503` edge `0.1086` maxDD `-4.5405`
- `market_context_high->crypto_alt_4h` score `1.0394` n `45` status `ready` deltaP `8.4587` edge `0.097` maxDD `-3.3417`
- `market_context_high->crypto_major_4h` score `0.9626` n `45` status `ready` deltaP `7.5846` edge `0.1201` maxDD `-5.2359`
- `news_risk_high->crypto_alt_24h` score `0.8808` n `85` status `ready` deltaP `8.9522` edge `0.4089` maxDD `-29.2814`
- `market_context_high->index_1h` score `0.7294` n `45` status `ready` deltaP `11.8995` edge `0.0093` maxDD `-0.2275`
- `market_context_high->metal_1h` score `0.2005` n `45` status `ready` deltaP `5.6021` edge `0.011` maxDD `-0.1976`
- `market_context_high->crypto_alt_1h` score `0.1863` n `45` status `ready` deltaP `4.7605` edge `0.0727` maxDD `-5.7799`
- `market_context_high->fx_1h` score `0.1818` n `45` status `ready` deltaP `7.8243` edge `0.0068` maxDD `-0.1854`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
