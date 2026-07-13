# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T08:07:28.577789+00:00`
- Price records: `672`
- Market context records: `6584`
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

- `market_context_high->unknown_24h` score `5.0987` n `152` status `ready` deltaP `7.7425` edge `0.7033` maxDD `-15.0689`
- `market_context_high->unknown_1h` score `1.9729` n `210` status `ready` deltaP `-5.5788` edge `0.2917` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `1.2462` n `152` status `ready` deltaP `13.1363` edge `0.2031` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.3604` n `210` status `ready` deltaP `0.7086` edge `-0.0002` maxDD `-0.7249`
- `market_context_high->crypto_major_1h` score `-0.429` n `210` status `ready` deltaP `6.8976` edge `0.0256` maxDD `-6.7936`
- `market_context_high->index_1h` score `-0.5537` n `210` status `ready` deltaP `-0.3807` edge `0.0035` maxDD `-0.7564`
- `market_context_high->commodity_1h` score `-0.5689` n `210` status `ready` deltaP `-0.1098` edge `-0.0039` maxDD `-2.1314`
- `market_context_high->crypto_alt_1h` score `-0.6007` n `210` status `ready` deltaP `4.9929` edge `0.021` maxDD `-5.8368`
- `market_context_high->index_4h` score `-0.9105` n `210` status `ready` deltaP `9.142` edge `0.0103` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-1.1465` n `210` status `ready` deltaP `2.2313` edge `0.0006` maxDD `-4.2147`
- `market_context_high->commodity_4h` score `-1.3065` n `210` status `ready` deltaP `-1.279` edge `-0.0095` maxDD `-5.6246`
- `market_context_high->metal_1h` score `-1.3782` n `210` status `ready` deltaP `-4.625` edge `-0.0033` maxDD `-2.1239`
- `market_context_high->unknown_4h` score `-1.6523` n `210` status `ready` deltaP `-16.6086` edge `0.2136` maxDD `-10.5788`
- `market_context_high->fx_4h` score `-1.729` n `210` status `ready` deltaP `0.3818` edge `-0.003` maxDD `-3.3635`
- `market_context_high->crypto_major_4h` score `-1.792` n `210` status `ready` deltaP `7.2765` edge `0.0532` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-2.0799` n `210` status `ready` deltaP `4.3235` edge `0.0447` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.154` n `210` status `ready` deltaP `-1.5012` edge `0.0199` maxDD `-5.2172`
- `market_context_high->metal_24h` score `-3.0032` n `152` status `ready` deltaP `3.8622` edge `0.0756` maxDD `-7.7961`
- `market_context_high->fx_24h` score `-3.738` n `152` status `ready` deltaP `-3.5315` edge `-0.0022` maxDD `-9.2795`
- `market_context_high->equity_4h` score `-4.7229` n `210` status `ready` deltaP `7.5058` edge `-0.0167` maxDD `-27.1529`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
