# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-24T19:52:24.523198+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7726`

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

- `market_context_high->unknown_4h` score `16.3333` n `103` status `ready` deltaP `-1.9432` edge `1.4076` maxDD `-1.016`
- `market_context_high->commodity_24h` score `1.1342` n `75` status `ready` deltaP `18.0625` edge `0.065` maxDD `-3.6055`
- `risk_on_high->commodity_24h` score `0.8871` n `31` status `ready` deltaP `18.3635` edge `0.0375` maxDD `-1.0285`
- `risk_on_and_context->commodity_24h` score `0.8871` n `31` status `ready` deltaP `18.3635` edge `0.0375` maxDD `-1.0285`
- `risk_on_high->fx_1h` score `0.8252` n `31` status `ready` deltaP `17.9592` edge `0.0036` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.8252` n `31` status `ready` deltaP `17.9592` edge `0.0036` maxDD `-0.0698`
- `market_context_high->commodity_4h` score `0.7352` n `103` status `ready` deltaP `11.4226` edge `0.0426` maxDD `-1.2655`
- `risk_on_high->index_1h` score `0.382` n `31` status `ready` deltaP `11.3579` edge `0.0003` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.382` n `31` status `ready` deltaP `11.3579` edge `0.0003` maxDD `-0.1637`
- `risk_on_high->equity_1h` score `0.2987` n `31` status `ready` deltaP `13.1543` edge `-0.0071` maxDD `-0.7172`
- `risk_on_and_context->equity_1h` score `0.2987` n `31` status `ready` deltaP `13.1543` edge `-0.0071` maxDD `-0.7172`
- `risk_on_high->fx_4h` score `0.2496` n `31` status `ready` deltaP `7.1007` edge `0.0069` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `0.2496` n `31` status `ready` deltaP `7.1007` edge `0.0069` maxDD `-0.1126`
- `market_context_high->fx_1h` score `-0.1484` n `111` status `ready` deltaP `2.0917` edge `0.0025` maxDD `-0.1712`
- `market_context_high->commodity_1h` score `-0.2234` n `111` status `ready` deltaP `3.0143` edge `0.0055` maxDD `-1.0053`
- `risk_on_high->metal_1h` score `-0.2361` n `31` status `ready` deltaP `-1.7771` edge `0.0073` maxDD `-0.058`
- `risk_on_and_context->metal_1h` score `-0.2361` n `31` status `ready` deltaP `-1.7771` edge `0.0073` maxDD `-0.058`
- `risk_on_high->metal_4h` score `-0.3783` n `31` status `ready` deltaP `1.49` edge `0.0167` maxDD `-0.3441`
- `risk_on_and_context->metal_4h` score `-0.3783` n `31` status `ready` deltaP `1.49` edge `0.0167` maxDD `-0.3441`
- `market_context_high->fx_4h` score `-0.4231` n `103` status `ready` deltaP `0.148` edge `0.0054` maxDD `-0.5168`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
