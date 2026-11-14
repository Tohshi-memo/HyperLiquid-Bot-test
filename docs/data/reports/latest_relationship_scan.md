# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-14T10:37:28.815865+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `9324`

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

- `market_context_high->unknown_24h` score `504.3575` n `72` status `ready` deltaP `4.5139` edge `41.9997` maxDD `0.0`
- `news_risk_high->equity_24h` score `38.0725` n `53` status `ready` deltaP `36.9661` edge `2.9969` maxDD `-3.6503`
- `market_context_high->equity_24h` score `31.4053` n `72` status `ready` deltaP `33.5069` edge `2.5479` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `19.1247` n `72` status `ready` deltaP `50.6945` edge `1.4307` maxDD `-11.3282`
- `news_risk_high->crypto_major_24h` score `15.9458` n `53` status `ready` deltaP `42.0434` edge `1.9606` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.2474` n `53` status `ready` deltaP `36.2402` edge `0.8087` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `6.8405` n `53` status `ready` deltaP `46.7014` edge `0.2587` maxDD `0.0`
- `market_context_high->index_24h` score `6.4561` n `72` status `ready` deltaP `38.8889` edge `0.2879` maxDD `-0.0653`
- `news_risk_high->index_24h` score `5.4088` n `53` status `ready` deltaP `34.5125` edge `0.251` maxDD `-0.4279`
- `news_risk_high->metal_4h` score `4.9331` n `53` status `ready` deltaP `46.5486` edge `0.1384` maxDD `-1.0104`
- `market_context_high->metal_24h` score `4.6133` n `72` status `ready` deltaP `44.4445` edge `0.3843` maxDD `-3.7989`
- `news_risk_high->crypto_major_4h` score `4.0906` n `53` status `ready` deltaP `21.2006` edge `0.3483` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.5385` n `53` status `ready` deltaP `18.3143` edge `0.2358` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.1529` n `53` status `ready` deltaP `28.6931` edge `0.0968` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.1823` n `53` status `ready` deltaP `25.4406` edge `0.0377` maxDD `-0.3692`
- `news_risk_high->index_4h` score `2.1553` n `53` status `ready` deltaP `21.9656` edge `0.0768` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `2.1315` n `53` status `ready` deltaP `26.1936` edge `0.2625` maxDD `-10.1088`
- `news_risk_high->crypto_alt_24h` score `1.7746` n `53` status `ready` deltaP `14.4261` edge `0.5819` maxDD `-29.0448`
- `news_risk_high->index_1h` score `1.2131` n `53` status `ready` deltaP `16.4275` edge `0.0217` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.7203` n `53` status `ready` deltaP `17.4443` edge `0.074` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
