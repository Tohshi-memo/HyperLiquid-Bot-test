# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-29T15:52:31.383261+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6784`

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

- `market_context_high->unknown_24h` score `1597.4245` n `135` status `ready` deltaP `0.2084` edge `133.1603` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `65.2181` n `135` status `ready` deltaP `7.0099` edge `5.4014` maxDD `-0.3966`
- `market_context_high->index_24h` score `1.9478` n `135` status `ready` deltaP `24.919` edge `0.0145` maxDD `-0.1315`
- `market_context_high->metal_1h` score `0.2676` n `135` status `ready` deltaP `10.3227` edge `0.0096` maxDD `-0.5285`
- `market_context_high->commodity_4h` score `0.2135` n `135` status `ready` deltaP `12.701` edge `0.055` maxDD `-1.0837`
- `market_context_high->metal_4h` score `0.0649` n `135` status `ready` deltaP `13.1132` edge `0.013` maxDD `-2.0349`
- `market_context_high->fx_1h` score `-0.0742` n `135` status `ready` deltaP `4.0663` edge `-0.0008` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.2872` n `135` status `ready` deltaP `1.8596` edge `0.0151` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.3416` n `135` status `ready` deltaP `2.4831` edge `-0.0005` maxDD `-0.4545`
- `market_context_high->equity_1h` score `-0.3832` n `135` status `ready` deltaP `1.2453` edge `0.031` maxDD `-2.4074`
- `market_context_high->index_1h` score `-0.6984` n `135` status `ready` deltaP `-3.9632` edge `-0.0031` maxDD `-1.1344`
- `market_context_high->crypto_major_1h` score `-0.7134` n `135` status `ready` deltaP `4.6496` edge `0.0217` maxDD `-5.9715`
- `market_context_high->fx_24h` score `-0.8253` n `135` status `ready` deltaP `7.3496` edge `0.0153` maxDD `-0.9792`
- `market_context_high->crypto_alt_1h` score `-1.3685` n `135` status `ready` deltaP `1.4415` edge `0.0123` maxDD `-9.1219`
- `market_context_high->equity_4h` score `-1.5968` n `135` status `ready` deltaP `-2.4164` edge `-0.0229` maxDD `-6.5903`
- `market_context_high->metal_24h` score `-1.7737` n `135` status `ready` deltaP `3.5995` edge `0.0133` maxDD `-10.5088`
- `market_context_high->index_4h` score `-2.4459` n `135` status `ready` deltaP `-6.9682` edge `-0.0241` maxDD `-3.6614`
- `market_context_high->crypto_major_4h` score `-2.6764` n `135` status `ready` deltaP `4.5122` edge `-0.0382` maxDD `-19.4671`
- `market_context_high->equity_24h` score `-3.7201` n `135` status `ready` deltaP `7.1412` edge `-0.0819` maxDD `-14.0571`
- `market_context_high->commodity_24h` score `-4.7541` n `135` status `ready` deltaP `-1.1227` edge `-0.043` maxDD `-24.0547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
