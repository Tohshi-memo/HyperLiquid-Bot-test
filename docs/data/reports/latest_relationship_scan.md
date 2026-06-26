# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T16:37:40.006890+00:00`
- Price records: `672`
- Market context records: `4845`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7616`

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

- `market_context_high->unknown_1h` score `13.4314` n `110` status `ready` deltaP `9.7115` edge `1.0963` maxDD `-1.674`
- `market_context_high->unknown_4h` score `11.1816` n `98` status `ready` deltaP `26.7421` edge `0.8223` maxDD `-2.5027`
- `market_context_high->unknown_24h` score `5.0689` n `90` status `ready` deltaP `24.3403` edge `0.2944` maxDD `-1.4072`
- `market_context_high->crypto_alt_4h` score `4.3473` n `98` status `ready` deltaP `17.91` edge `0.3781` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `4.2878` n `98` status `ready` deltaP `14.1799` edge `0.3852` maxDD `-7.1265`
- `market_context_high->metal_4h` score `1.4431` n `98` status `ready` deltaP `11.4578` edge `0.1101` maxDD `-1.9651`
- `market_context_high->crypto_major_1h` score `0.4313` n `110` status `ready` deltaP `6.1704` edge `0.118` maxDD `-5.6406`
- `market_context_high->crypto_alt_1h` score `0.4066` n `110` status `ready` deltaP `8.1709` edge `0.0999` maxDD `-5.5126`
- `market_context_high->index_4h` score `0.3254` n `98` status `ready` deltaP `8.5614` edge `0.0309` maxDD `-0.7006`
- `market_context_high->equity_4h` score `0.1983` n `98` status `ready` deltaP `10.5557` edge `0.0932` maxDD `-6.3852`
- `market_context_high->equity_1h` score `0.1755` n `110` status `ready` deltaP `4.2352` edge `0.054` maxDD `-2.779`
- `market_context_high->fx_4h` score `-0.1524` n `98` status `ready` deltaP `6.7322` edge `0.0106` maxDD `-0.788`
- `market_context_high->metal_1h` score `-0.198` n `110` status `ready` deltaP `0.4055` edge `0.0299` maxDD `-1.3057`
- `market_context_high->commodity_1h` score `-0.2121` n `110` status `ready` deltaP `3.4322` edge `0.0159` maxDD `-1.278`
- `market_context_high->commodity_4h` score `-0.4514` n `98` status `ready` deltaP `10.3192` edge `0.0108` maxDD `-4.377`
- `market_context_high->index_1h` score `-0.5235` n `110` status `ready` deltaP `-0.1388` edge `0.0093` maxDD `-0.7054`
- `market_context_high->fx_1h` score `-1.3442` n `110` status `ready` deltaP `-7.0169` edge `-0.0039` maxDD `-0.5734`
- `market_context_high->fx_24h` score `-1.869` n `90` status `ready` deltaP `-6.5278` edge `-0.0112` maxDD `-2.749`
- `market_context_high->index_24h` score `-4.768` n `90` status `ready` deltaP `-8.4028` edge `-0.1542` maxDD `-24.085`
- `market_context_high->commodity_24h` score `-5.3735` n `90` status `ready` deltaP `10.7986` edge `-0.0089` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
