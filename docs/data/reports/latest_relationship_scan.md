# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-11T05:52:32.973097+00:00`
- Price records: `672`
- Market context records: `3556`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13250`

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

- `risk_on_high->crypto_major_24h` score `51.5304` n `32` status `ready` deltaP `56.3204` edge `3.923` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `51.5304` n `32` status `ready` deltaP `56.3204` edge `3.923` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `46.2014` n `32` status `ready` deltaP `55.9738` edge `3.4921` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `46.2014` n `32` status `ready` deltaP `55.9738` edge `3.4921` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `44.6656` n `32` status `ready` deltaP `53.8995` edge `3.3628` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `44.6656` n `32` status `ready` deltaP `53.8995` edge `3.3628` maxDD `0.0`
- `risk_on_high->index_24h` score `25.6024` n `32` status `ready` deltaP `53.8995` edge `1.7742` maxDD `0.0`
- `risk_on_and_context->index_24h` score `25.6024` n `32` status `ready` deltaP `53.8995` edge `1.7742` maxDD `0.0`
- `market_context_high->equity_24h` score `19.0216` n `156` status `ready` deltaP `30.8226` edge `2.0209` maxDD `-40.9667`
- `risk_on_high->metal_24h` score `18.6307` n `32` status `ready` deltaP `37.0342` edge `1.3318` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `18.6307` n `32` status `ready` deltaP `37.0342` edge `1.3318` maxDD `-0.7574`
- `market_context_high->crypto_major_24h` score `16.0963` n `156` status `ready` deltaP `21.6249` edge `1.9703` maxDD `-54.8486`
- `market_context_high->index_24h` score `14.2177` n `156` status `ready` deltaP `38.5149` edge `1.1497` maxDD `-15.0661`
- `risk_on_high->crypto_major_4h` score `13.8994` n `32` status `ready` deltaP `26.372` edge `1.0947` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `13.8994` n `32` status `ready` deltaP `26.372` edge `1.0947` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `12.1143` n `156` status `ready` deltaP `16.1501` edge `1.7061` maxDD `-56.6728`
- `market_context_high->metal_24h` score `7.6015` n `156` status `ready` deltaP `31.1047` edge `1.2212` maxDD `-25.9879`
- `risk_on_high->crypto_alt_4h` score `5.4886` n `32` status `ready` deltaP `6.6311` edge `0.5976` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `5.4886` n `32` status `ready` deltaP `6.6311` edge `0.5976` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.7996` n `32` status `ready` deltaP `15.7774` edge `0.4954` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
