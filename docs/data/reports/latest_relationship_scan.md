# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-11T19:52:40.634620+00:00`
- Price records: `672`
- Market context records: `3616`
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

- `risk_on_high->crypto_major_24h` score `43.236` n `32` status `ready` deltaP `47.3958` edge `3.2913` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `43.236` n `32` status `ready` deltaP `47.3958` edge `3.2913` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `40.3171` n `32` status `ready` deltaP `49.4792` edge `3.0299` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `40.3171` n `32` status `ready` deltaP `49.4792` edge `3.0299` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `36.0557` n `32` status `ready` deltaP `46.5278` edge `2.7096` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `36.0557` n `32` status `ready` deltaP `46.5278` edge `2.7096` maxDD `-0.8779`
- `risk_on_high->index_24h` score `23.4391` n `32` status `ready` deltaP `49.4792` edge `1.6234` maxDD `0.0`
- `risk_on_and_context->index_24h` score `23.4391` n `32` status `ready` deltaP `49.4792` edge `1.6234` maxDD `0.0`
- `risk_on_high->metal_24h` score `16.2643` n `32` status `ready` deltaP `35.0694` edge `1.1477` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `16.2643` n `32` status `ready` deltaP `35.0694` edge `1.1477` maxDD `-0.7574`
- `market_context_high->equity_24h` score `14.5871` n `158` status `ready` deltaP `26.0615` edge `1.6831` maxDD `-40.9667`
- `risk_on_high->crypto_major_4h` score `12.7871` n `32` status `ready` deltaP `23.628` edge `1.0203` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `12.7871` n `32` status `ready` deltaP `23.628` edge `1.0203` maxDD `-5.9781`
- `market_context_high->index_24h` score `12.0892` n `158` status `ready` deltaP `34.2893` edge `1.0005` maxDD `-15.0661`
- `market_context_high->crypto_major_24h` score `7.9134` n `158` status `ready` deltaP `13.179` edge `1.3447` maxDD `-54.8486`
- `market_context_high->metal_24h` score `6.0962` n `158` status `ready` deltaP `28.9776` edge `1.0424` maxDD `-25.9879`
- `risk_on_high->crypto_alt_4h` score `4.4295` n `32` status `ready` deltaP `4.1921` edge `0.5256` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `4.4295` n `32` status `ready` deltaP `4.1921` edge `0.5256` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.2931` n `32` status `ready` deltaP `13.4909` edge `0.4457` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.2931` n `32` status `ready` deltaP `13.4909` edge `0.4457` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
