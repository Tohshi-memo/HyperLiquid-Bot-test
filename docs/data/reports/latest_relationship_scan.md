# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T08:46:19.182004+00:00`
- Price records: `672`
- Market context records: `5335`
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

- `market_context_high->unknown_24h` score `18.9309` n `153` status `ready` deltaP `22.8247` edge `1.4344` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `6.9668` n `153` status `ready` deltaP `24.52` edge `0.8321` maxDD `-26.5332`
- `market_context_high->equity_24h` score `4.906` n `153` status `ready` deltaP `17.882` edge `0.8525` maxDD `-40.0306`
- `market_context_high->crypto_major_4h` score `3.0535` n `194` status `ready` deltaP `13.3361` edge `0.3948` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `2.9849` n `194` status `ready` deltaP `11.8839` edge `0.3336` maxDD `-9.46`
- `market_context_high->equity_4h` score `2.1472` n `194` status `ready` deltaP `11.1594` edge `0.2684` maxDD `-7.4425`
- `market_context_high->index_24h` score `0.7232` n `153` status `ready` deltaP `24.1217` edge `0.0954` maxDD `-7.413`
- `market_context_high->equity_1h` score `0.5866` n `194` status `ready` deltaP `8.9111` edge `0.086` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.2956` n `153` status `ready` deltaP `11.0498` edge `0.0405` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.1489` n `194` status `ready` deltaP `2.6946` edge `0.0906` maxDD `-5.0257`
- `market_context_high->index_1h` score `0.0789` n `194` status `ready` deltaP `6.6671` edge `0.0125` maxDD `-1.0296`
- `market_context_high->crypto_major_1h` score `0.0707` n `194` status `ready` deltaP `4.6407` edge `0.0995` maxDD `-6.9639`
- `market_context_high->fx_1h` score `-0.3127` n `194` status `ready` deltaP `1.3134` edge `0.0001` maxDD `-0.5823`
- `market_context_high->metal_1h` score `-0.3358` n `194` status `ready` deltaP `2.2455` edge `0.0095` maxDD `-2.0682`
- `market_context_high->index_4h` score `-0.3588` n `194` status `ready` deltaP `6.5266` edge `0.0264` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.594` n `194` status `ready` deltaP `3.3552` edge `0.0044` maxDD `-1.567`
- `market_context_high->unknown_4h` score `-1.2699` n `194` status `ready` deltaP `7.908` edge `-0.0403` maxDD `-6.126`
- `market_context_high->commodity_1h` score `-1.4131` n `194` status `ready` deltaP `-3.0264` edge `-0.0058` maxDD `-3.3428`
- `market_context_high->metal_4h` score `-2.3575` n `194` status `ready` deltaP `-5.5475` edge `-0.0128` maxDD `-12.8631`
- `market_context_high->crypto_alt_24h` score `-3.3077` n `153` status `ready` deltaP `12.8268` edge `0.3314` maxDD `-53.6115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
