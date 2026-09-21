# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T20:22:26.143023+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9604`

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

- `market_context_high->unknown_4h` score `28.0027` n `58` status `ready` deltaP `1.6874` edge `2.3373` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `14.8385` n `101` status `ready` deltaP `2.9359` edge `1.9028` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `9.4385` n `101` status `ready` deltaP `3.3209` edge `1.2525` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `3.6579` n `101` status `ready` deltaP `17.3946` edge `0.3098` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `2.884` n `101` status `ready` deltaP `18.7666` edge `0.241` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.5927` n `101` status `ready` deltaP `15.7823` edge `0.1574` maxDD `-2.058`
- `news_risk_high->commodity_24h` score `2.0859` n `101` status `ready` deltaP `28.2315` edge `0.2098` maxDD `-3.4467`
- `news_risk_high->crypto_major_1h` score `1.8817` n `101` status `ready` deltaP `17.2793` edge `0.0939` maxDD `-2.8494`
- `market_context_high->index_24h` score `0.9032` n `42` status `ready` deltaP `-3.4722` edge `0.1773` maxDD `-1.644`
- `market_context_high->equity_1h` score `0.6485` n `58` status `ready` deltaP `4.6614` edge `0.0483` maxDD `-0.36`
- `news_risk_high->metal_1h` score `0.525` n `101` status `ready` deltaP `13.6998` edge `0.0126` maxDD `-0.8144`
- `market_context_high->index_1h` score `0.4932` n `58` status `ready` deltaP `8.1819` edge `0.0121` maxDD `-0.0435`
- `market_context_high->fx_1h` score `0.4217` n `58` status `ready` deltaP `9.6738` edge `0.0063` maxDD `-0.1854`
- `news_risk_high->fx_4h` score `0.3537` n `101` status `ready` deltaP `10.1651` edge `0.0253` maxDD `-0.421`
- `news_risk_high->metal_4h` score `0.2515` n `101` status `ready` deltaP `14.05` edge `0.0327` maxDD `-2.0994`
- `market_context_high->metal_1h` score `0.2471` n `58` status `ready` deltaP `5.2499` edge `0.0164` maxDD `-0.1314`
- `market_context_high->equity_24h` score `0.1568` n `42` status `ready` deltaP `-7.4652` edge `0.3496` maxDD `-17.7117`
- `market_context_high->index_4h` score `0.077` n `58` status `ready` deltaP `11.1228` edge `-0.0006` maxDD `-1.0949`
- `market_context_high->metal_24h` score `-0.0588` n `42` status `ready` deltaP `12.8224` edge `-0.067` maxDD `-0.2042`
- `news_risk_high->fx_1h` score `-0.1274` n `101` status `ready` deltaP `4.0404` edge `0.0068` maxDD `-0.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
