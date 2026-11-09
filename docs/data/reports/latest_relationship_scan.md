# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T11:37:27.519726+00:00`
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

- `market_context_high->equity_24h` score `7.8658` n `34` status `ready` deltaP `13.0005` edge `0.8061` maxDD `-16.6495`
- `market_context_high->commodity_24h` score `1.9344` n `34` status `ready` deltaP `4.1463` edge `0.1923` maxDD `-1.6995`
- `market_context_high->index_24h` score `1.0907` n `34` status `ready` deltaP `12.449` edge `0.1031` maxDD `-2.3671`
- `market_context_high->fx_24h` score `0.46` n `34` status `ready` deltaP `8.4252` edge `-0.0072` maxDD `-0.1843`
- `market_context_high->metal_1h` score `-0.303` n `88` status `ready` deltaP `4.3958` edge `0.0131` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.4595` n `88` status `ready` deltaP `0.8914` edge `0.0034` maxDD `-1.7935`
- `market_context_high->index_4h` score `-0.4634` n `88` status `ready` deltaP `4.4623` edge `0.0086` maxDD `-2.4871`
- `market_context_high->commodity_4h` score `-0.7387` n `88` status `ready` deltaP `-1.4689` edge `0.0257` maxDD `-4.182`
- `market_context_high->index_1h` score `-0.8873` n `88` status `ready` deltaP `-5.8587` edge `0.0084` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-0.9556` n `88` status `ready` deltaP `0.4712` edge `0.0127` maxDD `-4.0688`
- `market_context_high->equity_1h` score `-1.2509` n `88` status `ready` deltaP `-5.8587` edge `0.0623` maxDD `-8.0225`
- `market_context_high->fx_1h` score `-1.2805` n `88` status `ready` deltaP `-13.4594` edge `-0.006` maxDD `-0.8088`
- `market_context_high->crypto_alt_1h` score `-1.7799` n `88` status `ready` deltaP `1.6807` edge `-0.0415` maxDD `-10.8319`
- `market_context_high->metal_24h` score `-1.7913` n `34` status `ready` deltaP `-1.0417` edge `-0.1674` maxDD `-1.4245`
- `market_context_high->fx_4h` score `-2.1946` n `88` status `ready` deltaP `-8.1347` edge `-0.009` maxDD `-2.4506`
- `market_context_high->crypto_major_1h` score `-3.0521` n `88` status `ready` deltaP `-4.212` edge `-0.1009` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-4.6217` n `88` status `ready` deltaP `2.2866` edge `-0.0224` maxDD `-24.9053`
- `market_context_high->crypto_major_24h` score `-7.1404` n `34` status `ready` deltaP `-6.6993` edge `-0.0873` maxDD `-30.3789`
- `market_context_high->crypto_alt_4h` score `-8.0447` n `88` status `ready` deltaP `3.7694` edge `-0.1837` maxDD `-34.2787`
- `market_context_high->crypto_alt_24h` score `-10.5553` n `34` status `ready` deltaP `-20.0368` edge `-0.2366` maxDD `-33.4213`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
