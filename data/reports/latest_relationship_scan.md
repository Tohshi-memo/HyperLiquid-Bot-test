# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-08T16:52:37.220161+00:00`
- Price records: `672`
- Market context records: `3298`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13141`

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

- `risk_on_high->crypto_major_4h` score `15.8309` n `32` status `ready` deltaP `29.7256` edge `1.2333` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.8309` n `32` status `ready` deltaP `29.7256` edge `1.2333` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `14.0099` n `115` status `ready` deltaP `18.4933` edge `2.657` maxDD `-70.3986`
- `market_context_high->commodity_24h` score `10.2115` n `115` status `ready` deltaP `37.8276` edge `0.6714` maxDD `-3.4768`
- `market_context_high->index_24h` score `9.7355` n `115` status `ready` deltaP `31.0417` edge `0.8598` maxDD `-16.1026`
- `risk_on_high->crypto_alt_4h` score `7.5689` n `32` status `ready` deltaP `10.8994` edge `0.7425` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.5689` n `32` status `ready` deltaP `10.8994` edge `0.7425` maxDD `-11.7537`
- `market_context_high->equity_24h` score `7.4396` n `115` status `ready` deltaP `21.8131` edge `1.65` maxDD `-53.663`
- `risk_on_high->equity_4h` score `3.7005` n `32` status `ready` deltaP `14.7104` edge `0.4898` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.7005` n `32` status `ready` deltaP `14.7104` edge `0.4898` maxDD `-5.7426`
- `market_context_high->commodity_4h` score `2.0755` n `176` status `ready` deltaP `18.9718` edge `0.1423` maxDD `-3.9989`
- `risk_on_high->crypto_major_1h` score `2.0299` n `32` status `ready` deltaP `6.7178` edge `0.3224` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `2.0299` n `32` status `ready` deltaP `6.7178` edge `0.3224` maxDD `-5.8885`
- `market_context_high->crypto_major_24h` score `1.4148` n `115` status `ready` deltaP `19.0051` edge `2.1246` maxDD `-152.2601`
- `risk_on_high->index_4h` score `1.123` n `32` status `ready` deltaP `1.1433` edge `0.1951` maxDD `-1.7001`
- `risk_on_and_context->index_4h` score `1.123` n `32` status `ready` deltaP `1.1433` edge `0.1951` maxDD `-1.7001`
- `risk_on_high->metal_1h` score `0.2689` n `32` status `ready` deltaP `6.25` edge `0.0613` maxDD `-1.4793`
- `risk_on_and_context->metal_1h` score `0.2689` n `32` status `ready` deltaP `6.25` edge `0.0613` maxDD `-1.4793`
- `risk_on_high->crypto_alt_1h` score `0.2291` n `32` status `ready` deltaP `0.4491` edge `0.1701` maxDD `-8.1649`
- `risk_on_and_context->crypto_alt_1h` score `0.2291` n `32` status `ready` deltaP `0.4491` edge `0.1701` maxDD `-8.1649`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
