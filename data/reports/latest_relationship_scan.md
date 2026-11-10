# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T20:07:38.084776+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11742`

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

- `market_context_high->unknown_4h` score `56.2259` n `88` status `ready` deltaP `7.525` edge `4.6801` maxDD `-0.9153`
- `market_context_high->equity_24h` score `35.186` n `88` status `ready` deltaP `33.6489` edge `2.9483` maxDD `-16.9034`
- `market_context_high->crypto_alt_24h` score `6.2723` n `88` status `ready` deltaP `27.7304` edge `1.1287` maxDD `-33.4213`
- `market_context_high->index_24h` score `5.7888` n `88` status `ready` deltaP `28.8983` edge `0.336` maxDD `-2.3671`
- `market_context_high->metal_24h` score `1.6118` n `88` status `ready` deltaP `23.0429` edge `0.036` maxDD `-1.4245`
- `market_context_high->metal_1h` score `-0.3652` n `88` status `ready` deltaP `3.6473` edge `0.0129` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.3926` n `88` status `ready` deltaP `2.6878` edge `0.0` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.5075` n `88` status `ready` deltaP `3.5615` edge `0.0218` maxDD `-4.182`
- `market_context_high->index_4h` score `-0.5145` n `88` status `ready` deltaP `4.9196` edge `-0.001` maxDD `-2.4871`
- `market_context_high->index_1h` score `-0.9847` n `88` status `ready` deltaP `-7.3557` edge `0.0059` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.0063` n `88` status `ready` deltaP `-0.4434` edge `0.0123` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.2323` n `88` status `ready` deltaP `-12.7109` edge `-0.0048` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.5527` n `88` status `ready` deltaP `-7.3557` edge `0.0346` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.7931` n `88` status `ready` deltaP `1.3813` edge `-0.0412` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-1.7982` n `88` status `ready` deltaP `-1.275` edge `-0.0039` maxDD `-2.4506`
- `market_context_high->fx_24h` score `-1.845` n `88` status `ready` deltaP `2.7778` edge `-0.0123` maxDD `-3.4642`
- `market_context_high->crypto_major_1h` score `-2.9227` n `88` status `ready` deltaP `-3.4635` edge `-0.0893` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-5.8549` n `88` status `ready` deltaP `2.439` edge `-0.123` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-8.0659` n `88` status `ready` deltaP `4.9889` edge `-0.1936` maxDD `-34.2787`
- `market_context_high->crypto_major_24h` score `-8.1734` n `88` status `ready` deltaP `4.5455` edge `0.4511` maxDD `-80.6681`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
