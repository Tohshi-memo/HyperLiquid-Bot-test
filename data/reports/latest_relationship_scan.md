# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T15:37:37.829066+00:00`
- Price records: `672`
- Market context records: `8210`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5920`

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

- `news_risk_high->unknown_24h` score `8085.4347` n `43` status `ready` deltaP `36.9792` edge `673.5397` maxDD `0.0`
- `market_context_high->equity_24h` score `21.1239` n `33` status `ready` deltaP `39.4729` edge `1.5882` maxDD `-4.9489`
- `market_context_high->crypto_major_24h` score `15.4675` n `33` status `ready` deltaP `30.2084` edge `1.2189` maxDD `-7.1733`
- `market_context_high->crypto_alt_24h` score `15.3665` n `33` status `ready` deltaP `30.7292` edge `1.1612` maxDD `-3.508`
- `market_context_high->equity_4h` score `8.7524` n `33` status `ready` deltaP `47.1221` edge `0.4195` maxDD `-0.0094`
- `market_context_high->metal_24h` score `8.132` n `33` status `ready` deltaP `45.06` edge `0.3874` maxDD `-0.4771`
- `news_risk_high->equity_4h` score `7.2823` n `54` status `ready` deltaP `26.0783` edge `0.4927` maxDD `-3.4427`
- `market_context_high->crypto_major_4h` score `5.4591` n `33` status `ready` deltaP `23.6604` edge `0.3409` maxDD `-1.4966`
- `market_context_high->index_24h` score `5.0076` n `33` status `ready` deltaP `31.0764` edge `0.2631` maxDD `-0.9047`
- `market_context_high->crypto_alt_4h` score `4.5071` n `33` status `ready` deltaP `20.935` edge `0.2646` maxDD `-0.6195`
- `market_context_high->index_4h` score `3.7173` n `33` status `ready` deltaP `37.403` edge `0.0647` maxDD `-0.0092`
- `market_context_high->metal_4h` score `3.6287` n `33` status `ready` deltaP `35.8971` edge `0.0809` maxDD `-0.0926`
- `news_risk_high->equity_1h` score `3.1781` n `54` status `ready` deltaP `22.7268` edge `0.1442` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.6809` n `54` status `ready` deltaP `22.4198` edge `0.093` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.6284` n `54` status `ready` deltaP `13.2227` edge `0.3182` maxDD `-2.8833`
- `market_context_high->equity_1h` score `2.2474` n `33` status `ready` deltaP `12.2891` edge `0.12` maxDD `-0.1718`
- `market_context_high->fx_24h` score `2.2311` n `33` status `ready` deltaP `38.7153` edge `0.0746` maxDD `-0.4001`
- `news_risk_high->crypto_major_1h` score `1.9014` n `54` status `ready` deltaP `13.1515` edge `0.1105` maxDD `-1.1783`
- `news_risk_high->crypto_alt_1h` score `1.835` n `54` status `ready` deltaP `15.0033` edge `0.0963` maxDD `-1.1388`
- `news_risk_high->crypto_alt_4h` score `1.4227` n `54` status `ready` deltaP `17.2313` edge `0.2067` maxDD `-5.8012`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
