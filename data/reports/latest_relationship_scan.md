# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-16T19:52:27.677328+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11830`

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

- `market_context_high->unknown_24h` score `212.3699` n `84` status `ready` deltaP `-24.3799` edge `27.6578` maxDD `-7.8016`
- `market_context_high->commodity_24h` score `7.7441` n `84` status `ready` deltaP `41.369` edge `0.3753` maxDD `-0.1266`
- `market_context_high->commodity_4h` score `1.3171` n `121` status `ready` deltaP `13.1954` edge `0.0689` maxDD `-0.7687`
- `market_context_high->commodity_1h` score `-0.0405` n `124` status `ready` deltaP `2.7091` edge `0.0197` maxDD `-0.624`
- `market_context_high->fx_1h` score `-0.2564` n `124` status `ready` deltaP `2.0282` edge `0.0016` maxDD `-0.2527`
- `market_context_high->fx_4h` score `-0.2956` n `121` status `ready` deltaP `4.3855` edge `0.0066` maxDD `-0.504`
- `market_context_high->metal_1h` score `-0.5245` n `124` status `ready` deltaP `1.5791` edge `-0.0062` maxDD `-1.7257`
- `market_context_high->metal_4h` score `-0.6906` n `121` status `ready` deltaP `9.3277` edge `-0.01` maxDD `-4.5909`
- `market_context_high->index_1h` score `-1.1935` n `124` status `ready` deltaP `-6.6448` edge `-0.003` maxDD `-0.5064`
- `market_context_high->fx_24h` score `-1.4198` n `84` status `ready` deltaP `-7.242` edge `0.027` maxDD `-1.8596`
- `market_context_high->equity_1h` score `-1.6803` n `124` status `ready` deltaP `-9.8464` edge `-0.0458` maxDD `-4.9849`
- `market_context_high->index_24h` score `-1.847` n `84` status `ready` deltaP `-5.754` edge `-0.0653` maxDD `-1.9845`
- `market_context_high->index_4h` score `-1.9069` n `121` status `ready` deltaP `-10.5624` edge `-0.0076` maxDD `-0.8045`
- `market_context_high->metal_24h` score `-1.9532` n `84` status `ready` deltaP `-10.2926` edge `0.0694` maxDD `-7.0954`
- `market_context_high->crypto_alt_1h` score `-2.1357` n `124` status `ready` deltaP `-3.1679` edge `-0.0229` maxDD `-7.0497`
- `market_context_high->crypto_major_1h` score `-2.1933` n `124` status `ready` deltaP `-6.244` edge `-0.0345` maxDD `-5.5318`
- `market_context_high->crypto_major_4h` score `-3.3493` n `121` status `ready` deltaP `-1.3921` edge `-0.0616` maxDD `-11.9917`
- `market_context_high->crypto_major_24h` score `-4.0573` n `84` status `ready` deltaP `-5.258` edge `0.0183` maxDD `-29.9394`
- `market_context_high->unknown_1h` score `-6.8113` n `124` status `ready` deltaP `2.2359` edge `-0.5428` maxDD `-0.8437`
- `market_context_high->crypto_alt_4h` score `-7.7918` n `121` status `ready` deltaP `-10.3948` edge `-0.0997` maxDD `-25.7586`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
