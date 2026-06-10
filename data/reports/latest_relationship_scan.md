# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-10T19:56:52.506003+00:00`
- Price records: `672`
- Market context records: `3514`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13184`

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

- `risk_on_high->crypto_major_24h` score `53.8284` n `32` status `ready` deltaP `57.8802` edge `4.1041` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `53.8284` n `32` status `ready` deltaP `57.8802` edge `4.1041` maxDD `-0.0083`
- `risk_on_high->crypto_alt_24h` score `50.0582` n `32` status `ready` deltaP `57.5336` edge `3.8031` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `50.0582` n `32` status `ready` deltaP `57.5336` edge `3.8031` maxDD `-0.8779`
- `risk_on_high->equity_24h` score `44.2566` n `32` status `ready` deltaP `54.5927` edge `3.3241` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `44.2566` n `32` status `ready` deltaP `54.5927` edge `3.3241` maxDD `0.0`
- `risk_on_high->index_24h` score `24.5154` n `32` status `ready` deltaP `51.4731` edge `1.6998` maxDD `0.0`
- `risk_on_and_context->index_24h` score `24.5154` n `32` status `ready` deltaP `51.4731` edge `1.6998` maxDD `0.0`
- `market_context_high->equity_24h` score `18.6127` n `156` status `ready` deltaP `31.5158` edge `1.9822` maxDD `-40.9667`
- `market_context_high->crypto_major_24h` score `18.3943` n `156` status `ready` deltaP `23.1847` edge `2.1514` maxDD `-54.8486`
- `risk_on_high->metal_24h` score `16.9422` n `32` status `ready` deltaP `33.568` edge `1.2142` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `16.9422` n `32` status `ready` deltaP `33.568` edge `1.2142` maxDD `-0.7574`
- `market_context_high->crypto_alt_24h` score `15.9711` n `156` status `ready` deltaP `17.7099` edge `2.0171` maxDD `-56.6728`
- `risk_on_high->crypto_major_4h` score `15.0321` n `32` status `ready` deltaP `28.1107` edge `1.1775` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.0321` n `32` status `ready` deltaP `28.1107` edge `1.1775` maxDD `-5.9781`
- `market_context_high->index_24h` score `13.1308` n `156` status `ready` deltaP `36.0885` edge `1.0753` maxDD `-15.0661`
- `risk_on_high->crypto_alt_4h` score `7.3743` n `32` status `ready` deltaP `9.4416` edge `0.736` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.3743` n `32` status `ready` deltaP `9.4416` edge `0.736` maxDD `-11.7537`
- `market_context_high->metal_24h` score `6.504` n `156` status `ready` deltaP `27.6385` edge `1.1036` maxDD `-25.9879`
- `risk_on_high->equity_4h` score `3.8141` n `32` status `ready` deltaP `16.3099` edge `0.4937` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
