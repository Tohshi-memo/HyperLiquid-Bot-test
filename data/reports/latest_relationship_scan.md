# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T19:22:31.549136+00:00`
- Price records: `672`
- Market context records: `4858`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7626`

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

- `market_context_high->unknown_1h` score `13.4994` n `110` status `ready` deltaP `10.4709` edge `1.0969` maxDD `-1.674`
- `market_context_high->unknown_4h` score `10.3693` n `107` status `ready` deltaP `25.7608` edge `0.7455` maxDD `-1.917`
- `market_context_high->crypto_alt_4h` score `6.1594` n `107` status `ready` deltaP `19.3512` edge `0.5195` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `5.9272` n `107` status `ready` deltaP `16.5075` edge `0.5063` maxDD `-7.1265`
- `market_context_high->unknown_24h` score `5.1773` n `91` status `ready` deltaP `25.4693` edge `0.2959` maxDD `-1.4072`
- `market_context_high->metal_4h` score `1.4097` n `107` status `ready` deltaP `10.4556` edge `0.114` maxDD `-1.9651`
- `market_context_high->equity_4h` score `0.8315` n `107` status `ready` deltaP `11.6623` edge `0.167` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.5296` n `107` status `ready` deltaP `11.0326` edge `0.0406` maxDD `-0.7006`
- `market_context_high->crypto_major_1h` score `0.4438` n `110` status `ready` deltaP `6.3201` edge `0.1186` maxDD `-5.6406`
- `market_context_high->crypto_alt_1h` score `0.3848` n `110` status `ready` deltaP `7.7218` edge `0.1001` maxDD `-5.5126`
- `market_context_high->equity_1h` score `0.2122` n `110` status `ready` deltaP `4.0855` edge `0.0597` maxDD `-2.779`
- `market_context_high->metal_1h` score `-0.1674` n `110` status `ready` deltaP `0.8437` edge `0.0309` maxDD `-1.3057`
- `market_context_high->commodity_1h` score `-0.202` n `110` status `ready` deltaP `3.5819` edge `0.0162` maxDD `-1.278`
- `market_context_high->fx_4h` score `-0.4891` n `107` status `ready` deltaP `2.3165` edge `0.006` maxDD `-1.0651`
- `market_context_high->index_1h` score `-0.49` n `110` status `ready` deltaP `0.3103` edge `0.0106` maxDD `-0.7054`
- `market_context_high->commodity_4h` score `-0.7584` n `107` status `ready` deltaP `7.0949` edge `0.0068` maxDD `-4.384`
- `market_context_high->fx_1h` score `-1.3322` n `110` status `ready` deltaP `-6.8672` edge `-0.0039` maxDD `-0.5734`
- `market_context_high->fx_24h` score `-1.9676` n `91` status `ready` deltaP `-7.5512` edge `-0.0126` maxDD `-2.749`
- `market_context_high->index_24h` score `-4.867` n `91` status `ready` deltaP `-9.2281` edge `-0.1539` maxDD `-24.6845`
- `market_context_high->commodity_24h` score `-5.4985` n `91` status `ready` deltaP `9.9855` edge `-0.0139` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
