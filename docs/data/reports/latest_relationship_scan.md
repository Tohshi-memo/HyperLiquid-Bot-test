# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-11T20:37:37.286724+00:00`
- Price records: `672`
- Market context records: `3619`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13162`

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

- `risk_on_high->crypto_major_24h` score `42.5368` n `32` status `ready` deltaP `46.875` edge `3.2365` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `42.5368` n `32` status `ready` deltaP `46.875` edge `3.2365` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `39.6335` n `32` status `ready` deltaP `48.9583` edge `2.9764` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `39.6335` n `32` status `ready` deltaP `48.9583` edge `2.9764` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `35.2521` n `32` status `ready` deltaP `46.0069` edge `2.6461` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `35.2521` n `32` status `ready` deltaP `46.0069` edge `2.6461` maxDD `-0.8779`
- `risk_on_high->index_24h` score `22.9727` n `32` status `ready` deltaP `48.9583` edge `1.588` maxDD `0.0`
- `risk_on_and_context->index_24h` score `22.9727` n `32` status `ready` deltaP `48.9583` edge `1.588` maxDD `0.0`
- `risk_on_high->metal_24h` score `15.7079` n `32` status `ready` deltaP `34.5486` edge `1.1048` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `15.7079` n `32` status `ready` deltaP `34.5486` edge `1.1048` maxDD `-0.7574`
- `market_context_high->equity_24h` score `13.9034` n `158` status `ready` deltaP `25.5406` edge `1.6296` maxDD `-40.9667`
- `risk_on_high->crypto_major_4h` score `12.6353` n `32` status `ready` deltaP `23.1707` edge `1.0107` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `12.6353` n `32` status `ready` deltaP `23.1707` edge `1.0107` maxDD `-5.9781`
- `market_context_high->index_24h` score `11.6228` n `158` status `ready` deltaP `33.7684` edge `0.9651` maxDD `-15.0661`
- `market_context_high->crypto_major_24h` score `7.2142` n `158` status `ready` deltaP `12.6582` edge `1.2899` maxDD `-54.8486`
- `market_context_high->metal_24h` score `5.7345` n `158` status `ready` deltaP `28.4568` edge `0.9995` maxDD `-25.9879`
- `risk_on_high->crypto_alt_4h` score `4.2585` n `32` status `ready` deltaP `3.7348` edge `0.5144` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `4.2585` n `32` status `ready` deltaP `3.7348` edge `0.5144` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.1585` n `32` status `ready` deltaP `13.0335` edge `0.4315` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.1585` n `32` status `ready` deltaP `13.0335` edge `0.4315` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
