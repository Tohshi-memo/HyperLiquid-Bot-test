# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T02:07:15.680948+00:00`
- Price records: `672`
- Market context records: `1073`
- Flow alert records: `4994`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8728`

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

- `market_context_high->crypto_major_24h` score `16.0213` n `164` status `ready` deltaP `34.8543` edge `1.1491` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `5.5443` n `164` status `ready` deltaP `11.9741` edge `0.5056` maxDD `-9.5387`
- `market_context_high->equity_24h` score `5.0317` n `164` status `ready` deltaP `14.1103` edge `0.3749` maxDD `-3.6396`
- `market_context_high->index_24h` score `4.2543` n `164` status `ready` deltaP `14.6587` edge `0.2876` maxDD `-2.1308`
- `market_context_high->metal_24h` score `4.1422` n `164` status `ready` deltaP `-2.5046` edge `0.5286` maxDD `-6.3373`
- `market_context_high->equity_4h` score `1.3691` n `166` status `ready` deltaP `7.6678` edge `0.1418` maxDD `-3.6396`
- `market_context_high->crypto_major_4h` score `0.9803` n `166` status `ready` deltaP `12.1492` edge `0.1693` maxDD `-6.4882`
- `market_context_high->index_4h` score `0.6978` n `166` status `ready` deltaP `6.1729` edge `0.0853` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.4786` n `170` status `ready` deltaP `7.3828` edge `0.0242` maxDD `-0.683`
- `market_context_high->equity_1h` score `0.1281` n `170` status `ready` deltaP `2.0676` edge `0.0474` maxDD `-2.3739`
- `market_context_high->crypto_major_1h` score `0.035` n `170` status `ready` deltaP `7.316` edge `0.0279` maxDD `-3.9003`
- `market_context_high->fx_1h` score `-0.061` n `170` status `ready` deltaP `5.9687` edge `0.0007` maxDD `-0.3124`
- `market_context_high->metal_1h` score `-0.1948` n `170` status `ready` deltaP `6.5041` edge `-0.0073` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.6803` n `170` status `ready` deltaP `1.9479` edge `0.0226` maxDD `-4.0492`
- `market_context_high->fx_4h` score `-0.6929` n `166` status `ready` deltaP `1.3206` edge `0.002` maxDD `-1.6381`
- `market_context_high->crypto_alt_4h` score `-0.7798` n `166` status `ready` deltaP `6.0075` edge `0.1454` maxDD `-13.0347`
- `market_context_high->commodity_1h` score `-0.8792` n `170` status `ready` deltaP `-0.118` edge `0.0083` maxDD `-3.7959`
- `market_context_high->metal_4h` score `-2.0359` n `166` status `ready` deltaP `3.7944` edge `-0.0909` maxDD `-9.2991`
- `market_context_high->fx_24h` score `-3.0519` n `164` status `ready` deltaP `5.5901` edge `-0.0209` maxDD `-19.2774`
- `market_context_high->unknown_4h` score `-3.4163` n `166` status `ready` deltaP `7.6641` edge `-0.1933` maxDD `-6.7322`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
