# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-09T04:22:27.257804+00:00`
- Price records: `672`
- Market context records: `3347`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13151`

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

- `risk_on_high->crypto_major_24h` score `58.9712` n `32` status `ready` deltaP `63.0208` edge `4.4984` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `58.9712` n `32` status `ready` deltaP `63.0208` edge `4.4984` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `54.7761` n `32` status `ready` deltaP `57.8125` edge `4.1944` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `54.7761` n `32` status `ready` deltaP `57.8125` edge `4.1944` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `46.6845` n `32` status `ready` deltaP `56.7708` edge `3.5119` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `46.6845` n `32` status `ready` deltaP `56.7708` edge `3.5119` maxDD `0.0`
- `risk_on_high->index_24h` score `23.219` n `32` status `ready` deltaP `50.8681` edge `1.5958` maxDD `0.0`
- `risk_on_and_context->index_24h` score `23.219` n `32` status `ready` deltaP `50.8681` edge `1.5958` maxDD `0.0`
- `risk_on_high->metal_24h` score `16.0794` n `32` status `ready` deltaP `35.9375` edge `1.1265` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `16.0794` n `32` status `ready` deltaP `35.9375` edge `1.1265` maxDD `-0.7574`
- `risk_on_high->crypto_major_4h` score `16.0789` n `32` status `ready` deltaP `30.3354` edge `1.2499` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `16.0789` n `32` status `ready` deltaP `30.3354` edge `1.2499` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `12.5373` n `161` status `ready` deltaP `17.4592` edge `2.4751` maxDD `-70.3986`
- `market_context_high->index_24h` score `12.0671` n `161` status `ready` deltaP `35.9613` edge `1.0213` maxDD `-16.1026`
- `market_context_high->equity_24h` score `10.767` n `161` status `ready` deltaP `31.305` edge `2.0133` maxDD `-53.663`
- `risk_on_high->crypto_alt_4h` score `7.9243` n `32` status `ready` deltaP `10.1372` edge `0.7772` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.9243` n `32` status `ready` deltaP `10.1372` edge `0.7772` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.7301` n `32` status `ready` deltaP `14.7104` edge `0.4936` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.7301` n `32` status `ready` deltaP `14.7104` edge `0.4936` maxDD `-5.7426`
- `risk_on_high->crypto_major_1h` score `2.1289` n `32` status `ready` deltaP `7.0172` edge `0.3331` maxDD `-5.8885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
