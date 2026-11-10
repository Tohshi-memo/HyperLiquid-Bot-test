# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T20:22:34.727313+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11754`

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

- `market_context_high->unknown_4h` score `56.2583` n `88` status `ready` deltaP `7.525` edge `4.6828` maxDD `-0.9153`
- `market_context_high->equity_24h` score `35.2148` n `88` status `ready` deltaP `33.6489` edge `2.9507` maxDD `-16.9034`
- `market_context_high->crypto_alt_24h` score `6.3304` n `88` status `ready` deltaP `27.904` edge `1.135` maxDD `-33.4213`
- `market_context_high->index_24h` score `5.8111` n `88` status `ready` deltaP `29.0719` edge `0.3367` maxDD `-2.3671`
- `market_context_high->metal_24h` score `1.6652` n `88` status `ready` deltaP `23.2165` edge `0.0393` maxDD `-1.4245`
- `market_context_high->metal_1h` score `-0.3796` n `88` status `ready` deltaP `3.4976` edge `0.0127` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.3918` n `88` status `ready` deltaP `2.6878` edge `0.0001` maxDD `-1.7935`
- `market_context_high->index_4h` score `-0.505` n `88` status `ready` deltaP `5.072` edge `-0.0008` maxDD `-2.4871`
- `market_context_high->commodity_4h` score `-0.5083` n `88` status `ready` deltaP `3.5615` edge `0.0217` maxDD `-4.182`
- `market_context_high->index_1h` score `-0.9932` n `88` status `ready` deltaP `-7.5054` edge `0.0058` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.0071` n `88` status `ready` deltaP `-0.4434` edge `0.0122` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.2323` n `88` status `ready` deltaP `-12.7109` edge `-0.0048` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.5668` n `88` status `ready` deltaP `-7.5054` edge `0.0338` maxDD `-8.1039`
- `market_context_high->fx_4h` score `-1.8069` n `88` status `ready` deltaP `-1.4274` edge `-0.004` maxDD `-2.4506`
- `market_context_high->crypto_alt_1h` score `-1.8095` n `88` status `ready` deltaP `1.2316` edge `-0.0423` maxDD `-10.8319`
- `market_context_high->fx_24h` score `-1.8299` n `88` status `ready` deltaP `2.9514` edge `-0.0122` maxDD `-3.4642`
- `market_context_high->crypto_major_1h` score `-2.9359` n `88` status `ready` deltaP `-3.6132` edge `-0.09` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-5.8187` n `88` status `ready` deltaP `2.5915` edge `-0.121` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-8.0465` n `88` status `ready` deltaP `5.1414` edge `-0.193` maxDD `-34.2787`
- `market_context_high->crypto_major_24h` score `-8.0587` n `88` status `ready` deltaP `4.7191` edge `0.4595` maxDD `-80.6681`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
