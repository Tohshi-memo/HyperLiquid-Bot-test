# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T16:22:29.791056+00:00`
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

- `market_context_high->equity_24h` score `6.1919` n `34` status `ready` deltaP `10.2227` edge `0.6883` maxDD `-16.9034`
- `market_context_high->commodity_24h` score `1.9392` n `34` status `ready` deltaP `4.1463` edge `0.1927` maxDD `-1.6995`
- `market_context_high->index_24h` score `0.8483` n `34` status `ready` deltaP `9.4976` edge `0.0917` maxDD `-2.3671`
- `market_context_high->fx_24h` score `0.7271` n `34` status `ready` deltaP `11.0294` edge `-0.0023` maxDD `-0.1843`
- `market_context_high->metal_1h` score `-0.3041` n `88` status `ready` deltaP `4.2461` edge `0.014` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.5506` n `88` status `ready` deltaP `-0.3062` edge `-0.0003` maxDD `-1.7935`
- `market_context_high->index_4h` score `-0.6106` n `88` status `ready` deltaP `2.7855` edge `0.0009` maxDD `-2.4871`
- `market_context_high->commodity_4h` score `-0.8703` n `88` status `ready` deltaP `-2.2311` edge `0.0139` maxDD `-4.182`
- `market_context_high->metal_4h` score `-0.964` n `88` status `ready` deltaP `-0.1386` edge `0.0157` maxDD `-4.0688`
- `market_context_high->index_1h` score `-0.9675` n `88` status `ready` deltaP `-7.0563` edge `0.0061` maxDD `-0.9814`
- `market_context_high->fx_1h` score `-1.2868` n `88` status `ready` deltaP `-13.6091` edge `-0.0058` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.5629` n `88` status `ready` deltaP `-7.206` edge `0.0323` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.9467` n `88` status `ready` deltaP `0.4831` edge `-0.0549` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-2.1178` n `88` status `ready` deltaP `-6.7628` edge `-0.0083` maxDD `-2.4506`
- `market_context_high->metal_24h` score `-2.1523` n `34` status `ready` deltaP `-4.3403` edge `-0.1917` maxDD `-1.4245`
- `market_context_high->crypto_major_1h` score `-3.1908` n `88` status `ready` deltaP `-5.2599` edge `-0.1117` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-6.0976` n `88` status `ready` deltaP `-0.6098` edge `-0.1229` maxDD `-25.16`
- `market_context_high->crypto_major_24h` score `-6.1286` n `34` status `ready` deltaP `-6.3521` edge `-0.0053` maxDD `-30.3789`
- `market_context_high->crypto_alt_4h` score `-9.083` n `88` status `ready` deltaP `1.6353` edge `-0.256` maxDD `-34.2787`
- `market_context_high->crypto_alt_24h` score `-11.0381` n `34` status `ready` deltaP `-21.9465` edge `-0.2641` maxDD `-33.4213`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
