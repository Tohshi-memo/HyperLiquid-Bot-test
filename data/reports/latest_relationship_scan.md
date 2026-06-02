# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T06:07:21.924744+00:00`
- Price records: `672`
- Market context records: `2635`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9216`

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

- `market_context_high->unknown_24h` score `7.5194` n `141` status `ready` deltaP `18.1258` edge `0.5386` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `5.0909` n `141` status `ready` deltaP `24.786` edge `0.5269` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.3653` n `141` status `ready` deltaP `14.2871` edge `0.3662` maxDD `-10.1468`
- `market_context_high->crypto_alt_24h` score `1.6342` n `141` status `ready` deltaP `4.5804` edge `0.7022` maxDD `-37.3906`
- `market_context_high->index_24h` score `1.312` n `141` status `ready` deltaP `11.5211` edge `0.1306` maxDD `-2.5127`
- `market_context_high->crypto_alt_1h` score `1.2347` n `141` status `ready` deltaP `10.6542` edge `0.1506` maxDD `-6.1656`
- `market_context_high->unknown_4h` score `1.0664` n `141` status `ready` deltaP `7.3408` edge `0.1449` maxDD `-3.7312`
- `market_context_high->crypto_major_1h` score `0.6508` n `141` status `ready` deltaP `7.9278` edge `0.1208` maxDD `-4.2199`
- `market_context_high->index_4h` score `0.384` n `141` status `ready` deltaP `9.6674` edge `0.0517` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1973` n `141` status `ready` deltaP `3.2945` edge `0.011` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.2198` n `141` status `ready` deltaP `2.735` edge `0.0176` maxDD `-1.665`
- `market_context_high->commodity_1h` score `-0.3018` n `141` status `ready` deltaP `6.1781` edge `0.0215` maxDD `-4.3601`
- `market_context_high->metal_1h` score `-0.501` n `141` status `ready` deltaP `-0.0159` edge `0.0046` maxDD `-2.4982`
- `market_context_high->fx_1h` score `-0.623` n `141` status `ready` deltaP `-0.9927` edge `0.0035` maxDD `-0.2373`
- `market_context_high->metal_4h` score `-0.6259` n `141` status `ready` deltaP `3.105` edge `0.0296` maxDD `-3.5302`
- `market_context_high->commodity_4h` score `-0.8978` n `141` status `ready` deltaP `5.2597` edge `0.0441` maxDD `-10.2078`
- `market_context_high->fx_24h` score `-0.9284` n `141` status `ready` deltaP `2.9773` edge `-0.0026` maxDD `-1.236`
- `market_context_high->fx_4h` score `-0.9994` n `141` status `ready` deltaP `-1.5741` edge `0.0103` maxDD `-0.6474`
- `market_context_high->equity_1h` score `-1.0689` n `141` status `ready` deltaP `-2.5831` edge `0.012` maxDD `-2.7085`
- `market_context_high->equity_4h` score `-1.3816` n `141` status `ready` deltaP `1.6217` edge `0.0145` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
