# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T07:22:25.078492+00:00`
- Price records: `672`
- Market context records: `6581`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9808`

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

- `market_context_high->unknown_24h` score `5.5048` n `149` status `ready` deltaP `8.9347` edge `0.7292` maxDD `-15.0689`
- `market_context_high->unknown_1h` score `2.0268` n `210` status `ready` deltaP `-5.1297` edge `0.2932` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `1.4047` n `149` status `ready` deltaP `14.1415` edge `0.2096` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.3526` n `210` status `ready` deltaP `0.8583` edge `-0.0002` maxDD `-0.7249`
- `market_context_high->crypto_major_1h` score `-0.4002` n `210` status `ready` deltaP `7.197` edge `0.0273` maxDD `-6.7936`
- `market_context_high->index_1h` score `-0.5553` n `210` status `ready` deltaP `-0.3807` edge `0.0033` maxDD `-0.7564`
- `market_context_high->crypto_alt_1h` score `-0.5578` n `210` status `ready` deltaP `5.442` edge `0.0235` maxDD `-5.8368`
- `market_context_high->commodity_1h` score `-0.5954` n `210` status `ready` deltaP `-0.5589` edge `-0.0043` maxDD `-2.1314`
- `market_context_high->index_4h` score `-0.9318` n `210` status `ready` deltaP `8.8371` edge `0.0096` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-1.1489` n `210` status `ready` deltaP `2.2313` edge `0.0004` maxDD `-4.2147`
- `market_context_high->commodity_4h` score `-1.3096` n `210` status `ready` deltaP `-1.279` edge `-0.0099` maxDD `-5.6246`
- `market_context_high->metal_1h` score `-1.3339` n `210` status `ready` deltaP `-4.1759` edge `-0.0026` maxDD `-2.1239`
- `market_context_high->unknown_4h` score `-1.6049` n `210` status `ready` deltaP `-16.1513` edge `0.2145` maxDD `-10.5788`
- `market_context_high->crypto_major_4h` score `-1.7487` n `210` status `ready` deltaP `7.7338` edge `0.0557` maxDD `-16.8495`
- `market_context_high->fx_4h` score `-1.7543` n `210` status `ready` deltaP `-0.0755` edge `-0.0032` maxDD `-3.3635`
- `market_context_high->crypto_alt_4h` score `-2.0016` n `210` status `ready` deltaP `4.7808` edge `0.0517` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.154` n `210` status `ready` deltaP `-1.5012` edge `0.0199` maxDD `-5.2172`
- `market_context_high->metal_24h` score `-2.6087` n `149` status `ready` deltaP `4.6702` edge `0.0802` maxDD `-6.9645`
- `market_context_high->fx_24h` score `-3.7289` n `149` status `ready` deltaP `-3.2352` edge `-0.003` maxDD `-9.2795`
- `market_context_high->index_24h` score `-4.3033` n `149` status `ready` deltaP `-0.0718` edge `-0.0074` maxDD `-11.3917`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
