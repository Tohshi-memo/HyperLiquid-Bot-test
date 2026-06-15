# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T19:22:34.496864+00:00`
- Price records: `672`
- Market context records: `4019`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10566`

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

- `risk_on_high->unknown_4h` score `146.3643` n `40` status `ready` deltaP `-5.3615` edge `12.4144` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `146.3643` n `40` status `ready` deltaP `-5.3615` edge `12.4144` maxDD `-10.864`
- `market_context_high->unknown_24h` score `48.5654` n `134` status `ready` deltaP `-4.2927` edge `4.4786` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `26.3643` n `145` status `ready` deltaP `1.9661` edge `2.7262` maxDD `-35.7161`
- `risk_on_high->equity_24h` score `6.5821` n `40` status `ready` deltaP `38.8215` edge `0.2897` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `6.5821` n `40` status `ready` deltaP `38.8215` edge `0.2897` maxDD `0.0`
- `market_context_high->index_24h` score `3.6552` n `134` status `ready` deltaP `25.7702` edge `0.154` maxDD `-1.3629`
- `risk_on_high->equity_4h` score `3.3852` n `40` status `ready` deltaP `35.704` edge `0.0488` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `3.3852` n `40` status `ready` deltaP `35.704` edge `0.0488` maxDD `-0.0446`
- `market_context_high->metal_24h` score `2.654` n `134` status `ready` deltaP `13.7808` edge `0.228` maxDD `-4.8962`
- `market_context_high->equity_4h` score `1.6856` n `145` status `ready` deltaP `18.8937` edge `0.1426` maxDD `-6.9137`
- `market_context_high->equity_1h` score `1.2381` n `149` status `ready` deltaP `8.4365` edge `0.1029` maxDD `-2.144`
- `risk_on_high->index_24h` score `1.2129` n `40` status `ready` deltaP `26.5165` edge `-0.0757` maxDD `0.0`
- `risk_on_and_context->index_24h` score `1.2129` n `40` status `ready` deltaP `26.5165` edge `-0.0757` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `1.05` n `40` status `ready` deltaP `18.9231` edge `0.0279` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.05` n `40` status `ready` deltaP `18.9231` edge `0.0279` maxDD `-2.6576`
- `risk_on_high->commodity_24h` score `0.9584` n `40` status `ready` deltaP `4.2028` edge `0.28` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `0.9584` n `40` status `ready` deltaP `4.2028` edge `0.28` maxDD `-12.9187`
- `market_context_high->crypto_major_1h` score `0.9182` n `149` status `ready` deltaP `9.3498` edge `0.0684` maxDD `-2.3372`
- `market_context_high->crypto_major_4h` score `0.6663` n `145` status `ready` deltaP `16.0783` edge `0.105` maxDD `-7.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
