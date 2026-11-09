# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T12:37:27.642286+00:00`
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

- `market_context_high->equity_24h` score `7.5958` n `34` status `ready` deltaP `13.0005` edge `0.7836` maxDD `-16.6495`
- `market_context_high->commodity_24h` score `1.9608` n `34` status `ready` deltaP `4.1463` edge `0.1945` maxDD `-1.6995`
- `market_context_high->index_24h` score `1.0594` n `34` status `ready` deltaP `12.1017` edge `0.1014` maxDD `-2.3671`
- `market_context_high->fx_24h` score `0.5287` n `34` status `ready` deltaP `9.1197` edge `-0.0061` maxDD `-0.1843`
- `market_context_high->metal_1h` score `-0.3461` n `88` status `ready` deltaP `3.9467` edge `0.0125` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.4447` n `88` status `ready` deltaP `1.0411` edge `0.0043` maxDD `-1.7935`
- `market_context_high->index_4h` score `-0.4855` n `88` status `ready` deltaP `4.1574` edge `0.0078` maxDD `-2.4871`
- `market_context_high->commodity_4h` score `-0.748` n `88` status `ready` deltaP `-1.4689` edge `0.0245` maxDD `-4.182`
- `market_context_high->index_1h` score `-0.9037` n `88` status `ready` deltaP `-6.1581` edge `0.0083` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-0.9486` n `88` status `ready` deltaP `0.4712` edge `0.0136` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.2634` n `88` status `ready` deltaP `-13.16` edge `-0.0058` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.2875` n `88` status `ready` deltaP `-6.3078` edge `0.0606` maxDD `-8.0225`
- `market_context_high->crypto_alt_1h` score `-1.8095` n `88` status `ready` deltaP `1.531` edge `-0.0443` maxDD `-10.8319`
- `market_context_high->metal_24h` score `-1.8703` n `34` status `ready` deltaP `-1.7361` edge `-0.1729` maxDD `-1.4245`
- `market_context_high->fx_4h` score `-2.1693` n `88` status `ready` deltaP `-7.6774` edge `-0.0088` maxDD `-2.4506`
- `market_context_high->crypto_major_1h` score `-3.0778` n `88` status `ready` deltaP `-4.5114` edge `-0.1022` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-4.8337` n `88` status `ready` deltaP `1.6768` edge `-0.036` maxDD `-24.9053`
- `market_context_high->crypto_major_24h` score `-6.9304` n `34` status `ready` deltaP `-6.6993` edge `-0.0698` maxDD `-30.3789`
- `market_context_high->crypto_alt_4h` score `-8.1887` n `88` status `ready` deltaP `3.7694` edge `-0.1957` maxDD `-34.2787`
- `market_context_high->crypto_alt_24h` score `-10.5793` n `34` status `ready` deltaP `-20.0368` edge `-0.2386` maxDD `-33.4213`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
