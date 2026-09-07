# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-07T02:07:26.924184+00:00`
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

- `risk_on_high->unknown_24h` score `439.9109` n `99` status `ready` deltaP `26.7361` edge `36.481` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `439.9109` n `99` status `ready` deltaP `26.7361` edge `36.481` maxDD `0.0`
- `market_context_high->unknown_1h` score `22.8977` n `247` status `ready` deltaP `-2.8364` edge `1.9995` maxDD `-2.4626`
- `risk_on_high->crypto_major_24h` score `20.1394` n `99` status `ready` deltaP `33.791` edge `1.5047` maxDD `-1.4687`
- `risk_on_and_context->crypto_major_24h` score `20.1394` n `99` status `ready` deltaP `33.791` edge `1.5047` maxDD `-1.4687`
- `risk_on_high->crypto_alt_24h` score `13.8936` n `99` status `ready` deltaP `30.5556` edge `0.9541` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `13.8936` n `99` status `ready` deltaP `30.5556` edge `0.9541` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `8.8614` n `188` status `ready` deltaP `24.1726` edge `0.6348` maxDD `-2.5998`
- `market_context_high->equity_24h` score `6.6172` n `188` status `ready` deltaP `23.0903` edge `0.3975` maxDD `0.0`
- `risk_on_high->equity_24h` score `5.5492` n `99` status `ready` deltaP `23.0903` edge `0.3085` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `5.5492` n `99` status `ready` deltaP `23.0903` edge `0.3085` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `5.4937` n `122` status `ready` deltaP `28.676` edge `0.3038` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.4937` n `122` status `ready` deltaP `28.676` edge `0.3038` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `3.9693` n `122` status `ready` deltaP `22.4011` edge `0.2673` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `3.9693` n `122` status `ready` deltaP `22.4011` edge `0.2673` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.7359` n `99` status `ready` deltaP `23.3586` edge `0.0765` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.7359` n `99` status `ready` deltaP `23.3586` edge `0.0765` maxDD `-0.0051`
- `market_context_high->index_24h` score `2.607` n `188` status `ready` deltaP `21.6017` edge `0.0947` maxDD `-0.0505`
- `risk_on_high->crypto_alt_1h` score `0.9339` n `123` status `ready` deltaP `4.2391` edge `0.0848` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.9339` n `123` status `ready` deltaP `4.2391` edge `0.0848` maxDD `-1.1521`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
