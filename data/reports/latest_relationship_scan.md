# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T06:22:29.251295+00:00`
- Price records: `672`
- Market context records: `4906`
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

- `market_context_high->unknown_1h` score `14.5231` n `110` status `ready` deltaP `9.423` edge `1.1892` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.6456` n `110` status `ready` deltaP `23.3148` edge `0.7015` maxDD `-1.917`
- `market_context_high->crypto_alt_4h` score `6.5847` n `110` status `ready` deltaP `21.8182` edge `0.5385` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `6.4526` n `110` status `ready` deltaP `18.9495` edge `0.5338` maxDD `-7.1265`
- `market_context_high->unknown_24h` score `5.2848` n `92` status `ready` deltaP `23.6338` edge `0.3171` maxDD `-1.4072`
- `market_context_high->metal_4h` score `1.16` n `110` status `ready` deltaP `8.52` edge `0.1061` maxDD `-1.9651`
- `market_context_high->equity_4h` score `0.8629` n `110` status `ready` deltaP `11.9817` edge `0.1689` maxDD `-6.3852`
- `market_context_high->crypto_major_1h` score `0.5685` n `110` status `ready` deltaP `7.368` edge `0.1276` maxDD `-5.6406`
- `market_context_high->index_4h` score `0.5137` n `110` status `ready` deltaP `10.7733` edge `0.0403` maxDD `-0.7006`
- `market_context_high->crypto_alt_1h` score `0.4776` n `110` status `ready` deltaP `8.62` edge `0.106` maxDD `-5.5126`
- `market_context_high->equity_1h` score `0.2674` n `110` status `ready` deltaP `4.9837` edge `0.0608` maxDD `-2.779`
- `market_context_high->commodity_1h` score `-0.1942` n `110` status `ready` deltaP `3.7316` edge `0.0162` maxDD `-1.278`
- `market_context_high->metal_1h` score `-0.2087` n `110` status `ready` deltaP `0.0952` edge `0.0306` maxDD `-1.3057`
- `market_context_high->index_1h` score `-0.5079` n `110` status `ready` deltaP `-0.1388` edge `0.0113` maxDD `-0.7054`
- `market_context_high->fx_4h` score `-0.7376` n `110` status `ready` deltaP `-0.1524` edge `0.0035` maxDD `-1.0967`
- `market_context_high->commodity_4h` score `-0.7637` n `110` status `ready` deltaP `7.3392` edge `0.0061` maxDD `-4.4933`
- `market_context_high->fx_1h` score `-1.3729` n `110` status `ready` deltaP `-7.3163` edge `-0.0043` maxDD `-0.5734`
- `market_context_high->fx_24h` score `-1.55` n `92` status `ready` deltaP `-3.2156` edge `-0.0067` maxDD `-2.749`
- `market_context_high->commodity_24h` score `-4.479` n `92` status `ready` deltaP `17.1346` edge `0.0234` maxDD `-27.5371`
- `market_context_high->index_24h` score `-4.5627` n `92` status `ready` deltaP `-5.8651` edge `-0.1373` maxDD `-24.6845`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
