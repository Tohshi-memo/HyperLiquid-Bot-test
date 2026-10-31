# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T23:37:30.574502+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6775`

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

- `market_context_high->unknown_24h` score `3833.2892` n `84` status `ready` deltaP `-11.4087` edge `319.5598` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `129.5764` n `84` status `ready` deltaP `0.7839` edge `10.8061` maxDD `-0.3966`
- `news_risk_high->unknown_1h` score `80.0584` n `108` status `ready` deltaP `-5.1951` edge `6.7348` maxDD `-0.9571`
- `news_risk_high->crypto_alt_24h` score `16.7541` n `88` status `ready` deltaP `39.0941` edge `1.1901` maxDD `-2.6976`
- `market_context_high->equity_24h` score `10.6256` n `84` status `ready` deltaP `21.627` edge `1.017` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `5.6104` n `108` status `ready` deltaP `21.3415` edge `0.4639` maxDD `-7.4246`
- `market_context_high->index_24h` score `4.9961` n `84` status `ready` deltaP `44.0476` edge `0.141` maxDD `-0.1315`
- `market_context_high->commodity_4h` score `1.8621` n `84` status `ready` deltaP `20.3252` edge `0.0698` maxDD `-0.3436`
- `market_context_high->metal_4h` score `1.3098` n `84` status `ready` deltaP `16.3255` edge `0.0428` maxDD `-0.7323`
- `news_risk_high->crypto_alt_1h` score `0.9344` n `108` status `ready` deltaP `9.4755` edge `0.1101` maxDD `-3.9659`
- `market_context_high->metal_1h` score `0.6441` n `84` status `ready` deltaP `9.5381` edge `0.0191` maxDD `-0.3209`
- `market_context_high->fx_4h` score `0.6332` n `84` status `ready` deltaP `13.4655` edge `0.0021` maxDD `-0.1285`
- `market_context_high->fx_1h` score `0.4816` n `84` status `ready` deltaP `12.0402` edge `-0.0001` maxDD `-0.1407`
- `market_context_high->equity_1h` score `0.4572` n `84` status `ready` deltaP `2.9798` edge `0.1058` maxDD `-2.3383`
- `market_context_high->equity_4h` score `0.342` n `84` status `ready` deltaP `-1.0381` edge `0.1901` maxDD `-4.48`
- `market_context_high->crypto_major_1h` score `0.0271` n `84` status `ready` deltaP `5.5104` edge `0.0695` maxDD `-5.2213`
- `market_context_high->commodity_1h` score `-0.3032` n `84` status `ready` deltaP `-0.5774` edge `0.0164` maxDD `-0.4475`
- `market_context_high->index_1h` score `-0.4301` n `84` status `ready` deltaP `-0.1497` edge `0.0017` maxDD `-1.1344`
- `news_risk_high->index_1h` score `-0.7162` n `108` status `ready` deltaP `3.554` edge `-0.0034` maxDD `-1.3981`
- `market_context_high->metal_24h` score `-0.7225` n `84` status `ready` deltaP `4.3154` edge `0.1433` maxDD `-10.5088`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
