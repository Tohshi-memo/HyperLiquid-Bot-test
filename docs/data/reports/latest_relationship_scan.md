# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T01:24:40.379951+00:00`
- Price records: `672`
- Market context records: `7621`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14551`

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

- `market_context_high->equity_24h` score `0.7755` n `145` status `ready` deltaP `16.9771` edge `0.4768` maxDD `-34.5784`
- `market_context_high->unknown_24h` score `0.3592` n `146` status `ready` deltaP `10.8376` edge `0.0757` maxDD `-4.775`
- `market_context_high->commodity_24h` score `0.0715` n `145` status `ready` deltaP `13.9361` edge `0.0714` maxDD `-7.0012`
- `market_context_high->index_1h` score `0.064` n `146` status `ready` deltaP `6.8123` edge `0.0107` maxDD `-0.8324`
- `market_context_high->crypto_major_1h` score `-0.197` n `146` status `ready` deltaP `7.5568` edge `0.0204` maxDD `-4.0162`
- `market_context_high->crypto_alt_1h` score `-0.242` n `146` status `ready` deltaP `1.9051` edge `0.0195` maxDD `-2.7243`
- `market_context_high->commodity_1h` score `-0.2906` n `146` status `ready` deltaP `3.1798` edge `-0.0014` maxDD `-1.5641`
- `market_context_high->fx_24h` score `-0.3467` n `145` status `ready` deltaP `9.2803` edge `0.018` maxDD `-3.0343`
- `market_context_high->commodity_4h` score `-0.3587` n `146` status `ready` deltaP `4.8176` edge `0.0125` maxDD `-2.2943`
- `market_context_high->equity_1h` score `-0.4932` n `146` status `ready` deltaP `5.677` edge `0.0503` maxDD `-7.7764`
- `market_context_high->index_4h` score `-0.6129` n `146` status `ready` deltaP `9.3691` edge `0.0291` maxDD `-3.2774`
- `market_context_high->metal_1h` score `-0.6419` n `146` status `ready` deltaP `1.2386` edge `0.014` maxDD `-1.0307`
- `market_context_high->fx_1h` score `-0.663` n `146` status `ready` deltaP `-0.5718` edge `-0.0015` maxDD `-0.6615`
- `market_context_high->crypto_alt_4h` score `-0.9535` n `146` status `ready` deltaP `3.0446` edge `0.0564` maxDD `-9.5815`
- `market_context_high->crypto_major_4h` score `-1.198` n `146` status `ready` deltaP `8.0646` edge `0.0604` maxDD `-14.4206`
- `market_context_high->unknown_1h` score `-1.4343` n `146` status `ready` deltaP `-0.2358` edge `-0.0556` maxDD `-1.3217`
- `market_context_high->equity_4h` score `-1.4844` n `146` status `ready` deltaP `2.214` edge `0.2093` maxDD `-20.4824`
- `market_context_high->metal_4h` score `-1.6299` n `146` status `ready` deltaP `-1.2133` edge `0.0448` maxDD `-4.6535`
- `market_context_high->metal_24h` score `-1.9774` n `146` status `ready` deltaP `-3.2772` edge `0.094` maxDD `-7.3868`
- `market_context_high->fx_4h` score `-2.5752` n `146` status `ready` deltaP `-6.3529` edge `-0.0038` maxDD `-2.1425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
