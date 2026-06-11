# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-11T20:22:37.559962+00:00`
- Price records: `672`
- Market context records: `3618`
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

- `risk_on_high->crypto_major_24h` score `42.7522` n `32` status `ready` deltaP `47.0486` edge `3.2533` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `42.7522` n `32` status `ready` deltaP `47.0486` edge `3.2533` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `39.8598` n `32` status `ready` deltaP `49.1319` edge `2.9941` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `39.8598` n `32` status `ready` deltaP `49.1319` edge `2.9941` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `35.5012` n `32` status `ready` deltaP `46.1806` edge `2.6657` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `35.5012` n `32` status `ready` deltaP `46.1806` edge `2.6657` maxDD `-0.8779`
- `risk_on_high->index_24h` score `23.1306` n `32` status `ready` deltaP `49.1319` edge `1.6` maxDD `0.0`
- `risk_on_and_context->index_24h` score `23.1306` n `32` status `ready` deltaP `49.1319` edge `1.6` maxDD `0.0`
- `risk_on_high->metal_24h` score `15.8934` n `32` status `ready` deltaP `34.7222` edge `1.1191` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `15.8934` n `32` status `ready` deltaP `34.7222` edge `1.1191` maxDD `-0.7574`
- `market_context_high->equity_24h` score `14.1297` n `158` status `ready` deltaP `25.7142` edge `1.6473` maxDD `-40.9667`
- `risk_on_high->crypto_major_4h` score `12.6811` n `32` status `ready` deltaP `23.3232` edge `1.0135` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `12.6811` n `32` status `ready` deltaP `23.3232` edge `1.0135` maxDD `-5.9781`
- `market_context_high->index_24h` score `11.7806` n `158` status `ready` deltaP `33.942` edge `0.9771` maxDD `-15.0661`
- `market_context_high->crypto_major_24h` score `7.4297` n `158` status `ready` deltaP `12.8318` edge `1.3067` maxDD `-54.8486`
- `market_context_high->metal_24h` score `5.8551` n `158` status `ready` deltaP `28.6304` edge `1.0138` maxDD `-25.9879`
- `risk_on_high->crypto_alt_4h` score `4.3091` n `32` status `ready` deltaP `3.8872` edge `0.5176` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `4.3091` n `32` status `ready` deltaP `3.8872` edge `0.5176` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.2031` n `32` status `ready` deltaP `13.186` edge `0.4362` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.2031` n `32` status `ready` deltaP `13.186` edge `0.4362` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
