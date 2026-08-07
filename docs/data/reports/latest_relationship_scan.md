# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T14:22:28.638668+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11756`

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

- `market_context_high->metal_24h` score `1.1989` n `110` status `ready` deltaP `4.0204` edge `0.1557` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `0.8038` n `113` status `ready` deltaP `11.6717` edge `0.0738` maxDD `-2.7703`
- `market_context_high->commodity_1h` score `0.7855` n `121` status `ready` deltaP `10.9294` edge `0.0342` maxDD `-1.3282`
- `market_context_high->fx_24h` score `0.4918` n `110` status `ready` deltaP `20.3597` edge `0.0464` maxDD `-4.1933`
- `market_context_high->fx_1h` score `0.1531` n `121` status `ready` deltaP `9.2047` edge `-0.002` maxDD `-1.0616`
- `market_context_high->fx_4h` score `-0.2271` n `113` status `ready` deltaP `8.1278` edge `0.0027` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.446` n `121` status `ready` deltaP `-1.5205` edge `-0.0066` maxDD `-1.2359`
- `market_context_high->crypto_alt_1h` score `-0.8279` n `121` status `ready` deltaP `-4.5331` edge `-0.013` maxDD `-2.3669`
- `market_context_high->index_24h` score `-0.9051` n `110` status `ready` deltaP `0.4189` edge `0.0862` maxDD `-5.8201`
- `market_context_high->metal_4h` score `-1.0357` n `113` status `ready` deltaP `-0.0661` edge `-0.0043` maxDD `-2.1924`
- `market_context_high->index_1h` score `-1.0449` n `121` status `ready` deltaP `-3.2513` edge `-0.012` maxDD `-1.6054`
- `market_context_high->equity_1h` score `-1.476` n `121` status `ready` deltaP `2.2406` edge `-0.0477` maxDD `-10.5179`
- `market_context_high->crypto_alt_4h` score `-1.8502` n `113` status `ready` deltaP `1.6363` edge `-0.0261` maxDD `-5.7857`
- `market_context_high->index_4h` score `-2.3405` n `113` status `ready` deltaP `-6.1461` edge `-0.0307` maxDD `-4.5362`
- `market_context_high->crypto_major_1h` score `-2.4722` n `121` status `ready` deltaP `-5.3719` edge `-0.0405` maxDD `-7.0428`
- `market_context_high->crypto_alt_24h` score `-3.651` n `110` status `ready` deltaP `-9.3368` edge `-0.0977` maxDD `-4.5445`
- `market_context_high->crypto_major_4h` score `-4.8028` n `113` status `ready` deltaP `-6.7599` edge `-0.1771` maxDD `-25.1525`
- `market_context_high->equity_4h` score `-6.171` n `113` status `ready` deltaP `-0.9254` edge `-0.2643` maxDD `-34.6544`
- `market_context_high->crypto_major_24h` score `-6.8437` n `110` status `ready` deltaP `-6.6125` edge `-0.3114` maxDD `-31.0866`
- `market_context_high->unknown_1h` score `-8.2357` n `121` status `ready` deltaP `-0.1794` edge `-0.6404` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
