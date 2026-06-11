# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-11T15:07:29.520613+00:00`
- Price records: `672`
- Market context records: `3595`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13114`

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

- `risk_on_high->crypto_major_24h` score `46.9759` n `32` status `ready` deltaP `50.2545` edge `3.5839` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `46.9759` n `32` status `ready` deltaP `50.2545` edge `3.5839` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `43.2757` n `32` status `ready` deltaP `51.6464` edge `3.262` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `43.2757` n `32` status `ready` deltaP `51.6464` edge `3.262` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `40.5195` n `32` status `ready` deltaP `49.7346` edge `3.0602` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `40.5195` n `32` status `ready` deltaP `49.7346` edge `3.0602` maxDD `-0.8779`
- `risk_on_high->index_24h` score `25.3001` n `32` status `ready` deltaP `52.6863` edge `1.7571` maxDD `0.0`
- `risk_on_and_context->index_24h` score `25.3001` n `32` status `ready` deltaP `52.6863` edge `1.7571` maxDD `0.0`
- `risk_on_high->metal_24h` score `18.3301` n `32` status `ready` deltaP `36.8609` edge `1.3079` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `18.3301` n `32` status `ready` deltaP `36.8609` edge `1.3079` maxDD `-0.7574`
- `market_context_high->equity_24h` score `17.6318` n `156` status `ready` deltaP `28.5695` edge `1.9201` maxDD `-40.9667`
- `market_context_high->index_24h` score `13.9154` n `156` status `ready` deltaP `37.3017` edge `1.1326` maxDD `-15.0661`
- `risk_on_high->crypto_major_4h` score `13.4421` n `32` status `ready` deltaP `25.3049` edge `1.0637` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `13.4421` n `32` status `ready` deltaP `25.3049` edge `1.0637` maxDD `-5.9781`
- `market_context_high->crypto_major_24h` score `11.5418` n `156` status `ready` deltaP `15.559` edge `1.6312` maxDD `-54.8486`
- `market_context_high->metal_24h` score `7.4061` n `156` status `ready` deltaP `30.9314` edge `1.1973` maxDD `-25.9879`
- `market_context_high->crypto_alt_24h` score `6.4324` n `156` status `ready` deltaP `9.9109` edge `1.2742` maxDD `-56.6728`
- `risk_on_high->crypto_alt_4h` score `5.3068` n `32` status `ready` deltaP `6.1738` edge `0.5855` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `5.3068` n `32` status `ready` deltaP `6.1738` edge `0.5855` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `3.7448` n `32` status `ready` deltaP `15.4726` edge `0.4904` maxDD `-5.7426`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
