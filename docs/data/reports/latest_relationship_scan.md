# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-01T05:21:24.405386+00:00`
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

- `risk_on_high->unknown_4h` score `7.4304` n `107` status `ready` deltaP `22.0496` edge `0.534` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.4304` n `107` status `ready` deltaP `22.0496` edge `0.534` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `5.977` n `151` status `ready` deltaP `18.3422` edge `0.4453` maxDD `-2.5597`
- `risk_on_high->unknown_1h` score `2.2341` n `107` status `ready` deltaP `5.4676` edge `0.2074` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `2.2341` n `107` status `ready` deltaP `5.4676` edge `0.2074` maxDD `-1.9475`
- `market_context_high->unknown_1h` score `2.1033` n `151` status `ready` deltaP `4.8301` edge `0.2061` maxDD `-2.042`
- `news_risk_high->unknown_1h` score `1.3281` n `61` status `ready` deltaP `2.5719` edge `0.1282` maxDD `-1.1072`
- `risk_on_high->commodity_24h` score `1.2887` n `107` status `ready` deltaP `12.599` edge `0.1222` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `1.2887` n `107` status `ready` deltaP `12.599` edge `0.1222` maxDD `-0.5706`
- `risk_on_high->crypto_alt_24h` score `0.7708` n `107` status `ready` deltaP `13.6179` edge `0.6984` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `0.7708` n `107` status `ready` deltaP `13.6179` edge `0.6984` maxDD `-42.8959`
- `market_context_high->commodity_24h` score `0.6927` n `151` status `ready` deltaP `11.9676` edge `0.0975` maxDD `-1.2314`
- `news_risk_high->fx_4h` score `0.1377` n `61` status `ready` deltaP `10.5008` edge `0.0008` maxDD `-0.7461`
- `market_context_high->commodity_1h` score `0.0538` n `151` status `ready` deltaP `8.1235` edge `0.0153` maxDD `-1.5315`
- `news_risk_high->commodity_4h` score `0.0339` n `61` status `ready` deltaP `4.2908` edge `0.0174` maxDD `-1.3325`
- `risk_on_high->index_1h` score `-0.0103` n `107` status `ready` deltaP `6.4469` edge `0.0002` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.0103` n `107` status `ready` deltaP `6.4469` edge `0.0002` maxDD `-0.5605`
- `risk_on_high->fx_24h` score `-0.0367` n `107` status `ready` deltaP `36.1241` edge `0.0242` maxDD `-4.2453`
- `risk_on_and_context->fx_24h` score `-0.0367` n `107` status `ready` deltaP `36.1241` edge `0.0242` maxDD `-4.2453`
- `risk_on_high->commodity_1h` score `-0.0384` n `107` status `ready` deltaP `5.0227` edge `0.0138` maxDD `-0.8428`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
