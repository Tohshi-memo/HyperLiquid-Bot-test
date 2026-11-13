# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T12:37:39.434345+00:00`
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

- `market_context_high->unknown_24h` score `382.7059` n `74` status `ready` deltaP `5.9779` edge `31.8664` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `32.7198` n `53` status `ready` deltaP `31.9314` edge `2.5844` maxDD `-3.6503`
- `market_context_high->equity_24h` score `25.1635` n `74` status `ready` deltaP `27.5713` edge `2.0598` maxDD `-8.7317`
- `market_context_high->crypto_alt_24h` score `18.7377` n `74` status `ready` deltaP `52.1021` edge `1.4656` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `14.2338` n `53` status `ready` deltaP `42.3906` edge `1.7388` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `10.3536` n `53` status `ready` deltaP `34.5633` edge `0.7454` maxDD `-7.0416`
- `market_context_high->metal_24h` score `6.0171` n `74` status `ready` deltaP `38.0021` edge `0.3293` maxDD `-3.4976`
- `news_risk_high->commodity_24h` score `5.8006` n `53` status `ready` deltaP `37.1528` edge `0.2357` maxDD `0.0`
- `market_context_high->index_24h` score `4.813` n `74` status `ready` deltaP `25.6099` edge `0.2395` maxDD `-0.0653`
- `news_risk_high->metal_4h` score `4.595` n `53` status `ready` deltaP `43.9571` edge `0.1275` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.0989` n `53` status `ready` deltaP `23.7486` edge `0.2136` maxDD `-0.4279`
- `news_risk_high->equity_1h` score `3.325` n `53` status `ready` deltaP `17.7155` edge `0.222` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `3.0571` n `53` status `ready` deltaP `19.0664` edge `0.2764` maxDD `-9.2335`
- `news_risk_high->commodity_4h` score `3.0393` n `53` status `ready` deltaP `28.0833` edge `0.0914` maxDD `-0.3611`
- `news_risk_high->crypto_alt_24h` score `2.9727` n `53` status `ready` deltaP `19.2872` edge `0.7031` maxDD `-29.0448`
- `news_risk_high->metal_1h` score `2.0924` n `53` status `ready` deltaP `24.6921` edge `0.0352` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.9344` n `53` status `ready` deltaP `19.9839` edge `0.0716` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.8578` n `53` status `ready` deltaP `26.346` edge `0.2264` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.1603` n `53` status `ready` deltaP `15.9784` edge `0.0203` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.6034` n `53` status `ready` deltaP `16.8455` edge `0.063` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
