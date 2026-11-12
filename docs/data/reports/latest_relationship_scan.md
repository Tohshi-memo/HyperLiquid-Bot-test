# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T02:29:24.030484+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11536`

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

- `market_context_high->unknown_24h` score `106.1328` n `88` status `ready` deltaP `4.9937` edge `8.8252` maxDD `-0.4609`
- `market_context_high->unknown_4h` score `92.5864` n `88` status `ready` deltaP `7.9823` edge `7.7071` maxDD `-0.9161`
- `news_risk_high->equity_24h` score `41.4131` n `45` status `ready` deltaP `35.2941` edge `3.2158` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `24.0253` n `45` status `ready` deltaP `44.5751` edge `1.9015` maxDD `-12.7247`
- `market_context_high->equity_24h` score `18.2593` n `88` status `ready` deltaP `18.2486` edge `1.6391` maxDD `-16.7984`
- `news_risk_high->equity_4h` score `11.2783` n `53` status `ready` deltaP `33.9536` edge `0.8257` maxDD `-6.9762`
- `news_risk_high->commodity_24h` score `6.5944` n `45` status `ready` deltaP `39.9654` edge `0.2831` maxDD `0.0`
- `news_risk_high->index_24h` score `6.2674` n `45` status `ready` deltaP `32.0069` edge `0.3089` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `6.1008` n `88` status `ready` deltaP `34.9638` edge `1.0585` maxDD `-33.4213`
- `market_context_high->metal_24h` score `4.8561` n `88` status `ready` deltaP `35.0071` edge `0.2266` maxDD `-1.4245`
- `news_risk_high->metal_4h` score `4.3425` n `53` status `ready` deltaP `41.6705` edge `0.1217` maxDD `-1.0104`
- `news_risk_high->crypto_alt_24h` score `4.3343` n `45` status `ready` deltaP `15.6709` edge `0.7092` maxDD `-16.3061`
- `news_risk_high->crypto_major_4h` score `3.9064` n `53` status `ready` deltaP `20.7433` edge `0.336` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.4734` n `53` status `ready` deltaP `18.1646` edge `0.2396` maxDD `-3.6997`
- `market_context_high->index_24h` score `3.4166` n `88` status `ready` deltaP `18.3705` edge `0.2085` maxDD `-2.3671`
- `news_risk_high->commodity_4h` score `2.5872` n `53` status `ready` deltaP `23.6626` edge `0.0832` maxDD `-0.3611`
- `news_risk_high->crypto_alt_4h` score `2.1967` n `53` status `ready` deltaP `24.9741` edge `0.279` maxDD `-10.1088`
- `news_risk_high->index_4h` score `2.1936` n `53` status `ready` deltaP `20.8985` edge `0.0871` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `2.0672` n `53` status `ready` deltaP `24.6921` edge `0.0331` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3149` n `53` status `ready` deltaP `17.3257` edge `0.0242` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
