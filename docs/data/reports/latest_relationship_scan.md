# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T15:07:36.492390+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11964`

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

- `market_context_high->unknown_24h` score `291.6043` n `84` status `ready` deltaP `6.4425` edge `24.2715` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `99.3271` n `89` status `ready` deltaP `7.6271` edge `8.2712` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `27.1703` n `53` status `ready` deltaP `21.0486` edge `2.1945` maxDD `-3.6503`
- `market_context_high->equity_24h` score `19.1529` n `84` status `ready` deltaP `18.7799` edge `1.5415` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `10.9794` n `53` status `ready` deltaP `36.8969` edge `1.3582` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `10.066` n `53` status `ready` deltaP `33.9536` edge `0.7255` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `7.4453` n `53` status `ready` deltaP `42.9066` edge `0.3344` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `6.9128` n `84` status `ready` deltaP `38.2106` edge `1.0411` maxDD `-25.4331`
- `market_context_high->metal_24h` score `6.0095` n `84` status `ready` deltaP `38.8491` edge `0.2831` maxDD `-0.3044`
- `news_risk_high->metal_4h` score `4.67` n `53` status `ready` deltaP `44.4145` edge `0.1307` maxDD `-1.0104`
- `market_context_high->index_24h` score `3.8509` n `84` status `ready` deltaP `20.926` edge `0.1909` maxDD `-0.0934`
- `news_risk_high->equity_1h` score `3.5182` n `53` status `ready` deltaP `17.7155` edge `0.2381` maxDD `-3.7082`
- `news_risk_high->index_24h` score `3.4425` n `53` status `ready` deltaP `19.129` edge `0.1897` maxDD `-0.4279`
- `news_risk_high->crypto_major_4h` score `3.346` n `53` status `ready` deltaP `21.6579` edge `0.2832` maxDD `-9.2335`
- `news_risk_high->commodity_4h` score `3.0507` n `53` status `ready` deltaP `26.7114` edge `0.1015` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.2805` n `53` status `ready` deltaP `26.6382` edge `0.0379` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.9618` n `53` status `ready` deltaP `19.8315` edge `0.0749` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.6683` n `53` status `ready` deltaP `25.4314` edge `0.2082` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.3185` n `53` status `ready` deltaP `17.4754` edge `0.0235` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.8042` n `53` status `ready` deltaP `19.091` edge `0.081` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
