# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T05:52:32.201541+00:00`
- Price records: `672`
- Market context records: `4487`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11073`

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

- `risk_on_high->unknown_4h` score `124.2321` n `49` status `ready` deltaP `4.0256` edge `10.5089` maxDD `-10.9781`
- `risk_on_and_context->unknown_4h` score `124.2321` n `49` status `ready` deltaP `4.0256` edge `10.5089` maxDD `-10.9781`
- `market_context_high->unknown_1h` score `34.7733` n `220` status `ready` deltaP `3.318` edge `3.0262` maxDD `-9.7103`
- `market_context_high->unknown_4h` score `16.1567` n `220` status `ready` deltaP `3.265` edge `1.8711` maxDD `-36.0512`
- `risk_on_high->equity_4h` score `4.4777` n `49` status `ready` deltaP `39.7866` edge `0.1079` maxDD `0.0`
- `risk_on_and_context->equity_4h` score `4.4777` n `49` status `ready` deltaP `39.7866` edge `0.1079` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `2.7807` n `49` status `ready` deltaP `21.8517` edge `0.1526` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `2.7807` n `49` status `ready` deltaP `21.8517` edge `0.1526` maxDD `-2.6576`
- `risk_on_high->unknown_24h` score `2.2323` n `49` status `ready` deltaP `13.5381` edge `0.1761` maxDD `-5.0928`
- `risk_on_and_context->unknown_24h` score `2.2323` n `49` status `ready` deltaP `13.5381` edge `0.1761` maxDD `-5.0928`
- `risk_on_high->metal_24h` score `2.0692` n `49` status `ready` deltaP `-15.4797` edge `0.4664` maxDD `-4.834`
- `risk_on_and_context->metal_24h` score `2.0692` n `49` status `ready` deltaP `-15.4797` edge `0.4664` maxDD `-4.834`
- `risk_on_high->metal_4h` score `1.7064` n `49` status `ready` deltaP `13.6293` edge `0.0849` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `1.7064` n `49` status `ready` deltaP `13.6293` edge `0.0849` maxDD `-1.3516`
- `risk_on_high->equity_1h` score `1.2812` n `49` status `ready` deltaP `15.74` edge `0.0361` maxDD `-0.7415`
- `risk_on_and_context->equity_1h` score `1.2812` n `49` status `ready` deltaP `15.74` edge `0.0361` maxDD `-0.7415`
- `risk_on_high->fx_4h` score `0.6327` n `49` status `ready` deltaP `15.7043` edge `0.0071` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.6327` n `49` status `ready` deltaP `15.7043` edge `0.0071` maxDD `-0.3925`
- `risk_on_high->fx_1h` score `0.3387` n `49` status `ready` deltaP `7.1978` edge `0.0032` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.3387` n `49` status `ready` deltaP `7.1978` edge `0.0032` maxDD `-0.1704`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
