# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T08:37:29.789506+00:00`
- Price records: `672`
- Market context records: `5334`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9522`

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

- `market_context_high->unknown_24h` score `18.9381` n `153` status `ready` deltaP `22.8247` edge `1.435` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `6.9752` n `153` status `ready` deltaP `24.52` edge `0.8328` maxDD `-26.5332`
- `market_context_high->equity_24h` score `4.9343` n `153` status `ready` deltaP `18.0556` edge `0.8537` maxDD `-40.0306`
- `market_context_high->crypto_major_4h` score `3.0343` n `194` status `ready` deltaP `13.3361` edge `0.3932` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `2.9681` n `194` status `ready` deltaP `11.8839` edge `0.3322` maxDD `-9.46`
- `market_context_high->equity_4h` score `2.1448` n `194` status `ready` deltaP `11.1594` edge `0.2682` maxDD `-7.4425`
- `market_context_high->index_24h` score `0.7169` n `153` status `ready` deltaP `24.1217` edge `0.0946` maxDD `-7.413`
- `market_context_high->equity_1h` score `0.5997` n `194` status `ready` deltaP `9.0608` edge `0.0861` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.3119` n `153` status `ready` deltaP `11.2234` edge `0.0407` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.1513` n `194` status `ready` deltaP `2.6946` edge `0.0908` maxDD `-5.0257`
- `market_context_high->index_1h` score `0.0909` n `194` status `ready` deltaP `6.8168` edge `0.0125` maxDD `-1.0296`
- `market_context_high->crypto_major_1h` score `0.0695` n `194` status `ready` deltaP `4.6407` edge `0.0994` maxDD `-6.9639`
- `market_context_high->fx_1h` score `-0.3205` n `194` status `ready` deltaP `1.1637` edge `0.0001` maxDD `-0.5823`
- `market_context_high->metal_1h` score `-0.3264` n `194` status `ready` deltaP `2.3952` edge `0.0097` maxDD `-2.0682`
- `market_context_high->index_4h` score `-0.3595` n `194` status `ready` deltaP `6.5266` edge `0.0263` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.5845` n `194` status `ready` deltaP `3.5076` edge `0.0046` maxDD `-1.567`
- `market_context_high->unknown_4h` score `-1.2723` n `194` status `ready` deltaP `7.908` edge `-0.0405` maxDD `-6.126`
- `market_context_high->commodity_1h` score `-1.4167` n `194` status `ready` deltaP `-3.0264` edge `-0.0061` maxDD `-3.3428`
- `market_context_high->metal_4h` score `-2.3465` n `194` status `ready` deltaP `-5.5475` edge `-0.0114` maxDD `-12.8631`
- `market_context_high->crypto_alt_24h` score `-3.2976` n `153` status `ready` deltaP `12.8268` edge `0.3327` maxDD `-53.6115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
