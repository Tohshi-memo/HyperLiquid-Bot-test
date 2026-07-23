# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T02:07:30.003280+00:00`
- Price records: `672`
- Market context records: `7624`
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

- `market_context_high->equity_24h` score `0.6304` n `145` status `ready` deltaP `16.9771` edge `0.4582` maxDD `-34.5784`
- `market_context_high->unknown_24h` score `0.1687` n `146` status `ready` deltaP `10.3168` edge `0.0633` maxDD `-4.775`
- `market_context_high->index_1h` score `0.0555` n `146` status `ready` deltaP `6.6622` edge `0.0106` maxDD `-0.8324`
- `market_context_high->commodity_24h` score `-0.0147` n `145` status `ready` deltaP `13.4135` edge `0.0677` maxDD `-7.0012`
- `market_context_high->crypto_major_1h` score `-0.1557` n `146` status `ready` deltaP `8.0059` edge `0.0227` maxDD `-4.0162`
- `market_context_high->crypto_alt_1h` score `-0.21` n `146` status `ready` deltaP `2.2045` edge `0.0216` maxDD `-2.7243`
- `market_context_high->commodity_1h` score `-0.3077` n `146` status `ready` deltaP `2.8795` edge `-0.0016` maxDD `-1.5641`
- `market_context_high->fx_24h` score `-0.3491` n `145` status `ready` deltaP `9.2803` edge `0.0178` maxDD `-3.0343`
- `market_context_high->commodity_4h` score `-0.411` n `146` status `ready` deltaP `4.3589` edge `0.0112` maxDD `-2.2943`
- `market_context_high->equity_1h` score `-0.4924` n `146` status `ready` deltaP `5.677` edge `0.0504` maxDD `-7.7764`
- `market_context_high->index_4h` score `-0.6335` n `146` status `ready` deltaP `9.0633` edge `0.0285` maxDD `-3.2774`
- `market_context_high->fx_1h` score `-0.6377` n `146` status `ready` deltaP `-0.2715` edge `-0.0014` maxDD `-0.6615`
- `market_context_high->metal_1h` score `-0.6629` n `146` status `ready` deltaP `0.9392` edge `0.0133` maxDD `-1.0307`
- `market_context_high->crypto_alt_4h` score `-0.9125` n `146` status `ready` deltaP `3.5019` edge `0.0586` maxDD `-9.5815`
- `market_context_high->crypto_major_4h` score `-1.1728` n `146` status `ready` deltaP `8.3695` edge `0.0616` maxDD `-14.4206`
- `market_context_high->unknown_1h` score `-1.4966` n `146` status `ready` deltaP `-0.6849` edge `-0.0578` maxDD `-1.3217`
- `market_context_high->equity_4h` score `-1.5081` n `146` status `ready` deltaP `1.9081` edge `0.2083` maxDD `-20.4824`
- `market_context_high->metal_4h` score `-1.6504` n `146` status `ready` deltaP `-1.5181` edge `0.0442` maxDD `-4.6535`
- `market_context_high->metal_24h` score `-2.0024` n `146` status `ready` deltaP `-3.2772` edge `0.0908` maxDD `-7.3868`
- `market_context_high->fx_4h` score `-2.574` n `146` status `ready` deltaP `-6.3529` edge `-0.0037` maxDD `-2.1425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
