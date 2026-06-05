# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T22:37:25.523479+00:00`
- Price records: `672`
- Market context records: `3013`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6984`

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

- `market_context_high->crypto_alt_24h` score `20.941` n `98` status `ready` deltaP `8.5884` edge `2.0795` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `12.8756` n `98` status `ready` deltaP `43.3355` edge `0.7951` maxDD `-0.2165`
- `market_context_high->unknown_24h` score `12.5253` n `98` status `ready` deltaP `20.8263` edge `0.9514` maxDD `-1.7175`
- `market_context_high->equity_24h` score `11.0285` n `98` status `ready` deltaP `19.5614` edge `0.989` maxDD `-12.6963`
- `market_context_high->index_24h` score `6.8704` n `98` status `ready` deltaP `19.1717` edge `0.5428` maxDD `-2.5127`
- `market_context_high->commodity_4h` score `2.4126` n `106` status `ready` deltaP `18.0396` edge `0.1455` maxDD `-2.8438`
- `market_context_high->equity_4h` score `0.6606` n `106` status `ready` deltaP `13.6274` edge `0.1743` maxDD `-12.1029`
- `market_context_high->index_4h` score `0.2041` n `106` status `ready` deltaP `17.1997` edge `0.0962` maxDD `-10.4423`
- `market_context_high->crypto_alt_4h` score `-0.1024` n `106` status `ready` deltaP `22.6301` edge `0.3908` maxDD `-38.7172`
- `market_context_high->equity_1h` score `-0.181` n `116` status `ready` deltaP `5.1776` edge `0.0501` maxDD `-5.6254`
- `market_context_high->commodity_1h` score `-0.2091` n `116` status `ready` deltaP `0.2633` edge `0.0137` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.3021` n `116` status `ready` deltaP `5.6215` edge `0.0252` maxDD `-4.1126`
- `market_context_high->crypto_alt_1h` score `-0.5232` n `116` status `ready` deltaP `6.7469` edge `0.1009` maxDD `-14.7034`
- `market_context_high->fx_1h` score `-0.5704` n `116` status `ready` deltaP `-1.7603` edge `0.0008` maxDD `-0.2615`
- `market_context_high->unknown_1h` score `-1.0094` n `116` status `ready` deltaP `3.3399` edge `-0.0333` maxDD `-3.1801`
- `market_context_high->crypto_major_1h` score `-1.0384` n `116` status `ready` deltaP `4.4187` edge `0.0637` maxDD `-15.1032`
- `market_context_high->metal_1h` score `-1.1345` n `116` status `ready` deltaP `-1.5796` edge `-0.0031` maxDD `-6.8783`
- `market_context_high->fx_4h` score `-1.1714` n `106` status `ready` deltaP `-10.5298` edge `-0.001` maxDD `-0.6521`
- `market_context_high->unknown_4h` score `-1.5324` n `106` status `ready` deltaP `-2.439` edge `-0.0061` maxDD `-3.7602`
- `market_context_high->fx_24h` score `-1.7862` n `98` status `ready` deltaP `-5.4386` edge `-0.0254` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
