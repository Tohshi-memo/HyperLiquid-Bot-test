# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T06:07:26.329356+00:00`
- Price records: `672`
- Market context records: `4905`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9448`

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

- `market_context_high->unknown_1h` score `14.5183` n `110` status `ready` deltaP `9.423` edge `1.1888` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.636` n `110` status `ready` deltaP `23.3148` edge `0.7007` maxDD `-1.917`
- `market_context_high->crypto_alt_4h` score `6.5605` n `110` status `ready` deltaP `21.6658` edge `0.5375` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `6.4454` n `110` status `ready` deltaP `18.9495` edge `0.5332` maxDD `-7.1265`
- `market_context_high->unknown_24h` score `5.2824` n `92` status `ready` deltaP `23.6338` edge `0.3169` maxDD `-1.4072`
- `market_context_high->metal_4h` score `1.1466` n `110` status `ready` deltaP `8.3675` edge `0.106` maxDD `-1.9651`
- `market_context_high->equity_4h` score `0.8645` n `110` status `ready` deltaP `11.9817` edge `0.1691` maxDD `-6.3852`
- `market_context_high->crypto_major_1h` score `0.5677` n `110` status `ready` deltaP `7.368` edge `0.1275` maxDD `-5.6406`
- `market_context_high->index_4h` score `0.5137` n `110` status `ready` deltaP `10.7733` edge `0.0403` maxDD `-0.7006`
- `market_context_high->crypto_alt_1h` score `0.4791` n `110` status `ready` deltaP `8.62` edge `0.1062` maxDD `-5.5126`
- `market_context_high->equity_1h` score `0.2674` n `110` status `ready` deltaP `4.9837` edge `0.0608` maxDD `-2.779`
- `market_context_high->commodity_1h` score `-0.2028` n `110` status `ready` deltaP `3.5819` edge `0.0161` maxDD `-1.278`
- `market_context_high->metal_1h` score `-0.2087` n `110` status `ready` deltaP `0.0952` edge `0.0306` maxDD `-1.3057`
- `market_context_high->index_1h` score `-0.5079` n `110` status `ready` deltaP `-0.1388` edge `0.0113` maxDD `-0.7054`
- `market_context_high->fx_4h` score `-0.7383` n `110` status `ready` deltaP `-0.1524` edge `0.0034` maxDD `-1.0967`
- `market_context_high->commodity_4h` score `-0.7491` n `110` status `ready` deltaP `7.4916` edge `0.0063` maxDD `-4.4933`
- `market_context_high->fx_1h` score `-1.3729` n `110` status `ready` deltaP `-7.3163` edge `-0.0043` maxDD `-0.5734`
- `market_context_high->fx_24h` score `-1.5488` n `92` status `ready` deltaP `-3.2156` edge `-0.0066` maxDD `-2.749`
- `market_context_high->commodity_24h` score `-4.5001` n `92` status `ready` deltaP `16.961` edge `0.0228` maxDD `-27.5371`
- `market_context_high->index_24h` score `-4.5521` n `92` status `ready` deltaP `-5.6915` edge `-0.1371` maxDD `-24.6845`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
