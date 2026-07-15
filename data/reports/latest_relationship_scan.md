# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T14:52:28.307271+00:00`
- Price records: `672`
- Market context records: `6827`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11748`

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

- `market_context_high->unknown_24h` score `0.9092` n `176` status `ready` deltaP `-1.5467` edge `0.5021` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `0.2395` n `176` status `ready` deltaP `10.2273` edge `0.1386` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.1458` n `205` status `ready` deltaP `6.3349` edge `0.0316` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.3017` n `205` status `ready` deltaP `3.7462` edge `0.0263` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.3482` n `205` status `ready` deltaP `0.5046` edge `0.0005` maxDD `-0.5468`
- `market_context_high->index_1h` score `-0.8343` n `205` status `ready` deltaP `-3.2817` edge `-0.0045` maxDD `-1.447`
- `market_context_high->metal_1h` score `-0.9298` n `205` status `ready` deltaP `-5.6149` edge `-0.0079` maxDD `-1.9098`
- `market_context_high->commodity_1h` score `-1.1186` n `205` status `ready` deltaP `-2.7165` edge `-0.0068` maxDD `-2.1314`
- `market_context_high->fx_4h` score `-1.231` n `195` status `ready` deltaP `7.2827` edge `0.0` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.4664` n `195` status `ready` deltaP `-3.707` edge `-0.0143` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.6792` n `205` status `ready` deltaP `-4.6393` edge `-0.0189` maxDD `-3.2083`
- `market_context_high->index_4h` score `-1.7946` n `195` status `ready` deltaP `1.5463` edge `-0.0284` maxDD `-7.6259`
- `market_context_high->equity_1h` score `-2.0924` n `205` status `ready` deltaP `0.3651` edge `-0.0331` maxDD `-7.163`
- `market_context_high->metal_4h` score `-2.6795` n `195` status `ready` deltaP `-3.1957` edge `-0.0239` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-2.9649` n `195` status `ready` deltaP `0.2713` edge `-0.0492` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-3.1248` n `195` status `ready` deltaP `0.4096` edge `-0.045` maxDD `-20.6678`
- `market_context_high->unknown_4h` score `-3.2992` n `195` status `ready` deltaP `-11.0959` edge `0.0356` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.454` n `176` status `ready` deltaP `-9.7853` edge `-0.0023` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-5.5229` n `195` status `ready` deltaP `-0.8794` edge `-0.1787` maxDD `-34.8801`
- `market_context_high->metal_24h` score `-9.5163` n `176` status `ready` deltaP `-20.9281` edge `-0.232` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
