# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T05:52:25.039306+00:00`
- Price records: `672`
- Market context records: `4904`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9512`

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

- `market_context_high->unknown_1h` score `14.5195` n `110` status `ready` deltaP `9.423` edge `1.1889` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.6276` n `110` status `ready` deltaP `23.3148` edge `0.7` maxDD `-1.917`
- `market_context_high->crypto_alt_4h` score `6.5557` n `110` status `ready` deltaP `21.6658` edge `0.5371` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `6.4442` n `110` status `ready` deltaP `18.9495` edge `0.5331` maxDD `-7.1265`
- `market_context_high->unknown_24h` score `5.2824` n `92` status `ready` deltaP `23.6338` edge `0.3169` maxDD `-1.4072`
- `market_context_high->metal_4h` score `1.1344` n `110` status `ready` deltaP `8.2151` edge `0.106` maxDD `-1.9651`
- `market_context_high->equity_4h` score `0.874` n `110` status `ready` deltaP `12.1341` edge `0.1693` maxDD `-6.3852`
- `market_context_high->crypto_major_1h` score `0.5685` n `110` status `ready` deltaP `7.368` edge `0.1276` maxDD `-5.6406`
- `market_context_high->index_4h` score `0.5137` n `110` status `ready` deltaP `10.7733` edge `0.0403` maxDD `-0.7006`
- `market_context_high->crypto_alt_1h` score `0.49` n `110` status `ready` deltaP `8.7697` edge `0.1066` maxDD `-5.5126`
- `market_context_high->equity_1h` score `0.2682` n `110` status `ready` deltaP `4.9837` edge `0.0609` maxDD `-2.779`
- `market_context_high->metal_1h` score `-0.2095` n `110` status `ready` deltaP `0.0952` edge `0.0305` maxDD `-1.3057`
- `market_context_high->commodity_1h` score `-0.2113` n `110` status `ready` deltaP `3.4322` edge `0.016` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.5079` n `110` status `ready` deltaP `-0.1388` edge `0.0113` maxDD `-0.7054`
- `market_context_high->fx_4h` score `-0.7383` n `110` status `ready` deltaP `-0.1524` edge `0.0034` maxDD `-1.0967`
- `market_context_high->commodity_4h` score `-0.7479` n `110` status `ready` deltaP `7.4916` edge `0.0064` maxDD `-4.4933`
- `market_context_high->fx_1h` score `-1.3729` n `110` status `ready` deltaP `-7.3163` edge `-0.0043` maxDD `-0.5734`
- `market_context_high->fx_24h` score `-1.5639` n `92` status `ready` deltaP `-3.3892` edge `-0.0067` maxDD `-2.749`
- `market_context_high->commodity_24h` score `-4.5224` n `92` status `ready` deltaP `16.7874` edge `0.0221` maxDD `-27.5371`
- `market_context_high->index_24h` score `-4.5415` n `92` status `ready` deltaP `-5.5178` edge `-0.1369` maxDD `-24.6845`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
