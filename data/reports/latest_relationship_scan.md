# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T22:07:28.394418+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11740`

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

- `market_context_high->unknown_4h` score `56.0039` n `88` status `ready` deltaP `7.525` edge `4.6616` maxDD `-0.9153`
- `market_context_high->equity_24h` score `35.2772` n `88` status `ready` deltaP `33.6489` edge `2.9559` maxDD `-16.9034`
- `market_context_high->crypto_alt_24h` score `6.6713` n `88` status `ready` deltaP `29.1193` edge `1.1706` maxDD `-33.4213`
- `market_context_high->index_24h` score `5.9551` n `88` status `ready` deltaP `30.2872` edge `0.3406` maxDD `-2.3671`
- `market_context_high->metal_24h` score `2.0481` n `88` status `ready` deltaP `24.4318` edge `0.0631` maxDD `-1.4245`
- `market_context_high->commodity_1h` score `-0.3568` n `88` status `ready` deltaP `3.2866` edge `0.0006` maxDD `-1.7935`
- `market_context_high->metal_1h` score `-0.3664` n `88` status `ready` deltaP `3.6473` edge `0.0128` maxDD `-1.4122`
- `market_context_high->index_4h` score `-0.5255` n `88` status `ready` deltaP `4.7672` edge `-0.0014` maxDD `-2.4871`
- `market_context_high->commodity_4h` score `-0.5406` n `88` status `ready` deltaP `3.1042` edge `0.0206` maxDD `-4.182`
- `market_context_high->index_1h` score `-0.9995` n `88` status `ready` deltaP `-7.6551` edge `0.006` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.0213` n `88` status `ready` deltaP `-0.5959` edge `0.0114` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.2089` n `88` status `ready` deltaP `-12.2618` edge `-0.0048` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.5582` n `88` status `ready` deltaP `-7.5054` edge `0.0349` maxDD `-8.1039`
- `market_context_high->fx_24h` score `-1.7123` n `88` status `ready` deltaP `4.1667` edge `-0.0105` maxDD `-3.4642`
- `market_context_high->crypto_alt_1h` score `-1.8056` n `88` status `ready` deltaP `1.2316` edge `-0.0418` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-1.8156` n `88` status `ready` deltaP `-1.5798` edge `-0.0041` maxDD `-2.4506`
- `market_context_high->crypto_major_1h` score `-2.946` n `88` status `ready` deltaP `-3.7629` edge `-0.0903` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-5.9029` n `88` status `ready` deltaP `2.439` edge `-0.127` maxDD `-25.16`
- `market_context_high->crypto_major_24h` score `-7.3303` n `88` status `ready` deltaP `5.9344` edge `0.5121` maxDD `-80.6681`
- `market_context_high->crypto_alt_4h` score `-8.1719` n `88` status `ready` deltaP `4.6841` edge `-0.2004` maxDD `-34.2787`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
