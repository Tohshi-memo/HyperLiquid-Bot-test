# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-09T04:07:24.005882+00:00`
- Price records: `672`
- Market context records: `3346`
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

- `risk_on_high->crypto_major_24h` score `59.1195` n `32` status `ready` deltaP `63.1944` edge `4.5096` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `59.1195` n `32` status `ready` deltaP `63.1944` edge `4.5096` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `54.8649` n `32` status `ready` deltaP `57.8125` edge `4.2018` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `54.8649` n `32` status `ready` deltaP `57.8125` edge `4.2018` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `46.7001` n `32` status `ready` deltaP `56.7708` edge `3.5132` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `46.7001` n `32` status `ready` deltaP `56.7708` edge `3.5132` maxDD `0.0`
- `risk_on_high->index_24h` score `23.2094` n `32` status `ready` deltaP `50.8681` edge `1.595` maxDD `0.0`
- `risk_on_and_context->index_24h` score `23.2094` n `32` status `ready` deltaP `50.8681` edge `1.595` maxDD `0.0`
- `risk_on_high->metal_24h` score `16.0969` n `32` status `ready` deltaP `36.1111` edge `1.1268` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `16.0969` n `32` status `ready` deltaP `36.1111` edge `1.1268` maxDD `-0.7574`
- `risk_on_high->crypto_major_4h` score `16.0885` n `32` status `ready` deltaP `30.3354` edge `1.2507` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `16.0885` n `32` status `ready` deltaP `30.3354` edge `1.2507` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `12.6571` n `160` status `ready` deltaP `17.8125` edge `2.4881` maxDD `-70.3986`
- `market_context_high->index_24h` score `12.0057` n `160` status `ready` deltaP `35.8681` edge `1.0168` maxDD `-16.1026`
- `market_context_high->equity_24h` score `10.708` n `160` status `ready` deltaP `31.1458` edge `2.0068` maxDD `-53.663`
- `risk_on_high->crypto_alt_4h` score `7.9219` n `32` status `ready` deltaP `10.1372` edge `0.777` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.9219` n `32` status `ready` deltaP `10.1372` edge `0.777` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.7325` n `32` status `ready` deltaP `14.7104` edge `0.4939` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.7325` n `32` status `ready` deltaP `14.7104` edge `0.4939` maxDD `-5.7426`
- `risk_on_high->crypto_major_1h` score `2.1313` n `32` status `ready` deltaP `7.0172` edge `0.3334` maxDD `-5.8885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
