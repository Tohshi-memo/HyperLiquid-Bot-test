# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T11:22:29.736290+00:00`
- Price records: `672`
- Market context records: `5346`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11468`

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

- `market_context_high->unknown_24h` score `16.5141` n `158` status `ready` deltaP `20.8444` edge `1.2462` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `5.921` n `158` status `ready` deltaP `22.431` edge `0.7888` maxDD `-28.9274`
- `market_context_high->equity_24h` score `4.679` n `158` status `ready` deltaP `18.0599` edge `0.8324` maxDD `-40.0306`
- `market_context_high->crypto_major_4h` score `2.9371` n `194` status `ready` deltaP `13.3361` edge `0.3851` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `2.7343` n `194` status `ready` deltaP `11.1217` edge `0.3178` maxDD `-9.46`
- `market_context_high->equity_4h` score `1.8894` n `194` status `ready` deltaP `10.3972` edge `0.252` maxDD `-7.4425`
- `market_context_high->index_24h` score `0.8214` n `158` status `ready` deltaP `25.0813` edge `0.1016` maxDD `-7.413`
- `market_context_high->equity_1h` score `0.4991` n `194` status `ready` deltaP `8.0129` edge `0.0847` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.1784` n `158` status `ready` deltaP `9.8101` edge `0.039` maxDD `-0.8294`
- `market_context_high->crypto_major_1h` score `0.0935` n `194` status `ready` deltaP `4.6407` edge `0.1014` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `0.083` n `194` status `ready` deltaP `2.2455` edge `0.0881` maxDD `-5.0257`
- `market_context_high->index_1h` score `0.067` n `194` status `ready` deltaP `6.5174` edge `0.0125` maxDD `-1.0296`
- `market_context_high->index_4h` score `-0.377` n `194` status `ready` deltaP `6.2217` edge `0.0261` maxDD `-2.9391`
- `market_context_high->fx_1h` score `-0.3797` n `194` status `ready` deltaP `0.1158` edge `-0.0005` maxDD `-0.5823`
- `market_context_high->metal_1h` score `-0.4363` n `194` status `ready` deltaP `1.0479` edge `0.0046` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-0.6842` n `194` status `ready` deltaP `1.8308` edge `0.003` maxDD `-1.567`
- `market_context_high->unknown_4h` score `-1.2639` n `194` status `ready` deltaP `7.908` edge `-0.0398` maxDD `-6.126`
- `market_context_high->commodity_1h` score `-1.4539` n `194` status `ready` deltaP `-3.4755` edge `-0.0062` maxDD `-3.3428`
- `market_context_high->metal_4h` score `-2.5552` n `194` status `ready` deltaP `-6.9195` edge `-0.029` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-3.8274` n `194` status `ready` deltaP `-7.1662` edge `-0.0428` maxDD `-11.937`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
