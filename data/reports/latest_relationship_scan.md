# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-11T16:52:35.604293+00:00`
- Price records: `672`
- Market context records: `3602`
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

- `risk_on_high->crypto_major_24h` score `45.9323` n `32` status `ready` deltaP `49.4792` edge `3.5021` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `45.9323` n `32` status `ready` deltaP `49.4792` edge `3.5021` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `42.5212` n `32` status `ready` deltaP `51.2153` edge `3.202` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `42.5212` n `32` status `ready` deltaP `51.2153` edge `3.202` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `39.124` n `32` status `ready` deltaP `48.6111` edge `2.9514` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `39.124` n `32` status `ready` deltaP `48.6111` edge `2.9514` maxDD `-0.8779`
- `risk_on_high->index_24h` score `24.8574` n `32` status `ready` deltaP `51.5625` edge `1.7277` maxDD `0.0`
- `risk_on_and_context->index_24h` score `24.8574` n `32` status `ready` deltaP `51.5625` edge `1.7277` maxDD `0.0`
- `risk_on_high->metal_24h` score `17.8672` n `32` status `ready` deltaP `36.8056` edge `1.2697` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `17.8672` n `32` status `ready` deltaP `36.8056` edge `1.2697` maxDD `-0.7574`
- `market_context_high->equity_24h` score `16.7589` n `157` status `ready` deltaP `27.6484` edge `1.8535` maxDD `-40.9667`
- `market_context_high->index_24h` score `13.465` n `157` status `ready` deltaP `36.2759` edge `1.1019` maxDD `-15.0661`
- `risk_on_high->crypto_major_4h` score `13.4011` n `32` status `ready` deltaP `25.1524` edge `1.0613` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `13.4011` n `32` status `ready` deltaP `25.1524` edge `1.0613` maxDD `-5.9781`
- `market_context_high->crypto_major_24h` score `10.4779` n `157` status `ready` deltaP `15.0246` edge `1.5461` maxDD `-54.8486`
- `market_context_high->metal_24h` score `7.0509` n `157` status `ready` deltaP `30.476` edge `1.1548` maxDD `-25.9879`
- `risk_on_high->crypto_alt_4h` score `5.1789` n `32` status `ready` deltaP `5.564` edge `0.5789` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `5.1789` n `32` status `ready` deltaP `5.564` edge `0.5789` maxDD `-11.7537`
- `market_context_high->crypto_alt_24h` score `5.078` n `157` status `ready` deltaP `9.0609` edge `1.167` maxDD `-56.6728`
- `risk_on_high->equity_4h` score `3.6843` n `32` status `ready` deltaP `15.0152` edge `0.4857` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
