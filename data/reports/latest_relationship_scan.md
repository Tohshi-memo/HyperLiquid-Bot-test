# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T21:22:34.565143+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7982`

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

- `market_context_high->unknown_4h` score `92.5311` n `153` status `ready` deltaP `1.0172` edge `7.7377` maxDD `-1.0178`
- `market_context_high->unknown_1h` score `24.1369` n `153` status `ready` deltaP `1.4745` edge `2.0505` maxDD `-1.5807`
- `market_context_high->fx_1h` score `0.2782` n `153` status `ready` deltaP `8.4145` edge `0.0029` maxDD `-0.1986`
- `market_context_high->metal_24h` score `0.2643` n `112` status `ready` deltaP `23.762` edge `0.1381` maxDD `-7.0108`
- `market_context_high->fx_4h` score `0.0994` n `153` status `ready` deltaP `9.0198` edge `0.008` maxDD `-0.4545`
- `market_context_high->index_24h` score `-0.0191` n `112` status `ready` deltaP `16.3051` edge `0.0127` maxDD `-4.5747`
- `market_context_high->metal_1h` score `-0.1306` n `153` status `ready` deltaP `8.3304` edge `0.0069` maxDD `-1.6682`
- `market_context_high->fx_24h` score `-0.2041` n `112` status `ready` deltaP `15.7588` edge `0.026` maxDD `-1.2451`
- `market_context_high->commodity_1h` score `-0.2582` n `153` status `ready` deltaP `2.3023` edge `0.0132` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.5408` n `153` status `ready` deltaP `0.7612` edge `-0.0007` maxDD `-1.8971`
- `market_context_high->commodity_4h` score `-0.6078` n `153` status `ready` deltaP `4.6867` edge `0.041` maxDD `-1.165`
- `market_context_high->crypto_major_1h` score `-0.828` n `153` status `ready` deltaP `4.8325` edge `0.0197` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-0.9369` n `153` status `ready` deltaP `7.6648` edge `-0.0002` maxDD `-5.3474`
- `market_context_high->equity_1h` score `-1.759` n `153` status `ready` deltaP `1.904` edge `-0.0106` maxDD `-12.2088`
- `market_context_high->crypto_alt_1h` score `-1.9367` n `153` status `ready` deltaP `0.0235` edge `0.0` maxDD `-13.2099`
- `market_context_high->index_4h` score `-3.3497` n `153` status `ready` deltaP `-5.7747` edge `-0.023` maxDD `-6.7447`
- `market_context_high->crypto_major_24h` score `-4.4141` n `112` status `ready` deltaP `-2.4449` edge `-0.0639` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-4.486` n `153` status `ready` deltaP `0.6087` edge `-0.0752` maxDD `-32.9851`
- `market_context_high->commodity_24h` score `-6.125` n `112` status `ready` deltaP `-14.8242` edge `-0.1275` maxDD `-24.0477`
- `market_context_high->equity_24h` score `-6.4632` n `112` status `ready` deltaP `-5.6434` edge `-0.2477` maxDD `-35.4638`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
