# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T22:07:30.152087+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11442`

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

- `news_risk_high->unknown_24h` score `4436.3016` n `85` status `ready` deltaP `1.2153` edge `369.6837` maxDD `0.0`
- `market_context_high->unknown_1h` score `70.4899` n `45` status `ready` deltaP `10.2029` edge `5.8108` maxDD `-0.0395`
- `market_context_high->crypto_major_24h` score `49.5077` n `45` status `ready` deltaP `25.2084` edge `3.9927` maxDD `-2.4756`
- `market_context_high->equity_24h` score `27.0485` n `45` status `ready` deltaP `35.4514` edge `2.0491` maxDD `-2.1786`
- `market_context_high->crypto_alt_24h` score `26.8139` n `45` status `ready` deltaP `14.9653` edge `2.1727` maxDD `-2.7051`
- `market_context_high->index_24h` score `7.4132` n `45` status `ready` deltaP `30.0695` edge `0.4261` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.5655` n `45` status `ready` deltaP `30.7292` edge `0.1161` maxDD `-0.2401`
- `market_context_high->index_4h` score `3.314` n `45` status `ready` deltaP `37.2357` edge `0.035` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.9414` n `45` status `ready` deltaP `18.5434` edge `0.1633` maxDD `-1.3444`
- `news_risk_high->index_24h` score `2.0574` n `85` status `ready` deltaP `24.0564` edge `0.0681` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `1.4229` n `85` status `ready` deltaP `30.5985` edge `0.1432` maxDD `-6.8481`
- `market_context_high->equity_1h` score `1.196` n `45` status `ready` deltaP `13.3733` edge `0.0508` maxDD `-1.5564`
- `market_context_high->crypto_alt_4h` score `1.131` n `45` status `ready` deltaP `8.7635` edge `0.1026` maxDD `-3.3417`
- `market_context_high->crypto_major_1h` score `1.0964` n `45` status `ready` deltaP `8.503` edge `0.1081` maxDD `-4.5405`
- `market_context_high->crypto_major_4h` score `0.982` n `45` status `ready` deltaP `7.7371` edge `0.1207` maxDD `-5.2359`
- `news_risk_high->crypto_alt_24h` score `0.8952` n `85` status `ready` deltaP `8.9522` edge `0.4101` maxDD `-29.2814`
- `market_context_high->index_1h` score `0.7043` n `45` status `ready` deltaP `11.6001` edge `0.0092` maxDD `-0.2275`
- `market_context_high->fx_1h` score `0.1896` n `45` status `ready` deltaP `7.974` edge `0.0068` maxDD `-0.1854`
- `market_context_high->metal_1h` score `0.1886` n `45` status `ready` deltaP `5.4524` edge `0.011` maxDD `-0.1976`
- `market_context_high->crypto_alt_1h` score `0.1839` n `45` status `ready` deltaP `4.7605` edge `0.0725` maxDD `-5.7799`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
