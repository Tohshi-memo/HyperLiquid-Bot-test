# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T22:51:33.465088+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9868`

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

- `market_context_high->unknown_4h` score `25.2985` n `58` status `ready` deltaP `2.1447` edge `2.1089` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `12.344` n `101` status `ready` deltaP `1.1998` edge `1.7065` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `7.5632` n `101` status `ready` deltaP `1.5848` edge `1.1078` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `3.3262` n `101` status `ready` deltaP `16.0227` edge `0.2913` maxDD `-7.675`
- `news_risk_high->crypto_alt_1h` score `2.4284` n `101` status `ready` deltaP `14.8841` edge `0.1497` maxDD `-2.058`
- `news_risk_high->commodity_24h` score `2.3681` n `101` status `ready` deltaP `29.9677` edge `0.2344` maxDD `-3.4467`
- `news_risk_high->crypto_major_4h` score `2.3516` n `101` status `ready` deltaP `17.2422` edge `0.2068` maxDD `-8.0625`
- `market_context_high->crypto_major_24h` score `2.3137` n `49` status `ready` deltaP `2.3314` edge `0.9469` maxDD `-48.5989`
- `news_risk_high->crypto_major_1h` score `1.6323` n `101` status `ready` deltaP `16.0817` edge `0.0811` maxDD `-2.8494`
- `market_context_high->equity_24h` score `1.5692` n `49` status `ready` deltaP `-4.4395` edge `0.5105` maxDD `-17.7117`
- `market_context_high->index_24h` score `1.5005` n `49` status `ready` deltaP `-0.4464` edge `0.2069` maxDD `-1.644`
- `market_context_high->equity_1h` score `0.6162` n `58` status `ready` deltaP `4.362` edge `0.0476` maxDD `-0.36`
- `market_context_high->index_1h` score `0.4932` n `58` status `ready` deltaP `8.1819` edge `0.0121` maxDD `-0.0435`
- `news_risk_high->metal_1h` score `0.4831` n `101` status `ready` deltaP `13.2507` edge `0.0121` maxDD `-0.8144`
- `market_context_high->fx_1h` score `0.4576` n `58` status `ready` deltaP `10.1229` edge `0.0063` maxDD `-0.1854`
- `news_risk_high->fx_4h` score `0.4254` n `101` status `ready` deltaP `10.9273` edge `0.0262` maxDD `-0.421`
- `market_context_high->metal_1h` score `0.2052` n `58` status `ready` deltaP `4.8008` edge `0.0159` maxDD `-0.1314`
- `news_risk_high->metal_4h` score `0.1931` n `101` status `ready` deltaP `13.4403` edge `0.0319` maxDD `-2.0994`
- `market_context_high->metal_24h` score `0.1905` n `49` status `ready` deltaP `16.2237` edge `-0.0689` maxDD `-0.2042`
- `market_context_high->index_4h` score `0.0855` n `58` status `ready` deltaP `11.1228` edge `0.0005` maxDD `-1.0949`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
