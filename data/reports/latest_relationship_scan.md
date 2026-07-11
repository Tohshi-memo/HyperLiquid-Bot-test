# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T03:37:28.818759+00:00`
- Price records: `672`
- Market context records: `6351`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11134`

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

- `news_risk_high->crypto_alt_24h` score `15.0725` n `32` status `ready` deltaP `42.0139` edge `0.9907` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.1605` n `32` status `ready` deltaP `51.0417` edge `0.1731` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.4455` n `32` status `ready` deltaP `17.5347` edge `0.531` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `4.1022` n `32` status `ready` deltaP `42.6067` edge `0.0624` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.7012` n `32` status `ready` deltaP `32.2917` edge `0.1137` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.3632` n `32` status `ready` deltaP `28.4431` edge `0.0212` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.5185` n `32` status `ready` deltaP `14.8765` edge `0.1422` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.9003` n `32` status `ready` deltaP `11.4708` edge `0.0851` maxDD `-1.6923`
- `market_context_high->metal_4h` score `0.6743` n `197` status `ready` deltaP `14.0019` edge `0.0425` maxDD `-2.7056`
- `market_context_high->unknown_1h` score `0.0218` n `209` status `ready` deltaP `-7.4807` edge `0.1525` maxDD `-3.7317`
- `market_context_high->index_4h` score `-0.029` n `197` status `ready` deltaP `6.438` edge `0.0223` maxDD `-0.4108`
- `market_context_high->metal_1h` score `-0.5973` n `209` status `ready` deltaP `3.8235` edge `0.0025` maxDD `-1.8877`
- `market_context_high->commodity_24h` score `-0.5973` n `129` status `ready` deltaP `-4.7965` edge `0.1418` maxDD `-6.2457`
- `market_context_high->commodity_1h` score `-0.6534` n `209` status `ready` deltaP `-2.1237` edge `-0.0013` maxDD `-2.1314`
- `market_context_high->metal_24h` score `-0.7035` n `129` status `ready` deltaP `13.8687` edge `0.0742` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.7132` n `32` status `ready` deltaP `0.3472` edge `-0.0066` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.7146` n `209` status `ready` deltaP `-0.6239` edge `-0.002` maxDD `-0.9376`
- `news_risk_high->metal_1h` score `-0.773` n `32` status `ready` deltaP `-3.5928` edge `-0.0254` maxDD `-1.6464`
- `news_risk_high->unknown_1h` score `-0.7959` n `32` status `ready` deltaP `5.4828` edge `-0.0684` maxDD `-0.7581`
- `market_context_high->crypto_alt_1h` score `-0.9699` n `209` status `ready` deltaP `5.2058` edge `0.0162` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
