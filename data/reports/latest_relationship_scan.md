# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-16T18:07:23.868275+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11830`

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

- `market_context_high->unknown_24h` score `226.7478` n `88` status `ready` deltaP `-21.512` edge `29.482` maxDD `-7.8016`
- `market_context_high->commodity_24h` score `7.9897` n `88` status `ready` deltaP `41.3037` edge `0.3962` maxDD `-0.1266`
- `market_context_high->commodity_4h` score `1.4632` n `125` status `ready` deltaP `14.2268` edge `0.0742` maxDD `-0.7687`
- `market_context_high->commodity_1h` score `-0.0482` n `128` status `ready` deltaP `2.6572` edge `0.0194` maxDD `-0.624`
- `market_context_high->fx_4h` score `-0.3024` n `125` status `ready` deltaP `4.3598` edge `0.0062` maxDD `-0.504`
- `market_context_high->fx_1h` score `-0.3692` n `128` status `ready` deltaP `0.6643` edge `0.0013` maxDD `-0.2527`
- `market_context_high->metal_1h` score `-0.4757` n `128` status `ready` deltaP `2.442` edge `-0.0057` maxDD `-1.7257`
- `market_context_high->index_1h` score `-0.8081` n `128` status `ready` deltaP `-7.2511` edge `-0.0031` maxDD `-0.5064`
- `market_context_high->metal_4h` score `-0.8887` n `125` status `ready` deltaP `8.4378` edge `-0.0128` maxDD `-4.5909`
- `market_context_high->fx_24h` score `-1.3352` n `88` status `ready` deltaP `-6.4552` edge `0.0326` maxDD `-1.8596`
- `market_context_high->equity_1h` score `-1.6691` n `128` status `ready` deltaP `-9.796` edge `-0.0447` maxDD `-4.9849`
- `market_context_high->metal_24h` score `-1.8845` n `88` status `ready` deltaP `-9.0909` edge `0.0702` maxDD `-7.0954`
- `market_context_high->crypto_alt_1h` score `-1.9566` n `128` status `ready` deltaP `-1.5297` edge `-0.0189` maxDD `-7.0497`
- `market_context_high->index_4h` score `-2.0216` n `125` status `ready` deltaP `-11.7183` edge `-0.0091` maxDD `-0.8328`
- `market_context_high->crypto_major_1h` score `-2.1336` n `128` status `ready` deltaP `-5.7682` edge `-0.0327` maxDD `-5.5318`
- `market_context_high->index_24h` score `-2.1435` n `88` status `ready` deltaP `-7.6231` edge `-0.07` maxDD `-2.3194`
- `market_context_high->crypto_major_4h` score `-3.7396` n `125` status `ready` deltaP `-1.5427` edge `-0.0656` maxDD `-13.1929`
- `market_context_high->crypto_major_24h` score `-5.0802` n `88` status `ready` deltaP `-6.392` edge `-0.023` maxDD `-35.189`
- `market_context_high->unknown_1h` score `-7.1349` n `128` status `ready` deltaP `0.6971` edge `-0.5535` maxDD `-1.3246`
- `market_context_high->crypto_alt_4h` score `-7.9511` n `125` status `ready` deltaP `-11.4476` edge `-0.0984` maxDD `-26.3633`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
