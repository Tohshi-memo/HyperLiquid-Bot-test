# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T22:37:36.550346+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10650`

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

- `risk_on_high->unknown_4h` score `19.9339` n `133` status `ready` deltaP `8.9985` edge `1.663` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `19.9339` n `133` status `ready` deltaP `8.9985` edge `1.663` maxDD `-2.2797`
- `risk_on_high->unknown_1h` score `10.2981` n `133` status `ready` deltaP `-1.5027` edge `0.9259` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `10.2981` n `133` status `ready` deltaP `-1.5027` edge `0.9259` maxDD `-1.95`
- `market_context_high->unknown_4h` score `9.4364` n `217` status `ready` deltaP `9.4351` edge `0.793` maxDD `-2.563`
- `market_context_high->unknown_1h` score `7.5196` n `217` status `ready` deltaP `-0.5568` edge `0.6934` maxDD `-2.0446`
- `news_risk_high->crypto_alt_24h` score `4.5299` n `46` status `ready` deltaP `21.2334` edge `0.2629` maxDD `-0.8236`
- `news_risk_high->crypto_major_4h` score `2.3327` n `46` status `ready` deltaP `10.1869` edge `0.1748` maxDD `-1.5324`
- `news_risk_high->commodity_24h` score `1.9498` n `46` status `ready` deltaP `11.1715` edge `0.1052` maxDD `-0.042`
- `news_risk_high->metal_4h` score `1.6863` n `46` status `ready` deltaP `17.7757` edge `0.0483` maxDD `-0.7692`
- `news_risk_high->equity_1h` score `1.6207` n `46` status `ready` deltaP `15.6795` edge `0.0696` maxDD `-0.7924`
- `news_risk_high->commodity_4h` score `1.4535` n `46` status `ready` deltaP `9.9615` edge `0.0748` maxDD `-0.2737`
- `news_risk_high->index_1h` score `1.1217` n `46` status `ready` deltaP `14.3973` edge `0.0109` maxDD `-0.0724`
- `news_risk_high->metal_1h` score `0.7532` n `46` status `ready` deltaP `9.672` edge `0.0176` maxDD `-0.2118`
- `news_risk_high->crypto_alt_1h` score `0.2695` n `46` status `ready` deltaP `4.5041` edge `0.0227` maxDD `-1.0885`
- `news_risk_high->fx_4h` score `0.2665` n `46` status `ready` deltaP `10.1007` edge `0.0001` maxDD `-0.9514`
- `news_risk_high->commodity_1h` score `0.2233` n `46` status `ready` deltaP `8.93` edge `0.0037` maxDD `-0.9036`
- `news_risk_high->crypto_major_1h` score `0.1403` n `46` status `ready` deltaP `0.5272` edge `0.0437` maxDD `-1.0047`
- `risk_on_high->metal_1h` score `0.114` n `133` status `ready` deltaP `12.7122` edge `0.0011` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.114` n `133` status `ready` deltaP `12.7122` edge `0.0011` maxDD `-1.699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
