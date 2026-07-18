# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T15:10:11.083594+00:00`
- Price records: `672`
- Market context records: `7152`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11762`

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

- `market_context_high->fx_4h` score `0.3703` n `152` status `ready` deltaP `13.1338` edge `0.0133` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.1755` n `160` status `ready` deltaP `4.1991` edge `0.0025` maxDD `-0.276`
- `market_context_high->unknown_1h` score `-0.4632` n `160` status `ready` deltaP `-1.0816` edge `0.0328` maxDD `-1.4688`
- `market_context_high->crypto_alt_1h` score `-0.5978` n `160` status `ready` deltaP `0.0973` edge `0.0266` maxDD `-5.9775`
- `market_context_high->crypto_major_1h` score `-0.6125` n `160` status `ready` deltaP `3.8735` edge `0.0367` maxDD `-7.6171`
- `market_context_high->commodity_1h` score `-0.7194` n `160` status `ready` deltaP `-2.0172` edge `-0.0167` maxDD `-1.9668`
- `market_context_high->index_1h` score `-0.7729` n `160` status `ready` deltaP `1.0142` edge `-0.0047` maxDD `-2.3175`
- `market_context_high->metal_1h` score `-1.4564` n `160` status `ready` deltaP `-6.0367` edge `-0.005` maxDD `-2.0897`
- `market_context_high->unknown_4h` score `-1.8204` n `152` status `ready` deltaP `-6.1216` edge `0.0142` maxDD `-5.8754`
- `market_context_high->commodity_4h` score `-2.0664` n `152` status `ready` deltaP `-4.6453` edge `-0.0377` maxDD `-2.9494`
- `market_context_high->metal_4h` score `-2.9159` n `152` status `ready` deltaP `-10.061` edge `-0.0119` maxDD `-5.2551`
- `market_context_high->equity_1h` score `-3.529` n `160` status `ready` deltaP `-0.4379` edge `-0.0419` maxDD `-15.2742`
- `market_context_high->index_4h` score `-3.9255` n `152` status `ready` deltaP `-1.8934` edge `-0.0446` maxDD `-12.2591`
- `market_context_high->commodity_24h` score `-4.5024` n `133` status `ready` deltaP `-13.4581` edge `-0.1546` maxDD `-4.4704`
- `market_context_high->fx_24h` score `-4.9748` n `133` status `ready` deltaP `-15.8782` edge `-0.026` maxDD `-3.9503`
- `market_context_high->crypto_major_4h` score `-5.0334` n `152` status `ready` deltaP `1.5885` edge `0.0053` maxDD `-25.1605`
- `market_context_high->crypto_alt_4h` score `-5.5999` n `152` status `ready` deltaP `-3.811` edge `-0.0347` maxDD `-24.5243`
- `market_context_high->unknown_24h` score `-10.1004` n `133` status `ready` deltaP `-32.7029` edge `-0.109` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-14.6006` n `152` status `ready` deltaP `-4.2121` edge `-0.227` maxDD `-65.9309`
- `market_context_high->metal_24h` score `-14.6989` n `133` status `ready` deltaP `-31.6024` edge `-0.1961` maxDD `-40.7836`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
