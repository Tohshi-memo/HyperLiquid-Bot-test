# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T12:07:29.626700+00:00`
- Price records: `672`
- Market context records: `6815`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11680`

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

- `market_context_high->unknown_24h` score `0.8336` n `176` status `ready` deltaP `-1.5467` edge `0.4924` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `0.3983` n `176` status `ready` deltaP `10.9217` edge `0.1472` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.2761` n `196` status `ready` deltaP `5.7742` edge `0.0121` maxDD `-4.2122`
- `market_context_high->fx_1h` score `-0.3988` n `196` status `ready` deltaP `-0.3941` edge `0.0` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.538` n `196` status `ready` deltaP `3.0735` edge `0.0111` maxDD `-3.7803`
- `market_context_high->index_1h` score `-0.799` n `196` status `ready` deltaP `-3.7486` edge `-0.0039` maxDD `-0.8834`
- `market_context_high->metal_1h` score `-1.0134` n `196` status `ready` deltaP `-6.7885` edge `-0.0108` maxDD `-1.9098`
- `market_context_high->commodity_1h` score `-1.015` n `196` status `ready` deltaP `-1.6467` edge `-0.0053` maxDD `-2.1314`
- `market_context_high->commodity_4h` score `-1.3318` n `185` status `ready` deltaP `-1.9883` edge `-0.0085` maxDD `-5.5853`
- `market_context_high->fx_4h` score `-1.3389` n `185` status `ready` deltaP `5.5224` edge `-0.0021` maxDD `-2.1765`
- `market_context_high->index_4h` score `-1.6633` n `185` status `ready` deltaP `1.8375` edge `-0.0295` maxDD `-6.3458`
- `market_context_high->equity_1h` score `-1.6653` n `196` status `ready` deltaP `0.3391` edge `-0.0306` maxDD `-4.5017`
- `market_context_high->unknown_1h` score `-1.7875` n `196` status `ready` deltaP `-6.2783` edge `-0.017` maxDD `-3.2083`
- `market_context_high->metal_4h` score `-2.8835` n `185` status `ready` deltaP `-6.0094` edge `-0.0313` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-3.3498` n `185` status `ready` deltaP `-1.2673` edge `-0.0883` maxDD `-16.9508`
- `market_context_high->unknown_4h` score `-3.4831` n `185` status `ready` deltaP `-13.9651` edge `0.0394` maxDD `-10.2579`
- `market_context_high->crypto_alt_4h` score `-3.5584` n `185` status `ready` deltaP `-1.9743` edge `-0.0847` maxDD `-20.6678`
- `market_context_high->fx_24h` score `-4.4708` n `176` status `ready` deltaP `-9.7853` edge `-0.0037` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-5.0743` n `185` status `ready` deltaP `-0.81` edge `-0.1913` maxDD `-29.3079`
- `market_context_high->metal_24h` score `-9.6555` n `176` status `ready` deltaP `-21.9697` edge `-0.2429` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
