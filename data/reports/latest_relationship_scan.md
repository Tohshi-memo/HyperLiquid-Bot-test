# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-30T20:37:27.571608+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11706`

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

- `risk_on_high->crypto_alt_24h` score `25.6165` n `42` status `ready` deltaP `50.5208` edge `1.7979` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `25.6165` n `42` status `ready` deltaP `50.5208` edge `1.7979` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `15.7356` n `42` status `ready` deltaP `44.4444` edge `1.015` maxDD `0.0`
- `risk_on_and_context->crypto_major_24h` score `15.7356` n `42` status `ready` deltaP `44.4444` edge `1.015` maxDD `0.0`
- `risk_on_high->unknown_4h` score `9.0888` n `72` status `ready` deltaP `28.6416` edge `0.6093` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `9.0888` n `72` status `ready` deltaP `28.6416` edge `0.6093` maxDD `-1.0945`
- `risk_on_high->fx_24h` score `6.3106` n `42` status `ready` deltaP `71.0069` edge `0.0525` maxDD `0.0`
- `risk_on_and_context->fx_24h` score `6.3106` n `42` status `ready` deltaP `71.0069` edge `0.0525` maxDD `0.0`
- `risk_on_high->metal_24h` score `6.1971` n `42` status `ready` deltaP `53.2986` edge `0.1611` maxDD `0.0`
- `risk_on_and_context->metal_24h` score `6.1971` n `42` status `ready` deltaP `53.2986` edge `0.1611` maxDD `0.0`
- `risk_on_high->equity_24h` score `6.0542` n `42` status `ready` deltaP `39.0625` edge `0.2441` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `6.0542` n `42` status `ready` deltaP `39.0625` edge `0.2441` maxDD `0.0`
- `market_context_high->unknown_4h` score `5.1641` n `149` status `ready` deltaP `21.054` edge `0.337` maxDD `-1.0945`
- `risk_on_high->crypto_major_4h` score `4.9221` n `72` status `ready` deltaP `26.101` edge `0.271` maxDD `-1.1199`
- `risk_on_and_context->crypto_major_4h` score `4.9221` n `72` status `ready` deltaP `26.101` edge `0.271` maxDD `-1.1199`
- `market_context_high->metal_24h` score `4.5761` n `117` status `ready` deltaP `37.0593` edge `0.2362` maxDD `-3.1535`
- `risk_on_high->crypto_alt_4h` score `4.4118` n `72` status `ready` deltaP `17.7507` edge `0.2976` maxDD `-1.5298`
- `risk_on_and_context->crypto_alt_4h` score `4.4118` n `72` status `ready` deltaP `17.7507` edge `0.2976` maxDD `-1.5298`
- `risk_on_high->equity_4h` score `3.4896` n `72` status `ready` deltaP `31.9952` edge `0.0965` maxDD `-0.187`
- `risk_on_and_context->equity_4h` score `3.4896` n `72` status `ready` deltaP `31.9952` edge `0.0965` maxDD `-0.187`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
