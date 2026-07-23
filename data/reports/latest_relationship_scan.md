# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T02:22:31.210648+00:00`
- Price records: `672`
- Market context records: `7625`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14551`

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

- `market_context_high->equity_24h` score `0.5906` n `145` status `ready` deltaP `16.9771` edge `0.4531` maxDD `-34.5784`
- `market_context_high->unknown_24h` score `0.1068` n `146` status `ready` deltaP `10.1432` edge `0.0593` maxDD `-4.775`
- `market_context_high->index_1h` score `0.0648` n `146` status `ready` deltaP `6.8123` edge `0.0108` maxDD `-0.8324`
- `market_context_high->commodity_24h` score `-0.043` n `145` status `ready` deltaP `13.2392` edge `0.0665` maxDD `-7.0012`
- `market_context_high->crypto_major_1h` score `-0.1401` n `146` status `ready` deltaP `8.1556` edge `0.0237` maxDD `-4.0162`
- `market_context_high->crypto_alt_1h` score `-0.1944` n `146` status `ready` deltaP `2.3542` edge `0.0226` maxDD `-2.7243`
- `market_context_high->commodity_1h` score `-0.3077` n `146` status `ready` deltaP `2.8795` edge `-0.0016` maxDD `-1.5641`
- `market_context_high->fx_24h` score `-0.3503` n `145` status `ready` deltaP `9.2803` edge `0.0177` maxDD `-3.0343`
- `market_context_high->commodity_4h` score `-0.4257` n `146` status `ready` deltaP `4.206` edge `0.011` maxDD `-2.2943`
- `market_context_high->equity_1h` score `-0.4736` n `146` status `ready` deltaP `5.8271` edge `0.0518` maxDD `-7.7764`
- `market_context_high->index_4h` score `-0.6311` n `146` status `ready` deltaP `9.0633` edge `0.0288` maxDD `-3.2774`
- `market_context_high->fx_1h` score `-0.6377` n `146` status `ready` deltaP `-0.2715` edge `-0.0014` maxDD `-0.6615`
- `market_context_high->metal_1h` score `-0.6621` n `146` status `ready` deltaP `0.9392` edge `0.0134` maxDD `-1.0307`
- `market_context_high->crypto_alt_4h` score `-0.8929` n `146` status `ready` deltaP `3.6543` edge `0.0601` maxDD `-9.5815`
- `market_context_high->crypto_major_4h` score `-1.1532` n `146` status `ready` deltaP `8.5219` edge `0.0631` maxDD `-14.4206`
- `market_context_high->equity_4h` score `-1.4908` n `146` status `ready` deltaP `2.061` edge `0.2095` maxDD `-20.4824`
- `market_context_high->unknown_1h` score `-1.5134` n `146` status `ready` deltaP `-0.8346` edge `-0.0582` maxDD `-1.3217`
- `market_context_high->metal_4h` score `-1.6504` n `146` status `ready` deltaP `-1.5181` edge `0.0442` maxDD `-4.6535`
- `market_context_high->metal_24h` score `-2.0086` n `146` status `ready` deltaP `-3.2772` edge `0.09` maxDD `-7.3868`
- `market_context_high->fx_4h` score `-2.5728` n `146` status `ready` deltaP `-6.3529` edge `-0.0036` maxDD `-2.1425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
