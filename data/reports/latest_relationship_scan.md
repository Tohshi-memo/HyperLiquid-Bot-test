# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T08:37:27.136542+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4806`

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

- `market_context_high->unknown_1h` score `366.1282` n `50` status `ready` deltaP `10.8743` edge `30.4431` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `293.8606` n `50` status `ready` deltaP `12.0427` edge `24.4081` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `12.4919` n `50` status `ready` deltaP `25.9097` edge `1.0386` maxDD `-11.6271`
- `news_risk_high->equity_24h` score `10.5251` n `70` status `ready` deltaP `31.2252` edge `0.7174` maxDD `-2.8784`
- `market_context_high->crypto_major_24h` score `9.9291` n `50` status `ready` deltaP `33.5625` edge `0.7453` maxDD `-9.3299`
- `news_risk_high->crypto_major_4h` score `9.8047` n `75` status `ready` deltaP `37.5427` edge `0.5871` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.6475` n `75` status `ready` deltaP `30.0752` edge `0.5712` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.3777` n `50` status `ready` deltaP `17.5427` edge `0.5682` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `6.1541` n `50` status `ready` deltaP `17.4085` edge `0.5257` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.2324` n `70` status `ready` deltaP `33.0407` edge `0.1483` maxDD `-0.2696`
- `news_risk_high->equity_4h` score `3.9686` n `75` status `ready` deltaP `29.9979` edge `0.192` maxDD `-2.9013`
- `market_context_high->crypto_alt_1h` score `3.3225` n `50` status `ready` deltaP `15.2515` edge `0.2415` maxDD `-3.6376`
- `market_context_high->crypto_major_1h` score `3.0037` n `50` status `ready` deltaP `13.7006` edge `0.204` maxDD `-2.2692`
- `news_risk_high->crypto_major_1h` score `2.9951` n `75` status `ready` deltaP `15.0339` edge `0.1849` maxDD `-1.5096`
- `market_context_high->fx_4h` score `2.9311` n `50` status `ready` deltaP `32.8415` edge `0.0388` maxDD `-0.0791`
- `news_risk_high->index_4h` score `2.3429` n `75` status `ready` deltaP `26.4167` edge `0.0495` maxDD `-0.4296`
- `news_risk_high->metal_4h` score `2.2694` n `75` status `ready` deltaP `19.8293` edge `0.0985` maxDD `-0.993`
- `news_risk_high->crypto_alt_1h` score `1.9222` n `75` status `ready` deltaP `7.9182` edge `0.1593` maxDD `-2.4854`
- `market_context_high->fx_1h` score `1.4232` n `50` status `ready` deltaP `20.0419` edge `0.0114` maxDD `-0.113`
- `news_risk_high->equity_1h` score `1.3521` n `75` status `ready` deltaP `12.9242` edge `0.0627` maxDD `-0.8948`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
