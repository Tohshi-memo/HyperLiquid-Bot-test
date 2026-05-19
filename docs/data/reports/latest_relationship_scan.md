# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T08:07:20.338430+00:00`
- Price records: `672`
- Market context records: `1201`
- Flow alert records: `5363`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8768`

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

- `market_context_high->crypto_major_24h` score `18.5525` n `134` status `ready` deltaP `44.2553` edge `1.3642` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `7.495` n `134` status `ready` deltaP `22.0668` edge `0.6791` maxDD `-15.1306`
- `market_context_high->unknown_4h` score `5.6441` n `134` status `ready` deltaP `3.8837` edge `0.5661` maxDD `-6.7322`
- `market_context_high->metal_24h` score `4.3011` n `134` status `ready` deltaP `-4.0889` edge `0.5524` maxDD `-6.3373`
- `market_context_high->commodity_24h` score `3.222` n `134` status `ready` deltaP `-3.5292` edge `0.58` maxDD `-18.0378`
- `market_context_high->equity_4h` score `2.7947` n `134` status `ready` deltaP `14.5682` edge `0.2021` maxDD `-3.6396`
- `market_context_high->index_24h` score `2.1106` n `134` status `ready` deltaP `16.9828` edge `0.1713` maxDD `-5.3574`
- `market_context_high->equity_24h` score `1.6533` n `134` status `ready` deltaP `17.2264` edge `0.3298` maxDD `-14.2815`
- `market_context_high->index_4h` score `0.9338` n `134` status `ready` deltaP `10.4273` edge `0.0766` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.4652` n `134` status `ready` deltaP `8.1687` edge `0.016` maxDD `-0.5353`
- `market_context_high->fx_24h` score `0.4177` n `134` status `ready` deltaP `8.6701` edge `0.0529` maxDD `-2.7379`
- `market_context_high->equity_1h` score `0.342` n `134` status `ready` deltaP `3.6844` edge `0.0417` maxDD `-1.3546`
- `market_context_high->crypto_major_4h` score `-0.0956` n `134` status `ready` deltaP `6.4593` edge `0.1368` maxDD `-8.3693`
- `market_context_high->fx_1h` score `-0.137` n `134` status `ready` deltaP `5.063` edge `0.0004` maxDD `-0.3124`
- `market_context_high->metal_1h` score `-0.2094` n `134` status `ready` deltaP `8.3386` edge `-0.012` maxDD `-2.2164`
- `market_context_high->crypto_major_1h` score `-0.3535` n `134` status `ready` deltaP `3.4275` edge `0.0084` maxDD `-4.1256`
- `market_context_high->crypto_alt_1h` score `-0.3738` n `134` status `ready` deltaP `0.7284` edge `0.0315` maxDD `-3.4088`
- `market_context_high->unknown_24h` score `-0.7593` n `134` status `ready` deltaP `1.4382` edge `0.2001` maxDD `-10.1706`
- `market_context_high->commodity_1h` score `-0.8316` n `134` status `ready` deltaP `-2.8376` edge `0.0111` maxDD `-2.252`
- `market_context_high->metal_4h` score `-0.972` n `134` status `ready` deltaP `8.3067` edge `-0.0369` maxDD `-6.4478`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
