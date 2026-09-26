# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T23:07:28.829820+00:00`
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

- `news_risk_high->unknown_24h` score `4103.718` n `88` status `ready` deltaP `1.2153` edge `341.9684` maxDD `0.0`
- `market_context_high->unknown_1h` score `70.4827` n `45` status `ready` deltaP `10.2029` edge `5.8102` maxDD `-0.0395`
- `market_context_high->crypto_major_24h` score `49.6797` n `45` status `ready` deltaP `25.9028` edge `4.0024` maxDD `-2.4756`
- `market_context_high->equity_24h` score `27.1245` n `45` status `ready` deltaP `36.1459` edge `2.0508` maxDD `-2.1786`
- `market_context_high->crypto_alt_24h` score `26.8823` n `45` status `ready` deltaP `14.9653` edge `2.1784` maxDD `-2.7051`
- `market_context_high->index_24h` score `7.4759` n `45` status `ready` deltaP `30.7639` edge `0.4267` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.6259` n `45` status `ready` deltaP `31.4236` edge `0.1165` maxDD `-0.2401`
- `market_context_high->index_4h` score `3.2994` n `45` status `ready` deltaP `37.0833` edge `0.0348` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.9172` n `45` status `ready` deltaP `18.391` edge `0.1623` maxDD `-1.3444`
- `news_risk_high->index_24h` score `1.7859` n `88` status `ready` deltaP `21.6225` edge `0.0617` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `1.3011` n `88` status `ready` deltaP `28.6458` edge `0.1406` maxDD `-6.8481`
- `market_context_high->equity_1h` score `1.1685` n `45` status `ready` deltaP `13.0739` edge `0.0505` maxDD `-1.5564`
- `market_context_high->crypto_alt_4h` score `1.1674` n `45` status `ready` deltaP `9.0684` edge `0.1036` maxDD `-3.3417`
- `market_context_high->crypto_major_1h` score `1.1227` n `45` status `ready` deltaP `8.6527` edge `0.1093` maxDD `-4.5405`
- `market_context_high->crypto_major_4h` score `0.911` n `45` status `ready` deltaP `7.5846` edge `0.1158` maxDD `-5.2359`
- `market_context_high->index_1h` score `0.6552` n `45` status `ready` deltaP `11.0013` edge `0.0091` maxDD `-0.2275`
- `news_risk_high->crypto_alt_24h` score `0.2264` n `88` status `ready` deltaP `9.233` edge `0.3525` maxDD `-29.2814`
- `market_context_high->crypto_alt_1h` score `0.215` n `45` status `ready` deltaP `4.9102` edge `0.0741` maxDD `-5.7799`
- `market_context_high->fx_1h` score `0.181` n `45` status `ready` deltaP `7.8243` edge `0.0067` maxDD `-0.1854`
- `market_context_high->metal_1h` score `0.1766` n `45` status `ready` deltaP `5.3027` edge `0.011` maxDD `-0.1976`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
