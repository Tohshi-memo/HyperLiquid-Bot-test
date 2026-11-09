# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T17:07:38.146440+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `10126`

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

- `market_context_high->equity_24h` score `5.8358` n `34` status `ready` deltaP `9.7018` edge `0.6621` maxDD `-16.9034`
- `market_context_high->commodity_24h` score `1.9368` n `34` status `ready` deltaP `4.1463` edge `0.1925` maxDD `-1.6995`
- `market_context_high->index_24h` score `0.8002` n `34` status `ready` deltaP `8.9767` edge `0.089` maxDD `-2.3671`
- `market_context_high->fx_24h` score `0.7808` n `34` status `ready` deltaP `11.5502` edge `-0.0013` maxDD `-0.1843`
- `market_context_high->metal_1h` score `-0.261` n `88` status `ready` deltaP `4.6952` edge `0.0146` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.5576` n `88` status `ready` deltaP `-0.3062` edge `-0.0012` maxDD `-1.7935`
- `market_context_high->index_4h` score `-0.657` n `88` status `ready` deltaP `2.3281` edge `-0.002` maxDD `-2.4871`
- `market_context_high->commodity_4h` score `-0.9144` n `88` status `ready` deltaP `-2.6885` edge `0.0113` maxDD `-4.182`
- `market_context_high->index_1h` score `-0.9769` n `88` status `ready` deltaP `-7.206` edge `0.0059` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-0.9948` n `88` status `ready` deltaP `-0.5959` edge `0.0148` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.2868` n `88` status `ready` deltaP `-13.6091` edge `-0.0058` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.5925` n `88` status `ready` deltaP `-7.3557` edge `0.0295` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.935` n `88` status `ready` deltaP `0.4831` edge `-0.0534` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-2.102` n `88` status `ready` deltaP `-6.4579` edge `-0.0083` maxDD `-2.4506`
- `market_context_high->metal_24h` score `-2.2184` n `34` status `ready` deltaP `-4.8611` edge `-0.1967` maxDD `-1.4245`
- `market_context_high->crypto_major_1h` score `-3.1775` n `88` status `ready` deltaP `-5.2599` edge `-0.11` maxDD `-15.9848`
- `market_context_high->crypto_major_24h` score `-5.9364` n `34` status `ready` deltaP `-6.0049` edge `0.0084` maxDD `-30.3789`
- `market_context_high->equity_4h` score `-6.4822` n `88` status `ready` deltaP `-1.0671` edge `-0.1519` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-9.2456` n `88` status `ready` deltaP `1.178` edge `-0.2665` maxDD `-34.2787`
- `market_context_high->crypto_alt_24h` score `-11.1518` n `34` status `ready` deltaP `-22.4674` edge `-0.2701` maxDD `-33.4213`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
