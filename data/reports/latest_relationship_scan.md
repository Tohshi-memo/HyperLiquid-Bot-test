# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T15:57:19.148696+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9991`

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

- `risk_on_high->unknown_24h` score `130.8043` n `108` status `ready` deltaP `23.8426` edge `10.7524` maxDD `-0.2126`
- `risk_on_and_context->unknown_24h` score `130.8043` n `108` status `ready` deltaP `23.8426` edge `10.7524` maxDD `-0.2126`
- `risk_on_high->crypto_major_24h` score `12.442` n `108` status `ready` deltaP `25.7523` edge `1.23` maxDD `-23.1878`
- `risk_on_and_context->crypto_major_24h` score `12.442` n `108` status `ready` deltaP `25.7523` edge `1.23` maxDD `-23.1878`
- `risk_on_high->crypto_alt_24h` score `3.7868` n `108` status `ready` deltaP `14.0046` edge `0.5751` maxDD `-21.232`
- `risk_on_and_context->crypto_alt_24h` score `3.7868` n `108` status `ready` deltaP `14.0046` edge `0.5751` maxDD `-21.232`
- `market_context_high->equity_24h` score `3.6283` n `196` status `ready` deltaP `17.0316` edge `0.3642` maxDD `-8.0307`
- `market_context_high->crypto_alt_24h` score `1.9271` n `196` status `ready` deltaP `15.4974` edge `0.4355` maxDD `-22.5915`
- `risk_on_high->equity_24h` score `1.3569` n `108` status `ready` deltaP `9.5486` edge `0.2248` maxDD `-8.0307`
- `risk_on_and_context->equity_24h` score `1.3569` n `108` status `ready` deltaP `9.5486` edge `0.2248` maxDD `-8.0307`
- `risk_on_high->index_1h` score `-0.0985` n `131` status `ready` deltaP `5.3058` edge `-0.0033` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `-0.0985` n `131` status `ready` deltaP `5.3058` edge `-0.0033` maxDD `-0.5764`
- `market_context_high->index_24h` score `-0.1057` n `196` status `ready` deltaP `14.555` edge `0.0778` maxDD `-5.0249`
- `risk_on_high->metal_1h` score `-0.2735` n `131` status `ready` deltaP `5.8155` edge `-0.0026` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `-0.2735` n `131` status `ready` deltaP `5.8155` edge `-0.0026` maxDD `-1.699`
- `risk_on_high->crypto_alt_1h` score `-0.2758` n `131` status `ready` deltaP `2.6261` edge `0.0612` maxDD `-5.4685`
- `risk_on_and_context->crypto_alt_1h` score `-0.2758` n `131` status `ready` deltaP `2.6261` edge `0.0612` maxDD `-5.4685`
- `risk_on_high->equity_1h` score `-0.4447` n `131` status `ready` deltaP `6.6371` edge `-0.0138` maxDD `-2.6638`
- `risk_on_and_context->equity_1h` score `-0.4447` n `131` status `ready` deltaP `6.6371` edge `-0.0138` maxDD `-2.6638`
- `risk_on_high->commodity_1h` score `-0.5426` n `131` status `ready` deltaP `0.6651` edge `0.0007` maxDD `-1.0281`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
