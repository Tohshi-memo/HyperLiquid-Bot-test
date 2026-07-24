# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T05:07:31.508212+00:00`
- Price records: `672`
- Market context records: `7744`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14676`

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

- `market_context_high->equity_24h` score `4.5816` n `132` status `ready` deltaP `21.3124` edge `0.3739` maxDD `-6.0681`
- `market_context_high->crypto_major_1h` score `0.9758` n `133` status `ready` deltaP `12.8585` edge `0.0397` maxDD `-1.5286`
- `market_context_high->crypto_major_4h` score `0.6375` n `133` status `ready` deltaP `13.2794` edge `0.1364` maxDD `-6.7444`
- `market_context_high->equity_1h` score `0.5282` n `133` status `ready` deltaP `8.3463` edge `0.0743` maxDD `-4.2072`
- `market_context_high->metal_24h` score `0.4182` n `133` status `ready` deltaP `7.3687` edge `0.1948` maxDD `-2.3927`
- `market_context_high->crypto_alt_4h` score `0.4128` n `133` status `ready` deltaP `7.7423` edge `0.0945` maxDD `-3.9374`
- `market_context_high->equity_4h` score `0.3978` n `133` status `ready` deltaP `1.6636` edge `0.2312` maxDD `-6.9701`
- `market_context_high->index_1h` score `0.3794` n `133` status `ready` deltaP `8.9447` edge `0.015` maxDD `-0.7743`
- `market_context_high->fx_24h` score `0.328` n `132` status `ready` deltaP `17.8677` edge `0.0317` maxDD `-3.0343`
- `market_context_high->crypto_alt_1h` score `0.0921` n `133` status `ready` deltaP `3.8292` edge `0.0254` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `-0.1892` n `133` status `ready` deltaP `3.5449` edge `0.0065` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.2561` n `133` status `ready` deltaP `10.5585` edge `0.0426` maxDD `-1.3325`
- `market_context_high->commodity_4h` score `-0.3285` n `133` status `ready` deltaP `2.9523` edge `0.0123` maxDD `-1.0817`
- `market_context_high->fx_1h` score `-0.4759` n `133` status `ready` deltaP `-0.0767` edge `-0.0004` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.7788` n `133` status `ready` deltaP `2.3153` edge `0.02` maxDD `-0.6936`
- `market_context_high->metal_4h` score `-1.4515` n `133` status `ready` deltaP `1.2905` edge `0.0759` maxDD `-1.4368`
- `market_context_high->fx_4h` score `-1.4943` n `133` status `ready` deltaP `-4.1617` edge `-0.001` maxDD `-1.6936`
- `market_context_high->commodity_24h` score `-1.6805` n `132` status `ready` deltaP `5.6858` edge `-0.0196` maxDD `-7.0012`
- `market_context_high->unknown_1h` score `-2.244` n `133` status `ready` deltaP `-1.2741` edge `-0.1195` maxDD `-1.054`
- `market_context_high->index_24h` score `-2.4327` n `132` status `ready` deltaP `-17.5826` edge `0.0156` maxDD `-2.1544`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
