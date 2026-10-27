# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T07:07:27.784721+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9641`

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

- `market_context_high->unknown_4h` score `79.182` n `139` status `ready` deltaP `3.4282` edge `6.6092` maxDD `-1.0178`
- `market_context_high->unknown_1h` score `24.7575` n `139` status `ready` deltaP `0.9973` edge `2.1054` maxDD `-1.5807`
- `market_context_high->index_24h` score `1.1323` n `120` status `ready` deltaP `23.1138` edge `0.0293` maxDD `-2.4557`
- `market_context_high->fx_1h` score `0.497` n `139` status `ready` deltaP `11.0595` edge `0.0035` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.4902` n `139` status `ready` deltaP `13.5901` edge `0.0101` maxDD `-0.4545`
- `market_context_high->metal_1h` score `0.0906` n `139` status `ready` deltaP `11.234` edge `0.0114` maxDD `-1.3073`
- `market_context_high->metal_24h` score `-0.1016` n `120` status `ready` deltaP `18.6641` edge `0.1151` maxDD `-6.204`
- `market_context_high->commodity_1h` score `-0.1784` n `139` status `ready` deltaP `3.2999` edge `0.0132` maxDD `-1.0053`
- `market_context_high->fx_24h` score `-0.4171` n `120` status `ready` deltaP `12.2328` edge `0.0222` maxDD `-1.2451`
- `market_context_high->crypto_major_1h` score `-0.4419` n `139` status `ready` deltaP `6.2314` edge `0.0301` maxDD `-6.9306`
- `market_context_high->index_1h` score `-0.6116` n `139` status `ready` deltaP `-0.5719` edge `-0.0029` maxDD `-1.7354`
- `market_context_high->commodity_4h` score `-0.6389` n `139` status `ready` deltaP `4.6577` edge `0.0386` maxDD `-1.165`
- `market_context_high->metal_4h` score `-0.7864` n `139` status `ready` deltaP `9.2868` edge `0.0011` maxDD `-4.773`
- `market_context_high->equity_1h` score `-1.624` n `139` status `ready` deltaP `1.8524` edge `-0.0045` maxDD `-11.2848`
- `market_context_high->crypto_alt_1h` score `-1.9873` n `139` status `ready` deltaP `-0.8175` edge `-0.0049` maxDD `-12.8878`
- `market_context_high->equity_24h` score `-2.5955` n `120` status `ready` deltaP `1.6941` edge `-0.0253` maxDD `-17.5005`
- `market_context_high->index_4h` score `-2.8586` n `139` status `ready` deltaP `-4.3955` edge `-0.0248` maxDD `-6.0625`
- `market_context_high->crypto_major_4h` score `-3.7076` n `139` status `ready` deltaP `3.0181` edge `-0.0609` maxDD `-27.4312`
- `market_context_high->crypto_major_24h` score `-4.5446` n `120` status `ready` deltaP `-0.4997` edge `-0.0936` maxDD `-29.1905`
- `market_context_high->equity_4h` score `-5.3628` n `139` status `ready` deltaP `2.5125` edge `-0.1267` maxDD `-38.2067`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
