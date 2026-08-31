# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-31T23:37:27.379151+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11496`

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

- `risk_on_high->unknown_4h` score `7.6828` n `107` status `ready` deltaP `23.2691` edge `0.5468` maxDD `-2.2689`
- `risk_on_and_context->unknown_4h` score `7.6828` n `107` status `ready` deltaP `23.2691` edge `0.5468` maxDD `-2.2689`
- `market_context_high->unknown_4h` score `6.1356` n `159` status `ready` deltaP `19.9657` edge `0.4476` maxDD `-2.5526`
- `risk_on_high->unknown_1h` score `2.0937` n `107` status `ready` deltaP `5.1682` edge `0.1977` maxDD `-1.9477`
- `risk_on_and_context->unknown_1h` score `2.0937` n `107` status `ready` deltaP `5.1682` edge `0.1977` maxDD `-1.9477`
- `market_context_high->unknown_1h` score `1.8699` n `159` status `ready` deltaP `4.5099` edge `0.1888` maxDD `-2.0436`
- `risk_on_high->commodity_24h` score `1.628` n `92` status `ready` deltaP `13.2398` edge `0.1462` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `1.628` n `92` status `ready` deltaP `13.2398` edge `0.1462` maxDD `-0.5706`
- `news_risk_high->unknown_1h` score `1.1881` n `61` status `ready` deltaP `2.2725` edge `0.1185` maxDD `-1.1049`
- `risk_on_high->fx_24h` score `0.8199` n `92` status `ready` deltaP `41.9007` edge `0.0243` maxDD `-3.5486`
- `risk_on_and_context->fx_24h` score `0.8199` n `92` status `ready` deltaP `41.9007` edge `0.0243` maxDD `-3.5486`
- `news_risk_high->commodity_4h` score `0.1807` n `61` status `ready` deltaP `6.2725` edge `0.023` maxDD `-1.3325`
- `market_context_high->commodity_1h` score `0.1743` n `159` status `ready` deltaP `9.3304` edge `0.0173` maxDD `-1.5315`
- `risk_on_high->crypto_alt_24h` score `0.1501` n `92` status `ready` deltaP `11.8207` edge `0.6308` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `0.1501` n `92` status `ready` deltaP `11.8207` edge `0.6308` maxDD `-42.8959`
- `news_risk_high->fx_4h` score `0.1353` n `61` status `ready` deltaP `10.5008` edge `0.0006` maxDD `-0.7461`
- `risk_on_high->commodity_1h` score `-0.0018` n `107` status `ready` deltaP `5.6215` edge `0.0145` maxDD `-0.8428`
- `risk_on_and_context->commodity_1h` score `-0.0018` n `107` status `ready` deltaP `5.6215` edge `0.0145` maxDD `-0.8428`
- `risk_on_high->index_1h` score `-0.0283` n `107` status `ready` deltaP `6.1475` edge `-0.0001` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.0283` n `107` status `ready` deltaP `6.1475` edge `-0.0001` maxDD `-0.5605`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
