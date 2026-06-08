# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-08T16:18:17.528713+00:00`
- Price records: `672`
- Market context records: `3295`
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

- `risk_on_high->crypto_major_4h` score `15.8105` n `32` status `ready` deltaP `29.7256` edge `1.2316` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `15.8105` n `32` status `ready` deltaP `29.7256` edge `1.2316` maxDD `-5.9781`
- `market_context_high->crypto_alt_24h` score `13.8825` n `113` status `ready` deltaP `17.9941` edge `2.644` maxDD `-70.3986`
- `market_context_high->commodity_24h` score `10.8643` n `113` status `ready` deltaP `39.3974` edge `0.6931` maxDD `-2.3649`
- `market_context_high->index_24h` score `9.5584` n `113` status `ready` deltaP `30.6877` edge `0.8474` maxDD `-16.1026`
- `risk_on_high->crypto_alt_4h` score `7.5425` n `32` status `ready` deltaP `10.8994` edge `0.7403` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `7.5425` n `32` status `ready` deltaP `10.8994` edge `0.7403` maxDD `-11.7537`
- `market_context_high->equity_24h` score `7.1783` n `113` status `ready` deltaP `21.1821` edge `1.6207` maxDD `-53.663`
- `risk_on_high->equity_4h` score `3.7209` n `32` status `ready` deltaP `14.8628` edge `0.4914` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `3.7209` n `32` status `ready` deltaP `14.8628` edge `0.4914` maxDD `-5.7426`
- `market_context_high->commodity_4h` score `2.142` n `174` status `ready` deltaP `19.3527` edge `0.1453` maxDD `-3.9989`
- `risk_on_high->crypto_major_1h` score `1.9847` n `32` status `ready` deltaP `6.4184` edge `0.3186` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `1.9847` n `32` status `ready` deltaP `6.4184` edge `0.3186` maxDD `-5.8885`
- `market_context_high->crypto_major_24h` score `1.1266` n `113` status `ready` deltaP `18.4135` edge `2.0916` maxDD `-152.2601`
- `risk_on_high->index_4h` score `1.123` n `32` status `ready` deltaP `1.1433` edge `0.1951` maxDD `-1.7001`
- `risk_on_and_context->index_4h` score `1.123` n `32` status `ready` deltaP `1.1433` edge `0.1951` maxDD `-1.7001`
- `risk_on_high->metal_1h` score `0.2634` n `32` status `ready` deltaP `6.25` edge `0.0606` maxDD `-1.4793`
- `risk_on_and_context->metal_1h` score `0.2634` n `32` status `ready` deltaP `6.25` edge `0.0606` maxDD `-1.4793`
- `risk_on_high->commodity_4h` score `0.2172` n `32` status `ready` deltaP `8.6128` edge `0.0474` maxDD `-3.6044`
- `risk_on_and_context->commodity_4h` score `0.2172` n `32` status `ready` deltaP `8.6128` edge `0.0474` maxDD `-3.6044`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
