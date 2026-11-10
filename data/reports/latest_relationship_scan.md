# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T04:07:28.376734+00:00`
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

- `market_context_high->unknown_4h` score `37.8511` n `88` status `ready` deltaP `7.2201` edge `3.1509` maxDD `-0.9153`
- `market_context_high->equity_24h` score `33.4639` n `76` status `ready` deltaP `31.563` edge `2.8187` maxDD `-16.9034`
- `market_context_high->index_24h` score `5.4344` n `76` status `ready` deltaP `25.4583` edge `0.3294` maxDD `-2.3671`
- `market_context_high->crypto_alt_24h` score `2.6967` n `76` status `ready` deltaP `18.4439` edge `0.7322` maxDD `-33.4213`
- `market_context_high->metal_24h` score `-0.0109` n `76` status `ready` deltaP `15.2399` edge `-0.0472` maxDD `-1.4245`
- `market_context_high->metal_1h` score `-0.3976` n `88` status `ready` deltaP `3.4976` edge `0.0112` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.4961` n `88` status `ready` deltaP `0.592` edge `0.0007` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.6984` n `88` status `ready` deltaP `0.0554` edge `0.0207` maxDD `-4.182`
- `market_context_high->index_4h` score `-0.8248` n `88` status `ready` deltaP `0.3464` edge `-0.0103` maxDD `-2.4871`
- `market_context_high->index_1h` score `-1.0563` n `88` status `ready` deltaP `-8.5533` edge `0.0047` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.2132` n `88` status `ready` deltaP `-2.5776` edge `0.0` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.3958` n `88` status `ready` deltaP `-15.5552` edge `-0.0068` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.7445` n `88` status `ready` deltaP `-8.5533` edge `0.018` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.967` n `88` status `ready` deltaP `0.4831` edge `-0.0575` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-2.2482` n `88` status `ready` deltaP `-8.7445` edge `-0.0118` maxDD `-2.4506`
- `market_context_high->fx_24h` score `-3.1788` n `76` status `ready` deltaP `-10.0999` edge `-0.0376` maxDD `-3.4642`
- `market_context_high->crypto_major_1h` score `-3.1924` n `88` status `ready` deltaP `-5.2599` edge `-0.1119` maxDD `-15.9848`
- `market_context_high->commodity_24h` score `-4.4846` n `76` status `ready` deltaP `-20.5806` edge `-0.0261` maxDD `-18.2654`
- `market_context_high->equity_4h` score `-7.4799` n `88` status `ready` deltaP `-2.439` edge `-0.2259` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-9.1158` n `88` status `ready` deltaP `2.245` edge `-0.2628` maxDD `-34.2787`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
