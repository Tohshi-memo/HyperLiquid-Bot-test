# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T15:22:30.375957+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9286`

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

- `market_context_high->equity_24h` score `6.6519` n `34` status `ready` deltaP `10.9171` edge `0.722` maxDD `-16.9034`
- `market_context_high->commodity_24h` score `1.9464` n `34` status `ready` deltaP `4.1463` edge `0.1933` maxDD `-1.6995`
- `market_context_high->index_24h` score `0.9125` n `34` status `ready` deltaP `10.192` edge `0.0953` maxDD `-2.3671`
- `market_context_high->fx_24h` score `0.656` n `34` status `ready` deltaP `10.335` edge `-0.0036` maxDD `-0.1843`
- `market_context_high->metal_1h` score `-0.3137` n `88` status `ready` deltaP `4.0964` edge `0.0142` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.5288` n `88` status `ready` deltaP `-0.0068` edge `0.0005` maxDD `-1.7935`
- `market_context_high->index_4h` score `-0.5524` n `88` status `ready` deltaP `3.3952` edge `0.0043` maxDD `-2.4871`
- `market_context_high->commodity_4h` score `-0.8051` n `88` status `ready` deltaP `-1.6214` edge `0.0182` maxDD `-4.182`
- `market_context_high->metal_4h` score `-0.9221` n `88` status `ready` deltaP `0.4712` edge `0.017` maxDD `-4.0688`
- `market_context_high->index_1h` score `-0.9566` n `88` status `ready` deltaP `-6.9066` edge `0.0065` maxDD `-0.9814`
- `market_context_high->fx_1h` score `-1.2868` n `88` status `ready` deltaP `-13.6091` edge `-0.0058` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.5029` n `88` status `ready` deltaP `-7.0563` edge `0.039` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.8875` n `88` status `ready` deltaP `0.9322` edge `-0.0503` maxDD `-10.8319`
- `market_context_high->metal_24h` score `-2.0632` n `34` status `ready` deltaP `-3.6458` edge `-0.1849` maxDD `-1.4245`
- `market_context_high->fx_4h` score `-2.0933` n `88` status `ready` deltaP `-6.3054` edge `-0.0082` maxDD `-2.4506`
- `market_context_high->crypto_major_1h` score `-3.1308` n `88` status `ready` deltaP `-4.8108` edge `-0.107` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-5.6228` n `88` status `ready` deltaP `0.0` edge `-0.0874` maxDD `-25.16`
- `market_context_high->crypto_major_24h` score `-6.3117` n `34` status `ready` deltaP `-6.5257` edge `-0.0194` maxDD `-30.3789`
- `market_context_high->crypto_alt_4h` score `-8.7786` n `88` status `ready` deltaP `2.245` edge `-0.2347` maxDD `-34.2787`
- `market_context_high->crypto_alt_24h` score `-10.8614` n `34` status `ready` deltaP `-21.2521` edge `-0.254` maxDD `-33.4213`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
