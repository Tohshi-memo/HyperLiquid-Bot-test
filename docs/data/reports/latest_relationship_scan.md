# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T04:07:21.591347+00:00`
- Price records: `672`
- Market context records: `3036`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6988`

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

- `market_context_high->crypto_alt_24h` score `23.4556` n `99` status `ready` deltaP `11.5056` edge `2.2696` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `13.1632` n `99` status `ready` deltaP `23.2797` edge `0.9882` maxDD `-1.7175`
- `market_context_high->commodity_24h` score `12.8513` n `99` status `ready` deltaP `42.3769` edge `0.8125` maxDD `-1.2589`
- `market_context_high->equity_24h` score `8.4061` n `99` status `ready` deltaP `22.68` edge `1.2017` maxDD `-18.3486`
- `market_context_high->index_24h` score `8.1242` n `99` status `ready` deltaP `22.2696` edge `0.6541` maxDD `-4.7103`
- `market_context_high->commodity_4h` score `2.8044` n `126` status `ready` deltaP `18.8419` edge `0.1728` maxDD `-2.8438`
- `market_context_high->commodity_1h` score `0.0241` n `129` status `ready` deltaP `2.2908` edge `0.029` maxDD `-1.7142`
- `market_context_high->unknown_4h` score `-0.3213` n `126` status `ready` deltaP `2.0495` edge `0.0649` maxDD `-3.7602`
- `market_context_high->index_1h` score `-0.3811` n `129` status `ready` deltaP `4.2369` edge `0.0243` maxDD `-4.1126`
- `market_context_high->equity_1h` score `-0.4778` n `129` status `ready` deltaP `3.5685` edge `0.0365` maxDD `-6.7232`
- `market_context_high->fx_1h` score `-0.533` n `129` status `ready` deltaP `-4.7394` edge `0.0001` maxDD `-0.2801`
- `market_context_high->crypto_alt_1h` score `-0.5404` n `129` status `ready` deltaP `6.3861` edge `0.1011` maxDD `-14.7034`
- `market_context_high->index_4h` score `-0.556` n `126` status `ready` deltaP `13.1823` edge `0.0728` maxDD `-14.2235`
- `market_context_high->unknown_1h` score `-0.7721` n `129` status `ready` deltaP `4.0709` edge `-0.0184` maxDD `-3.1801`
- `market_context_high->crypto_major_1h` score `-0.9817` n `129` status `ready` deltaP `4.2798` edge `0.0719` maxDD `-15.1032`
- `market_context_high->fx_4h` score `-1.1271` n `126` status `ready` deltaP `-8.7616` edge `-0.0034` maxDD `-0.9481`
- `market_context_high->metal_1h` score `-1.1341` n `129` status `ready` deltaP `-1.7987` edge `-0.0016` maxDD `-6.8783`
- `market_context_high->crypto_alt_4h` score `-1.4069` n `126` status `ready` deltaP `18.6072` edge `0.33` maxDD `-45.0873`
- `market_context_high->fx_24h` score `-1.4599` n `99` status `ready` deltaP `-2.32` edge `-0.019` maxDD `-0.6418`
- `market_context_high->equity_4h` score `-2.0555` n `126` status `ready` deltaP `10.044` edge `0.0757` maxDD `-28.4948`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
