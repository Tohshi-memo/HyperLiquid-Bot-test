# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T21:02:00.161062+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `9980`

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

- `market_context_high->equity_24h` score `12.6598` n `48` status `ready` deltaP `21.4363` edge `1.7206` maxDD `-16.9034`
- `market_context_high->unknown_4h` score `10.1925` n `88` status `ready` deltaP `7.043` edge `0.8472` maxDD `-0.9153`
- `market_context_high->index_24h` score `2.2586` n `48` status `ready` deltaP `17.8076` edge `0.2171` maxDD `-2.3671`
- `market_context_high->metal_1h` score `-0.4156` n `88` status `ready` deltaP `3.1982` edge `0.0117` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.5841` n `88` status `ready` deltaP `-0.7553` edge `-0.0016` maxDD `-1.7935`
- `market_context_high->commodity_24h` score `-0.6266` n `48` status `ready` deltaP `-10.1567` edge `0.1082` maxDD `-4.3321`
- `market_context_high->index_4h` score `-0.833` n `88` status `ready` deltaP `0.2785` edge `-0.0109` maxDD `-2.4871`
- `market_context_high->commodity_4h` score `-0.9628` n `88` status `ready` deltaP `-3.3641` edge `0.0096` maxDD `-4.182`
- `market_context_high->metal_24h` score `-1.0577` n `48` status `ready` deltaP `7.0443` edge `-0.0798` maxDD `-1.4245`
- `market_context_high->metal_4h` score `-1.0822` n `88` status `ready` deltaP `-1.5878` edge `0.0102` maxDD `-4.0688`
- `market_context_high->index_1h` score `-1.096` n `88` status `ready` deltaP `-9.1521` edge `0.0036` maxDD `-0.9814`
- `market_context_high->fx_1h` score `-1.3016` n `88` status `ready` deltaP `-13.9085` edge `-0.0057` maxDD `-0.8088`
- `market_context_high->fx_24h` score `-1.451` n `48` status `ready` deltaP `-7.1888` edge `-0.0433` maxDD `-2.2509`
- `market_context_high->equity_1h` score `-1.7734` n `88` status `ready` deltaP `-8.4036` edge `0.0133` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-2.0098` n `88` status `ready` deltaP `0.034` edge `-0.06` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-2.082` n `88` status `ready` deltaP `-6.0727` edge `-0.0083` maxDD `-2.4506`
- `market_context_high->crypto_major_1h` score `-3.243` n `88` status `ready` deltaP `-5.709` edge `-0.1154` maxDD `-15.9848`
- `market_context_high->crypto_alt_24h` score `-4.1595` n `48` status `ready` deltaP `0.0758` edge `0.1623` maxDD `-33.4213`
- `market_context_high->equity_4h` score `-7.3981` n `88` status `ready` deltaP `-2.5114` edge `-0.2186` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-9.2461` n `88` status `ready` deltaP `1.3958` edge `-0.268` maxDD `-34.2787`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
