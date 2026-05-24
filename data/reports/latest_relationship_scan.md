# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T21:22:16.817502+00:00`
- Price records: `672`
- Market context records: `1778`
- Flow alert records: `7015`
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

- `market_context_high->metal_24h` score `7.1973` n `180` status `ready` deltaP `28.5416` edge `0.6521` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `5.9784` n `194` status `ready` deltaP `21.7076` edge `0.5301` maxDD `-9.1295`
- `news_risk_high->commodity_4h` score `5.8686` n `30` status `ready` deltaP `27.124` edge `0.3737` maxDD `-3.5713`
- `market_context_high->crypto_major_4h` score `4.6` n `194` status `ready` deltaP `22.935` edge `0.471` maxDD `-10.9117`
- `market_context_high->index_24h` score `3.5605` n `180` status `ready` deltaP `17.9167` edge `0.3001` maxDD `-4.1604`
- `market_context_high->unknown_4h` score `3.4382` n `194` status `ready` deltaP `14.84` edge `0.4147` maxDD `-11.1695`
- `market_context_high->equity_4h` score `3.1043` n `194` status `ready` deltaP `16.6269` edge `0.2573` maxDD `-5.0894`
- `news_risk_high->commodity_1h` score `3.0252` n `30` status `ready` deltaP `23.523` edge `0.127` maxDD `-1.2043`
- `market_context_high->equity_24h` score `2.3562` n `180` status `ready` deltaP `16.4236` edge `0.5767` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `2.0891` n `180` status `ready` deltaP `13.7153` edge `0.6147` maxDD `-35.8966`
- `market_context_high->index_4h` score `0.9679` n `194` status `ready` deltaP `12.4591` edge `0.1065` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `0.9376` n `194` status `ready` deltaP `8.5792` edge `0.1233` maxDD `-4.1892`
- `news_risk_high->fx_4h` score `0.8071` n `30` status `ready` deltaP `20.2643` edge `-0.0044` maxDD `-0.1774`
- `market_context_high->crypto_major_1h` score `0.385` n `194` status `ready` deltaP `5.7195` edge `0.1013` maxDD `-3.9211`
- `news_risk_high->unknown_4h` score `0.3442` n `30` status `ready` deltaP `10.1321` edge `0.0489` maxDD `-2.7857`
- `market_context_high->equity_1h` score `0.1339` n `194` status `ready` deltaP `5.5513` edge `0.055` maxDD `-2.8014`
- `market_context_high->crypto_major_24h` score `-0.0787` n `180` status `ready` deltaP `18.3333` edge `0.7298` maxDD `-62.3533`
- `market_context_high->index_1h` score `-0.0825` n `194` status `ready` deltaP `5.0698` edge `0.0225` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.1354` n `194` status `ready` deltaP `13.4743` edge `0.162` maxDD `-12.5349`
- `news_risk_high->unknown_1h` score `-0.4341` n `30` status `ready` deltaP `17.006` edge `-0.1218` maxDD `-2.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
