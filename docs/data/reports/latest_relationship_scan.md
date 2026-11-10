# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T17:52:28.607327+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11460`

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

- `market_context_high->unknown_4h` score `52.6337` n `88` status `ready` deltaP `7.0676` edge `4.3838` maxDD `-0.9153`
- `market_context_high->equity_24h` score `35.0056` n `88` status `ready` deltaP `33.7344` edge `2.9327` maxDD `-16.9034`
- `market_context_high->crypto_alt_24h` score `5.7408` n `88` status `ready` deltaP `26.2407` edge `1.0705` maxDD `-33.4213`
- `market_context_high->index_24h` score `5.612` n `88` status `ready` deltaP `27.4381` edge `0.331` maxDD `-2.3671`
- `market_context_high->metal_24h` score `1.189` n `88` status `ready` deltaP `21.583` edge `0.0105` maxDD `-1.4245`
- `market_context_high->metal_1h` score `-0.3185` n `88` status `ready` deltaP `4.0964` edge `0.0138` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.4089` n `88` status `ready` deltaP `2.3884` edge `-0.0001` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.4786` n `88` status `ready` deltaP `3.5615` edge `0.0255` maxDD `-4.182`
- `market_context_high->index_4h` score `-0.5871` n `88` status `ready` deltaP `3.8525` edge `-0.0032` maxDD `-2.4871`
- `market_context_high->index_1h` score `-0.9652` n `88` status `ready` deltaP `-7.0563` edge `0.0064` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.0244` n `88` status `ready` deltaP `-0.5959` edge `0.011` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.2471` n `88` status `ready` deltaP `-13.0103` edge `-0.0047` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.5013` n `88` status `ready` deltaP `-6.9066` edge `0.0382` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.7534` n `88` status `ready` deltaP `1.6807` edge `-0.0381` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-1.8258` n `88` status `ready` deltaP `-1.7323` edge `-0.0044` maxDD `-2.4506`
- `market_context_high->fx_24h` score `-1.9884` n `88` status `ready` deltaP `1.2998` edge `-0.0144` maxDD `-3.4642`
- `market_context_high->crypto_major_1h` score `-2.8432` n `88` status `ready` deltaP `-2.8647` edge `-0.0831` maxDD `-15.9848`
- `market_context_high->equity_4h` score `-6.243` n `88` status `ready` deltaP `1.0671` edge `-0.1462` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-8.3793` n `88` status `ready` deltaP `3.9219` edge `-0.2126` maxDD `-34.2787`
- `market_context_high->crypto_major_24h` score `-9.1983` n `88` status `ready` deltaP `3.029` edge `0.3758` maxDD `-80.6681`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
