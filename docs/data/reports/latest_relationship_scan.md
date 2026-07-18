# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T11:07:29.203406+00:00`
- Price records: `672`
- Market context records: `7132`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11670`

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

- `market_context_high->fx_4h` score `0.502` n `139` status `ready` deltaP `17.8584` edge `0.0153` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.0916` n `151` status `ready` deltaP `5.2028` edge `0.0028` maxDD `-0.276`
- `market_context_high->unknown_1h` score `-0.3954` n `151` status `ready` deltaP `-2.6986` edge `0.0409` maxDD `-1.4688`
- `market_context_high->crypto_alt_1h` score `-0.5876` n `151` status `ready` deltaP `0.3311` edge `0.0255` maxDD `-5.91`
- `market_context_high->crypto_major_1h` score `-0.6339` n `151` status `ready` deltaP `3.6424` edge `0.0355` maxDD `-7.6171`
- `market_context_high->index_1h` score `-0.7128` n `151` status `ready` deltaP `1.8103` edge `-0.005` maxDD `-2.3175`
- `market_context_high->commodity_1h` score `-0.7223` n `151` status `ready` deltaP `-2.0869` edge `-0.0166` maxDD `-1.9668`
- `market_context_high->metal_1h` score `-1.3422` n `151` status `ready` deltaP `-4.5128` edge `-0.0053` maxDD `-2.1172`
- `market_context_high->unknown_4h` score `-2.1656` n `139` status `ready` deltaP `-5.2115` edge `0.0198` maxDD `-4.9083`
- `market_context_high->commodity_4h` score `-2.3144` n `139` status `ready` deltaP `-6.8904` edge `-0.0434` maxDD `-2.9494`
- `market_context_high->crypto_major_4h` score `-3.2453` n `139` status `ready` deltaP `1.7075` edge `0.0016` maxDD `-24.6569`
- `market_context_high->equity_1h` score `-3.4618` n `151` status `ready` deltaP `0.4451` edge `-0.0457` maxDD `-14.9936`
- `market_context_high->index_4h` score `-4.1434` n `139` status `ready` deltaP `-3.4622` edge `-0.0523` maxDD `-12.2591`
- `market_context_high->commodity_24h` score `-4.3029` n `136` status `ready` deltaP `-12.4796` edge `-0.1445` maxDD `-4.4704`
- `market_context_high->metal_4h` score `-4.3602` n `139` status `ready` deltaP `-8.2898` edge `-0.0128` maxDD `-5.2896`
- `market_context_high->fx_24h` score `-4.8654` n `136` status `ready` deltaP `-14.6752` edge `-0.0249` maxDD `-3.9503`
- `market_context_high->crypto_alt_4h` score `-5.2165` n `139` status `ready` deltaP `-2.2855` edge `-0.0338` maxDD `-22.8538`
- `market_context_high->unknown_24h` score `-9.9048` n `136` status `ready` deltaP `-30.9028` edge `-0.1047` maxDD `-23.5076`
- `market_context_high->equity_4h` score `-13.8821` n `139` status `ready` deltaP `-1.5902` edge `-0.2572` maxDD `-64.1233`
- `market_context_high->metal_24h` score `-14.5121` n `136` status `ready` deltaP `-29.0237` edge `-0.1809` maxDD `-41.1296`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
