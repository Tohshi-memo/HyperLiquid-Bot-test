# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-13T11:52:33.492999+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9804`

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

- `market_context_high->crypto_alt_4h` score `8.1328` n `117` status `ready` deltaP `21.0327` edge `0.6824` maxDD `-9.2574`
- `market_context_high->crypto_major_4h` score `7.1796` n `117` status `ready` deltaP `24.931` edge `0.588` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `6.7217` n `54` status `ready` deltaP `23.3119` edge `0.4495` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `6.7217` n `54` status `ready` deltaP `23.3119` edge `0.4495` maxDD `-1.9151`
- `risk_on_high->commodity_24h` score `5.8118` n `48` status `ready` deltaP `31.6522` edge `0.2733` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.8118` n `48` status `ready` deltaP `31.6522` edge `0.2733` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `5.2066` n `54` status `ready` deltaP `38.0364` edge `0.4992` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `5.2066` n `54` status `ready` deltaP `38.0364` edge `0.4992` maxDD `-4.1548`
- `market_context_high->unknown_4h` score `3.111` n `117` status `ready` deltaP `-3.467` edge `0.347` maxDD `-1.8373`
- `market_context_high->crypto_alt_1h` score `2.222` n `117` status `ready` deltaP `15.5126` edge `0.1885` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.6518` n `117` status `ready` deltaP `8.5061` edge `0.1615` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.0498` n `117` status `ready` deltaP `12.0883` edge `0.0281` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.0827` n `54` status `ready` deltaP `3.9477` edge `0.0353` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.0827` n `54` status `ready` deltaP `3.9477` edge `0.0353` maxDD `-3.7781`
- `market_context_high->fx_1h` score `-0.2663` n `117` status `ready` deltaP `1.9982` edge `0.0025` maxDD `-0.3742`
- `risk_on_high->crypto_alt_1h` score `-0.2889` n `54` status `ready` deltaP `5.2562` edge `0.0305` maxDD `-5.8734`
- `risk_on_and_context->crypto_alt_1h` score `-0.2889` n `54` status `ready` deltaP `5.2562` edge `0.0305` maxDD `-5.8734`
- `market_context_high->metal_1h` score `-0.4572` n `117` status `ready` deltaP `6.5165` edge `0.0054` maxDD `-0.9556`
- `market_context_high->index_1h` score `-0.5047` n `117` status `ready` deltaP `1.6747` edge `-0.0011` maxDD `-1.3154`
- `risk_on_high->metal_1h` score `-0.5116` n `54` status `ready` deltaP `1.1034` edge `0.0002` maxDD `-0.8513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
