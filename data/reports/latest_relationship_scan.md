# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T16:37:21.615672+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5374`

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

- `market_context_high->unknown_4h` score `33.5401` n `113` status `ready` deltaP `-0.4439` edge `2.8315` maxDD `-1.016`
- `market_context_high->fx_1h` score `-0.042` n `113` status `ready` deltaP `4.0088` edge `0.0028` maxDD `-0.1258`
- `market_context_high->fx_4h` score `-0.0427` n `113` status `ready` deltaP `7.1539` edge `0.0086` maxDD `-0.4545`
- `market_context_high->commodity_24h` score `-0.1663` n `64` status `ready` deltaP `6.0764` edge `0.0374` maxDD `-3.6055`
- `market_context_high->commodity_1h` score `-0.4918` n `113` status `ready` deltaP `-0.0331` edge `0.0093` maxDD `-1.0053`
- `market_context_high->metal_1h` score `-0.6395` n `113` status `ready` deltaP `4.6341` edge `-0.005` maxDD `-1.6682`
- `market_context_high->index_1h` score `-0.6931` n `113` status `ready` deltaP `-2.635` edge `-0.0061` maxDD `-1.2155`
- `market_context_high->commodity_4h` score `-0.7944` n `113` status `ready` deltaP `-1.6283` edge `0.0319` maxDD `-1.165`
- `market_context_high->crypto_major_1h` score `-1.3589` n `113` status `ready` deltaP `2.6482` edge `-0.0338` maxDD `-9.3126`
- `market_context_high->fx_24h` score `-1.3973` n `64` status `ready` deltaP `4.5139` edge `0.0107` maxDD `-1.2451`
- `market_context_high->crypto_major_24h` score `-1.448` n `64` status `ready` deltaP `-3.9931` edge `0.0085` maxDD `-4.5369`
- `market_context_high->metal_4h` score `-1.894` n `113` status `ready` deltaP `4.7661` edge `-0.0186` maxDD `-5.3474`
- `market_context_high->index_24h` score `-1.9695` n `64` status `ready` deltaP `-0.5208` edge `-0.1208` maxDD `-4.925`
- `market_context_high->index_4h` score `-2.1886` n `113` status `ready` deltaP `-8.3774` edge `-0.0373` maxDD `-4.3282`
- `market_context_high->crypto_alt_1h` score `-3.1858` n `113` status `ready` deltaP `-2.0097` edge `-0.0647` maxDD `-11.3243`
- `market_context_high->metal_24h` score `-3.4236` n `64` status `ready` deltaP `-7.4653` edge `0.0315` maxDD `-7.3625`
- `market_context_high->equity_1h` score `-3.9242` n `113` status `ready` deltaP `-0.9883` edge `-0.0931` maxDD `-12.1865`
- `market_context_high->crypto_alt_24h` score `-7.2041` n `64` status `ready` deltaP `-2.6042` edge `-0.2606` maxDD `-42.3182`
- `market_context_high->crypto_major_4h` score `-9.9632` n `113` status `ready` deltaP `-12.7428` edge `-0.2455` maxDD `-32.9851`
- `market_context_high->equity_24h` score `-11.3673` n `64` status `ready` deltaP `-15.9722` edge `-0.8225` maxDD `-36.6024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
