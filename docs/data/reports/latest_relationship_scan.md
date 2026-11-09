# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T20:52:30.339084+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `10180`

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

- `market_context_high->equity_24h` score `12.1299` n `47` status `ready` deltaP `20.7714` edge `1.6571` maxDD `-16.9034`
- `market_context_high->unknown_4h` score `10.0305` n `88` status `ready` deltaP `7.043` edge `0.8337` maxDD `-0.9153`
- `market_context_high->index_24h` score `2.1677` n `47` status `ready` deltaP `17.2757` edge `0.209` maxDD `-2.3671`
- `market_context_high->metal_1h` score `-0.4156` n `88` status `ready` deltaP `3.1982` edge `0.0117` maxDD `-1.4122`
- `market_context_high->commodity_24h` score `-0.4948` n `47` status `ready` deltaP `-9.4878` edge `0.1128` maxDD `-4.0382`
- `market_context_high->commodity_1h` score `-0.5717` n `88` status `ready` deltaP `-0.6056` edge `-0.001` maxDD `-1.7935`
- `market_context_high->index_4h` score `-0.8323` n `88` status `ready` deltaP `0.2785` edge `-0.0108` maxDD `-2.4871`
- `market_context_high->commodity_4h` score `-0.9628` n `88` status `ready` deltaP `-3.3641` edge `0.0096` maxDD `-4.182`
- `market_context_high->metal_4h` score `-1.0799` n `88` status `ready` deltaP `-1.5878` edge `0.0105` maxDD `-4.0688`
- `market_context_high->index_1h` score `-1.0952` n `88` status `ready` deltaP `-9.1521` edge `0.0037` maxDD `-0.9814`
- `market_context_high->metal_24h` score `-1.2061` n `47` status `ready` deltaP `6.4641` edge `-0.0883` maxDD `-1.4245`
- `market_context_high->fx_1h` score `-1.3016` n `88` status `ready` deltaP `-13.9085` edge `-0.0057` maxDD `-0.8088`
- `market_context_high->fx_24h` score `-1.3446` n `47` status `ready` deltaP `-6.2539` edge `-0.0416` maxDD `-2.1272`
- `market_context_high->equity_1h` score `-1.771` n `88` status `ready` deltaP `-8.4036` edge `0.0136` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-2.0231` n `88` status `ready` deltaP `-0.1157` edge `-0.0607` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-2.082` n `88` status `ready` deltaP `-6.0727` edge `-0.0083` maxDD `-2.4506`
- `market_context_high->crypto_major_1h` score `-3.243` n `88` status `ready` deltaP `-5.709` edge `-0.1154` maxDD `-15.9848`
- `market_context_high->crypto_alt_24h` score `-4.5481` n `47` status `ready` deltaP `-1.121` edge `0.1379` maxDD `-33.4213`
- `market_context_high->equity_4h` score `-7.4139` n `88` status `ready` deltaP `-2.6636` edge `-0.2189` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-9.2751` n `88` status `ready` deltaP `1.2436` edge `-0.2694` maxDD `-34.2787`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
