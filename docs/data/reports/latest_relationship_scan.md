# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-01T05:37:25.210268+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11498`

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

- `risk_on_high->unknown_4h` score `7.4292` n `107` status `ready` deltaP `22.0496` edge `0.5339` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.4292` n `107` status `ready` deltaP `22.0496` edge `0.5339` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `5.9758` n `151` status `ready` deltaP `18.3422` edge `0.4452` maxDD `-2.5597`
- `risk_on_high->unknown_1h` score `2.2581` n `107` status `ready` deltaP `5.6173` edge `0.2084` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `2.2581` n `107` status `ready` deltaP `5.6173` edge `0.2084` maxDD `-1.9475`
- `market_context_high->unknown_1h` score `2.1273` n `151` status `ready` deltaP `4.9798` edge `0.2071` maxDD `-2.042`
- `news_risk_high->unknown_1h` score `1.352` n `61` status `ready` deltaP `2.7216` edge `0.1292` maxDD `-1.1072`
- `risk_on_high->commodity_24h` score `1.2532` n `107` status `ready` deltaP `12.4254` edge `0.1204` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `1.2532` n `107` status `ready` deltaP `12.4254` edge `0.1204` maxDD `-0.5706`
- `risk_on_high->crypto_alt_24h` score `0.7033` n `107` status `ready` deltaP `13.4443` edge `0.6909` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `0.7033` n `107` status `ready` deltaP `13.4443` edge `0.6909` maxDD `-42.8959`
- `market_context_high->commodity_24h` score `0.6572` n `151` status `ready` deltaP `11.794` edge `0.0957` maxDD `-1.2314`
- `news_risk_high->fx_4h` score `0.1511` n `61` status `ready` deltaP `10.6533` edge `0.0009` maxDD `-0.7461`
- `market_context_high->commodity_1h` score `0.0538` n `151` status `ready` deltaP `8.1235` edge `0.0153` maxDD `-1.5315`
- `news_risk_high->commodity_4h` score `0.03` n `61` status `ready` deltaP `4.2908` edge `0.0169` maxDD `-1.3325`
- `risk_on_high->index_1h` score `-0.0103` n `107` status `ready` deltaP `6.4469` edge `0.0002` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.0103` n `107` status `ready` deltaP `6.4469` edge `0.0002` maxDD `-0.5605`
- `risk_on_high->fx_24h` score `-0.0269` n `107` status `ready` deltaP `36.2977` edge `0.0243` maxDD `-4.2453`
- `risk_on_and_context->fx_24h` score `-0.0269` n `107` status `ready` deltaP `36.2977` edge `0.0243` maxDD `-4.2453`
- `risk_on_high->commodity_1h` score `-0.0384` n `107` status `ready` deltaP `5.0227` edge `0.0138` maxDD `-0.8428`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
