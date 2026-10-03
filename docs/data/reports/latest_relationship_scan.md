# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T07:07:29.470860+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4826`

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

- `market_context_high->unknown_1h` score `366.199` n `50` status `ready` deltaP `11.024` edge `30.448` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `293.6984` n `50` status `ready` deltaP `11.8902` edge `24.3956` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `11.9754` n `50` status `ready` deltaP `24.8681` edge `1.0025` maxDD `-11.6271`
- `news_risk_high->equity_24h` score `10.8638` n `70` status `ready` deltaP `33.7351` edge `0.7289` maxDD `-2.8784`
- `market_context_high->crypto_major_24h` score `9.5074` n `50` status `ready` deltaP `32.5208` edge `0.7171` maxDD `-9.3299`
- `news_risk_high->crypto_major_4h` score `9.2771` n `81` status `ready` deltaP `36.5872` edge `0.5495` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.581` n `81` status `ready` deltaP `30.4445` edge `0.5632` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.3109` n `50` status `ready` deltaP `16.9329` edge `0.5667` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.9693` n `50` status `ready` deltaP `16.4939` edge `0.5164` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.1052` n `70` status `ready` deltaP `33.0407` edge `0.1377` maxDD `-0.2696`
- `news_risk_high->equity_4h` score `3.888` n `81` status `ready` deltaP `30.4747` edge `0.1821` maxDD `-2.9013`
- `market_context_high->crypto_alt_1h` score `3.2638` n `50` status `ready` deltaP `14.8024` edge `0.2396` maxDD `-3.6376`
- `market_context_high->crypto_major_1h` score `2.9701` n `50` status `ready` deltaP `13.2515` edge `0.2042` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.8677` n `50` status `ready` deltaP `32.0793` edge `0.0386` maxDD `-0.0791`
- `news_risk_high->crypto_major_1h` score `2.6307` n `81` status `ready` deltaP `13.449` edge `0.1651` maxDD `-1.5096`
- `news_risk_high->metal_4h` score `2.0405` n `81` status `ready` deltaP `17.7187` edge `0.0935` maxDD `-0.993`
- `news_risk_high->crypto_alt_24h` score `1.782` n `70` status `ready` deltaP `6.5824` edge `0.5793` maxDD `-24.2447`
- `news_risk_high->crypto_alt_1h` score `1.601` n `81` status `ready` deltaP `6.8271` edge `0.1398` maxDD `-2.4854`
- `news_risk_high->index_4h` score `1.5002` n `81` status `ready` deltaP `20.2932` edge `0.0451` maxDD `-0.4296`
- `market_context_high->fx_1h` score `1.4484` n `50` status `ready` deltaP `20.3413` edge `0.0115` maxDD `-0.113`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
