# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-13T04:52:27.410619+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12599`

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

- `market_context_high->unknown_24h` score `16612.0383` n `59` status `ready` deltaP `13.2769` edge `1384.2532` maxDD `-0.082`
- `news_risk_high->unknown_1h` score `379.3946` n `82` status `ready` deltaP `-4.502` edge `31.6884` maxDD `-1.7068`
- `news_risk_high->crypto_major_24h` score `17.8629` n `82` status `ready` deltaP `38.6306` edge `1.3781` maxDD `-9.098`
- `news_risk_high->crypto_alt_24h` score `17.8437` n `82` status `ready` deltaP `31.8851` edge `1.3232` maxDD `-2.2369`
- `market_context_high->equity_24h` score `10.8465` n `59` status `ready` deltaP `48.6111` edge `0.5798` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `9.9451` n `59` status `ready` deltaP `21.8397` edge `0.7659` maxDD `-3.9523`
- `news_risk_high->equity_24h` score `6.5893` n `82` status `ready` deltaP `18.1233` edge `0.6063` maxDD `-6.5742`
- `news_risk_high->index_24h` score `6.2253` n `82` status `ready` deltaP `43.5213` edge `0.2463` maxDD `-0.0797`
- `news_risk_high->metal_24h` score `4.7791` n `82` status `ready` deltaP `25.9612` edge `0.2706` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `4.239` n `59` status `ready` deltaP `42.1875` edge `0.072` maxDD `0.0`
- `market_context_high->index_24h` score `4.104` n `59` status `ready` deltaP `44.1208` edge `0.0871` maxDD `-0.1391`
- `news_risk_high->index_4h` score `0.2355` n `82` status `ready` deltaP `9.6036` edge `0.029` maxDD `-0.6935`
- `market_context_high->metal_24h` score `0.2154` n `59` status `ready` deltaP `6.759` edge `0.1023` maxDD `-2.9132`
- `risk_on_high->crypto_alt_4h` score `0.1526` n `55` status `ready` deltaP `8.0294` edge `0.1335` maxDD `-6.7304`
- `risk_on_and_context->crypto_alt_4h` score `0.1526` n `55` status `ready` deltaP `8.0294` edge `0.1335` maxDD `-6.7304`
- `risk_on_high->fx_1h` score `0.1101` n `65` status `ready` deltaP `4.7029` edge `0.0034` maxDD `-0.0464`
- `risk_on_and_context->fx_1h` score `0.1101` n `65` status `ready` deltaP `4.7029` edge `0.0034` maxDD `-0.0464`
- `market_context_high->fx_1h` score `-0.072` n `125` status `ready` deltaP `3.5952` edge `-0.0016` maxDD `-0.5274`
- `risk_on_high->metal_1h` score `-0.0999` n `65` status `ready` deltaP `3.4638` edge `0.0016` maxDD `-0.3081`
- `risk_on_and_context->metal_1h` score `-0.0999` n `65` status `ready` deltaP `3.4638` edge `0.0016` maxDD `-0.3081`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
