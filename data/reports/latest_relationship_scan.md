# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T21:07:30.774687+00:00`
- Price records: `672`
- Market context records: `6854`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11809`

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

- `market_context_high->unknown_24h` score `1.1237` n `176` status `ready` deltaP `-1.5467` edge `0.5296` maxDD `-12.3511`
- `market_context_high->fx_1h` score `-0.2367` n `223` status `ready` deltaP `2.4684` edge `0.0017` maxDD `-0.5468`
- `market_context_high->commodity_24h` score `-0.5105` n `176` status `ready` deltaP `6.5815` edge `0.1004` maxDD `-5.2791`
- `market_context_high->crypto_alt_1h` score `-0.6192` n `223` status `ready` deltaP `1.5628` edge `0.0144` maxDD `-3.7803`
- `market_context_high->crypto_major_1h` score `-0.6262` n `223` status `ready` deltaP `3.6559` edge `0.0136` maxDD `-4.2122`
- `market_context_high->commodity_1h` score `-0.693` n `223` status `ready` deltaP `-2.171` edge `-0.0059` maxDD `-2.1443`
- `market_context_high->index_1h` score `-0.881` n `223` status `ready` deltaP `-2.7651` edge `-0.0034` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.9557` n `223` status `ready` deltaP `-5.602` edge `-0.0084` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-1.0086` n `217` status `ready` deltaP `10.6454` edge `0.0061` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.451` n `217` status `ready` deltaP `-3.7259` edge `-0.0122` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.6178` n `223` status `ready` deltaP `-2.6121` edge `-0.0273` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.9823` n `223` status `ready` deltaP `-0.3773` edge `-0.0336` maxDD `-13.1084`
- `market_context_high->index_4h` score `-2.0703` n `217` status `ready` deltaP `2.7222` edge `-0.0256` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-2.4693` n `217` status `ready` deltaP `-0.7439` edge `-0.0133` maxDD `-5.5324`
- `market_context_high->crypto_major_4h` score `-3.0658` n `217` status `ready` deltaP `-0.9505` edge `-0.054` maxDD `-16.9508`
- `market_context_high->unknown_4h` score `-3.1699` n `217` status `ready` deltaP `-9.1948` edge `0.0337` maxDD `-10.2579`
- `market_context_high->crypto_alt_4h` score `-3.181` n `217` status `ready` deltaP `-0.6561` edge `-0.0451` maxDD `-20.6678`
- `market_context_high->fx_24h` score `-4.5044` n `176` status `ready` deltaP `-9.7853` edge `-0.0065` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.6363` n `217` status `ready` deltaP `-0.2129` edge `-0.1831` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-9.0702` n `176` status `ready` deltaP `-18.8447` edge `-0.1887` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
