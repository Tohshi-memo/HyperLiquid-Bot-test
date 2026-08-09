# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T21:37:26.403148+00:00`
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

- `market_context_high->metal_24h` score `1.2498` n `120` status `ready` deltaP `7.2222` edge `0.1136` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.0941` n `143` status `ready` deltaP `14.2899` edge `0.0632` maxDD `-2.7169`
- `market_context_high->equity_24h` score `0.978` n `120` status `ready` deltaP `3.4028` edge `0.3648` maxDD `-21.1456`
- `market_context_high->commodity_1h` score `0.7812` n `153` status `ready` deltaP `10.6493` edge `0.0284` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.5358` n `120` status `ready` deltaP `19.5833` edge `0.0248` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.0303` n `120` status `ready` deltaP `5.6598` edge `0.1193` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.5378` n `153` status `ready` deltaP `1.2945` edge `-0.0039` maxDD `-0.9639`
- `market_context_high->metal_1h` score `-0.6171` n `153` status `ready` deltaP `-3.4411` edge `-0.0066` maxDD `-0.9664`
- `market_context_high->index_1h` score `-0.6244` n `153` status `ready` deltaP `-4.1094` edge `-0.0054` maxDD `-0.7809`
- `market_context_high->fx_4h` score `-0.7258` n `143` status `ready` deltaP `2.9316` edge `-0.0047` maxDD `-1.6928`
- `market_context_high->equity_1h` score `-0.9319` n `153` status `ready` deltaP `0.0753` edge `0.0047` maxDD `-4.6286`
- `market_context_high->index_4h` score `-0.955` n `143` status `ready` deltaP `-1.5254` edge `-0.0089` maxDD `-1.1743`
- `market_context_high->metal_4h` score `-1.0019` n `143` status `ready` deltaP `-1.6608` edge `-0.0165` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-1.2127` n `153` status `ready` deltaP `-9.4184` edge `-0.0285` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.5662` n `143` status `ready` deltaP `-2.0286` edge `-0.0666` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.269` n `153` status `ready` deltaP `-12.022` edge `-0.0589` maxDD `-7.3365`
- `market_context_high->crypto_alt_4h` score `-4.1328` n `143` status `ready` deltaP `-9.0387` edge `-0.1185` maxDD `-6.585`
- `market_context_high->crypto_major_24h` score `-4.1942` n `120` status `ready` deltaP `2.4306` edge `-0.1163` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-5.3606` n `120` status `ready` deltaP `-15.4514` edge `-0.1994` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-8.0061` n `153` status `ready` deltaP `-7.8705` edge `-0.569` maxDD `-1.323`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
