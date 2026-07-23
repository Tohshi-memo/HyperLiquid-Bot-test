# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T15:07:29.017115+00:00`
- Price records: `672`
- Market context records: `7680`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14676`

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

- `market_context_high->index_1h` score `0.0418` n `143` status `ready` deltaP `6.0985` edge `0.0121` maxDD `-0.7914`
- `market_context_high->crypto_major_1h` score `-0.0414` n `143` status `ready` deltaP `8.7413` edge `0.025` maxDD `-3.7537`
- `market_context_high->crypto_alt_1h` score `-0.1923` n `143` status `ready` deltaP `2.4968` edge `0.0214` maxDD `-2.6829`
- `market_context_high->equity_1h` score `-0.2083` n `143` status `ready` deltaP `5.2963` edge `0.0578` maxDD `-6.2518`
- `market_context_high->fx_24h` score `-0.2282` n `142` status `ready` deltaP `10.4162` edge `0.0203` maxDD `-3.0343`
- `market_context_high->commodity_1h` score `-0.5139` n `143` status `ready` deltaP `1.2338` edge `-0.0013` maxDD `-0.98`
- `market_context_high->index_4h` score `-0.5869` n `143` status `ready` deltaP `8.5884` edge `0.0317` maxDD `-2.8023`
- `market_context_high->commodity_4h` score `-0.5943` n `143` status `ready` deltaP `0.8597` edge `0.0041` maxDD `-1.0817`
- `market_context_high->fx_1h` score `-0.6039` n `143` status `ready` deltaP `-1.1949` edge `-0.0017` maxDD `-0.5861`
- `market_context_high->metal_1h` score `-0.6064` n `143` status `ready` deltaP `1.5451` edge `0.0165` maxDD `-1.0307`
- `market_context_high->crypto_major_4h` score `-0.8108` n `143` status `ready` deltaP `10.9916` edge `0.0857` maxDD `-11.1237`
- `market_context_high->crypto_alt_4h` score `-0.8543` n `143` status `ready` deltaP `4.3035` edge `0.0695` maxDD `-8.2174`
- `market_context_high->equity_4h` score `-1.1109` n `143` status `ready` deltaP `0.3722` edge `0.2002` maxDD `-15.9419`
- `market_context_high->equity_24h` score `-1.1894` n `142` status `ready` deltaP `13.5275` edge `0.0959` maxDD `-22.4193`
- `market_context_high->commodity_24h` score `-1.3789` n `142` status `ready` deltaP `6.9662` edge `-0.003` maxDD `-7.0012`
- `market_context_high->unknown_1h` score `-1.5014` n `143` status `ready` deltaP `-1.4981` edge `-0.0537` maxDD `-1.2478`
- `market_context_high->metal_4h` score `-1.531` n `143` status `ready` deltaP `-1.6225` edge `0.0527` maxDD `-4.0536`
- `market_context_high->metal_24h` score `-1.8193` n `143` status `ready` deltaP `-1.9983` edge `0.0726` maxDD `-5.7347`
- `market_context_high->fx_4h` score `-2.5722` n `143` status `ready` deltaP `-6.5375` edge `-0.0045` maxDD `-1.9678`
- `market_context_high->index_24h` score `-3.4114` n `142` status `ready` deltaP `-21.0679` edge `-0.0348` maxDD `-6.3017`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
