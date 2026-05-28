# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T02:52:17.616824+00:00`
- Price records: `672`
- Market context records: `2101`
- Flow alert records: `7942`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9146`

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

- `market_context_high->crypto_alt_4h` score `10.6429` n `180` status `ready` deltaP `31.1212` edge `0.7939` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `10.465` n `180` status `ready` deltaP `37.5271` edge `0.6749` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `5.7787` n `180` status `ready` deltaP `23.7263` edge `0.3983` maxDD `-2.6599`
- `market_context_high->equity_4h` score `4.1241` n `180` status `ready` deltaP `22.5644` edge `0.3027` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `2.5586` n `179` status `ready` deltaP `22.8992` edge `0.5926` maxDD `-35.8966`
- `market_context_high->index_4h` score `2.5314` n `180` status `ready` deltaP `18.872` edge `0.1535` maxDD `-1.8022`
- `market_context_high->index_24h` score `2.2798` n `179` status `ready` deltaP `11.6429` edge `0.2352` maxDD `-4.1604`
- `market_context_high->crypto_major_1h` score `2.223` n `180` status `ready` deltaP `15.835` edge `0.1783` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `2.0116` n `180` status `ready` deltaP `12.6913` edge `0.1944` maxDD `-4.9097`
- `market_context_high->equity_24h` score `1.603` n `179` status `ready` deltaP `22.8344` edge `0.4712` maxDD `-33.1875`
- `market_context_high->equity_1h` score `0.8542` n `180` status `ready` deltaP `10.998` edge `0.0767` maxDD `-2.6402`
- `market_context_high->metal_4h` score `0.709` n `180` status `ready` deltaP `14.9763` edge `0.1722` maxDD `-10.0364`
- `market_context_high->unknown_1h` score `0.2452` n `180` status `ready` deltaP `5.489` edge `0.0558` maxDD `-3.0902`
- `market_context_high->index_1h` score `0.1861` n `180` status `ready` deltaP `6.4272` edge `0.0317` maxDD `-1.3898`
- `market_context_high->crypto_major_24h` score `0.0369` n `179` status `ready` deltaP `20.9932` edge `0.7217` maxDD `-62.3533`
- `market_context_high->fx_24h` score `-0.1153` n `179` status `ready` deltaP `14.9089` edge `0.0303` maxDD `-2.811`
- `market_context_high->metal_1h` score `-0.1662` n `180` status `ready` deltaP `7.0093` edge `0.0415` maxDD `-5.166`
- `market_context_high->fx_1h` score `-0.8431` n `180` status `ready` deltaP `-1.3041` edge `0.0012` maxDD `-0.3548`
- `market_context_high->fx_4h` score `-1.0312` n `180` status `ready` deltaP `-6.294` edge `-0.0021` maxDD `-1.0513`
- `market_context_high->metal_24h` score `-1.0506` n `179` status `ready` deltaP `10.2704` edge `0.2341` maxDD `-23.2095`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
