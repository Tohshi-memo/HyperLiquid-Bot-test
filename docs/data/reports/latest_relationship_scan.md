# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T10:52:25.883450+00:00`
- Price records: `672`
- Market context records: `5344`
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

- `market_context_high->unknown_24h` score `16.5706` n `158` status `ready` deltaP `21.1916` edge `1.2486` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `5.9318` n `158` status `ready` deltaP `22.431` edge `0.7897` maxDD `-28.9274`
- `market_context_high->equity_24h` score `4.6922` n `158` status `ready` deltaP `18.0599` edge `0.8335` maxDD `-40.0306`
- `market_context_high->crypto_major_4h` score `2.9647` n `194` status `ready` deltaP `13.3361` edge `0.3874` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `2.8091` n `194` status `ready` deltaP `11.4266` edge `0.322` maxDD `-9.46`
- `market_context_high->equity_4h` score `1.9642` n `194` status `ready` deltaP `10.7021` edge `0.2562` maxDD `-7.4425`
- `market_context_high->index_24h` score `0.8074` n `158` status `ready` deltaP `25.0813` edge `0.0998` maxDD `-7.413`
- `market_context_high->equity_1h` score `0.4955` n `194` status `ready` deltaP `8.0129` edge `0.0844` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.2122` n `158` status `ready` deltaP `10.1573` edge `0.0395` maxDD `-0.8294`
- `market_context_high->index_1h` score `0.067` n `194` status `ready` deltaP `6.5174` edge `0.0125` maxDD `-1.0296`
- `market_context_high->crypto_alt_1h` score `0.0398` n `194` status `ready` deltaP `2.0958` edge `0.0855` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.0239` n `194` status `ready` deltaP `4.3413` edge `0.0976` maxDD `-6.9639`
- `market_context_high->fx_1h` score `-0.3633` n `194` status `ready` deltaP `0.4152` edge `-0.0004` maxDD `-0.5823`
- `market_context_high->index_4h` score `-0.3675` n `194` status `ready` deltaP `6.3741` edge `0.0263` maxDD `-2.9391`
- `market_context_high->metal_1h` score `-0.4082` n `194` status `ready` deltaP `1.3473` edge `0.0062` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-0.6668` n `194` status `ready` deltaP `2.1357` edge `0.0032` maxDD `-1.567`
- `market_context_high->unknown_4h` score `-1.2579` n `194` status `ready` deltaP `7.908` edge `-0.0393` maxDD `-6.126`
- `market_context_high->commodity_1h` score `-1.4347` n `194` status `ready` deltaP `-3.3258` edge `-0.0056` maxDD `-3.3428`
- `market_context_high->metal_4h` score `-2.512` n `194` status `ready` deltaP `-6.6146` edge `-0.0255` maxDD `-12.8631`
- `market_context_high->crypto_alt_24h` score `-3.7956` n `158` status `ready` deltaP `11.2342` edge `0.3082` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
