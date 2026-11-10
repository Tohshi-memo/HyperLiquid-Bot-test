# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T21:07:27.967403+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11752`

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

- `market_context_high->unknown_4h` score `56.3135` n `88` status `ready` deltaP `7.525` edge `4.6874` maxDD `-0.9153`
- `market_context_high->equity_24h` score `35.252` n `88` status `ready` deltaP `33.6489` edge `2.9538` maxDD `-16.9034`
- `market_context_high->crypto_alt_24h` score `6.4839` n `88` status `ready` deltaP `28.4249` edge `1.1512` maxDD `-33.4213`
- `market_context_high->index_24h` score `5.8744` n `88` status `ready` deltaP `29.5928` edge `0.3385` maxDD `-2.3671`
- `market_context_high->metal_24h` score `1.8257` n `88` status `ready` deltaP `23.7374` edge `0.0492` maxDD `-1.4245`
- `market_context_high->commodity_1h` score `-0.3825` n `88` status `ready` deltaP `2.8375` edge `0.0003` maxDD `-1.7935`
- `market_context_high->metal_1h` score `-0.4192` n `88` status `ready` deltaP `3.0485` edge `0.0124` maxDD `-1.4122`
- `market_context_high->index_4h` score `-0.4947` n `88` status `ready` deltaP `5.2245` edge `-0.0005` maxDD `-2.4871`
- `market_context_high->commodity_4h` score `-0.5091` n `88` status `ready` deltaP `3.5615` edge `0.0216` maxDD `-4.182`
- `market_context_high->metal_4h` score `-1.0102` n `88` status `ready` deltaP `-0.4434` edge `0.0118` maxDD `-4.0688`
- `market_context_high->index_1h` score `-1.0104` n `88` status `ready` deltaP `-7.8048` edge `0.0056` maxDD `-0.9814`
- `market_context_high->fx_1h` score `-1.24` n `88` status `ready` deltaP `-12.8606` edge `-0.0048` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.5855` n `88` status `ready` deltaP `-7.5054` edge `0.0314` maxDD `-8.1039`
- `market_context_high->fx_24h` score `-1.7811` n `88` status `ready` deltaP `3.4722` edge `-0.0116` maxDD `-3.4642`
- `market_context_high->fx_4h` score `-1.8163` n `88` status `ready` deltaP `-1.5798` edge `-0.0042` maxDD `-2.4506`
- `market_context_high->crypto_alt_1h` score `-1.8259` n `88` status `ready` deltaP `1.0819` edge `-0.0434` maxDD `-10.8319`
- `market_context_high->crypto_major_1h` score `-2.953` n `88` status `ready` deltaP `-3.7629` edge `-0.0912` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-5.7837` n `88` status `ready` deltaP `2.7439` edge `-0.1191` maxDD `-25.16`
- `market_context_high->crypto_major_24h` score `-7.7338` n `88` status `ready` deltaP `5.2399` edge `0.4831` maxDD `-80.6681`
- `market_context_high->crypto_alt_4h` score `-8.0537` n `88` status `ready` deltaP `5.1414` edge `-0.1936` maxDD `-34.2787`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
