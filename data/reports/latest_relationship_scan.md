# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T11:52:33.993585+00:00`
- Price records: `672`
- Market context records: `5768`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8670`

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

- `market_context_high->equity_24h` score `0.7039` n `228` status `ready` deltaP `15.3052` edge `0.4961` maxDD `-31.6316`
- `market_context_high->equity_4h` score `0.158` n `285` status `ready` deltaP `7.4743` edge `0.1272` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.3799` n `297` status `ready` deltaP `2.301` edge `0.0011` maxDD `-0.5144`
- `market_context_high->metal_1h` score `-0.4164` n `297` status `ready` deltaP `2.2254` edge `-0.0007` maxDD `-2.0682`
- `market_context_high->equity_1h` score `-0.6232` n `297` status `ready` deltaP `3.2335` edge `0.0272` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.6515` n `297` status `ready` deltaP `-0.0569` edge `0.0037` maxDD `-0.9472`
- `market_context_high->commodity_1h` score `-0.7954` n `297` status `ready` deltaP `-2.3378` edge `-0.0059` maxDD `-3.7721`
- `market_context_high->fx_24h` score `-0.9094` n `228` status `ready` deltaP `14.9488` edge `0.0421` maxDD `-3.6674`
- `market_context_high->crypto_major_1h` score `-0.9165` n `297` status `ready` deltaP `3.3484` edge `0.0334` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-1.1148` n `297` status `ready` deltaP `1.6271` edge `0.0297` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.202` n `285` status `ready` deltaP `0.5894` edge `0.0107` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.2469` n `285` status `ready` deltaP `2.8156` edge `0.0059` maxDD `-1.4288`
- `market_context_high->metal_4h` score `-2.5545` n `285` status `ready` deltaP `-6.4569` edge `-0.0485` maxDD `-11.5426`
- `market_context_high->crypto_major_4h` score `-2.7369` n `285` status `ready` deltaP `7.8198` edge `0.1541` maxDD `-25.4113`
- `market_context_high->index_24h` score `-2.9306` n `228` status `ready` deltaP `1.4619` edge `0.029` maxDD `-18.1572`
- `market_context_high->commodity_4h` score `-3.7687` n `285` status `ready` deltaP `-2.7605` edge `-0.0281` maxDD `-14.071`
- `market_context_high->crypto_alt_4h` score `-4.1666` n `285` status `ready` deltaP `5.7146` edge `0.1031` maxDD `-27.7396`
- `market_context_high->crypto_major_24h` score `-5.1486` n `228` status `ready` deltaP `5.4368` edge `-0.0196` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.1104` n `228` status `ready` deltaP `-8.1689` edge `-0.2421` maxDD `-27.8689`
- `market_context_high->commodity_24h` score `-10.9668` n `228` status `ready` deltaP `-13.0574` edge `-0.0782` maxDD `-41.2254`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
