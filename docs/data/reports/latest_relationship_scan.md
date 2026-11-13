# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T13:37:36.569818+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10554`

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

- `market_context_high->unknown_24h` score `372.1173` n `75` status `ready` deltaP `5.3194` edge `30.9884` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `32.6176` n `53` status `ready` deltaP `31.5842` edge `2.5782` maxDD `-3.6503`
- `market_context_high->equity_24h` score `24.3839` n `75` status `ready` deltaP `26.125` edge `2.012` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `18.4935` n `75` status `ready` deltaP `51.75` edge `1.4476` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `14.2318` n `53` status `ready` deltaP `42.217` edge `1.7397` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `10.1932` n `53` status `ready` deltaP `33.9536` edge `0.7361` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `5.72` n `53` status `ready` deltaP `36.8056` edge `0.2313` maxDD `0.0`
- `market_context_high->index_24h` score `4.7135` n `75` status `ready` deltaP `25.0417` edge `0.235` maxDD `-0.0653`
- `news_risk_high->metal_4h` score `4.567` n `53` status `ready` deltaP `43.6523` edge `0.1272` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.0326` n `53` status `ready` deltaP `23.0542` edge `0.2127` maxDD `-0.4279`
- `market_context_high->metal_24h` score `3.7818` n `75` status `ready` deltaP `37.5139` edge `0.3239` maxDD `-3.7989`
- `news_risk_high->equity_1h` score `3.3106` n `53` status `ready` deltaP `17.7155` edge `0.2208` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.0151` n `53` status `ready` deltaP `27.9309` edge `0.0904` maxDD `-0.3611`
- `news_risk_high->crypto_major_4h` score `2.9197` n `53` status `ready` deltaP `18.6091` edge `0.268` maxDD `-9.2335`
- `news_risk_high->crypto_alt_24h` score `2.815` n `53` status `ready` deltaP `18.5927` edge `0.6875` maxDD `-29.0448`
- `news_risk_high->metal_1h` score `2.0888` n `53` status `ready` deltaP `24.6921` edge `0.0349` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.9076` n `53` status `ready` deltaP `19.679` edge `0.0714` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.795` n `53` status `ready` deltaP `25.8887` edge `0.2214` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.1735` n `53` status `ready` deltaP `16.1281` edge `0.0204` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.5777` n `53` status `ready` deltaP `16.6958` edge `0.0607` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
