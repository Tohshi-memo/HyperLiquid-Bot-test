# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-01T06:07:29.978507+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11462`

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

- `risk_on_high->unknown_4h` score `7.4098` n `107` status `ready` deltaP `21.8971` edge `0.5333` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.4098` n `107` status `ready` deltaP `21.8971` edge `0.5333` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `5.9564` n `151` status `ready` deltaP `18.1897` edge `0.4446` maxDD `-2.5597`
- `risk_on_high->unknown_1h` score `2.2617` n `107` status `ready` deltaP `5.6173` edge `0.2087` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `2.2617` n `107` status `ready` deltaP `5.6173` edge `0.2087` maxDD `-1.9475`
- `market_context_high->unknown_1h` score `2.1309` n `151` status `ready` deltaP `4.9798` edge `0.2074` maxDD `-2.042`
- `news_risk_high->unknown_1h` score `1.3556` n `61` status `ready` deltaP `2.7216` edge `0.1295` maxDD `-1.1072`
- `risk_on_high->commodity_24h` score `1.1823` n `107` status `ready` deltaP `12.0782` edge `0.1168` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `1.1823` n `107` status `ready` deltaP `12.0782` edge `0.1168` maxDD `-0.5706`
- `market_context_high->commodity_24h` score `0.5862` n `151` status `ready` deltaP `11.4468` edge `0.0921` maxDD `-1.2314`
- `risk_on_high->crypto_alt_24h` score `0.5511` n `107` status `ready` deltaP `13.0971` edge `0.6737` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `0.5511` n `107` status `ready` deltaP `13.0971` edge `0.6737` maxDD `-42.8959`
- `news_risk_high->fx_4h` score `0.1657` n `61` status `ready` deltaP `10.8057` edge `0.0011` maxDD `-0.7461`
- `market_context_high->commodity_1h` score `0.0502` n `151` status `ready` deltaP `8.1235` edge `0.015` maxDD `-1.5315`
- `news_risk_high->commodity_4h` score `0.012` n `61` status `ready` deltaP `4.1384` edge `0.0156` maxDD `-1.3325`
- `risk_on_high->index_1h` score `-0.0103` n `107` status `ready` deltaP `6.4469` edge `0.0002` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.0103` n `107` status `ready` deltaP `6.4469` edge `0.0002` maxDD `-0.5605`
- `risk_on_high->fx_24h` score `-0.0179` n `107` status `ready` deltaP `36.4713` edge `0.0243` maxDD `-4.2453`
- `risk_on_and_context->fx_24h` score `-0.0179` n `107` status `ready` deltaP `36.4713` edge `0.0243` maxDD `-4.2453`
- `risk_on_high->commodity_1h` score `-0.0407` n `107` status `ready` deltaP `5.0227` edge `0.0135` maxDD `-0.8428`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
