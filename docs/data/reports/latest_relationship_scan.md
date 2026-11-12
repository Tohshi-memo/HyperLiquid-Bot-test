# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T12:22:30.022550+00:00`
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

- `market_context_high->unknown_24h` score `269.8093` n `87` status `ready` deltaP `6.5246` edge `22.4547` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `108.2614` n `87` status `ready` deltaP `7.4205` edge `9.0171` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `27.5207` n `53` status `ready` deltaP `21.0486` edge `2.2237` maxDD `-3.6503`
- `market_context_high->equity_24h` score `15.0452` n `87` status `ready` deltaP `15.8653` edge `1.3412` maxDD `-11.7897`
- `news_risk_high->crypto_major_24h` score `11.3055` n `53` status `ready` deltaP `36.8969` edge `1.4` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.0116` n `53` status `ready` deltaP `33.9536` edge `0.8043` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `7.2135` n `53` status `ready` deltaP `41.8685` edge `0.322` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `5.4217` n `87` status `ready` deltaP `35.7475` edge `0.926` maxDD `-30.2052`
- `market_context_high->metal_24h` score `5.2812` n `87` status `ready` deltaP `35.9345` edge `0.2508` maxDD `-1.021`
- `news_risk_high->metal_4h` score `4.6132` n `53` status `ready` deltaP `44.1096` edge `0.128` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `3.8692` n `53` status `ready` deltaP `21.6579` edge `0.3268` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.6334` n `53` status `ready` deltaP `18.0149` edge `0.2457` maxDD `-3.7082`
- `news_risk_high->index_24h` score `3.5469` n `53` status `ready` deltaP `19.129` edge `0.1984` maxDD `-0.4279`
- `market_context_high->index_24h` score `3.0342` n `87` status `ready` deltaP `17.8061` edge `0.1683` maxDD `-1.7328`
- `news_risk_high->commodity_4h` score `2.9758` n `53` status `ready` deltaP `26.2541` edge `0.0983` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.2038` n `53` status `ready` deltaP `26.0394` edge `0.0355` maxDD `-0.3692`
- `news_risk_high->index_4h` score `2.1184` n `53` status `ready` deltaP `20.2888` edge `0.0849` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `2.1043` n `53` status `ready` deltaP `25.4314` edge `0.2641` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.3317` n `53` status `ready` deltaP `17.4754` edge `0.0246` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.819` n `53` status `ready` deltaP `19.091` edge `0.0829` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
