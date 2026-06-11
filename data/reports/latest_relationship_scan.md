# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-11T07:37:31.151411+00:00`
- Price records: `672`
- Market context records: `3563`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13076`

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

- `risk_on_high->crypto_major_24h` score `50.3821` n `32` status `ready` deltaP `55.1072` edge `3.8354` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `50.3821` n `32` status `ready` deltaP `55.1072` edge `3.8354` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `44.89` n `32` status `ready` deltaP `54.7606` edge `3.3909` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `44.89` n `32` status `ready` deltaP `54.7606` edge `3.3909` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `44.4364` n `32` status `ready` deltaP `53.8995` edge `3.3437` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `44.4364` n `32` status `ready` deltaP `53.8995` edge `3.3437` maxDD `0.0`
- `risk_on_high->index_24h` score `25.5952` n `32` status `ready` deltaP `53.8995` edge `1.7736` maxDD `0.0`
- `risk_on_and_context->index_24h` score `25.5952` n `32` status `ready` deltaP `53.8995` edge `1.7736` maxDD `0.0`
- `market_context_high->equity_24h` score `18.7924` n `156` status `ready` deltaP `30.8226` edge `2.0018` maxDD `-40.9667`
- `risk_on_high->metal_24h` score `18.6823` n `32` status `ready` deltaP `37.0342` edge `1.3361` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `18.6823` n `32` status `ready` deltaP `37.0342` edge `1.3361` maxDD `-0.7574`
- `market_context_high->crypto_major_24h` score `14.948` n `156` status `ready` deltaP `20.4117` edge `1.8827` maxDD `-54.8486`
- `market_context_high->index_24h` score `14.2105` n `156` status `ready` deltaP `38.5149` edge `1.1491` maxDD `-15.0661`
- `risk_on_high->crypto_major_4h` score `13.3113` n `32` status `ready` deltaP `25.3049` edge `1.0528` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `13.3113` n `32` status `ready` deltaP `25.3049` edge `1.0528` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `10.8028` n `156` status `ready` deltaP `14.9369` edge `1.6049` maxDD `-56.6728`
- `market_context_high->metal_24h` score `7.635` n `156` status `ready` deltaP `31.1047` edge `1.2255` maxDD `-25.9879`
- `risk_on_high->crypto_alt_4h` score `4.8261` n `32` status `ready` deltaP `5.564` edge `0.5495` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `4.8261` n `32` status `ready` deltaP `5.564` edge `0.5495` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.5718` n `32` status `ready` deltaP `14.7104` edge `0.4733` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
