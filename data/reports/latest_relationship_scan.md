# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T08:22:28.727662+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11174`

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

- `market_context_high->unknown_24h` score `281.9114` n `80` status `ready` deltaP `6.1806` edge `23.4655` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `77.431` n `90` status `ready` deltaP `6.355` edge `6.455` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `32.2464` n `53` status `ready` deltaP `30.8897` edge `2.5519` maxDD `-3.6503`
- `market_context_high->equity_24h` score `24.9459` n `80` status `ready` deltaP `27.8472` edge `1.9638` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `13.6266` n `53` status `ready` deltaP `41.3489` edge `1.6679` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `10.3662` n `53` status `ready` deltaP `35.0207` edge `0.7434` maxDD `-7.0416`
- `market_context_high->crypto_alt_24h` score `10.2772` n `80` status `ready` deltaP `47.9514` edge `1.4075` maxDD `-25.4331`
- `market_context_high->metal_24h` score `7.2749` n `80` status `ready` deltaP `44.1667` edge `0.3531` maxDD `-0.3044`
- `news_risk_high->commodity_24h` score `6.2078` n `53` status `ready` deltaP `39.0625` edge `0.2569` maxDD `0.0`
- `market_context_high->index_24h` score `4.5485` n `80` status `ready` deltaP `25.4167` edge `0.2191` maxDD `-0.0934`
- `news_risk_high->metal_4h` score `4.5464` n `53` status `ready` deltaP `43.4998` edge `0.1265` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.1219` n `53` status `ready` deltaP `24.0959` edge `0.2132` maxDD `-0.4279`
- `news_risk_high->crypto_major_4h` score `3.4368` n `53` status `ready` deltaP `20.4384` edge `0.2989` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.2338` n `53` status `ready` deltaP `17.7155` edge `0.2144` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.1023` n `53` status `ready` deltaP `28.5406` edge `0.0936` maxDD `-0.3611`
- `news_risk_high->crypto_alt_24h` score `2.981` n `53` status `ready` deltaP `19.4608` edge `0.703` maxDD `-29.0448`
- `news_risk_high->metal_1h` score `2.1151` n `53` status `ready` deltaP `24.9915` edge `0.0351` maxDD `-0.3692`
- `news_risk_high->crypto_alt_4h` score `1.9461` n `53` status `ready` deltaP `26.4985` edge `0.2367` maxDD `-10.1088`
- `news_risk_high->index_4h` score `1.9224` n `53` status `ready` deltaP `19.9839` edge `0.0706` maxDD `-0.8235`
- `news_risk_high->index_1h` score `1.1747` n `53` status `ready` deltaP `16.2778` edge `0.0195` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
