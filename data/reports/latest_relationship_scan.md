# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T07:52:24.866476+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11824`

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

- `market_context_high->unknown_24h` score `272.009` n `82` status `ready` deltaP `6.2416` edge `22.6399` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `73.076` n `92` status `ready` deltaP `6.5482` edge `6.0908` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `32.1011` n `53` status `ready` deltaP `30.5425` edge `2.5421` maxDD `-3.6503`
- `market_context_high->equity_24h` score `24.4711` n `82` status `ready` deltaP `27.8963` edge `1.9239` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `13.4931` n `53` status `ready` deltaP `41.0017` edge `1.6531` maxDD `-12.7247`
- `market_context_high->crypto_alt_24h` score `10.3144` n `82` status `ready` deltaP `48.3359` edge `1.4097` maxDD `-25.4331`
- `news_risk_high->equity_4h` score `10.2578` n `53` status `ready` deltaP `34.7158` edge `0.7364` maxDD `-7.0416`
- `market_context_high->metal_24h` score `7.2512` n `82` status `ready` deltaP `44.2157` edge `0.3508` maxDD `-0.3044`
- `news_risk_high->commodity_24h` score `6.268` n `53` status `ready` deltaP `39.4097` edge `0.2596` maxDD `0.0`
- `market_context_high->index_24h` score `4.5368` n `82` status `ready` deltaP `25.6606` edge `0.2165` maxDD `-0.0934`
- `news_risk_high->metal_4h` score `4.504` n `53` status `ready` deltaP `43.1949` edge `0.125` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.1123` n `53` status `ready` deltaP `24.0959` edge `0.2124` maxDD `-0.4279`
- `news_risk_high->crypto_major_4h` score `3.4164` n `53` status `ready` deltaP `20.4384` edge `0.2972` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.1775` n `53` status `ready` deltaP `17.4161` edge `0.2117` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.1181` n `53` status `ready` deltaP `28.6931` edge `0.0939` maxDD `-0.3611`
- `news_risk_high->crypto_alt_24h` score `2.9154` n `53` status `ready` deltaP `19.1136` edge `0.6969` maxDD `-29.0448`
- `news_risk_high->metal_1h` score `2.078` n `53` status `ready` deltaP `24.6921` edge `0.034` maxDD `-0.3692`
- `news_risk_high->crypto_alt_4h` score `1.9508` n `53` status `ready` deltaP `26.4985` edge `0.2373` maxDD `-10.1088`
- `news_risk_high->index_4h` score `1.8872` n `53` status `ready` deltaP `19.679` edge `0.0697` maxDD `-0.8235`
- `news_risk_high->index_1h` score `1.1459` n `53` status `ready` deltaP `15.9784` edge `0.0191` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
