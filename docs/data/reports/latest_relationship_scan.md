# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T12:37:27.558102+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11734`

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

- `market_context_high->unknown_24h` score `270.1165` n `87` status `ready` deltaP `6.5246` edge `22.4803` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `107.9962` n `87` status `ready` deltaP `7.4205` edge `8.995` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `27.4655` n `53` status `ready` deltaP `21.0486` edge `2.2191` maxDD `-3.6503`
- `market_context_high->equity_24h` score `14.99` n `87` status `ready` deltaP `15.8653` edge `1.3366` maxDD `-11.7897`
- `news_risk_high->crypto_major_24h` score `11.2587` n `53` status `ready` deltaP `36.8969` edge `1.394` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `10.9168` n `53` status `ready` deltaP `33.9536` edge `0.7964` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `7.2489` n `53` status `ready` deltaP `42.0415` edge `0.3238` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `5.4154` n `87` status `ready` deltaP `35.7475` edge `0.9252` maxDD `-30.2052`
- `market_context_high->metal_24h` score `5.2908` n `87` status `ready` deltaP `35.9345` edge `0.2516` maxDD `-1.021`
- `news_risk_high->metal_4h` score `4.6144` n `53` status `ready` deltaP `44.1096` edge `0.1281` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `3.8092` n `53` status `ready` deltaP `21.6579` edge `0.3218` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.6334` n `53` status `ready` deltaP `18.0149` edge `0.2457` maxDD `-3.7082`
- `news_risk_high->index_24h` score `3.5361` n `53` status `ready` deltaP `19.129` edge `0.1975` maxDD `-0.4279`
- `market_context_high->index_24h` score `3.0234` n `87` status `ready` deltaP `17.8061` edge `0.1674` maxDD `-1.7328`
- `news_risk_high->commodity_4h` score `3.0` n `53` status `ready` deltaP `26.4065` edge `0.0993` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.2038` n `53` status `ready` deltaP `26.0394` edge `0.0355` maxDD `-0.3692`
- `news_risk_high->index_4h` score `2.0954` n `53` status `ready` deltaP `20.1363` edge `0.084` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `2.0614` n `53` status `ready` deltaP `25.4314` edge `0.2586` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.3305` n `53` status `ready` deltaP `17.4754` edge `0.0245` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.8166` n `53` status `ready` deltaP `19.091` edge `0.0826` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
