# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-07T02:22:24.630514+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10761`

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

- `risk_on_high->unknown_24h` score `456.1157` n `98` status `ready` deltaP `26.7361` edge `37.8314` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `456.1157` n `98` status `ready` deltaP `26.7361` edge `37.8314` maxDD `0.0`
- `market_context_high->unknown_1h` score `21.2112` n `246` status `ready` deltaP `-2.708` edge `1.8581` maxDD `-2.4626`
- `risk_on_high->crypto_major_24h` score `20.2616` n `98` status `ready` deltaP `33.6982` edge `1.5155` maxDD `-1.4687`
- `risk_on_and_context->crypto_major_24h` score `20.2616` n `98` status `ready` deltaP `33.6982` edge `1.5155` maxDD `-1.4687`
- `risk_on_high->crypto_alt_24h` score `13.9788` n `98` status `ready` deltaP `30.5556` edge `0.9612` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `13.9788` n `98` status `ready` deltaP `30.5556` edge `0.9612` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `8.8995` n `187` status `ready` deltaP `24.1385` edge `0.6382` maxDD `-2.5998`
- `market_context_high->equity_24h` score `6.6076` n `187` status `ready` deltaP `23.0903` edge `0.3967` maxDD `0.0`
- `risk_on_high->equity_24h` score `5.5` n `98` status `ready` deltaP `23.0903` edge `0.3044` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `5.5` n `98` status `ready` deltaP `23.0903` edge `0.3044` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `5.4816` n `121` status `ready` deltaP `28.7946` edge `0.302` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.4816` n `121` status `ready` deltaP `28.7946` edge `0.302` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `3.9515` n `121` status `ready` deltaP `22.2385` edge `0.2669` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `3.9515` n `121` status `ready` deltaP `22.2385` edge `0.2669` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.7275` n `98` status `ready` deltaP `23.3277` edge `0.076` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.7275` n `98` status `ready` deltaP `23.3277` edge `0.076` maxDD `-0.0051`
- `market_context_high->index_24h` score `2.6049` n `187` status `ready` deltaP `21.5761` edge `0.0947` maxDD `-0.0505`
- `risk_on_high->crypto_alt_1h` score `0.9239` n `122` status `ready` deltaP `4.0689` edge `0.0851` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.9239` n `122` status `ready` deltaP `4.0689` edge `0.0851` maxDD `-1.1521`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
