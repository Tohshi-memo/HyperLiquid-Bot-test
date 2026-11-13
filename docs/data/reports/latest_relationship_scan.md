# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T19:37:33.554246+00:00`
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

- `market_context_high->unknown_24h` score `370.286` n `75` status `ready` deltaP `2.8889` edge `30.852` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `34.0765` n `53` status `ready` deltaP `33.3203` edge `2.6882` maxDD `-3.6503`
- `market_context_high->equity_24h` score `25.8428` n `75` status `ready` deltaP `27.8611` edge `2.122` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `17.1831` n `75` status `ready` deltaP `48.1042` edge `1.3627` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `14.4419` n `53` status `ready` deltaP `42.0434` edge `1.7678` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `10.9622` n `53` status `ready` deltaP `34.7158` edge `0.7951` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `5.754` n `53` status `ready` deltaP `37.5` edge `0.2295` maxDD `0.0`
- `market_context_high->index_24h` score `4.9465` n `75` status `ready` deltaP `26.6042` edge `0.244` maxDD `-0.0653`
- `news_risk_high->metal_4h` score `4.818` n `53` status `ready` deltaP `45.634` edge `0.1349` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.2656` n `53` status `ready` deltaP `24.6167` edge `0.2217` maxDD `-0.4279`
- `market_context_high->metal_24h` score `4.0003` n `75` status `ready` deltaP `40.2917` edge `0.3334` maxDD `-3.7989`
- `news_risk_high->equity_1h` score `3.3611` n `53` status `ready` deltaP `17.2664` edge `0.228` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.2694` n `53` status `ready` deltaP `29.7601` edge `0.0994` maxDD `-0.3611`
- `news_risk_high->crypto_major_4h` score `3.1597` n `53` status `ready` deltaP `19.5237` edge `0.2819` maxDD `-9.2335`
- `news_risk_high->metal_1h` score `2.2242` n `53` status `ready` deltaP `26.0394` edge `0.0372` maxDD `-0.3692`
- `news_risk_high->index_4h` score `2.0054` n `53` status `ready` deltaP `20.1363` edge `0.0765` maxDD `-0.8235`
- `news_risk_high->crypto_alt_24h` score `1.9632` n `53` status `ready` deltaP `14.9469` edge `0.6026` maxDD `-29.0448`
- `news_risk_high->crypto_alt_4h` score `1.785` n `53` status `ready` deltaP `26.0411` edge `0.2191` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.1723` n `53` status `ready` deltaP `15.9784` edge `0.0213` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.5769` n `53` status `ready` deltaP `16.5461` edge `0.0616` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
