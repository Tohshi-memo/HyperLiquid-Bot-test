# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T19:52:26.916994+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10858`

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

- `market_context_high->equity_24h` score `1.7292` n `113` status `ready` deltaP `2.4736` edge `0.4336` maxDD `-21.1456`
- `market_context_high->metal_24h` score `1.6063` n `113` status `ready` deltaP `7.5083` edge `0.1414` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.2142` n `143` status `ready` deltaP `15.3569` edge `0.0661` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.8266` n `146` status `ready` deltaP `11.2173` edge `0.0284` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.5894` n `113` status `ready` deltaP `20.208` edge `0.0275` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.1299` n `113` status `ready` deltaP `5.4295` edge `0.1336` maxDD `-5.9181`
- `market_context_high->index_1h` score `-0.4627` n `146` status `ready` deltaP `-2.2639` edge `-0.0053` maxDD `-0.7809`
- `market_context_high->fx_1h` score `-0.5456` n `146` status `ready` deltaP `1.2427` edge `-0.0042` maxDD `-0.9639`
- `market_context_high->metal_1h` score `-0.6462` n `146` status `ready` deltaP `-4.0603` edge `-0.0062` maxDD `-0.9664`
- `market_context_high->fx_4h` score `-0.7416` n `143` status `ready` deltaP `2.7791` edge `-0.005` maxDD `-1.6928`
- `market_context_high->index_4h` score `-0.9598` n `143` status `ready` deltaP `-1.5254` edge `-0.0093` maxDD `-1.1743`
- `market_context_high->metal_4h` score `-1.024` n `143` status `ready` deltaP `-1.9657` edge `-0.0173` maxDD `-2.7373`
- `market_context_high->equity_1h` score `-1.0519` n `146` status `ready` deltaP `-1.5299` edge `0.0054` maxDD `-4.6286`
- `market_context_high->crypto_alt_1h` score `-1.9733` n `146` status `ready` deltaP `-10.3744` edge `-0.0311` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.6034` n `143` status `ready` deltaP `-2.0286` edge `-0.0697` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.2342` n `146` status `ready` deltaP `-11.3629` edge `-0.0613` maxDD `-7.2638`
- `market_context_high->crypto_alt_4h` score `-4.1208` n `143` status `ready` deltaP `-9.0387` edge `-0.1175` maxDD `-6.585`
- `market_context_high->crypto_major_24h` score `-4.3673` n `113` status `ready` deltaP `0.8819` edge `-0.1204` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-6.1282` n `113` status `ready` deltaP `-17.5163` edge `-0.2496` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-7.9185` n `146` status `ready` deltaP `-7.1487` edge `-0.5675` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
