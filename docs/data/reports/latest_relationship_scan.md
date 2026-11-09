# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T11:07:26.839689+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9226`

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

- `market_context_high->equity_24h` score `7.999` n `34` status `ready` deltaP `13.0005` edge `0.8172` maxDD `-16.6495`
- `market_context_high->commodity_24h` score `1.926` n `34` status `ready` deltaP `4.1463` edge `0.1916` maxDD `-1.6995`
- `market_context_high->index_24h` score `1.1052` n `34` status `ready` deltaP `12.6226` edge `0.1038` maxDD `-2.3671`
- `market_context_high->fx_24h` score `0.425` n `34` status `ready` deltaP `8.078` edge `-0.0078` maxDD `-0.1843`
- `market_context_high->metal_1h` score `-0.3149` n `88` status `ready` deltaP `4.2461` edge `0.0131` maxDD `-1.4122`
- `market_context_high->index_4h` score `-0.4523` n `88` status `ready` deltaP `4.6147` edge `0.009` maxDD `-2.4871`
- `market_context_high->commodity_1h` score `-0.4673` n `88` status `ready` deltaP `0.8914` edge `0.0024` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.7355` n `88` status `ready` deltaP `-1.4689` edge `0.0261` maxDD `-4.182`
- `market_context_high->index_1h` score `-0.8865` n `88` status `ready` deltaP `-5.8587` edge `0.0085` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-0.958` n `88` status `ready` deltaP `0.4712` edge `0.0124` maxDD `-4.0688`
- `market_context_high->equity_1h` score `-1.2408` n `88` status `ready` deltaP `-5.709` edge `0.0626` maxDD `-8.0225`
- `market_context_high->fx_1h` score `-1.2891` n `88` status `ready` deltaP `-13.6091` edge `-0.0061` maxDD `-0.8088`
- `market_context_high->metal_24h` score `-1.7522` n `34` status `ready` deltaP `-0.6944` edge `-0.1647` maxDD `-1.4245`
- `market_context_high->crypto_alt_1h` score `-1.7706` n `88` status `ready` deltaP `1.6807` edge `-0.0403` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-2.1859` n `88` status `ready` deltaP `-7.9823` edge `-0.0089` maxDD `-2.4506`
- `market_context_high->crypto_major_1h` score `-3.0318` n `88` status `ready` deltaP `-4.0623` edge `-0.0993` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-4.5157` n `88` status `ready` deltaP `2.5915` edge `-0.0156` maxDD `-24.9053`
- `market_context_high->unknown_4h` score `-5.3617` n `88` status `ready` deltaP `6.4579` edge `-0.4451` maxDD `-0.9139`
- `market_context_high->crypto_major_24h` score `-7.2424` n `34` status `ready` deltaP `-6.6993` edge `-0.0958` maxDD `-30.3789`
- `market_context_high->crypto_alt_4h` score `-7.9871` n `88` status `ready` deltaP `3.7694` edge `-0.1789` maxDD `-34.2787`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
