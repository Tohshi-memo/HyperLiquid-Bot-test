# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-14T10:22:28.978377+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `9444`

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

- `market_context_high->unknown_24h` score `492.9592` n `73` status `ready` deltaP `3.3176` edge `41.0644` maxDD `-0.1931`
- `news_risk_high->equity_24h` score `37.9999` n `53` status `ready` deltaP `36.7925` edge `2.992` maxDD `-3.6503`
- `market_context_high->equity_24h` score `30.8889` n `73` status `ready` deltaP `33.5616` edge `2.5045` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `18.4094` n `73` status `ready` deltaP `49.629` edge `1.4008` maxDD `-12.8035`
- `news_risk_high->crypto_major_24h` score `15.9107` n `53` status `ready` deltaP `42.0434` edge `1.9561` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.2474` n `53` status `ready` deltaP `36.2402` edge `0.8087` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `6.823` n `53` status `ready` deltaP `46.5278` edge `0.2584` maxDD `0.0`
- `market_context_high->index_24h` score `6.3862` n `73` status `ready` deltaP `38.8104` edge `0.2826` maxDD `-0.0653`
- `news_risk_high->index_24h` score `5.3901` n `53` status `ready` deltaP `34.3389` edge `0.2506` maxDD `-0.4279`
- `news_risk_high->metal_4h` score `4.9343` n `53` status `ready` deltaP `46.5486` edge `0.1385` maxDD `-1.0104`
- `market_context_high->metal_24h` score `4.5282` n `73` status `ready` deltaP `43.379` edge `0.3805` maxDD `-3.7989`
- `news_risk_high->crypto_major_4h` score `4.0918` n `53` status `ready` deltaP `21.2006` edge `0.3484` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.5385` n `53` status `ready` deltaP `18.3143` edge `0.2358` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.1395` n `53` status `ready` deltaP `28.5406` edge `0.0967` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.1823` n `53` status `ready` deltaP `25.4406` edge `0.0377` maxDD `-0.3692`
- `news_risk_high->index_4h` score `2.1419` n `53` status `ready` deltaP `21.8132` edge `0.0767` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `2.1205` n `53` status `ready` deltaP `26.1936` edge `0.2611` maxDD `-10.1088`
- `news_risk_high->crypto_alt_24h` score `1.7535` n `53` status `ready` deltaP `14.4261` edge `0.5792` maxDD `-29.0448`
- `news_risk_high->index_1h` score `1.225` n `53` status `ready` deltaP `16.5772` edge `0.0217` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.7203` n `53` status `ready` deltaP `17.4443` edge `0.074` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
