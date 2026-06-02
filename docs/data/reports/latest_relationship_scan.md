# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T08:37:25.119559+00:00`
- Price records: `672`
- Market context records: `2646`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9223`

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

- `market_context_high->unknown_24h` score `7.6546` n `131` status `ready` deltaP `17.7468` edge `0.5524` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `5.7232` n `131` status `ready` deltaP `26.4802` edge `0.5683` maxDD `-15.4319`
- `market_context_high->crypto_alt_24h` score `5.1903` n `131` status `ready` deltaP `7.9463` edge `0.7983` maxDD `-25.5001`
- `market_context_high->crypto_major_4h` score `4.2829` n `131` status `ready` deltaP `17.3268` edge `0.4224` maxDD `-10.1468`
- `market_context_high->unknown_4h` score `1.3459` n `131` status `ready` deltaP `7.8652` edge `0.1647` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `1.1334` n `133` status `ready` deltaP `10.3035` edge `0.1445` maxDD `-6.1656`
- `market_context_high->index_24h` score `1.0512` n `131` status `ready` deltaP `11.2317` edge `0.1108` maxDD `-2.5127`
- `market_context_high->crypto_major_1h` score `0.5068` n `133` status `ready` deltaP `6.8468` edge `0.116` maxDD `-4.2199`
- `market_context_high->index_4h` score `0.4213` n `131` status `ready` deltaP `10.4636` edge `0.0495` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `0.0322` n `133` status `ready` deltaP `2.9445` edge `0.0372` maxDD `-1.665`
- `market_context_high->index_1h` score `-0.1804` n `133` status `ready` deltaP `3.2507` edge `0.0127` maxDD `-1.2855`
- `market_context_high->metal_4h` score `-0.1985` n `131` status `ready` deltaP `5.2621` edge `0.03` maxDD `-2.5301`
- `market_context_high->commodity_1h` score `-0.3521` n `133` status `ready` deltaP `5.9385` edge `0.0189` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.4073` n `133` status `ready` deltaP `0.9883` edge `0.0041` maxDD `-0.2373`
- `market_context_high->metal_1h` score `-0.4949` n `133` status `ready` deltaP `-0.6787` edge `0.005` maxDD `-2.114`
- `market_context_high->fx_24h` score `-0.5937` n `131` status `ready` deltaP `5.7888` edge `-0.0002` maxDD `-0.6957`
- `market_context_high->equity_1h` score `-0.9608` n `133` status `ready` deltaP `-1.9821` edge `0.017` maxDD `-2.7085`
- `market_context_high->fx_4h` score `-1.0113` n `131` status `ready` deltaP `-1.7524` edge `0.0105` maxDD `-0.6474`
- `market_context_high->commodity_4h` score `-1.2312` n `131` status `ready` deltaP `3.4374` edge `0.0135` maxDD `-10.2078`
- `market_context_high->equity_24h` score `-1.3171` n `131` status `ready` deltaP `8.7296` edge `-0.0702` maxDD `-3.1535`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
