# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T05:37:36.016334+00:00`
- Price records: `672`
- Market context records: `5322`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9648`

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

- `market_context_high->unknown_24h` score `19.0305` n `153` status `ready` deltaP `22.8247` edge `1.4427` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `6.9812` n `153` status `ready` deltaP `24.52` edge `0.8333` maxDD `-26.5332`
- `market_context_high->equity_24h` score `5.0678` n `153` status `ready` deltaP `18.75` edge `0.8602` maxDD `-40.0306`
- `market_context_high->crypto_alt_4h` score `2.9751` n `194` status `ready` deltaP `11.7315` edge `0.3338` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `2.9547` n `194` status `ready` deltaP `13.0312` edge `0.3886` maxDD `-14.0065`
- `market_context_high->equity_4h` score `2.173` n `194` status `ready` deltaP `11.6168` edge `0.2675` maxDD `-7.4425`
- `market_context_high->equity_1h` score `0.5446` n `194` status `ready` deltaP `8.6117` edge `0.0845` maxDD `-5.0555`
- `market_context_high->index_24h` score `0.524` n `153` status `ready` deltaP `22.212` edge `0.0826` maxDD `-7.413`
- `market_context_high->fx_24h` score `0.497` n `153` status `ready` deltaP `13.1331` edge `0.0434` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.0626` n `194` status `ready` deltaP `2.3952` edge `0.0854` maxDD `-5.0257`
- `market_context_high->index_1h` score `0.037` n `194` status `ready` deltaP `6.218` edge `0.012` maxDD `-1.0296`
- `market_context_high->crypto_major_1h` score `0.0047` n `194` status `ready` deltaP `4.6407` edge `0.094` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.2766` n `194` status `ready` deltaP `3.1437` edge `0.0111` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.3283` n `194` status `ready` deltaP `1.014` edge `0.0001` maxDD `-0.5823`
- `market_context_high->index_4h` score `-0.4236` n `194` status `ready` deltaP `5.4595` edge `0.0252` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.5924` n `194` status `ready` deltaP `3.3552` edge `0.0046` maxDD `-1.567`
- `market_context_high->unknown_4h` score `-1.0639` n `194` status `ready` deltaP `9.4324` edge `-0.0333` maxDD `-6.126`
- `market_context_high->commodity_1h` score `-1.4084` n `194` status `ready` deltaP `-2.8767` edge `-0.0064` maxDD `-3.3428`
- `market_context_high->metal_4h` score `-2.2708` n `194` status `ready` deltaP `-5.3951` edge `-0.0027` maxDD `-12.8631`
- `market_context_high->crypto_alt_24h` score `-3.2648` n `153` status `ready` deltaP `12.8268` edge `0.3369` maxDD `-53.6115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
