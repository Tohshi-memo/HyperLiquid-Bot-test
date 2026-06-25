# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-25T18:07:35.011274+00:00`
- Price records: `672`
- Market context records: `4747`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7470`

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

- `market_context_high->unknown_1h` score `83.1099` n `136` status `ready` deltaP `13.7681` edge `6.8758` maxDD `-1.674`
- `market_context_high->unknown_4h` score `5.1881` n `133` status `ready` deltaP `12.2227` edge `0.4719` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `3.1878` n `124` status `ready` deltaP `15.7482` edge `0.253` maxDD `-4.7201`
- `market_context_high->index_4h` score `-0.372` n `133` status `ready` deltaP `7.7527` edge `0.0075` maxDD `-5.5505`
- `market_context_high->commodity_1h` score `-0.5` n `136` status `ready` deltaP `2.2851` edge `0.0227` maxDD `-2.0345`
- `market_context_high->equity_4h` score `-0.5073` n `133` status `ready` deltaP `6.5331` edge `0.06` maxDD `-8.8203`
- `market_context_high->equity_1h` score `-0.9274` n `136` status `ready` deltaP `-1.3341` edge `-0.0148` maxDD `-5.2828`
- `market_context_high->fx_4h` score `-0.9403` n `133` status `ready` deltaP `-1.5438` edge `-0.0034` maxDD `-1.882`
- `market_context_high->fx_1h` score `-1.2331` n `136` status `ready` deltaP `-4.6583` edge `-0.0052` maxDD `-0.9869`
- `market_context_high->index_1h` score `-1.5082` n `136` status `ready` deltaP `-2.6946` edge `-0.0073` maxDD `-2.6999`
- `market_context_high->commodity_4h` score `-1.6046` n `133` status `ready` deltaP `6.9824` edge `0.0168` maxDD `-9.0989`
- `market_context_high->commodity_24h` score `-2.4896` n `124` status `ready` deltaP `17.5347` edge `0.0748` maxDD `-27.5371`
- `market_context_high->metal_1h` score `-2.5051` n `136` status `ready` deltaP `-2.8751` edge `-0.069` maxDD `-15.3067`
- `market_context_high->crypto_alt_1h` score `-2.6502` n `136` status `ready` deltaP `-0.1365` edge `-0.041` maxDD `-19.8288`
- `market_context_high->crypto_major_1h` score `-3.16` n `136` status `ready` deltaP `0.6252` edge `-0.0662` maxDD `-24.7815`
- `market_context_high->fx_24h` score `-4.3155` n `124` status `ready` deltaP `-14.6057` edge `-0.0203` maxDD `-4.6897`
- `market_context_high->crypto_alt_4h` score `-5.7279` n `133` status `ready` deltaP `1.4534` edge `-0.0485` maxDD `-50.3098`
- `market_context_high->index_24h` score `-7.2104` n `124` status `ready` deltaP `-11.1` edge `-0.1065` maxDD `-23.629`
- `market_context_high->crypto_major_4h` score `-8.4213` n `133` status `ready` deltaP `1.7788` edge `-0.155` maxDD `-69.5875`
- `market_context_high->metal_4h` score `-8.4656` n `133` status `ready` deltaP `2.8562` edge `-0.2803` maxDD `-61.2596`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
