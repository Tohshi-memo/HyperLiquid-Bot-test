# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-08T16:37:31.958461+00:00`
- Price records: `672`
- Market context records: `3297`
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

- `risk_on_high->crypto_major_4h` score `15.8225` n `32` status `ready` deltaP `29.7256` edge `1.2326` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.8225` n `32` status `ready` deltaP `29.7256` edge `1.2326` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `13.9534` n `114` status `ready` deltaP `18.2475` edge `2.6514` maxDD `-70.3986`
- `market_context_high->commodity_24h` score `10.5281` n `114` status `ready` deltaP `38.6056` edge `0.6817` maxDD `-2.9386`
- `market_context_high->index_24h` score `9.6447` n `114` status `ready` deltaP `30.8663` edge `0.8534` maxDD `-16.1026`
- `risk_on_high->crypto_alt_4h` score `7.5581` n `32` status `ready` deltaP `10.8994` edge `0.7416` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.5581` n `32` status `ready` deltaP `10.8994` edge `0.7416` maxDD `-11.7537`
- `market_context_high->equity_24h` score `7.3095` n `114` status `ready` deltaP `21.5004` edge `1.6354` maxDD `-53.663`
- `risk_on_high->equity_4h` score `3.7178` n `32` status `ready` deltaP `14.8628` edge `0.491` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.7178` n `32` status `ready` deltaP `14.8628` edge `0.491` maxDD `-5.7426`
- `market_context_high->commodity_4h` score `2.0859` n `175` status `ready` deltaP `18.9521` edge `0.1433` maxDD `-3.9989`
- `risk_on_high->crypto_major_1h` score `2.0073` n `32` status `ready` deltaP `6.5681` edge `0.3205` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `2.0073` n `32` status `ready` deltaP `6.5681` edge `0.3205` maxDD `-5.8885`
- `market_context_high->crypto_major_24h` score `1.2818` n `114` status `ready` deltaP `18.7134` edge `2.1095` maxDD `-152.2601`
- `risk_on_high->index_4h` score `1.1245` n `32` status `ready` deltaP `1.1433` edge `0.1953` maxDD `-1.7001`
- `risk_on_and_context->index_4h` score `1.1245` n `32` status `ready` deltaP `1.1433` edge `0.1953` maxDD `-1.7001`
- `risk_on_high->metal_1h` score `0.265` n `32` status `ready` deltaP `6.25` edge `0.0608` maxDD `-1.4793`
- `risk_on_and_context->metal_1h` score `0.265` n `32` status `ready` deltaP `6.25` edge `0.0608` maxDD `-1.4793`
- `risk_on_high->crypto_alt_1h` score `0.2096` n `32` status `ready` deltaP `0.2994` edge `0.1686` maxDD `-8.1649`
- `risk_on_and_context->crypto_alt_1h` score `0.2096` n `32` status `ready` deltaP `0.2994` edge `0.1686` maxDD `-8.1649`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
