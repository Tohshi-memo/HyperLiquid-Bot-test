# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-22T15:55:59.279708+00:00`
- Price records: `672`
- Market context records: `7580`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14512`

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

- `market_context_high->commodity_4h` score `0.2518` n `162` status `ready` deltaP `9.8086` edge `0.0316` maxDD `-2.4139`
- `market_context_high->index_1h` score `-0.005` n `162` status `ready` deltaP `5.639` edge `0.0106` maxDD `-0.9072`
- `market_context_high->commodity_24h` score `-0.1046` n `154` status `ready` deltaP `12.5594` edge `0.0659` maxDD `-7.0012`
- `market_context_high->commodity_1h` score `-0.1297` n `162` status `ready` deltaP `6.1061` edge `0.0057` maxDD `-1.5775`
- `market_context_high->index_4h` score `-0.4664` n `162` status `ready` deltaP `11.4056` edge `0.0368` maxDD `-3.4775`
- `market_context_high->fx_1h` score `-0.5384` n `162` status `ready` deltaP `0.8508` edge `-0.0006` maxDD `-0.6615`
- `market_context_high->metal_1h` score `-0.6977` n `162` status `ready` deltaP `0.3752` edge `0.0126` maxDD `-1.0307`
- `market_context_high->crypto_alt_1h` score `-0.7135` n `162` status `ready` deltaP `-0.3179` edge `0.0024` maxDD `-5.0068`
- `market_context_high->unknown_24h` score `-0.721` n `155` status `ready` deltaP `8.1463` edge `0.0959` maxDD `-9.4117`
- `market_context_high->equity_1h` score `-0.7973` n `162` status `ready` deltaP `4.5546` edge `0.0395` maxDD `-9.0994`
- `market_context_high->crypto_major_1h` score `-0.8027` n `162` status `ready` deltaP `5.1065` edge `0.001` maxDD `-7.3694`
- `market_context_high->unknown_1h` score `-0.9484` n `162` status `ready` deltaP `0.4306` edge `-0.0621` maxDD `-1.3217`
- `market_context_high->fx_24h` score `-0.9785` n `154` status `ready` deltaP `6.6202` edge `0.014` maxDD `-3.8406`
- `market_context_high->crypto_alt_4h` score `-1.436` n `162` status `ready` deltaP `0.9222` edge `0.04` maxDD `-11.753`
- `market_context_high->metal_4h` score `-1.4954` n `162` status `ready` deltaP `0.5947` edge `0.0525` maxDD `-4.8549`
- `market_context_high->equity_4h` score `-1.5336` n `162` status `ready` deltaP `3.3753` edge `0.2176` maxDD `-21.9375`
- `market_context_high->fx_4h` score `-2.1608` n `162` status `ready` deltaP `-1.6196` edge `-0.0008` maxDD `-2.1439`
- `market_context_high->crypto_major_4h` score `-2.1714` n `162` status `ready` deltaP `5.0832` edge `0.0409` maxDD `-20.5874`
- `market_context_high->unknown_4h` score `-2.1938` n `162` status `ready` deltaP `9.9462` edge `-0.1119` maxDD `-6.1862`
- `market_context_high->metal_24h` score `-3.4214` n `155` status `ready` deltaP `-4.9093` edge `0.0791` maxDD `-14.8006`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
