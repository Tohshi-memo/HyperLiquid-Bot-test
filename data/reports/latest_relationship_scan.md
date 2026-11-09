# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T23:22:26.903622+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `9892`

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

- `market_context_high->unknown_4h` score `29.6371` n `88` status `ready` deltaP `7.2201` edge `2.4664` maxDD `-0.9153`
- `market_context_high->equity_24h` score `17.4029` n `57` status `ready` deltaP `26.3705` edge `2.2958` maxDD `-16.9034`
- `market_context_high->index_24h` score `3.0254` n `57` status `ready` deltaP `21.755` edge `0.2891` maxDD `-2.3671`
- `market_context_high->crypto_alt_24h` score `0.4398` n `57` status `ready` deltaP `8.9574` edge `0.5061` maxDD `-33.4213`
- `market_context_high->metal_24h` score `0.0533` n `57` status `ready` deltaP `11.0766` edge `-0.0141` maxDD `-1.4245`
- `market_context_high->metal_1h` score `-0.3904` n `88` status `ready` deltaP `3.4976` edge `0.0118` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.5405` n `88` status `ready` deltaP `-0.0068` edge `-0.001` maxDD `-1.7935`
- `market_context_high->index_4h` score `-0.8485` n `88` status `ready` deltaP `0.0416` edge `-0.0113` maxDD `-2.4871`
- `market_context_high->commodity_4h` score `-0.8791` n `88` status `ready` deltaP `-2.3836` edge `0.0138` maxDD `-4.182`
- `market_context_high->index_1h` score `-1.1131` n `88` status `ready` deltaP `-9.4515` edge `0.0034` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.1254` n `88` status `ready` deltaP `-1.9678` edge `0.0072` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.3273` n `88` status `ready` deltaP `-14.3576` edge `-0.006` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.7742` n `88` status `ready` deltaP `-8.4036` edge `0.0132` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.9561` n `88` status `ready` deltaP `0.4831` edge `-0.0561` maxDD `-10.8319`
- `market_context_high->commodity_24h` score `-1.9718` n `57` status `ready` deltaP `-14.8469` edge `0.0553` maxDD `-8.396`
- `market_context_high->fx_4h` score `-2.1154` n `88` status `ready` deltaP `-6.6103` edge `-0.009` maxDD `-2.4506`
- `market_context_high->fx_24h` score `-2.2536` n `57` status `ready` deltaP `-13.8527` edge `-0.0523` maxDD `-3.2079`
- `market_context_high->crypto_major_1h` score `-3.2414` n `88` status `ready` deltaP `-5.709` edge `-0.1152` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-7.4069` n `88` status `ready` deltaP `-2.5915` edge `-0.2188` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-9.1206` n `88` status `ready` deltaP `2.245` edge `-0.2632` maxDD `-34.2787`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
