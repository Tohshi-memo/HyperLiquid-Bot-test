# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T15:07:32.265055+00:00`
- Price records: `672`
- Market context records: `4734`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7448`

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

- `market_context_high->unknown_1h` score `79.3386` n `141` status `ready` deltaP `14.9414` edge `6.5537` maxDD `-1.674`
- `market_context_high->unknown_4h` score `5.2933` n `141` status `ready` deltaP `14.2277` edge `0.4673` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `3.4134` n `132` status `ready` deltaP `17.1875` edge `0.2622` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `-0.3269` n `141` status `ready` deltaP `2.1584` edge `0.0233` maxDD `-2.0345`
- `market_context_high->index_4h` score `-0.5767` n `141` status `ready` deltaP `5.2197` edge `0.0007` maxDD `-5.7542`
- `market_context_high->fx_4h` score `-0.874` n `141` status `ready` deltaP `-0.3946` edge `-0.002` maxDD `-1.9274`
- `market_context_high->equity_1h` score `-0.9279` n `141` status `ready` deltaP `-1.3632` edge `-0.0123` maxDD `-5.4726`
- `market_context_high->index_1h` score `-1.02` n `141` status `ready` deltaP `-3.459` edge `-0.0073` maxDD `-2.6999`
- `market_context_high->equity_4h` score `-1.0389` n `141` status `ready` deltaP `3.4434` edge `0.0166` maxDD `-8.8203`
- `market_context_high->fx_1h` score `-1.4121` n `141` status `ready` deltaP `-6.5412` edge `-0.0061` maxDD `-1.1038`
- `market_context_high->commodity_4h` score `-1.5195` n `141` status `ready` deltaP `8.6457` edge `0.0265` maxDD `-9.1941`
- `market_context_high->metal_1h` score `-2.7464` n `141` status `ready` deltaP `-5.3829` edge `-0.0752` maxDD `-15.9475`
- `market_context_high->crypto_alt_1h` score `-2.8857` n `141` status `ready` deltaP `-0.0159` edge `-0.0553` maxDD `-21.1642`
- `market_context_high->crypto_major_1h` score `-3.5115` n `141` status `ready` deltaP `-0.4969` edge `-0.0728` maxDD `-27.2597`
- `market_context_high->commodity_24h` score `-4.2251` n `132` status `ready` deltaP `16.5878` edge `0.0621` maxDD `-28.6488`
- `market_context_high->fx_24h` score `-4.777` n `132` status `ready` deltaP `-14.3308` edge `-0.0197` maxDD `-5.2943`
- `market_context_high->crypto_alt_4h` score `-7.2153` n `141` status `ready` deltaP `-1.0574` edge `-0.107` maxDD `-59.5456`
- `market_context_high->index_24h` score `-8.2165` n `132` status `ready` deltaP `-11.9002` edge `-0.1056` maxDD `-27.3155`
- `market_context_high->metal_4h` score `-8.5656` n `141` status `ready` deltaP `1.6931` edge `-0.2598` maxDD `-62.6377`
- `market_context_high->crypto_major_4h` score `-10.123` n `141` status `ready` deltaP `-0.6465` edge `-0.2199` maxDD `-80.5555`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
