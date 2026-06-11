# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-11T20:08:10.466978+00:00`
- Price records: `672`
- Market context records: `3617`
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

- `risk_on_high->crypto_major_24h` score `42.9893` n `32` status `ready` deltaP `47.2222` edge `3.2719` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `42.9893` n `32` status `ready` deltaP `47.2222` edge `3.2719` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `40.0872` n `32` status `ready` deltaP `49.3056` edge `3.0119` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `40.0872` n `32` status `ready` deltaP `49.3056` edge `3.0119` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `35.7743` n `32` status `ready` deltaP `46.3542` edge `2.6873` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `35.7743` n `32` status `ready` deltaP `46.3542` edge `2.6873` maxDD `-0.8779`
- `risk_on_high->index_24h` score `23.286` n `32` status `ready` deltaP `49.3056` edge `1.6118` maxDD `0.0`
- `risk_on_and_context->index_24h` score `23.286` n `32` status `ready` deltaP `49.3056` edge `1.6118` maxDD `0.0`
- `risk_on_high->metal_24h` score `16.0825` n `32` status `ready` deltaP `34.8958` edge `1.1337` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `16.0825` n `32` status `ready` deltaP `34.8958` edge `1.1337` maxDD `-0.7574`
- `market_context_high->equity_24h` score `14.3572` n `158` status `ready` deltaP `25.8879` edge `1.6651` maxDD `-40.9667`
- `risk_on_high->crypto_major_4h` score `12.7317` n `32` status `ready` deltaP `23.4756` edge `1.0167` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `12.7317` n `32` status `ready` deltaP `23.4756` edge `1.0167` maxDD `-5.9781`
- `market_context_high->index_24h` score `11.9361` n `158` status `ready` deltaP `34.1157` edge `0.9889` maxDD `-15.0661`
- `market_context_high->crypto_major_24h` score `7.6667` n `158` status `ready` deltaP `13.0054` edge `1.3253` maxDD `-54.8486`
- `market_context_high->metal_24h` score `5.978` n `158` status `ready` deltaP `28.804` edge `1.0284` maxDD `-25.9879`
- `risk_on_high->crypto_alt_4h` score `4.3669` n `32` status `ready` deltaP `4.0396` edge `0.5214` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `4.3669` n `32` status `ready` deltaP `4.0396` edge `0.5214` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.2469` n `32` status `ready` deltaP `13.3384` edge `0.4408` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.2469` n `32` status `ready` deltaP `13.3384` edge `0.4408` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
