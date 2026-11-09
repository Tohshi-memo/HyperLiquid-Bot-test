# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T15:37:28.396468+00:00`
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

- `market_context_high->equity_24h` score `6.5468` n `34` status `ready` deltaP `10.7435` edge `0.7144` maxDD `-16.9034`
- `market_context_high->commodity_24h` score `1.9428` n `34` status `ready` deltaP `4.1463` edge `0.193` maxDD `-1.6995`
- `market_context_high->index_24h` score `0.898` n `34` status `ready` deltaP `10.0184` edge `0.0946` maxDD `-2.3671`
- `market_context_high->fx_24h` score `0.6734` n `34` status `ready` deltaP `10.5086` edge `-0.0033` maxDD `-0.1843`
- `market_context_high->metal_1h` score `-0.3149` n `88` status `ready` deltaP `4.0964` edge `0.0141` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.5374` n `88` status `ready` deltaP `-0.1565` edge `0.0004` maxDD `-1.7935`
- `market_context_high->index_4h` score `-0.5658` n `88` status `ready` deltaP `3.2428` edge `0.0036` maxDD `-2.4871`
- `market_context_high->commodity_4h` score `-0.8232` n `88` status `ready` deltaP `-1.7738` edge `0.0169` maxDD `-4.182`
- `market_context_high->metal_4h` score `-0.9308` n `88` status `ready` deltaP `0.3188` edge `0.0169` maxDD `-4.0688`
- `market_context_high->index_1h` score `-0.9574` n `88` status `ready` deltaP `-6.9066` edge `0.0064` maxDD `-0.9814`
- `market_context_high->fx_1h` score `-1.2868` n `88` status `ready` deltaP `-13.6091` edge `-0.0058` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.5153` n `88` status `ready` deltaP `-7.0563` edge `0.0374` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.9077` n `88` status `ready` deltaP `0.7825` edge `-0.0519` maxDD `-10.8319`
- `market_context_high->metal_24h` score `-2.0847` n `34` status `ready` deltaP `-3.8194` edge `-0.1865` maxDD `-1.4245`
- `market_context_high->fx_4h` score `-2.1012` n `88` status `ready` deltaP `-6.4579` edge `-0.0082` maxDD `-2.4506`
- `market_context_high->crypto_major_1h` score `-3.1518` n `88` status `ready` deltaP `-4.9605` edge `-0.1087` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-5.7202` n `88` status `ready` deltaP `-0.1524` edge `-0.0945` maxDD `-25.16`
- `market_context_high->crypto_major_24h` score `-6.2709` n `34` status `ready` deltaP `-6.5257` edge `-0.016` maxDD `-30.3789`
- `market_context_high->crypto_alt_4h` score `-8.8568` n `88` status `ready` deltaP `2.0926` edge `-0.2402` maxDD `-34.2787`
- `market_context_high->crypto_alt_24h` score `-10.9077` n `34` status `ready` deltaP `-21.4257` edge `-0.2567` maxDD `-33.4213`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
