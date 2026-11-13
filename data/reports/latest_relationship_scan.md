# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T08:52:24.741789+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11174`

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

- `market_context_high->unknown_24h` score `292.6498` n `78` status `ready` deltaP `6.1165` edge `24.3608` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `80.8876` n `88` status `ready` deltaP `6.153` edge `6.7444` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `32.3774` n `53` status `ready` deltaP `31.2369` edge `2.5605` maxDD `-3.6503`
- `market_context_high->equity_24h` score `25.5704` n `78` status `ready` deltaP `27.7777` edge `2.0163` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `13.7468` n `53` status `ready` deltaP `41.6962` edge `1.681` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `10.4854` n `53` status `ready` deltaP `35.3255` edge `0.7513` maxDD `-7.0416`
- `market_context_high->crypto_alt_24h` score `10.2951` n `78` status `ready` deltaP `47.5294` edge `1.4126` maxDD `-25.4331`
- `market_context_high->metal_24h` score `7.3245` n `78` status `ready` deltaP `44.0972` edge `0.3577` maxDD `-0.3044`
- `news_risk_high->commodity_24h` score `6.1452` n `53` status `ready` deltaP `38.7153` edge `0.254` maxDD `0.0`
- `market_context_high->index_24h` score `4.5935` n `78` status `ready` deltaP `25.3339` edge `0.2234` maxDD `-0.0934`
- `news_risk_high->metal_4h` score `4.5852` n `53` status `ready` deltaP `43.8047` edge `0.1277` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.1442` n `53` status `ready` deltaP `24.2695` edge `0.2139` maxDD `-0.4279`
- `news_risk_high->crypto_major_4h` score `3.4308` n `53` status `ready` deltaP `20.4384` edge `0.2984` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.2998` n `53` status `ready` deltaP `18.0149` edge `0.2179` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.0719` n `53` status `ready` deltaP `28.2358` edge `0.0931` maxDD `-0.3611`
- `news_risk_high->crypto_alt_24h` score `3.0349` n `53` status `ready` deltaP `19.808` edge `0.7076` maxDD `-29.0448`
- `news_risk_high->metal_1h` score `2.1499` n `53` status `ready` deltaP `25.2909` edge `0.036` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.9576` n `53` status `ready` deltaP `20.2888` edge `0.0715` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.9258` n `53` status `ready` deltaP `26.4985` edge `0.2341` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.2046` n `53` status `ready` deltaP `16.5772` edge `0.02` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
