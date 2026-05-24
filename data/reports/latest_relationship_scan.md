# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T19:22:15.327522+00:00`
- Price records: `672`
- Market context records: `1768`
- Flow alert records: `6989`
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

- `market_context_high->metal_24h` score `7.1706` n `175` status `ready` deltaP `28.1478` edge `0.6525` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `6.2272` n `194` status `ready` deltaP `22.0125` edge `0.5488` maxDD `-9.1295`
- `news_risk_high->commodity_4h` score `5.8542` n `30` status `ready` deltaP `27.124` edge `0.3725` maxDD `-3.5713`
- `market_context_high->crypto_major_4h` score `4.7768` n `194` status `ready` deltaP `23.2399` edge `0.4837` maxDD `-10.9117`
- `market_context_high->index_24h` score `3.9232` n `175` status `ready` deltaP `18.8958` edge `0.3238` maxDD `-4.1604`
- `market_context_high->equity_4h` score `3.2239` n `194` status `ready` deltaP `17.2366` edge `0.2632` maxDD `-5.0894`
- `market_context_high->unknown_4h` score `3.1802` n `194` status `ready` deltaP `13.9253` edge `0.3993` maxDD `-11.1695`
- `news_risk_high->commodity_1h` score `3.0887` n `30` status `ready` deltaP `24.1218` edge `0.1283` maxDD `-1.2043`
- `market_context_high->unknown_24h` score `2.8444` n `175` status `ready` deltaP `14.7867` edge `0.6705` maxDD `-35.8966`
- `market_context_high->equity_24h` score `2.8178` n `175` status `ready` deltaP `17.3046` edge `0.6093` maxDD `-33.1875`
- `market_context_high->index_4h` score `1.0537` n `194` status `ready` deltaP `12.9165` edge `0.1106` maxDD `-3.7119`
- `news_risk_high->fx_4h` score `0.834` n `30` status `ready` deltaP `20.7216` edge `-0.004` maxDD `-0.1774`
- `market_context_high->crypto_alt_1h` score `0.8273` n `194` status `ready` deltaP `7.8307` edge `0.1191` maxDD `-4.1892`
- `market_context_high->crypto_major_24h` score `0.6033` n `175` status `ready` deltaP `19.3443` edge `0.7799` maxDD `-62.3533`
- `market_context_high->crypto_major_1h` score `0.2891` n `194` status `ready` deltaP `5.1207` edge `0.0973` maxDD `-3.9211`
- `news_risk_high->unknown_4h` score `0.1765` n `30` status `ready` deltaP `9.2174` edge `0.0335` maxDD `-2.7857`
- `market_context_high->equity_1h` score `0.1147` n `194` status `ready` deltaP `5.4016` edge `0.0544` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.1556` n `194` status `ready` deltaP `4.3213` edge `0.0214` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.2102` n `194` status `ready` deltaP `12.5597` edge `0.1585` maxDD `-12.5349`
- `news_risk_high->unknown_1h` score `-0.459` n `30` status `ready` deltaP `16.7066` edge `-0.123` maxDD `-2.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
