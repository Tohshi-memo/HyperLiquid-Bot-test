# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T21:52:35.530411+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `9954`

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

- `market_context_high->unknown_4h` score `22.1253` n `88` status `ready` deltaP `7.043` edge `1.8416` maxDD `-0.9153`
- `market_context_high->equity_24h` score `14.2545` n `51` status `ready` deltaP `23.2745` edge `1.9128` maxDD `-16.9034`
- `market_context_high->index_24h` score `2.534` n `51` status `ready` deltaP `19.2782` edge `0.2426` maxDD `-2.3671`
- `market_context_high->metal_1h` score `-0.4156` n `88` status `ready` deltaP `3.1982` edge `0.0117` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.5849` n `88` status `ready` deltaP `-0.7553` edge `-0.0017` maxDD `-1.7935`
- `market_context_high->metal_24h` score `-0.6483` n `51` status `ready` deltaP `8.6078` edge `-0.0561` maxDD `-1.4245`
- `market_context_high->index_4h` score `-0.852` n `88` status `ready` deltaP `-0.026` edge `-0.0113` maxDD `-2.4871`
- `market_context_high->commodity_4h` score `-0.9479` n `88` status `ready` deltaP `-3.2119` edge `0.0105` maxDD `-4.182`
- `market_context_high->commodity_24h` score `-1.0588` n `51` status `ready` deltaP `-11.9652` edge `0.0916` maxDD `-5.4724`
- `market_context_high->metal_4h` score `-1.09` n `88` status `ready` deltaP `-1.5878` edge `0.0092` maxDD `-4.0688`
- `market_context_high->index_1h` score `-1.1046` n `88` status `ready` deltaP `-9.3018` edge `0.0035` maxDD `-0.9814`
- `market_context_high->fx_1h` score `-1.3023` n `88` status `ready` deltaP `-13.9085` edge `-0.0058` maxDD `-0.8088`
- `market_context_high->fx_24h` score `-1.7492` n `51` status `ready` deltaP `-9.7326` edge `-0.0475` maxDD `-2.6162`
- `market_context_high->equity_1h` score `-1.7726` n `88` status `ready` deltaP `-8.4036` edge `0.0134` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.9857` n `88` status `ready` deltaP `0.1837` edge `-0.0579` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-2.0748` n `88` status `ready` deltaP `-5.9205` edge `-0.0084` maxDD `-2.4506`
- `market_context_high->crypto_alt_24h` score `-2.8904` n `51` status `ready` deltaP `3.3846` edge `0.246` maxDD `-33.4213`
- `market_context_high->crypto_major_1h` score `-3.2282` n `88` status `ready` deltaP `-5.5593` edge `-0.1145` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-7.4139` n `88` status `ready` deltaP `-2.6636` edge `-0.2189` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-9.1796` n `88` status `ready` deltaP `1.8524` edge `-0.2655` maxDD `-34.2787`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
