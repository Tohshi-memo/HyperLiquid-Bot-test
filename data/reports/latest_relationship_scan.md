# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T23:22:31.280824+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11444`

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

- `news_risk_high->unknown_24h` score `3997.848` n `89` status `ready` deltaP `1.2153` edge `333.1459` maxDD `0.0`
- `market_context_high->unknown_1h` score `70.4335` n `45` status `ready` deltaP `10.2029` edge `5.8061` maxDD `-0.0395`
- `market_context_high->crypto_major_24h` score `49.7164` n `45` status `ready` deltaP `26.0764` edge `4.0043` maxDD `-2.4756`
- `market_context_high->equity_24h` score `27.1329` n `45` status `ready` deltaP `36.1459` edge `2.0515` maxDD `-2.1786`
- `market_context_high->crypto_alt_24h` score `26.8943` n `45` status `ready` deltaP `14.9653` edge `2.1794` maxDD `-2.7051`
- `market_context_high->index_24h` score `7.4922` n `45` status `ready` deltaP `30.9375` edge `0.4269` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.6398` n `45` status `ready` deltaP `31.5972` edge `0.1165` maxDD `-0.2401`
- `market_context_high->index_4h` score `3.2982` n `45` status `ready` deltaP `37.0833` edge `0.0347` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.899` n `45` status `ready` deltaP `18.2385` edge `0.1618` maxDD `-1.3444`
- `news_risk_high->index_24h` score `1.6949` n `89` status `ready` deltaP `20.8001` edge `0.0596` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `1.2593` n `89` status `ready` deltaP `27.9767` edge `0.1397` maxDD `-6.8481`
- `market_context_high->equity_1h` score `1.1685` n `45` status `ready` deltaP `13.0739` edge `0.0505` maxDD `-1.5564`
- `market_context_high->crypto_alt_4h` score `1.1506` n `45` status `ready` deltaP `9.0684` edge `0.1022` maxDD `-3.3417`
- `market_context_high->crypto_major_1h` score `1.106` n `45` status `ready` deltaP `8.503` edge `0.1089` maxDD `-4.5405`
- `market_context_high->crypto_major_4h` score `0.8688` n `45` status `ready` deltaP `7.4322` edge `0.1133` maxDD `-5.2359`
- `market_context_high->index_1h` score `0.6552` n `45` status `ready` deltaP `11.0013` edge `0.0091` maxDD `-0.2275`
- `market_context_high->crypto_alt_1h` score `0.2162` n `45` status `ready` deltaP `4.9102` edge `0.0742` maxDD `-5.7799`
- `market_context_high->fx_1h` score `0.1888` n `45` status `ready` deltaP `7.974` edge `0.0067` maxDD `-0.1854`
- `market_context_high->metal_1h` score `0.1766` n `45` status `ready` deltaP `5.3027` edge `0.011` maxDD `-0.1976`
- `news_risk_high->crypto_alt_24h` score `-0.0076` n `89` status `ready` deltaP `9.3223` edge `0.3324` maxDD `-29.2814`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
