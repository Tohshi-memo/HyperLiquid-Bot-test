# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T00:22:23.178456+00:00`
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

- `market_context_high->equity_24h` score `3.1176` n `103` status `ready` deltaP `4.5729` edge `0.5353` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.5077` n `103` status `ready` deltaP `12.3854` edge `0.184` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.5704` n `115` status `ready` deltaP `15.3248` edge `0.096` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.8612` n `127` status `ready` deltaP `10.4802` edge `0.0362` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.856` n `103` status `ready` deltaP `22.0958` edge `0.0491` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.4651` n `103` status `ready` deltaP `9.1002` edge `0.1521` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.403` n `127` status `ready` deltaP `3.0553` edge `-0.0044` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.5056` n `127` status `ready` deltaP `-2.8938` edge `-0.0066` maxDD `-0.7809`
- `market_context_high->metal_1h` score `-0.5667` n `127` status `ready` deltaP `-2.5166` edge `-0.0063` maxDD `-0.9664`
- `market_context_high->fx_4h` score `-0.6001` n `115` status `ready` deltaP `4.3982` edge `-0.004` maxDD `-1.6928`
- `market_context_high->index_4h` score `-0.6187` n `115` status `ready` deltaP `-0.9306` edge `-0.0126` maxDD `-1.1743`
- `market_context_high->equity_1h` score `-0.8403` n `127` status `ready` deltaP `0.7555` edge `0.0078` maxDD `-4.6286`
- `market_context_high->metal_4h` score `-1.1265` n `115` status `ready` deltaP `-4.1318` edge `-0.016` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-2.2291` n `127` status `ready` deltaP `-12.9414` edge `-0.0353` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.2883` n `115` status `ready` deltaP `0.9955` edge `-0.0636` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.118` n `127` status `ready` deltaP `-10.7737` edge `-0.0668` maxDD `-6.3636`
- `market_context_high->crypto_major_24h` score `-3.7795` n `103` status `ready` deltaP `6.2197` edge `-0.107` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-4.453` n `103` status `ready` deltaP `-12.4461` edge `-0.1438` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-4.7127` n `115` status `ready` deltaP `-12.7094` edge `-0.1428` maxDD `-6.5487`
- `market_context_high->unknown_1h` score `-8.3264` n `127` status `ready` deltaP `-5.3786` edge `-0.6133` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
