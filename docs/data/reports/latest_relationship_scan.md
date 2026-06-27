# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T04:22:28.209862+00:00`
- Price records: `672`
- Market context records: `4897`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8584`

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

- `market_context_high->unknown_1h` score `14.8399` n `110` status `ready` deltaP `9.423` edge `1.2156` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.511` n `110` status `ready` deltaP `23.1624` edge `0.6913` maxDD `-1.917`
- `market_context_high->crypto_alt_4h` score `6.5134` n `110` status `ready` deltaP `21.3609` edge `0.5356` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `6.4466` n `110` status `ready` deltaP `18.9495` edge `0.5333` maxDD `-7.1265`
- `market_context_high->unknown_24h` score `5.3891` n `91` status `ready` deltaP `24.4277` edge `0.3205` maxDD `-1.4072`
- `market_context_high->metal_4h` score `1.1101` n `110` status `ready` deltaP `7.9102` edge `0.106` maxDD `-1.9651`
- `market_context_high->equity_4h` score `0.8992` n `110` status `ready` deltaP `12.439` edge `0.1705` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.5478` n `110` status `ready` deltaP `11.383` edge `0.0406` maxDD `-0.7006`
- `market_context_high->crypto_major_1h` score `0.4843` n `110` status `ready` deltaP `6.6195` edge `0.1218` maxDD `-5.6406`
- `market_context_high->crypto_alt_1h` score `0.437` n `110` status `ready` deltaP `8.3206` edge `0.1028` maxDD `-5.5126`
- `market_context_high->equity_1h` score `0.2192` n `110` status `ready` deltaP `4.2352` edge `0.0596` maxDD `-2.779`
- `market_context_high->metal_1h` score `-0.2258` n `110` status `ready` deltaP `-0.2042` edge `0.0304` maxDD `-1.3057`
- `market_context_high->commodity_1h` score `-0.2308` n `110` status `ready` deltaP `3.1328` edge `0.0155` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.5164` n `110` status `ready` deltaP `-0.2885` edge `0.0112` maxDD `-0.7054`
- `market_context_high->fx_4h` score `-0.7281` n `110` status `ready` deltaP `0.0` edge `0.0037` maxDD `-1.0967`
- `market_context_high->commodity_4h` score `-0.8196` n `110` status `ready` deltaP `6.7295` edge `0.0055` maxDD `-4.4933`
- `market_context_high->fx_1h` score `-1.3609` n `110` status `ready` deltaP `-7.1666` edge `-0.0043` maxDD `-0.5734`
- `market_context_high->fx_24h` score `-1.593` n `91` status `ready` deltaP `-3.5581` edge `-0.008` maxDD `-2.749`
- `market_context_high->index_24h` score `-4.551` n `91` status `ready` deltaP `-5.2351` edge `-0.14` maxDD `-24.6845`
- `market_context_high->commodity_24h` score `-4.6277` n `91` status `ready` deltaP `16.2355` edge `0.017` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
