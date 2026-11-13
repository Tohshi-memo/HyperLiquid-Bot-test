# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T05:52:25.547871+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11860`

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

- `market_context_high->unknown_24h` score `273.9145` n `84` status `ready` deltaP `6.2996` edge `22.7983` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `55.6944` n `94` status `ready` deltaP `6.7333` edge `4.6411` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `31.5927` n `53` status `ready` deltaP `29.1536` edge `2.509` maxDD `-3.6503`
- `market_context_high->equity_24h` score `23.5753` n `84` status `ready` deltaP `26.8849` edge `1.856` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `13.0153` n `53` status `ready` deltaP `39.6128` edge `1.6011` maxDD `-12.7247`
- `market_context_high->crypto_alt_24h` score `10.0975` n `84` status `ready` deltaP `47.6439` edge `1.3865` maxDD `-25.4331`
- `news_risk_high->equity_4h` score `9.7739` n `53` status `ready` deltaP `33.4963` edge `0.7042` maxDD `-7.0416`
- `market_context_high->metal_24h` score `7.0383` n `84` status `ready` deltaP `43.2044` edge `0.3398` maxDD `-0.3044`
- `news_risk_high->commodity_24h` score `6.5315` n `53` status `ready` deltaP `40.7986` edge `0.2723` maxDD `0.0`
- `market_context_high->index_24h` score `4.4664` n `84` status `ready` deltaP `25.5456` edge `0.2114` maxDD `-0.0934`
- `news_risk_high->metal_4h` score `4.3453` n `53` status `ready` deltaP `41.9754` edge `0.1199` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.0581` n `53` status `ready` deltaP `23.7486` edge `0.2102` maxDD `-0.4279`
- `news_risk_high->commodity_4h` score `3.2187` n `53` status `ready` deltaP `29.4553` edge `0.0972` maxDD `-0.3611`
- `news_risk_high->equity_1h` score `3.2086` n `53` status `ready` deltaP `17.5658` edge `0.2133` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `3.1563` n `53` status `ready` deltaP `19.6762` edge `0.2806` maxDD `-9.2335`
- `news_risk_high->crypto_alt_24h` score `2.6598` n `53` status `ready` deltaP `17.7247` edge `0.6734` maxDD `-29.0448`
- `news_risk_high->metal_1h` score `2.0432` n `53` status `ready` deltaP `24.3927` edge `0.0331` maxDD `-0.3692`
- `news_risk_high->crypto_alt_4h` score `1.8661` n `53` status `ready` deltaP `26.0411` edge `0.2295` maxDD `-10.1088`
- `news_risk_high->index_4h` score `1.7428` n `53` status `ready` deltaP `18.4595` edge `0.0658` maxDD `-0.8235`
- `news_risk_high->index_1h` score `1.1747` n `53` status `ready` deltaP `16.2778` edge `0.0195` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
