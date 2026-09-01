# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-01T06:37:32.021568+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11438`

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

- `risk_on_high->unknown_4h` score `7.3687` n `107` status `ready` deltaP `21.5922` edge `0.5319` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.3687` n `107` status `ready` deltaP `21.5922` edge `0.5319` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `5.9152` n `151` status `ready` deltaP `17.8848` edge `0.4432` maxDD `-2.5597`
- `risk_on_high->unknown_1h` score `2.2437` n `107` status `ready` deltaP `5.4676` edge `0.2082` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `2.2437` n `107` status `ready` deltaP `5.4676` edge `0.2082` maxDD `-1.9475`
- `market_context_high->unknown_1h` score `2.1129` n `151` status `ready` deltaP `4.8301` edge `0.2069` maxDD `-2.042`
- `news_risk_high->unknown_1h` score `1.3377` n `61` status `ready` deltaP `2.5719` edge `0.129` maxDD `-1.1072`
- `risk_on_high->commodity_24h` score `1.1125` n `107` status `ready` deltaP `11.731` edge `0.1133` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `1.1125` n `107` status `ready` deltaP `11.731` edge `0.1133` maxDD `-0.5706`
- `market_context_high->commodity_24h` score `0.5165` n `151` status `ready` deltaP `11.0996` edge `0.0886` maxDD `-1.2314`
- `risk_on_high->crypto_alt_24h` score `0.4035` n `107` status `ready` deltaP `12.7499` edge `0.6571` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `0.4035` n `107` status `ready` deltaP `12.7499` edge `0.6571` maxDD `-42.8959`
- `news_risk_high->fx_4h` score `0.1669` n `61` status `ready` deltaP `10.8057` edge `0.0012` maxDD `-0.7461`
- `market_context_high->commodity_1h` score `0.0466` n `151` status `ready` deltaP `8.1235` edge `0.0147` maxDD `-1.5315`
- `risk_on_high->index_1h` score `-0.0026` n `107` status `ready` deltaP `6.5966` edge `0.0002` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.0026` n `107` status `ready` deltaP `6.5966` edge `0.0002` maxDD `-0.5605`
- `news_risk_high->commodity_4h` score `-0.0077` n `61` status `ready` deltaP `3.9859` edge `0.0141` maxDD `-1.3325`
- `risk_on_high->fx_24h` score `-0.0186` n `107` status `ready` deltaP `36.4713` edge `0.0242` maxDD `-4.2453`
- `risk_on_and_context->fx_24h` score `-0.0186` n `107` status `ready` deltaP `36.4713` edge `0.0242` maxDD `-4.2453`
- `risk_on_high->commodity_1h` score `-0.043` n `107` status `ready` deltaP `5.0227` edge `0.0132` maxDD `-0.8428`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
