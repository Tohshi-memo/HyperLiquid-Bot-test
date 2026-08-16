# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-16T21:22:33.092141+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11831`

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

- `market_context_high->unknown_24h` score `165.7394` n `83` status `ready` deltaP `-25.1401` edge `21.6846` maxDD `-7.8016`
- `market_context_high->commodity_24h` score `6.9654` n `83` status `ready` deltaP `41.3404` edge `0.3106` maxDD `-0.1266`
- `market_context_high->commodity_4h` score `1.1256` n `118` status `ready` deltaP `12.376` edge `0.0584` maxDD `-0.7687`
- `market_context_high->commodity_1h` score `-0.0221` n `120` status `ready` deltaP `3.0739` edge `0.0188` maxDD `-0.624`
- `market_context_high->fx_4h` score `-0.271` n `118` status `ready` deltaP `4.7669` edge `0.0061` maxDD `-0.504`
- `market_context_high->fx_1h` score `-0.3253` n `120` status `ready` deltaP `1.1527` edge `0.0017` maxDD `-0.2527`
- `market_context_high->metal_1h` score `-0.5459` n `120` status `ready` deltaP `1.1527` edge `-0.0061` maxDD `-1.7257`
- `market_context_high->metal_4h` score `-0.5669` n `118` status `ready` deltaP `10.7302` edge `-0.0035` maxDD `-4.5909`
- `market_context_high->index_1h` score `-0.7045` n `120` status `ready` deltaP `-5.3044` edge `-0.0028` maxDD `-0.5064`
- `market_context_high->index_4h` score `-1.1472` n `118` status `ready` deltaP `-9.043` edge `-0.0059` maxDD `-0.8045`
- `market_context_high->index_24h` score `-1.2323` n `83` status `ready` deltaP `0.046` edge `-0.0569` maxDD `-1.4451`
- `market_context_high->fx_24h` score `-1.7769` n `83` status `ready` deltaP `-11.724` edge `0.0111` maxDD `-1.8596`
- `market_context_high->metal_24h` score `-2.0509` n `83` status `ready` deltaP `-10.8664` edge `0.0607` maxDD `-7.0954`
- `market_context_high->crypto_major_4h` score `-2.2033` n `118` status `ready` deltaP `-0.1524` edge `-0.0371` maxDD `-7.3063`
- `market_context_high->crypto_major_1h` score `-2.2585` n `120` status `ready` deltaP `-5.4491` edge `-0.037` maxDD `-5.8571`
- `market_context_high->crypto_alt_1h` score `-2.3319` n `120` status `ready` deltaP `-4.6158` edge `-0.0296` maxDD `-7.0497`
- `market_context_high->equity_1h` score `-2.7311` n `120` status `ready` deltaP `-11.4171` edge `-0.0475` maxDD `-4.9849`
- `market_context_high->crypto_major_24h` score `-2.8754` n `83` status `ready` deltaP `-4.7273` edge `0.07` maxDD `-24.237`
- `market_context_high->unknown_1h` score `-6.4804` n `120` status `ready` deltaP `4.1218` edge `-0.5278` maxDD `-0.8437`
- `market_context_high->crypto_alt_4h` score `-6.6157` n `118` status `ready` deltaP `-9.4073` edge `-0.0739` maxDD `-20.5088`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
