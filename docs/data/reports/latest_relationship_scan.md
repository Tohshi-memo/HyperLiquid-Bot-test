# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T03:37:25.550478+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `104`

- Symbol pattern count: `9966`

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

- `market_context_high->unknown_4h` score `37.7899` n `88` status `ready` deltaP `7.2201` edge `3.1458` maxDD `-0.9153`
- `market_context_high->equity_24h` score `33.4058` n `74` status `ready` deltaP `31.3761` edge `2.8151` maxDD `-16.9034`
- `market_context_high->index_24h` score `5.4592` n `74` status `ready` deltaP `25.3783` edge `0.332` maxDD `-2.3671`
- `market_context_high->crypto_alt_24h` score `2.5782` n `74` status `ready` deltaP `17.6215` edge `0.7225` maxDD `-33.4213`
- `market_context_high->metal_24h` score `0.0633` n `74` status `ready` deltaP `14.9819` edge `-0.0393` maxDD `-1.4245`
- `market_context_high->metal_1h` score `-0.3928` n `88` status `ready` deltaP `3.4976` edge `0.0116` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.5047` n `88` status `ready` deltaP `0.4423` edge `0.0006` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.7244` n `88` status `ready` deltaP `-0.2494` edge `0.0194` maxDD `-4.182`
- `market_context_high->index_4h` score `-0.8256` n `88` status `ready` deltaP `0.3464` edge `-0.0104` maxDD `-2.4871`
- `market_context_high->index_1h` score `-1.0571` n `88` status `ready` deltaP `-8.5533` edge `0.0046` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.207` n `88` status `ready` deltaP `-2.5776` edge `0.0008` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.4113` n `88` status `ready` deltaP `-15.8546` edge `-0.0068` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.7492` n `88` status `ready` deltaP `-8.5533` edge `0.0174` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.9506` n `88` status `ready` deltaP `0.6328` edge `-0.0564` maxDD `-10.8319`
- `market_context_high->fx_24h` score `-2.1545` n `74` status `ready` deltaP `-11.5579` edge `-0.0392` maxDD `-3.4642`
- `market_context_high->fx_4h` score `-2.2569` n `88` status `ready` deltaP `-8.8969` edge `-0.0119` maxDD `-2.4506`
- `market_context_high->crypto_major_1h` score `-3.1924` n `88` status `ready` deltaP `-5.2599` edge `-0.1119` maxDD `-15.9848`
- `market_context_high->commodity_24h` score `-4.1231` n `74` status `ready` deltaP `-19.9049` edge `-0.0123` maxDD `-16.6878`
- `market_context_high->equity_4h` score `-7.4847` n `88` status `ready` deltaP `-2.439` edge `-0.2263` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-9.1074` n `88` status `ready` deltaP `2.245` edge `-0.2621` maxDD `-34.2787`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
