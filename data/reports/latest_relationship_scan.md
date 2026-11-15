# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T04:37:32.885867+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `9680`

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

- `market_context_high->unknown_24h` score `553.5285` n `66` status `ready` deltaP `2.4263` edge `46.1112` maxDD `0.0`
- `news_risk_high->equity_24h` score `41.5654` n `53` status `ready` deltaP `46.4112` edge `3.225` maxDD `-3.6503`
- `market_context_high->equity_24h` score `37.8117` n `66` status `ready` deltaP `41.4369` edge `3.0289` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `29.6572` n `66` status `ready` deltaP `57.8121` edge `2.1937` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `21.1326` n `53` status `ready` deltaP `43.1052` edge `2.6185` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.7584` n `53` status `ready` deltaP `38.9075` edge `0.8335` maxDD `-7.0416`
- `market_context_high->index_24h` score `7.3931` n `66` status `ready` deltaP `43.5507` edge `0.3349` maxDD `-0.0653`
- `news_risk_high->commodity_24h` score `7.2132` n `53` status `ready` deltaP `49.74` edge `0.2695` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `6.436` n `53` status `ready` deltaP `14.473` edge `1.1792` maxDD `-29.0448`
- `news_risk_high->index_24h` score `6.0351` n `53` status `ready` deltaP `39.8057` edge `0.2679` maxDD `-0.4279`
- `market_context_high->metal_24h` score `5.7678` n `66` status `ready` deltaP `54.6925` edge `0.464` maxDD `-3.7989`
- `news_risk_high->crypto_major_4h` score `5.5556` n `53` status `ready` deltaP `22.1734` edge `0.4639` maxDD `-9.2335`
- `news_risk_high->metal_4h` score `5.0189` n `53` status `ready` deltaP `46.001` edge `0.1492` maxDD `-1.0104`
- `news_risk_high->equity_1h` score `3.723` n `53` status `ready` deltaP `19.961` edge `0.2402` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.3405` n `53` status `ready` deltaP `30.9038` edge `0.0977` maxDD `-0.3611`
- `news_risk_high->crypto_alt_4h` score `3.0075` n `53` status `ready` deltaP `26.5558` edge `0.3724` maxDD `-10.1088`
- `market_context_high->crypto_major_24h` score `2.5121` n `66` status `ready` deltaP `12.6306` edge `1.1577` maxDD `-76.2717`
- `news_risk_high->index_4h` score `2.4268` n `53` status `ready` deltaP `24.939` edge `0.0796` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `2.2242` n `53` status `ready` deltaP `25.5903` edge `0.0402` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3771` n `53` status `ready` deltaP `18.3736` edge `0.0224` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
