# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T05:22:25.978949+00:00`
- Price records: `672`
- Market context records: `4901`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8608`

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

- `market_context_high->unknown_1h` score `14.51` n `110` status `ready` deltaP `9.2733` edge `1.1891` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.5868` n `110` status `ready` deltaP `23.3148` edge `0.6966` maxDD `-1.917`
- `market_context_high->crypto_alt_4h` score `6.5461` n `110` status `ready` deltaP `21.6658` edge `0.5363` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `6.4442` n `110` status `ready` deltaP `18.9495` edge `0.5331` maxDD `-7.1265`
- `market_context_high->unknown_24h` score `5.2776` n `92` status `ready` deltaP `23.6338` edge `0.3165` maxDD `-1.4072`
- `market_context_high->metal_4h` score `1.1223` n `110` status `ready` deltaP `8.0627` edge `0.106` maxDD `-1.9651`
- `market_context_high->equity_4h` score `0.8937` n `110` status `ready` deltaP `12.439` edge `0.1698` maxDD `-6.3852`
- `market_context_high->crypto_major_1h` score `0.5388` n `110` status `ready` deltaP `7.0686` edge `0.1258` maxDD `-5.6406`
- `market_context_high->index_4h` score `0.5224` n `110` status `ready` deltaP `10.9257` edge `0.0404` maxDD `-0.7006`
- `market_context_high->crypto_alt_1h` score `0.4721` n `110` status `ready` deltaP `8.62` edge `0.1053` maxDD `-5.5126`
- `market_context_high->equity_1h` score `0.2495` n `110` status `ready` deltaP `4.6843` edge `0.0605` maxDD `-2.779`
- `market_context_high->commodity_1h` score `-0.2113` n `110` status `ready` deltaP `3.4322` edge `0.016` maxDD `-1.278`
- `market_context_high->metal_1h` score `-0.2172` n `110` status `ready` deltaP `-0.0545` edge `0.0305` maxDD `-1.3057`
- `market_context_high->index_1h` score `-0.5079` n `110` status `ready` deltaP `-0.1388` edge `0.0113` maxDD `-0.7054`
- `market_context_high->fx_4h` score `-0.7422` n `110` status `ready` deltaP `-0.1524` edge `0.0029` maxDD `-1.0967`
- `market_context_high->commodity_4h` score `-0.7625` n `110` status `ready` deltaP `7.3392` edge `0.0062` maxDD `-4.4933`
- `market_context_high->fx_1h` score `-1.3777` n `110` status `ready` deltaP `-7.3163` edge `-0.0047` maxDD `-0.5734`
- `market_context_high->fx_24h` score `-1.5723` n `92` status `ready` deltaP `-3.3892` edge `-0.0074` maxDD `-2.749`
- `market_context_high->index_24h` score `-4.5203` n `92` status `ready` deltaP `-5.1706` edge `-0.1365` maxDD `-24.6845`
- `market_context_high->commodity_24h` score `-4.5657` n `92` status `ready` deltaP `16.4402` edge `0.0208` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
