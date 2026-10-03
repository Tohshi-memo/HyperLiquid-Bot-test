# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T06:22:27.323144+00:00`
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

- `market_context_high->unknown_1h` score `366.1786` n `50` status `ready` deltaP `11.024` edge `30.4463` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `293.5958` n `50` status `ready` deltaP `11.4329` edge `24.3901` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `11.7825` n `50` status `ready` deltaP `24.3472` edge `0.9899` maxDD `-11.6271`
- `news_risk_high->equity_24h` score `10.7714` n `70` status `ready` deltaP `33.7351` edge `0.7212` maxDD `-2.8784`
- `market_context_high->crypto_major_24h` score `9.3385` n `50` status `ready` deltaP `32.0` edge `0.7065` maxDD `-9.3299`
- `news_risk_high->crypto_major_4h` score `9.031` n `84` status `ready` deltaP `35.6853` edge `0.535` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.6833` n `84` status `ready` deltaP `31.0177` edge `0.5679` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.2879` n `50` status `ready` deltaP `16.7805` edge `0.5658` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.9333` n `50` status `ready` deltaP `16.4939` edge `0.5134` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.0044` n `70` status `ready` deltaP `33.0407` edge `0.1293` maxDD `-0.2696`
- `news_risk_high->equity_4h` score `3.8314` n `84` status `ready` deltaP `30.5024` edge `0.1772` maxDD `-2.9013`
- `market_context_high->crypto_alt_1h` score `3.2194` n `50` status `ready` deltaP `14.503` edge `0.2379` maxDD `-3.6376`
- `news_risk_high->crypto_alt_24h` score `3.2119` n `70` status `ready` deltaP `10.3472` edge `0.6701` maxDD `-19.8504`
- `market_context_high->crypto_major_1h` score `2.9378` n `50` status `ready` deltaP `12.9521` edge `0.2035` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.8299` n `50` status `ready` deltaP `31.622` edge `0.0385` maxDD `-0.0791`
- `news_risk_high->crypto_major_1h` score `2.579` n `84` status `ready` deltaP `13.2378` edge `0.1622` maxDD `-1.5096`
- `news_risk_high->metal_4h` score `1.848` n `84` status `ready` deltaP `15.6867` edge `0.091` maxDD `-0.993`
- `news_risk_high->crypto_alt_1h` score `1.6365` n `84` status `ready` deltaP `6.8363` edge `0.1427` maxDD `-2.4854`
- `market_context_high->fx_1h` score `1.4352` n `50` status `ready` deltaP `20.1916` edge `0.0114` maxDD `-0.113`
- `news_risk_high->equity_1h` score `1.343` n `84` status `ready` deltaP `13.6655` edge `0.057` maxDD `-0.8948`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
