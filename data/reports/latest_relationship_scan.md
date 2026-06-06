# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T22:52:23.067162+00:00`
- Price records: `672`
- Market context records: `3120`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7023`

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

- `market_context_high->commodity_24h` score `14.6099` n `98` status `ready` deltaP `46.8927` edge `0.9477` maxDD `-2.0927`
- `market_context_high->unknown_24h` score `12.297` n `98` status `ready` deltaP `21.3223` edge `0.9314` maxDD `-1.9039`
- `market_context_high->crypto_alt_24h` score `12.0762` n `98` status `ready` deltaP `10.8205` edge `2.3407` maxDD `-60.5022`
- `market_context_high->index_24h` score `6.6045` n `98` status `ready` deltaP `31.5866` edge `0.8916` maxDD `-16.1026`
- `market_context_high->equity_24h` score `4.9455` n `98` status `ready` deltaP `12.7587` edge `1.3144` maxDD `-50.2332`
- `market_context_high->commodity_4h` score `2.9996` n `124` status `ready` deltaP `18.4894` edge `0.1725` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `0.0105` n `136` status `ready` deltaP `2.4657` edge `0.0267` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.4586` n `136` status `ready` deltaP `4.3017` edge `0.0188` maxDD `-4.5023`
- `market_context_high->fx_24h` score `-0.533` n `98` status `ready` deltaP `4.3722` edge `-0.0008` maxDD `-0.4876`
- `market_context_high->crypto_alt_1h` score `-0.797` n `136` status `ready` deltaP `2.8311` edge `0.0919` maxDD `-14.7034`
- `market_context_high->equity_1h` score `-1.07` n `136` status `ready` deltaP `0.2994` edge `0.0094` maxDD `-8.8863`
- `market_context_high->fx_1h` score `-1.1277` n `136` status `ready` deltaP `-10.7168` edge `-0.0056` maxDD `-0.736`
- `market_context_high->index_4h` score `-1.3524` n `124` status `ready` deltaP `10.5478` edge `0.0472` maxDD `-17.6057`
- `market_context_high->fx_4h` score `-1.4168` n `124` status `ready` deltaP `-13.6015` edge `-0.0066` maxDD `-1.0829`
- `market_context_high->crypto_major_1h` score `-2.1481` n `136` status `ready` deltaP `-0.7529` edge `0.0523` maxDD `-15.1032`
- `market_context_high->metal_1h` score `-2.2313` n `136` status `ready` deltaP `-5.966` edge `-0.0068` maxDD `-7.4828`
- `market_context_high->unknown_4h` score `-2.4938` n `124` status `ready` deltaP `2.2276` edge `-0.0083` maxDD `-14.4824`
- `market_context_high->unknown_1h` score `-2.9096` n `136` status `ready` deltaP `2.426` edge `-0.056` maxDD `-14.2111`
- `market_context_high->crypto_alt_4h` score `-3.7506` n `124` status `ready` deltaP `13.4146` edge `0.2342` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-3.8763` n `124` status `ready` deltaP `7.3662` edge `-0.0155` maxDD `-36.7784`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
