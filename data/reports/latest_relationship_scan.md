# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-10T23:07:27.719224+00:00`
- Price records: `672`
- Market context records: `3528`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13197`

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

- `risk_on_high->crypto_major_24h` score `53.4648` n `32` status `ready` deltaP `57.8802` edge `4.0738` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `53.4648` n `32` status `ready` deltaP `57.8802` edge `4.0738` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `49.115` n `32` status `ready` deltaP `57.5336` edge `3.7245` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `49.115` n `32` status `ready` deltaP `57.5336` edge `3.7245` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `44.6946` n `32` status `ready` deltaP `54.5927` edge `3.3606` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `44.6946` n `32` status `ready` deltaP `54.5927` edge `3.3606` maxDD `0.0`
- `risk_on_high->index_24h` score `25.1461` n `32` status `ready` deltaP `53.2062` edge `1.7408` maxDD `0.0`
- `risk_on_and_context->index_24h` score `25.1461` n `32` status `ready` deltaP `53.2062` edge `1.7408` maxDD `0.0`
- `market_context_high->equity_24h` score `19.0507` n `156` status `ready` deltaP `31.5158` edge `2.0187` maxDD `-40.9667`
- `risk_on_high->metal_24h` score `18.0921` n `32` status `ready` deltaP `35.8211` edge `1.295` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `18.0921` n `32` status `ready` deltaP `35.8211` edge `1.295` maxDD `-0.7574`
- `market_context_high->crypto_major_24h` score `18.0307` n `156` status `ready` deltaP `23.1847` edge `2.1211` maxDD `-54.8486`
- `market_context_high->crypto_alt_24h` score `15.0279` n `156` status `ready` deltaP `17.7099` edge `1.9385` maxDD `-56.6728`
- `risk_on_high->crypto_major_4h` score `14.9278` n `32` status `ready` deltaP `28.2012` edge `1.1682` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `14.9278` n `32` status `ready` deltaP `28.2012` edge `1.1682` maxDD `-5.9781`
- `market_context_high->index_24h` score `13.7614` n `156` status `ready` deltaP `37.8216` edge `1.1163` maxDD `-15.0661`
- `market_context_high->metal_24h` score `7.2514` n `156` status `ready` deltaP `29.8916` edge `1.1844` maxDD `-25.9879`
- `risk_on_high->crypto_alt_4h` score `7.2301` n `32` status `ready` deltaP `9.6799` edge `0.7224` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.2301` n `32` status `ready` deltaP `9.6799` edge `0.7224` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.9359` n `32` status `ready` deltaP `16.3872` edge `0.5088` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
