# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-06T15:22:32.662869+00:00`
- Price records: `465`
- Market context records: `555`
- Flow alert records: `1568`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `807`

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

- `market_context_high->crypto_alt_24h` score `4.9973` n `140` status `ready` deltaP `7.6868` edge `0.37` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `3.0015` n `140` status `ready` deltaP `10.1278` edge `0.216` maxDD `-1.3382`
- `market_context_high->fx_4h` score `0.0217` n `146` status `ready` deltaP `10.354` edge `0.0209` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3042` n `146` status `ready` deltaP `2.1447` edge `0.0045` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5299` n `146` status `ready` deltaP `1.9933` edge `0.04` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.601` n `146` status `ready` deltaP `1.4403` edge `-0.0013` maxDD `-2.8282`
- `market_context_high->equity_1h` score `-1.1246` n `146` status `ready` deltaP `-0.7479` edge `-0.0077` maxDD `-4.4826`
- `market_context_high->unknown_1h` score `-1.1931` n `146` status `ready` deltaP `-3.6133` edge `-0.015` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.3209` n `146` status `ready` deltaP `4.5138` edge `-0.0087` maxDD `-8.1842`
- `market_context_high->index_24h` score `-1.7325` n `140` status `ready` deltaP `-5.7241` edge `0.0933` maxDD `-5.9609`
- `market_context_high->crypto_major_1h` score `-2.0135` n `146` status `ready` deltaP `3.4068` edge `-0.0182` maxDD `-11.4508`
- `market_context_high->index_4h` score `-2.1173` n `146` status `ready` deltaP `1.0236` edge `-0.031` maxDD `-6.5149`
- `market_context_high->crypto_alt_4h` score `-2.5262` n `146` status `ready` deltaP `1.5392` edge `0.0362` maxDD `-15.2248`
- `market_context_high->equity_4h` score `-3.1554` n `146` status `ready` deltaP `-3.0214` edge `-0.0276` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.3791` n `146` status `ready` deltaP `-5.3948` edge `-0.0497` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.4794` n `146` status `ready` deltaP `-5.7534` edge `0.0985` maxDD `-13.0076`
- `market_context_high->crypto_major_4h` score `-3.6449` n `146` status `ready` deltaP `8.8888` edge `0.0076` maxDD `-22.648`
- `market_context_high->equity_24h` score `-3.6479` n `140` status `ready` deltaP `-10.0979` edge `0.0238` maxDD `-10.5047`
- `market_context_high->unknown_4h` score `-4.0565` n `146` status `ready` deltaP `0.4469` edge `-0.1532` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-4.3922` n `140` status `ready` deltaP `-5.6164` edge `-0.0427` maxDD `-18.3035`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
