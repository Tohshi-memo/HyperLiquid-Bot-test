# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T19:37:30.128427+00:00`
- Price records: `672`
- Market context records: `4859`
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

- `market_context_high->unknown_1h` score `13.473` n `110` status `ready` deltaP `10.3212` edge `1.0957` maxDD `-1.674`
- `market_context_high->unknown_4h` score `10.1684` n `108` status `ready` deltaP `25.0339` edge `0.7336` maxDD `-1.917`
- `market_context_high->crypto_alt_4h` score `6.1976` n `108` status `ready` deltaP `19.6195` edge `0.5209` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `5.9414` n `108` status `ready` deltaP `16.8191` edge `0.5054` maxDD `-7.1265`
- `market_context_high->unknown_24h` score `5.1749` n `91` status `ready` deltaP `25.4693` edge `0.2957` maxDD `-1.4072`
- `market_context_high->metal_4h` score `1.3577` n `108` status `ready` deltaP `10.1061` edge `0.112` maxDD `-1.9651`
- `market_context_high->equity_4h` score `0.7868` n `108` status `ready` deltaP `11.2523` edge `0.164` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.5001` n `108` status `ready` deltaP `10.6313` edge `0.0395` maxDD `-0.7006`
- `market_context_high->crypto_major_1h` score `0.4383` n `110` status `ready` deltaP `6.3201` edge `0.1179` maxDD `-5.6406`
- `market_context_high->crypto_alt_1h` score `0.3825` n `110` status `ready` deltaP `7.7218` edge `0.0998` maxDD `-5.5126`
- `market_context_high->equity_1h` score `0.2106` n `110` status `ready` deltaP `4.0855` edge `0.0595` maxDD `-2.779`
- `market_context_high->metal_1h` score `-0.1588` n `110` status `ready` deltaP `0.9934` edge `0.031` maxDD `-1.3057`
- `market_context_high->commodity_1h` score `-0.2028` n `110` status `ready` deltaP `3.5819` edge `0.0161` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.49` n `110` status `ready` deltaP `0.3103` edge `0.0106` maxDD `-0.7054`
- `market_context_high->fx_4h` score `-0.5392` n `108` status `ready` deltaP `1.993` edge `0.006` maxDD `-1.0729`
- `market_context_high->commodity_4h` score `-0.7154` n `108` status `ready` deltaP `7.5881` edge `0.0071` maxDD `-4.384`
- `market_context_high->fx_1h` score `-1.3322` n `110` status `ready` deltaP `-6.8672` edge `-0.0039` maxDD `-0.5734`
- `market_context_high->fx_24h` score `-1.949` n `91` status `ready` deltaP `-7.3776` edge `-0.0122` maxDD `-2.749`
- `market_context_high->index_24h` score `-4.8541` n `91` status `ready` deltaP `-9.0545` edge `-0.1534` maxDD `-24.6845`
- `market_context_high->commodity_24h` score `-5.4678` n `91` status `ready` deltaP `10.1591` edge `-0.0125` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
