# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T04:07:23.880848+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8733`

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

- `market_context_high->equity_24h` score `3.4608` n `103` status `ready` deltaP `4.5729` edge `0.5639` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.6815` n `103` status `ready` deltaP `13.2535` edge `0.1927` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.4313` n `130` status `ready` deltaP `15.1008` edge `0.0859` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.9364` n `140` status `ready` deltaP `11.6595` edge `0.0346` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.8105` n `103` status `ready` deltaP `21.4013` edge `0.0479` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.5251` n `103` status `ready` deltaP `9.1002` edge `0.1598` maxDD `-5.9181`
- `market_context_high->fx_4h` score `-0.3068` n `130` status `ready` deltaP `7.8236` edge `-0.0024` maxDD `-1.6928`
- `market_context_high->fx_1h` score `-0.3069` n `140` status `ready` deltaP `4.136` edge `-0.0036` maxDD `-0.9639`
- `market_context_high->metal_1h` score `-0.6441` n `140` status `ready` deltaP `-3.9136` edge `-0.0069` maxDD `-0.9664`
- `market_context_high->index_4h` score `-0.6644` n `130` status `ready` deltaP `-1.7659` edge `-0.0129` maxDD `-1.1743`
- `market_context_high->index_1h` score `-0.8471` n `140` status `ready` deltaP `-3.7297` edge `-0.0068` maxDD `-0.7809`
- `market_context_high->equity_1h` score `-0.9525` n `140` status `ready` deltaP `-0.0172` edge `0.0036` maxDD `-4.6286`
- `market_context_high->metal_4h` score `-1.0268` n `130` status `ready` deltaP `-1.8832` edge `-0.0182` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-2.0539` n `140` status `ready` deltaP `-11.1719` edge `-0.0325` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.5767` n `130` status `ready` deltaP `-1.2594` edge `-0.0726` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.2743` n `140` status `ready` deltaP `-11.3815` edge `-0.0649` maxDD `-7.2335`
- `market_context_high->crypto_major_24h` score `-3.4123` n `103` status `ready` deltaP `6.2197` edge `-0.0764` maxDD `-14.2873`
- `market_context_high->crypto_alt_4h` score `-4.2913` n `130` status `ready` deltaP `-10.0891` edge `-0.1247` maxDD `-6.585`
- `market_context_high->crypto_alt_24h` score `-4.5046` n `103` status `ready` deltaP `-12.4461` edge `-0.1481` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-8.2993` n `140` status `ready` deltaP `-5.864` edge `-0.6078` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
