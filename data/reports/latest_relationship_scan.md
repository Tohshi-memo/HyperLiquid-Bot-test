# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T17:37:30.610983+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8502`

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

- `news_risk_high->crypto_major_24h` score `51.6054` n `72` status `ready` deltaP `29.1666` edge `4.1952` maxDD `-5.8019`
- `market_context_high->unknown_4h` score `45.4131` n `128` status `ready` deltaP `-2.8582` edge `3.8268` maxDD `-0.5326`
- `news_risk_high->crypto_alt_24h` score `45.1819` n `72` status `ready` deltaP `34.375` edge `3.6739` maxDD `-9.3661`
- `risk_on_high->unknown_4h` score `23.2113` n `38` status `ready` deltaP `-12.9733` edge `2.0433` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `23.2113` n `38` status `ready` deltaP `-12.9733` edge `2.0433` maxDD `-0.4694`
- `news_risk_high->equity_24h` score `9.3704` n `72` status `ready` deltaP `38.7153` edge `0.527` maxDD `-0.0053`
- `risk_on_high->commodity_24h` score `9.3283` n `38` status `ready` deltaP `48.2639` edge `0.4556` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.3283` n `38` status `ready` deltaP `48.2639` edge `0.4556` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.6027` n `128` status `ready` deltaP `40.4514` edge `0.4164` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `5.678` n `98` status `ready` deltaP `21.4659` edge `0.451` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.2627` n `98` status `ready` deltaP `21.4659` edge `0.3379` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `3.2879` n `98` status `ready` deltaP `19.2228` edge `0.1924` maxDD `-2.058`
- `market_context_high->commodity_4h` score `2.5562` n `128` status `ready` deltaP `27.0198` edge `0.0747` maxDD `-0.345`
- `news_risk_high->crypto_major_1h` score `2.3875` n `98` status `ready` deltaP `19.9713` edge `0.1181` maxDD `-2.8494`
- `risk_on_high->commodity_4h` score `2.2922` n `38` status `ready` deltaP `26.7731` edge `0.0475` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.2922` n `38` status `ready` deltaP `26.7731` edge `0.0475` maxDD `-0.1313`
- `news_risk_high->metal_24h` score `1.7261` n `72` status `ready` deltaP `22.5694` edge `0.0778` maxDD `-2.4203`
- `market_context_high->commodity_1h` score `1.461` n `128` status `ready` deltaP `18.2167` edge `0.0255` maxDD `-0.3491`
- `risk_on_high->commodity_1h` score `1.3054` n `38` status `ready` deltaP `16.3253` edge `0.0185` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `1.3054` n `38` status `ready` deltaP `16.3253` edge `0.0185` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
