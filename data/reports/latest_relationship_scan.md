# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T13:22:28.030434+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11754`

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

- `market_context_high->unknown_24h` score `281.5218` n `85` status `ready` deltaP `6.4706` edge `23.4311` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `107.7365` n `85` status `ready` deltaP `7.2041` edge `8.9748` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `27.3419` n `53` status `ready` deltaP `21.0486` edge `2.2088` maxDD `-3.6503`
- `market_context_high->equity_24h` score `18.0457` n `85` status `ready` deltaP `17.7855` edge `1.4788` maxDD `-3.8182`
- `news_risk_high->crypto_major_24h` score `11.1432` n `53` status `ready` deltaP `36.8969` edge `1.3792` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `10.5724` n `53` status `ready` deltaP `33.9536` edge `0.7677` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `7.3282` n `53` status `ready` deltaP `42.3875` edge `0.3281` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `6.5165` n `85` status `ready` deltaP `37.3702` edge `0.9959` maxDD `-25.4331`
- `market_context_high->metal_24h` score `5.7534` n `85` status `ready` deltaP `37.8547` edge `0.2684` maxDD `-0.3053`
- `news_risk_high->metal_4h` score `4.5938` n `53` status `ready` deltaP `43.9571` edge `0.1274` maxDD `-1.0104`
- `market_context_high->index_24h` score `3.6327` n `85` status `ready` deltaP `19.8616` edge `0.1857` maxDD `-0.5643`
- `news_risk_high->equity_1h` score `3.6202` n `53` status `ready` deltaP `18.0149` edge `0.2446` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `3.61` n `53` status `ready` deltaP `21.6579` edge `0.3052` maxDD `-9.2335`
- `news_risk_high->index_24h` score `3.5061` n `53` status `ready` deltaP `19.129` edge `0.195` maxDD `-0.4279`
- `news_risk_high->commodity_4h` score `3.0495` n `53` status `ready` deltaP `26.7114` edge `0.1014` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.1918` n `53` status `ready` deltaP `25.8897` edge `0.0355` maxDD `-0.3692`
- `news_risk_high->index_4h` score `2.0472` n `53` status `ready` deltaP `19.9839` edge `0.081` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.9085` n `53` status `ready` deltaP `25.4314` edge `0.239` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.3293` n `53` status `ready` deltaP `17.4754` edge `0.0244` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.7886` n `53` status `ready` deltaP `18.9413` edge `0.08` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
