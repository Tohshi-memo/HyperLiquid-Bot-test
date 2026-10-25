# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T02:07:25.299787+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7284`

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

- `market_context_high->unknown_4h` score `37.9605` n `95` status `ready` deltaP `0.8408` edge `3.1913` maxDD `-1.016`
- `market_context_high->commodity_24h` score `1.5505` n `50` status `ready` deltaP `20.6111` edge `0.0827` maxDD `-3.6055`
- `market_context_high->commodity_4h` score `0.5004` n `95` status `ready` deltaP `7.4888` edge `0.048` maxDD `-1.165`
- `market_context_high->commodity_1h` score `-0.293` n `107` status `ready` deltaP `2.3323` edge `0.0101` maxDD `-1.0053`
- `market_context_high->fx_1h` score `-0.3307` n `107` status `ready` deltaP `-1.3977` edge `0.0024` maxDD `-0.1712`
- `market_context_high->fx_4h` score `-0.6694` n `95` status `ready` deltaP `-4.4977` edge `0.0043` maxDD `-0.4771`
- `market_context_high->metal_1h` score `-0.9872` n `107` status `ready` deltaP `0.3987` edge `-0.0055` maxDD `-1.6873`
- `market_context_high->index_1h` score `-1.0912` n `107` status `ready` deltaP `-2.7814` edge `-0.0072` maxDD `-1.2155`
- `market_context_high->fx_24h` score `-1.1389` n `50` status `ready` deltaP `-2.2083` edge `-0.0008` maxDD `-1.3509`
- `market_context_high->crypto_major_1h` score `-1.3582` n `107` status `ready` deltaP `3.0444` edge `-0.0279` maxDD `-9.9883`
- `market_context_high->crypto_major_24h` score `-1.3834` n `50` status `ready` deltaP `4.5278` edge `0.0074` maxDD `-12.5288`
- `market_context_high->equity_1h` score `-2.555` n `107` status `ready` deltaP `-0.3498` edge `-0.0931` maxDD `-12.5703`
- `market_context_high->metal_4h` score `-2.9434` n `95` status `ready` deltaP `-5.6017` edge `-0.0305` maxDD `-5.862`
- `market_context_high->metal_24h` score `-3.0466` n `50` status `ready` deltaP `-9.5208` edge `-0.0002` maxDD `-6.8838`
- `market_context_high->crypto_alt_1h` score `-3.2535` n `107` status `ready` deltaP `-0.277` edge `-0.0595` maxDD `-13.782`
- `market_context_high->index_4h` score `-4.4813` n `95` status `ready` deltaP `-18.9731` edge `-0.0506` maxDD `-5.0415`
- `market_context_high->crypto_alt_24h` score `-4.5224` n `50` status `ready` deltaP `7.7361` edge `-0.0814` maxDD `-38.3305`
- `market_context_high->index_24h` score `-7.4088` n `50` status `ready` deltaP `-37.0417` edge `-0.1826` maxDD `-6.3616`
- `market_context_high->unknown_1h` score `-7.8377` n `107` status `ready` deltaP `1.3725` edge `-0.6134` maxDD `-1.5781`
- `market_context_high->crypto_major_4h` score `-11.9894` n `95` status `ready` deltaP `-19.1255` edge `-0.2849` maxDD `-40.2702`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
