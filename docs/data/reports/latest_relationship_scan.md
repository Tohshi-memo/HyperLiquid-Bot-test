# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T21:22:27.513268+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11772`

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

- `market_context_high->unknown_24h` score `311.3036` n `84` status `ready` deltaP `6.4732` edge `25.9129` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `75.6018` n `94` status `ready` deltaP `8.1053` edge `6.2909` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `29.0989` n `53` status `ready` deltaP `23.9453` edge `2.3359` maxDD `-3.6503`
- `market_context_high->equity_24h` score `21.0815` n `84` status `ready` deltaP `21.6766` edge `1.6829` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `11.6347` n `53` status `ready` deltaP `37.1823` edge `1.4403` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `9.0747` n `53` status `ready` deltaP `31.9719` edge `0.6561` maxDD `-7.0416`
- `market_context_high->crypto_alt_24h` score `8.5253` n `84` status `ready` deltaP `41.7411` edge `1.2243` maxDD `-25.4331`
- `news_risk_high->commodity_24h` score `7.3703` n `53` status `ready` deltaP `43.2292` edge `0.326` maxDD `0.0`
- `market_context_high->metal_24h` score `6.2584` n `84` status `ready` deltaP `38.6905` edge `0.3049` maxDD `-0.3044`
- `news_risk_high->metal_4h` score `4.5922` n `53` status `ready` deltaP `43.6523` edge `0.1293` maxDD `-1.0104`
- `market_context_high->index_24h` score `4.1397` n `84` status `ready` deltaP `23.6359` edge `0.1969` maxDD `-0.0934`
- `news_risk_high->index_24h` score `3.7313` n `53` status `ready` deltaP `21.8389` edge `0.1957` maxDD `-0.4279`
- `news_risk_high->equity_1h` score `3.0671` n `53` status `ready` deltaP `17.2664` edge `0.2035` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `2.9439` n `53` status `ready` deltaP `26.7114` edge `0.0926` maxDD `-0.3611`
- `news_risk_high->crypto_major_4h` score `2.7295` n `53` status `ready` deltaP `19.9811` edge `0.243` maxDD `-9.2335`
- `news_risk_high->metal_1h` score `2.2373` n `53` status `ready` deltaP `26.3388` edge `0.0363` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.5975` n `53` status `ready` deltaP `17.3924` edge `0.0608` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.3987` n `53` status `ready` deltaP `24.8216` edge `0.1777` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.1866` n `53` status `ready` deltaP `16.5772` edge `0.0185` maxDD `-0.4103`
- `news_risk_high->crypto_alt_24h` score `1.0877` n `53` status `ready` deltaP `11.8219` edge `0.5112` maxDD `-29.0448`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
