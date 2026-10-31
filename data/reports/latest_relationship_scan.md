# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T14:37:26.464896+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7285`

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

- `market_context_high->unknown_24h` score `2571.8902` n `106` status `ready` deltaP `-8.2252` edge `214.422` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `89.7037` n `104` status `ready` deltaP `-5.6943` edge `7.5419` maxDD `-0.9571`
- `market_context_high->unknown_4h` score `70.6318` n `106` status `ready` deltaP `0.8657` edge `5.8935` maxDD `-0.3966`
- `news_risk_high->crypto_alt_24h` score `17.6463` n `52` status `ready` deltaP `45.1121` edge `1.1749` maxDD `-0.0763`
- `market_context_high->equity_24h` score `11.1806` n `106` status `ready` deltaP `27.1095` edge `1.0267` maxDD `-14.0571`
- `market_context_high->index_24h` score `4.7859` n `106` status `ready` deltaP `42.8459` edge `0.1315` maxDD `-0.1315`
- `news_risk_high->crypto_alt_4h` score `4.512` n `98` status `ready` deltaP `16.6563` edge `0.4036` maxDD `-7.4246`
- `market_context_high->metal_4h` score `1.8724` n `106` status `ready` deltaP `23.0125` edge `0.0451` maxDD `-0.7323`
- `market_context_high->equity_4h` score `1.4579` n `106` status `ready` deltaP `8.8242` edge `0.202` maxDD `-4.48`
- `market_context_high->metal_1h` score `1.0454` n `106` status `ready` deltaP `14.5548` edge `0.0191` maxDD `-0.3209`
- `market_context_high->crypto_major_1h` score `0.8809` n `106` status `ready` deltaP `11.366` edge `0.1004` maxDD `-5.2213`
- `market_context_high->equity_1h` score `0.783` n `106` status `ready` deltaP `7.6969` edge `0.1015` maxDD `-2.3383`
- `news_risk_high->crypto_alt_1h` score `0.4262` n `104` status `ready` deltaP `6.6041` edge `0.0869` maxDD `-3.9659`
- `market_context_high->crypto_major_4h` score `0.3486` n `106` status `ready` deltaP `18.0396` edge `0.1828` maxDD `-14.5879`
- `market_context_high->metal_24h` score `0.1839` n `106` status `ready` deltaP `14.7864` edge `0.1897` maxDD `-10.5088`
- `market_context_high->fx_1h` score `0.1768` n `106` status `ready` deltaP `7.4879` edge `-0.0005` maxDD `-0.1407`
- `market_context_high->fx_4h` score `0.0927` n `106` status `ready` deltaP `6.995` edge `0.0002` maxDD `-0.1285`
- `market_context_high->commodity_4h` score `-0.0097` n `106` status `ready` deltaP `10.2048` edge `0.0526` maxDD `-1.0837`
- `market_context_high->index_1h` score `-0.2364` n `106` status `ready` deltaP `4.9571` edge `0.0031` maxDD `-1.1344`
- `market_context_high->crypto_alt_1h` score `-0.471` n `106` status `ready` deltaP `3.6832` edge `0.0926` maxDD `-7.536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
