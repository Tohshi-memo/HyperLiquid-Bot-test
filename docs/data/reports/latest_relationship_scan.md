# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T19:37:29.491563+00:00`
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

- `market_context_high->equity_24h` score `9.1134` n `42` status `ready` deltaP `16.972` edge `1.2957` maxDD `-16.9034`
- `market_context_high->index_24h` score `1.6618` n `42` status `ready` deltaP `14.2362` edge `0.1644` maxDD `-2.3671`
- `market_context_high->unknown_4h` score `0.98` n `88` status `ready` deltaP `6.8908` edge `0.0805` maxDD `-0.9153`
- `market_context_high->commodity_24h` score `0.4377` n `42` status `ready` deltaP `-5.5418` edge `0.1573` maxDD `-1.8062`
- `market_context_high->metal_1h` score `-0.3341` n `88` status `ready` deltaP `3.9467` edge `0.0135` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.5904` n `88` status `ready` deltaP `-0.7553` edge `-0.0024` maxDD `-1.7935`
- `market_context_high->fx_24h` score `-0.7179` n `42` status `ready` deltaP `-0.7882` edge `-0.0284` maxDD `-1.3369`
- `market_context_high->index_4h` score `-0.7881` n `88` status `ready` deltaP `0.8873` edge `-0.0092` maxDD `-2.4871`
- `market_context_high->commodity_4h` score `-0.9958` n `88` status `ready` deltaP `-3.6685` edge `0.0074` maxDD `-4.182`
- `market_context_high->metal_4h` score `-1.0326` n `88` status `ready` deltaP `-0.9789` edge `0.0125` maxDD `-4.0688`
- `market_context_high->index_1h` score `-1.0477` n `88` status `ready` deltaP `-8.4036` edge `0.0048` maxDD `-0.9814`
- `market_context_high->fx_1h` score `-1.3187` n `88` status `ready` deltaP `-14.2079` edge `-0.0059` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.6845` n `88` status `ready` deltaP `-7.8048` edge `0.0207` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-2.0223` n `88` status `ready` deltaP `-0.2654` edge `-0.0596` maxDD `-10.8319`
- `market_context_high->metal_24h` score `-2.0861` n `42` status `ready` deltaP `3.0247` edge `-0.1387` maxDD `-1.4245`
- `market_context_high->fx_4h` score `-2.0986` n `88` status `ready` deltaP `-6.3771` edge `-0.0084` maxDD `-2.4506`
- `market_context_high->crypto_major_1h` score `-3.2181` n `88` status `ready` deltaP `-5.4096` edge `-0.1142` maxDD `-15.9848`
- `market_context_high->crypto_alt_24h` score `-6.8316` n `42` status `ready` deltaP `-7.9599` edge `-0.0068` maxDD `-33.4213`
- `market_context_high->equity_4h` score `-7.3297` n `88` status `ready` deltaP `-2.5114` edge `-0.2129` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-9.385` n `88` status `ready` deltaP `0.6348` edge `-0.2745` maxDD `-34.2787`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
