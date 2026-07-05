# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T18:37:26.832671+00:00`
- Price records: `672`
- Market context records: `5800`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9058`

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

- `market_context_high->equity_24h` score `0.4889` n `248` status `ready` deltaP `15.3954` edge `0.446` maxDD `-31.6316`
- `market_context_high->equity_4h` score `-0.0671` n `299` status `ready` deltaP `6.1006` edge `0.1176` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2422` n `299` status `ready` deltaP `2.4733` edge `0.001` maxDD `-0.5499`
- `market_context_high->equity_1h` score `-0.6215` n `299` status `ready` deltaP `3.2699` edge `0.0271` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.6294` n `299` status `ready` deltaP `0.368` edge `0.0037` maxDD `-0.9472`
- `market_context_high->metal_1h` score `-0.6303` n `299` status `ready` deltaP `2.3842` edge `-0.0009` maxDD `-2.0682`
- `market_context_high->commodity_1h` score `-0.7827` n `299` status `ready` deltaP `-2.1995` edge `-0.0052` maxDD `-3.7721`
- `market_context_high->crypto_major_1h` score `-0.9198` n `299` status `ready` deltaP `3.2028` edge `0.0341` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-1.1217` n `299` status `ready` deltaP `1.451` edge `0.0303` maxDD `-6.6758`
- `market_context_high->fx_24h` score `-1.2092` n `248` status `ready` deltaP `12.4272` edge `0.0361` maxDD `-4.918`
- `market_context_high->index_4h` score `-1.2127` n `299` status `ready` deltaP `0.4879` edge `0.01` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.4576` n `299` status `ready` deltaP `0.6495` edge `0.0037` maxDD `-2.2593`
- `market_context_high->commodity_4h` score `-2.2499` n `299` status `ready` deltaP `-2.9678` edge `-0.0239` maxDD `-12.2474`
- `market_context_high->metal_4h` score `-2.4352` n `299` status `ready` deltaP `-5.0157` edge `-0.047` maxDD `-11.208`
- `market_context_high->index_24h` score `-2.7987` n `248` status `ready` deltaP `3.7131` edge `0.0309` maxDD `-18.1572`
- `market_context_high->crypto_major_4h` score `-2.9011` n `299` status `ready` deltaP `7.7525` edge `0.1438` maxDD `-25.6458`
- `market_context_high->crypto_alt_4h` score `-4.515` n `299` status `ready` deltaP `5.5046` edge `0.0879` maxDD `-28.7346`
- `market_context_high->metal_24h` score `-6.5125` n `248` status `ready` deltaP `-6.6028` edge `-0.2473` maxDD `-24.4893`
- `market_context_high->crypto_major_24h` score `-9.2246` n `248` status `ready` deltaP `-0.3865` edge `-0.1918` maxDD `-30.9471`
- `market_context_high->commodity_24h` score `-10.2813` n `248` status `ready` deltaP `-13.8385` edge `-0.0778` maxDD `-37.604`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
