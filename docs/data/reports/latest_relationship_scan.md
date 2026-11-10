# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T04:22:42.220387+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11562`

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

- `market_context_high->unknown_4h` score `37.8475` n `88` status `ready` deltaP `7.2201` edge `3.1506` maxDD `-0.9153`
- `market_context_high->equity_24h` score `33.5594` n `77` status `ready` deltaP `31.646` edge `2.8261` maxDD `-16.9034`
- `market_context_high->index_24h` score `5.4309` n `77` status `ready` deltaP `25.4901` edge `0.3289` maxDD `-2.3671`
- `market_context_high->crypto_alt_24h` score `2.782` n `77` status `ready` deltaP `18.7491` edge `0.7411` maxDD `-33.4213`
- `market_context_high->metal_24h` score `-0.0423` n `77` status `ready` deltaP `15.3571` edge `-0.0506` maxDD `-1.4245`
- `market_context_high->metal_1h` score `-0.4` n `88` status `ready` deltaP `3.4976` edge `0.011` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.4953` n `88` status `ready` deltaP `0.592` edge `0.0008` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.6827` n `88` status `ready` deltaP `0.2079` edge `0.0217` maxDD `-4.182`
- `market_context_high->index_4h` score `-0.8248` n `88` status `ready` deltaP `0.3464` edge `-0.0103` maxDD `-2.4871`
- `market_context_high->index_1h` score `-1.0571` n `88` status `ready` deltaP `-8.5533` edge `0.0046` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.2171` n `88` status `ready` deltaP `-2.5776` edge `-0.0005` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.3872` n `88` status `ready` deltaP `-15.4055` edge `-0.0067` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.7468` n `88` status `ready` deltaP `-8.5533` edge `0.0177` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.9693` n `88` status `ready` deltaP `0.4831` edge `-0.0578` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-2.2395` n `88` status `ready` deltaP `-8.592` edge `-0.0117` maxDD `-2.4506`
- `market_context_high->fx_24h` score `-3.1108` n `77` status `ready` deltaP `-9.3993` edge `-0.0366` maxDD `-3.4642`
- `market_context_high->crypto_major_1h` score `-3.1947` n `88` status `ready` deltaP `-5.2599` edge `-0.1122` maxDD `-15.9848`
- `market_context_high->commodity_24h` score `-4.6631` n `77` status `ready` deltaP `-20.9053` edge `-0.0327` maxDD `-19.0615`
- `market_context_high->equity_4h` score `-7.4835` n `88` status `ready` deltaP `-2.439` edge `-0.2262` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-9.1364` n `88` status `ready` deltaP `2.0926` edge `-0.2635` maxDD `-34.2787`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
