# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-18T03:37:26.159061+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10534`

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

- `risk_on_high->commodity_24h` score `6.3527` n `56` status `ready` deltaP `35.8014` edge `0.3016` maxDD `-0.2041`
- `risk_on_and_context->commodity_24h` score `6.3527` n `56` status `ready` deltaP `35.8014` edge `0.3016` maxDD `-0.2041`
- `market_context_high->crypto_major_4h` score `1.5058` n `162` status `ready` deltaP `15.3794` edge `0.3634` maxDD `-15.2359`
- `market_context_high->commodity_24h` score `1.055` n `116` status `ready` deltaP `15.2349` edge `0.149` maxDD `-6.6787`
- `market_context_high->crypto_major_1h` score `0.5035` n `162` status `ready` deltaP `4.2083` edge `0.1028` maxDD `-3.7781`
- `market_context_high->crypto_alt_1h` score `0.3652` n `162` status `ready` deltaP `8.2686` edge `0.1253` maxDD `-7.3329`
- `risk_on_high->crypto_major_4h` score `0.2017` n `91` status `ready` deltaP `13.609` edge `0.1832` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `0.2017` n `91` status `ready` deltaP `13.609` edge `0.1832` maxDD `-11.1788`
- `risk_on_high->index_1h` score `-0.0257` n `91` status `ready` deltaP `4.5556` edge `0.0059` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.0257` n `91` status `ready` deltaP `4.5556` edge `0.0059` maxDD `-0.7394`
- `market_context_high->index_1h` score `-0.1485` n `162` status `ready` deltaP `7.5742` edge `0.0053` maxDD `-1.3195`
- `risk_on_high->fx_1h` score `-0.2492` n `91` status `ready` deltaP `1.3481` edge `-0.0029` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.2492` n `91` status `ready` deltaP `1.3481` edge `-0.0029` maxDD `-0.376`
- `market_context_high->metal_1h` score `-0.3287` n `162` status `ready` deltaP `5.4447` edge `0.0085` maxDD `-0.9556`
- `market_context_high->metal_4h` score `-0.4153` n `162` status `ready` deltaP `8.4444` edge `0.0428` maxDD `-1.6961`
- `risk_on_high->equity_1h` score `-0.4332` n `91` status `ready` deltaP `9.4084` edge `0.0308` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.4332` n `91` status `ready` deltaP `9.4084` edge `0.0308` maxDD `-5.3696`
- `risk_on_high->metal_1h` score `-0.4938` n `91` status `ready` deltaP `0.8455` edge `0.0042` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4938` n `91` status `ready` deltaP `0.8455` edge `0.0042` maxDD `-0.8513`
- `market_context_high->fx_1h` score `-0.5325` n `162` status `ready` deltaP `-2.1522` edge `-0.0018` maxDD `-0.503`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
