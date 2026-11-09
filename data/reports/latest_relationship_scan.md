# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T14:07:30.887090+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9232`

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

- `market_context_high->equity_24h` score `7.1136` n `34` status `ready` deltaP `12.1324` edge `0.7492` maxDD `-16.6495`
- `market_context_high->commodity_24h` score `1.9728` n `34` status `ready` deltaP `4.1463` edge `0.1955` maxDD `-1.6995`
- `market_context_high->index_24h` score `0.9842` n `34` status `ready` deltaP `11.0601` edge `0.0987` maxDD `-2.3671`
- `market_context_high->fx_24h` score `0.6023` n `34` status `ready` deltaP `9.8141` edge `-0.0046` maxDD `-0.1843`
- `market_context_high->metal_1h` score `-0.3521` n `88` status `ready` deltaP `3.797` edge `0.013` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.4821` n `88` status `ready` deltaP `0.592` edge `0.0025` maxDD `-1.7935`
- `market_context_high->index_4h` score `-0.5004` n `88` status `ready` deltaP `4.005` edge `0.0069` maxDD `-2.4871`
- `market_context_high->commodity_4h` score `-0.7667` n `88` status `ready` deltaP `-1.4689` edge `0.0221` maxDD `-4.182`
- `market_context_high->index_1h` score `-0.9208` n `88` status `ready` deltaP `-6.4575` edge `0.0081` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-0.9268` n `88` status `ready` deltaP `0.4712` edge `0.0164` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.279` n `88` status `ready` deltaP `-13.4594` edge `-0.0058` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.3468` n `88` status `ready` deltaP `-6.7569` edge `0.056` maxDD `-8.0225`
- `market_context_high->crypto_alt_1h` score `-1.8438` n `88` status `ready` deltaP `1.3813` edge `-0.0477` maxDD `-10.8319`
- `market_context_high->metal_24h` score `-1.9783` n `34` status `ready` deltaP `-2.7778` edge `-0.1798` maxDD `-1.4245`
- `market_context_high->fx_4h` score `-2.1345` n `88` status `ready` deltaP `-7.0676` edge `-0.0084` maxDD `-2.4506`
- `market_context_high->crypto_major_1h` score `-3.077` n `88` status `ready` deltaP `-4.3617` edge `-0.1031` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-5.1384` n `88` status `ready` deltaP `0.7622` edge `-0.0553` maxDD `-24.9053`
- `market_context_high->crypto_major_24h` score `-6.5625` n `34` status `ready` deltaP `-6.5257` edge `-0.0403` maxDD `-30.3789`
- `market_context_high->crypto_alt_4h` score `-8.444` n `88` status `ready` deltaP `3.0072` edge `-0.2119` maxDD `-34.2787`
- `market_context_high->crypto_alt_24h` score `-10.6815` n `34` status `ready` deltaP `-20.384` edge `-0.2448` maxDD `-33.4213`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
