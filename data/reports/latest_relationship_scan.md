# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T12:07:29.546145+00:00`
- Price records: `672`
- Market context records: `4825`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7588`

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

- `market_context_high->unknown_1h` score `13.5837` n `110` status `ready` deltaP `12.1394` edge `1.0928` maxDD `-1.674`
- `market_context_high->unknown_4h` score `8.0795` n `110` status `ready` deltaP `17.4196` edge `0.6782` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `3.0672` n `103` status `ready` deltaP `15.8324` edge `0.2189` maxDD `-2.8416`
- `market_context_high->index_4h` score `0.8822` n `110` status `ready` deltaP `10.7677` edge `0.0484` maxDD `-0.7334`
- `market_context_high->equity_4h` score `0.8472` n `110` status `ready` deltaP `12.5804` edge `0.1629` maxDD `-6.3852`
- `market_context_high->commodity_4h` score `0.473` n `110` status `ready` deltaP `15.8038` edge `0.0725` maxDD `-4.377`
- `market_context_high->commodity_1h` score `0.2467` n `110` status `ready` deltaP `6.4698` edge `0.0256` maxDD `-1.1869`
- `market_context_high->equity_1h` score `0.0011` n `110` status `ready` deltaP `4.0855` edge `0.0345` maxDD `-2.928`
- `market_context_high->fx_4h` score `-0.4821` n `110` status `ready` deltaP `2.4335` edge `-0.0004` maxDD `-1.5439`
- `market_context_high->index_1h` score `-0.5019` n `110` status `ready` deltaP `0.4709` edge `0.008` maxDD `-0.7054`
- `market_context_high->fx_1h` score `-1.1006` n `110` status `ready` deltaP `-3.3696` edge `-0.0043` maxDD `-0.8626`
- `market_context_high->crypto_alt_1h` score `-1.8825` n `110` status `ready` deltaP `5.2831` edge `-0.0039` maxDD `-12.7225`
- `market_context_high->crypto_major_1h` score `-2.1165` n `110` status `ready` deltaP `3.2825` edge `-0.0357` maxDD `-17.9354`
- `market_context_high->metal_1h` score `-2.1326` n `110` status `ready` deltaP `0.2558` edge `-0.0648` maxDD `-13.4916`
- `market_context_high->fx_24h` score `-2.3706` n `103` status `ready` deltaP `-11.4162` edge `-0.0196` maxDD `-2.814`
- `market_context_high->commodity_24h` score `-2.4262` n `103` status `ready` deltaP `17.5247` edge `0.083` maxDD `-27.5371`
- `market_context_high->crypto_alt_4h` score `-3.7465` n `110` status `ready` deltaP `8.4922` edge `0.0082` maxDD `-38.2779`
- `market_context_high->index_24h` score `-3.9834` n `103` status `ready` deltaP `-2.9615` edge `-0.1001` maxDD `-23.2678`
- `market_context_high->crypto_major_4h` score `-7.2649` n `110` status `ready` deltaP `5.3188` edge `-0.1437` maxDD `-60.5192`
- `market_context_high->metal_4h` score `-8.6798` n `110` status `ready` deltaP `5.8038` edge `-0.341` maxDD `-60.1721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
