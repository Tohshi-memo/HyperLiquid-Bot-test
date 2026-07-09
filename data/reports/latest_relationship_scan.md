# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-09T21:22:29.086957+00:00`
- Price records: `672`
- Market context records: `6219`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11110`

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

- `news_risk_high->crypto_alt_24h` score `13.181` n `32` status `ready` deltaP `42.2194` edge `0.8317` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.501` n `32` status `ready` deltaP `56.1224` edge `0.1676` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1379` n `32` status `ready` deltaP `43.3689` edge `0.0603` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `2.4875` n `32` status `ready` deltaP `15.625` edge `0.2927` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.3332` n `32` status `ready` deltaP `28.1437` edge `0.0207` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.9448` n `192` status `ready` deltaP `1.812` edge `0.2508` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.3844` n `32` status `ready` deltaP `14.128` edge `0.13` maxDD `-2.0691`
- `news_risk_high->commodity_24h` score `1.2087` n `32` status `ready` deltaP `20.7696` edge `-0.0172` maxDD `-0.3101`
- `news_risk_high->crypto_alt_1h` score `0.7421` n `32` status `ready` deltaP `9.8241` edge `0.0758` maxDD `-1.6923`
- `market_context_high->unknown_4h` score `0.5155` n `192` status `ready` deltaP `-2.1469` edge `0.3105` maxDD `-11.925`
- `market_context_high->metal_24h` score `-0.0447` n `192` status `ready` deltaP `19.8023` edge `0.1191` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.2292` n `32` status `ready` deltaP `8.801` edge `-0.0009` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.3003` n `192` status `ready` deltaP `1.0604` edge `-0.001` maxDD `-0.5659`
- `market_context_high->commodity_1h` score `-0.5835` n `192` status `ready` deltaP `-0.8982` edge `0.002` maxDD `-0.5708`
- `market_context_high->metal_4h` score `-0.6717` n `192` status `ready` deltaP `3.214` edge `0.0112` maxDD `-3.4996`
- `news_risk_high->metal_1h` score `-0.7995` n `32` status `ready` deltaP `-3.7425` edge `-0.0278` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.8892` n `192` status `ready` deltaP `1.4658` edge `-0.004` maxDD `-2.0564`
- `market_context_high->crypto_major_1h` score `-0.9152` n `192` status `ready` deltaP `4.2322` edge `0.0312` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-0.9216` n `192` status `ready` deltaP `4.0949` edge `0.0298` maxDD `-9.3536`
- `market_context_high->equity_4h` score `-1.1034` n `192` status `ready` deltaP `0.686` edge `-0.0048` maxDD `-2.671`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
