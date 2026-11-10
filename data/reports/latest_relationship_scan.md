# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-10T02:52:30.357528+00:00`
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

- `market_context_high->unknown_4h` score `37.8093` n `88` status `ready` deltaP `7.3725` edge `3.1464` maxDD `-0.9153`
- `market_context_high->equity_24h` score `21.5215` n `71` status `ready` deltaP `31.0396` edge `2.7927` maxDD `-16.9034`
- `market_context_high->index_24h` score `5.4592` n `71` status `ready` deltaP `25.213` edge `0.3331` maxDD `-2.3671`
- `market_context_high->crypto_alt_24h` score `2.3832` n `71` status `ready` deltaP `16.196` edge `0.707` maxDD `-33.4213`
- `market_context_high->metal_24h` score `0.1424` n `71` status `ready` deltaP `14.5312` edge `-0.0297` maxDD `-1.4245`
- `market_context_high->metal_1h` score `-0.3892` n `88` status `ready` deltaP `3.4976` edge `0.0119` maxDD `-1.4122`
- `market_context_high->commodity_1h` score `-0.5335` n `88` status `ready` deltaP `-0.0068` edge `-0.0001` maxDD `-1.7935`
- `market_context_high->commodity_4h` score `-0.7607` n `88` status `ready` deltaP `-0.7068` edge `0.0178` maxDD `-4.182`
- `market_context_high->index_4h` score `-0.8264` n `88` status `ready` deltaP `0.3464` edge `-0.0105` maxDD `-2.4871`
- `market_context_high->index_1h` score `-1.0664` n `88` status `ready` deltaP `-8.703` edge `0.0044` maxDD `-0.9814`
- `market_context_high->metal_4h` score `-1.1961` n `88` status `ready` deltaP `-2.5776` edge `0.0022` maxDD `-4.0688`
- `market_context_high->fx_1h` score `-1.4113` n `88` status `ready` deltaP `-15.8546` edge `-0.0068` maxDD `-0.8088`
- `market_context_high->equity_1h` score `-1.7414` n `88` status `ready` deltaP `-8.4036` edge `0.0174` maxDD `-8.1039`
- `market_context_high->crypto_alt_1h` score `-1.9304` n `88` status `ready` deltaP `0.7825` edge `-0.0548` maxDD `-10.8319`
- `market_context_high->fx_4h` score `-2.2474` n `88` status `ready` deltaP `-8.7445` edge `-0.0117` maxDD `-2.4506`
- `market_context_high->fx_24h` score `-2.2997` n `71` status `ready` deltaP `-13.899` edge `-0.0422` maxDD `-3.4642`
- `market_context_high->crypto_major_1h` score `-3.1885` n `88` status `ready` deltaP `-5.2599` edge `-0.1114` maxDD `-15.9848`
- `market_context_high->commodity_24h` score `-3.6017` n `71` status `ready` deltaP `-18.9933` edge `0.0078` maxDD `-14.4347`
- `market_context_high->equity_4h` score `-7.4451` n `88` status `ready` deltaP `-2.439` edge `-0.223` maxDD `-25.16`
- `market_context_high->crypto_alt_4h` score `-9.1026` n `88` status `ready` deltaP `2.245` edge `-0.2617` maxDD `-34.2787`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
