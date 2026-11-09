# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T11:22:26.565035+00:00`
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

- `market_context_high->equity_24h` score `7.9306` n `34` status `ready` deltaP `13.0005` edge `0.8115` maxDD `-16.6495`
- `market_context_high->commodity_24h` score `1.9296` n `34` status `ready` deltaP `4.1463` edge `0.1919` maxDD `-1.6995`
- `market_context_high->index_24h` score `1.0931` n `34` status `ready` deltaP `12.449` edge `0.1034` maxDD `-2.3671`
- `market_context_high->fx_24h` score `0.4425` n `34` status `ready` deltaP `8.2516` edge `-0.0075` maxDD `-0.1843`
- `market_context_high->metal_1h` score `-0.3018` n `88` status `ready` deltaP `4.3958` edge `0.0132` maxDD `-1.4122`
- `market_context_high->index_4h` score `-0.4531` n `88` status `ready` deltaP `4.6147` edge `0.0089` maxDD `-2.4871`
- `market_context_high->commodity_1h` score `-0.4642` n `88` status `ready` deltaP `0.8914` edge `0.0028` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.7363` n `88` status `ready` deltaP `-1.4689` edge `0.026` maxDD `-4.182`
- `market_context_high->index_1h` score `-0.8865` n `88` status `ready` deltaP `-5.8587` edge `0.0085` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-0.9564` n `88` status `ready` deltaP `0.4712` edge `0.0126` maxDD `-4.0688`
- `market_context_high->equity_1h` score `-1.2408` n `88` status `ready` deltaP `-5.709` edge `0.0626` maxDD `-8.0225`
- `market_context_high->fx_1h` score `-1.2891` n `88` status `ready` deltaP `-13.6091` edge `-0.0061` maxDD `-0.8088`
- `market_context_high->metal_24h` score `-1.7705` n `34` status `ready` deltaP `-0.8681` edge `-0.1659` maxDD `-1.4245`
- `market_context_high->crypto_alt_1h` score `-1.7745` n `88` status `ready` deltaP `1.6807` edge `-0.0408` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-2.1939` n `88` status `ready` deltaP `-8.1347` edge `-0.0089` maxDD `-2.4506`
- `market_context_high->crypto_major_1h` score `-3.0458` n `88` status `ready` deltaP `-4.212` edge `-0.1001` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-4.5567` n `88` status `ready` deltaP `2.439` edge `-0.018` maxDD `-24.9053`
- `market_context_high->crypto_major_24h` score `-7.1932` n `34` status `ready` deltaP `-6.6993` edge `-0.0917` maxDD `-30.3789`
- `market_context_high->crypto_alt_4h` score `-8.0183` n `88` status `ready` deltaP `3.7694` edge `-0.1815` maxDD `-34.2787`
- `market_context_high->unknown_4h` score `-9.8533` n `88` status `ready` deltaP `6.4579` edge `-0.8194` maxDD `-0.9139`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
