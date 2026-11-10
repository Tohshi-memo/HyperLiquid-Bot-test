# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T05:22:32.183361+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11538`

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

- `market_context_high->unknown_4h` score `37.9981` n `88` status `ready` deltaP `7.6774` edge `3.1601` maxDD `-0.9153`
- `market_context_high->equity_24h` score `34.0117` n `81` status `ready` deltaP `31.9148` edge `2.862` maxDD `-16.9034`
- `market_context_high->index_24h` score `5.4263` n `81` status `ready` deltaP `25.5665` edge `0.328` maxDD `-2.3671`
- `market_context_high->crypto_alt_24h` score `3.1595` n `81` status `ready` deltaP `20.0248` edge `0.781` maxDD `-33.4213`
- `market_context_high->metal_24h` score `-0.1533` n `81` status `ready` deltaP `15.7541` edge `-0.0625` maxDD `-1.4245`
- `market_context_high->metal_1h` score `-0.4575` n `88` status `ready` deltaP `2.8988` edge `0.0102` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.4852` n `88` status `ready` deltaP `0.7417` edge `0.0011` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.6252` n `88` status `ready` deltaP `0.8176` edge `0.025` maxDD `-4.182`
- `market_context_high->index_4h` score `-0.8272` n `88` status `ready` deltaP `0.3464` edge `-0.0106` maxDD `-2.4871`
- `market_context_high->index_1h` score `-1.0929` n `88` status `ready` deltaP `-9.1521` edge `0.004` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.2455` n `88` status `ready` deltaP `-2.8825` edge `-0.0021` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.3786` n `88` status `ready` deltaP `-15.2558` edge `-0.0066` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.8076` n `88` status `ready` deltaP `-9.1521` edge `0.0139` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.9654` n `88` status `ready` deltaP `0.4831` edge `-0.0573` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-2.2054` n `88` status `ready` deltaP `-7.9823` edge `-0.0114` maxDD `-2.4506`
- `market_context_high->fx_24h` score `-2.8608` n `81` status `ready` deltaP `-6.7698` edge `-0.0333` maxDD `-3.4642`
- `market_context_high->crypto_major_1h` score `-3.1955` n `88` status `ready` deltaP `-5.2599` edge `-0.1123` maxDD `-15.9848`
- `market_context_high->commodity_24h` score `-5.3204` n `81` status `ready` deltaP `-22.1238` edge `-0.0549` maxDD `-22.044`
- `market_context_high->equity_4h` score `-7.5185` n `88` status `ready` deltaP `-2.5915` edge `-0.2281` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-9.1752` n `88` status `ready` deltaP `1.7877` edge `-0.2647` maxDD `-34.2787`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
