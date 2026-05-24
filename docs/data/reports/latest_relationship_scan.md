# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T19:37:15.925272+00:00`
- Price records: `672`
- Market context records: `1769`
- Flow alert records: `6992`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8872`

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

- `market_context_high->metal_24h` score `7.168` n `176` status `ready` deltaP `28.2355` edge `0.6517` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `6.2018` n `194` status `ready` deltaP `21.86` edge `0.5477` maxDD `-9.1295`
- `news_risk_high->commodity_4h` score `5.8494` n `30` status `ready` deltaP `27.124` edge `0.3721` maxDD `-3.5713`
- `market_context_high->crypto_major_4h` score `4.755` n `194` status `ready` deltaP `23.0875` edge `0.4829` maxDD `-10.9117`
- `market_context_high->index_24h` score `3.871` n `176` status `ready` deltaP `18.8131` edge `0.32` maxDD `-4.1604`
- `market_context_high->equity_4h` score `3.2263` n `194` status `ready` deltaP `17.2366` edge `0.2634` maxDD `-5.0894`
- `market_context_high->unknown_4h` score `3.2056` n `194` status `ready` deltaP `14.0778` edge `0.4004` maxDD `-11.1695`
- `news_risk_high->commodity_1h` score `3.0875` n `30` status `ready` deltaP `24.1218` edge `0.1282` maxDD `-1.2043`
- `market_context_high->equity_24h` score `2.7583` n `176` status `ready` deltaP `17.2349` edge `0.6048` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `2.7074` n `176` status `ready` deltaP `14.6781` edge `0.6598` maxDD `-35.8966`
- `market_context_high->index_4h` score `1.0537` n `194` status `ready` deltaP `12.9165` edge `0.1106` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `0.8465` n `194` status `ready` deltaP `7.9804` edge `0.1197` maxDD `-4.1892`
- `news_risk_high->fx_4h` score `0.8261` n `30` status `ready` deltaP `20.5691` edge `-0.004` maxDD `-0.1774`
- `market_context_high->crypto_major_24h` score `0.5206` n `176` status `ready` deltaP `19.2551` edge `0.7736` maxDD `-62.3533`
- `market_context_high->crypto_major_1h` score `0.2963` n `194` status `ready` deltaP `5.1207` edge `0.0979` maxDD `-3.9211`
- `news_risk_high->unknown_4h` score `0.193` n `30` status `ready` deltaP `9.3699` edge `0.0346` maxDD `-2.7857`
- `market_context_high->equity_1h` score `0.1303` n `194` status `ready` deltaP `5.5513` edge `0.0547` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.1544` n `194` status `ready` deltaP `4.3213` edge `0.0215` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.1953` n `194` status `ready` deltaP `12.7122` edge `0.1594` maxDD `-12.5349`
- `news_risk_high->unknown_1h` score `-0.4458` n `30` status `ready` deltaP `16.8563` edge `-0.1223` maxDD `-2.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
