# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T16:37:19.828127+00:00`
- Price records: `672`
- Market context records: `1440`
- Flow alert records: `6060`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8797`

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

- `market_context_high->crypto_alt_24h` score `12.3773` n `154` status `ready` deltaP `28.7811` edge `1.0412` maxDD `-15.1306`
- `market_context_high->metal_24h` score `12.1383` n `154` status `ready` deltaP `13.5507` edge `1.0879` maxDD `-6.3373`
- `market_context_high->crypto_major_24h` score `11.6072` n `154` status `ready` deltaP `27.3539` edge `0.8981` maxDD `-8.0553`
- `market_context_high->index_24h` score `4.1733` n `154` status `ready` deltaP `19.3813` edge `0.3272` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.5679` n `154` status `ready` deltaP `12.5271` edge `0.4465` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.2684` n `213` status `ready` deltaP `6.6293` edge `0.1445` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.2056` n `154` status `ready` deltaP `10.4009` edge `0.0527` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.1294` n `225` status `ready` deltaP `2.3` edge `0.0339` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.1475` n `225` status `ready` deltaP `3.5117` edge `0.0108` maxDD `-1.7205`
- `market_context_high->index_4h` score `-0.6846` n `213` status `ready` deltaP `-0.2176` edge `0.0533` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `-0.7137` n `225` status `ready` deltaP `1.364` edge `0.0338` maxDD `-4.1892`
- `market_context_high->commodity_1h` score `-0.7171` n `225` status `ready` deltaP `-0.821` edge `0.0072` maxDD `-2.252`
- `market_context_high->fx_1h` score `-0.7237` n `225` status `ready` deltaP `0.7977` edge `-0.0024` maxDD `-0.3914`
- `market_context_high->crypto_alt_4h` score `-0.926` n `213` status `ready` deltaP `9.3131` edge `0.1927` maxDD `-19.5565`
- `market_context_high->fx_4h` score `-1.0708` n `213` status `ready` deltaP `-4.5639` edge `-0.0098` maxDD `-1.4313`
- `market_context_high->crypto_major_4h` score `-1.2198` n `213` status `ready` deltaP `5.0756` edge `0.1354` maxDD `-13.3376`
- `market_context_high->metal_1h` score `-1.2226` n `225` status `ready` deltaP `4.7698` edge `-0.0001` maxDD `-6.3532`
- `market_context_high->metal_4h` score `-1.5943` n `213` status `ready` deltaP `6.0575` edge `0.0244` maxDD `-12.5349`
- `market_context_high->crypto_major_1h` score `-1.7249` n `225` status `ready` deltaP `-1.2981` edge `0.0006` maxDD `-6.1883`
- `market_context_high->commodity_4h` score `-4.1045` n `213` status `ready` deltaP `-10.1061` edge `-0.02` maxDD `-8.04`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
