# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-11T16:37:34.898896+00:00`
- Price records: `672`
- Market context records: `3601`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13138`

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

- `risk_on_high->crypto_major_24h` score `46.0998` n `32` status `ready` deltaP `49.6528` edge `3.5149` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `46.0998` n `32` status `ready` deltaP `49.6528` edge `3.5149` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `42.6412` n `32` status `ready` deltaP `51.2153` edge `3.212` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `42.6412` n `32` status `ready` deltaP `51.2153` edge `3.212` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `39.3359` n `32` status `ready` deltaP `48.7847` edge `2.9679` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `39.3359` n `32` status `ready` deltaP `48.7847` edge `2.9679` maxDD `-0.8779`
- `risk_on_high->index_24h` score `24.9385` n `32` status `ready` deltaP `51.7361` edge `1.7333` maxDD `0.0`
- `risk_on_and_context->index_24h` score `24.9385` n `32` status `ready` deltaP `51.7361` edge `1.7333` maxDD `0.0`
- `risk_on_high->metal_24h` score `17.9392` n `32` status `ready` deltaP `36.8056` edge `1.2757` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `17.9392` n `32` status `ready` deltaP `36.8056` edge `1.2757` maxDD `-0.7574`
- `market_context_high->equity_24h` score `16.9973` n `156` status `ready` deltaP `28.1384` edge `1.8701` maxDD `-40.9667`
- `market_context_high->index_24h` score `13.5538` n `156` status `ready` deltaP `36.3515` edge `1.1088` maxDD `-15.0661`
- `risk_on_high->crypto_major_4h` score `13.3987` n `32` status `ready` deltaP `25.1524` edge `1.0611` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `13.3987` n `32` status `ready` deltaP `25.1524` edge `1.0611` maxDD `-5.9781`
- `market_context_high->crypto_major_24h` score `10.6657` n `156` status `ready` deltaP `14.9573` edge `1.5622` maxDD `-54.8486`
- `market_context_high->metal_24h` score `7.152` n `156` status `ready` deltaP `30.8761` edge `1.1651` maxDD `-25.9879`
- `market_context_high->crypto_alt_24h` score `5.2488` n `156` status `ready` deltaP `8.961` edge `1.1819` maxDD `-56.6728`
- `risk_on_high->crypto_alt_4h` score `5.2019` n `32` status `ready` deltaP `5.7165` edge `0.5798` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `5.2019` n `32` status `ready` deltaP `5.7165` edge `0.5798` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.7009` n `32` status `ready` deltaP `15.1677` edge `0.4868` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
