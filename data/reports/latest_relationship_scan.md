# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T02:52:38.235139+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4818`

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

- `market_context_high->unknown_1h` score `364.9006` n `50` status `ready` deltaP `10.5749` edge `30.3428` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `293.1645` n `50` status `ready` deltaP `10.061` edge `24.3633` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `13.1531` n `70` status `ready` deltaP `27.9167` edge `0.9968` maxDD `-4.6123`
- `market_context_high->crypto_alt_24h` score `11.0457` n `50` status `ready` deltaP `21.9167` edge `0.9447` maxDD `-11.6271`
- `news_risk_high->equity_24h` score `10.229` n `70` status `ready` deltaP `33.7351` edge `0.676` maxDD `-2.8784`
- `market_context_high->crypto_major_24h` score `8.8954` n `50` status `ready` deltaP `31.3056` edge `0.6742` maxDD `-9.3299`
- `news_risk_high->crypto_alt_4h` score `7.9254` n `98` status `ready` deltaP `32.6188` edge `0.5774` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.3329` n `50` status `ready` deltaP `17.2378` edge `0.5665` maxDD `-3.294`
- `news_risk_high->crypto_major_24h` score `7.1254` n `70` status `ready` deltaP `12.1627` edge `0.6023` maxDD `-3.835`
- `news_risk_high->crypto_major_4h` score `6.8037` n `98` status `ready` deltaP `25.7684` edge `0.4455` maxDD `-2.025`
- `market_context_high->crypto_alt_4h` score `5.785` n `50` status `ready` deltaP `15.8841` edge `0.5051` maxDD `-7.6465`
- `news_risk_high->equity_4h` score `3.3672` n `98` status `ready` deltaP `27.9399` edge `0.1556` maxDD `-2.9013`
- `market_context_high->crypto_alt_1h` score `3.175` n `50` status `ready` deltaP `14.3533` edge `0.2352` maxDD `-3.6376`
- `market_context_high->crypto_major_1h` score `2.9881` n `50` status `ready` deltaP `13.4012` edge `0.2047` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.7787` n `50` status `ready` deltaP `31.0122` edge `0.0383` maxDD `-0.0791`
- `news_risk_high->index_24h` score `2.6128` n `70` status `ready` deltaP `24.256` edge `0.0844` maxDD `-0.2696`
- `news_risk_high->metal_24h` score `1.8386` n `70` status `ready` deltaP `9.6329` edge `0.195` maxDD `-2.1466`
- `news_risk_high->crypto_alt_1h` score `1.7274` n `98` status `ready` deltaP `7.537` edge `0.1456` maxDD `-2.4854`
- `news_risk_high->crypto_major_1h` score `1.4519` n `98` status `ready` deltaP `7.5645` edge `0.1293` maxDD `-2.0325`
- `market_context_high->fx_1h` score `1.4352` n `50` status `ready` deltaP `20.1916` edge `0.0114` maxDD `-0.113`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
