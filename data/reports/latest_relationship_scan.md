# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T06:37:28.407945+00:00`
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

- `market_context_high->unknown_1h` score `366.1342` n `50` status `ready` deltaP `11.024` edge `30.4426` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `293.6128` n `50` status `ready` deltaP `11.5854` edge `24.3905` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `11.848` n `50` status `ready` deltaP `24.5208` edge `0.9942` maxDD `-11.6271`
- `news_risk_high->equity_24h` score `10.8002` n `70` status `ready` deltaP `33.7351` edge `0.7236` maxDD `-2.8784`
- `market_context_high->crypto_major_24h` score `9.3968` n `50` status `ready` deltaP `32.1736` edge `0.7102` maxDD `-9.3299`
- `news_risk_high->crypto_major_4h` score `9.0809` n `83` status `ready` deltaP `35.6799` edge `0.5392` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.6492` n `83` status `ready` deltaP `30.8312` edge `0.5663` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.3061` n `50` status `ready` deltaP `16.9329` edge `0.5663` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.9465` n `50` status `ready` deltaP `16.4939` edge `0.5145` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.038` n `70` status `ready` deltaP `33.0407` edge `0.1321` maxDD `-0.2696`
- `news_risk_high->equity_4h` score `3.8502` n `83` status `ready` deltaP `30.497` edge `0.1788` maxDD `-2.9013`
- `market_context_high->crypto_alt_1h` score `3.241` n `50` status `ready` deltaP `14.6527` edge `0.2387` maxDD `-3.6376`
- `market_context_high->crypto_major_1h` score `2.9546` n `50` status `ready` deltaP `13.1018` edge `0.2039` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.8421` n `50` status `ready` deltaP `31.7744` edge `0.0385` maxDD `-0.0791`
- `news_risk_high->crypto_alt_24h` score `2.7304` n `70` status `ready` deltaP `9.0922` edge `0.6391` maxDD `-21.3063`
- `news_risk_high->crypto_major_1h` score `2.5589` n `83` status `ready` deltaP `12.9572` edge `0.1624` maxDD `-1.5096`
- `news_risk_high->metal_4h` score `1.9184` n `83` status `ready` deltaP `16.4469` edge `0.0918` maxDD `-0.993`
- `news_risk_high->crypto_alt_1h` score `1.5771` n `83` status `ready` deltaP `6.484` edge `0.1401` maxDD `-2.4854`
- `market_context_high->fx_1h` score `1.4484` n `50` status `ready` deltaP `20.3413` edge `0.0115` maxDD `-0.113`
- `news_risk_high->equity_1h` score `1.3288` n `83` status `ready` deltaP `13.428` edge `0.0574` maxDD `-0.8948`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
