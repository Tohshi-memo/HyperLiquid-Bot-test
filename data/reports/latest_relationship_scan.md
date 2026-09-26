# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-26T08:22:32.887133+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11858`

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

- `news_risk_high->unknown_24h` score `3347.3744` n `101` status `ready` deltaP `-0.6429` edge `278.9566` maxDD `-0.0226`
- `market_context_high->unknown_1h` score `69.9105` n `47` status `ready` deltaP `8.7687` edge `5.7745` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `47.8815` n `47` status `ready` deltaP `23.1309` edge `3.8752` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `29.119` n `47` status `ready` deltaP `21.3098` edge `2.3225` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.4055` n `47` status `ready` deltaP `33.3739` edge `1.9302` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.1524` n `47` status `ready` deltaP `30.0753` edge `0.4085` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.3951` n `47` status `ready` deltaP `28.8084` edge `0.1147` maxDD `-0.2401`
- `market_context_high->equity_4h` score `2.7143` n `47` status `ready` deltaP `17.1445` edge `0.1537` maxDD `-1.3444`
- `market_context_high->index_4h` score `2.5554` n `47` status `ready` deltaP `29.4532` edge `0.032` maxDD `-0.2323`
- `market_context_high->crypto_alt_4h` score `1.4197` n `47` status `ready` deltaP `11.5172` edge `0.1083` maxDD `-3.3417`
- `news_risk_high->metal_24h` score `1.1938` n `101` status `ready` deltaP `27.6076` edge `0.1351` maxDD `-6.9545`
- `market_context_high->equity_1h` score `1.0506` n `47` status `ready` deltaP `12.0652` edge `0.0474` maxDD `-1.5564`
- `market_context_high->index_1h` score `0.8074` n `47` status `ready` deltaP `12.8137` edge `0.0097` maxDD `-0.2275`
- `market_context_high->crypto_major_4h` score `0.6138` n `47` status `ready` deltaP `5.9094` edge `0.1022` maxDD `-5.2359`
- `market_context_high->fx_1h` score `0.5081` n `47` status `ready` deltaP `10.5586` edge `0.0076` maxDD `-0.1854`
- `news_risk_high->index_24h` score `0.4302` n `101` status `ready` deltaP `13.686` edge `0.04` maxDD `-2.2981`
- `market_context_high->crypto_major_1h` score `0.3734` n `47` status `ready` deltaP `5.5007` edge `0.0762` maxDD `-4.5405`
- `news_risk_high->crypto_alt_1h` score `0.0422` n `137` status `ready` deltaP `5.6067` edge `0.0572` maxDD `-4.2849`
- `market_context_high->fx_4h` score `0.0359` n `47` status `ready` deltaP `9.3215` edge `0.0076` maxDD `-0.6736`
- `market_context_high->metal_1h` score `0.004` n `47` status `ready` deltaP `3.2775` edge `0.0103` maxDD `-0.1976`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
