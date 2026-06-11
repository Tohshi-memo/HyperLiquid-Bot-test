# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-11T23:37:31.370121+00:00`
- Price records: `672`
- Market context records: `3632`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13163`

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

- `risk_on_high->crypto_major_24h` score `39.9689` n `32` status `ready` deltaP `44.7917` edge `3.0364` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `39.9689` n `32` status `ready` deltaP `44.7917` edge `3.0364` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `36.786` n `32` status `ready` deltaP `46.875` edge `2.753` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `36.786` n `32` status `ready` deltaP `46.875` edge `2.753` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `32.3746` n `32` status `ready` deltaP `43.9236` edge `2.4202` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `32.3746` n `32` status `ready` deltaP `43.9236` edge `2.4202` maxDD `-0.8779`
- `risk_on_high->index_24h` score `21.084` n `32` status `ready` deltaP `46.875` edge `1.4445` maxDD `0.0`
- `risk_on_and_context->index_24h` score `21.084` n `32` status `ready` deltaP `46.875` edge `1.4445` maxDD `0.0`
- `risk_on_high->metal_24h` score `13.4316` n `32` status `ready` deltaP `32.4653` edge `0.929` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `13.4316` n `32` status `ready` deltaP `32.4653` edge `0.929` maxDD `-0.7574`
- `risk_on_high->crypto_major_4h` score `12.2752` n `32` status `ready` deltaP `22.1037` edge `0.9878` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `12.2752` n `32` status `ready` deltaP `22.1037` edge `0.9878` maxDD `-5.9781`
- `market_context_high->equity_24h` score `11.056` n `158` status `ready` deltaP `23.4573` edge `1.4062` maxDD `-40.9667`
- `market_context_high->index_24h` score `9.7341` n `158` status `ready` deltaP `31.6851` edge `0.8216` maxDD `-15.0661`
- `market_context_high->crypto_major_24h` score `4.6463` n `158` status `ready` deltaP `10.5749` edge `1.0898` maxDD `-54.8486`
- `market_context_high->metal_24h` score `4.255` n `158` status `ready` deltaP `26.3735` edge `0.8237` maxDD `-25.9879`
- `risk_on_high->crypto_alt_4h` score `3.789` n `32` status `ready` deltaP `2.5152` edge `0.4834` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `3.789` n `32` status `ready` deltaP `2.5152` edge `0.4834` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `2.6999` n `32` status `ready` deltaP `11.2043` edge `0.3849` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.6999` n `32` status `ready` deltaP `11.2043` edge `0.3849` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
