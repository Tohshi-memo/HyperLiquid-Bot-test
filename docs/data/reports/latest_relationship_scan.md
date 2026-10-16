# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-16T05:37:31.852354+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9028`

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

- `risk_on_high->commodity_24h` score `8.0382` n `54` status `ready` deltaP `42.6829` edge `0.3853` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.0382` n `54` status `ready` deltaP `42.6829` edge `0.3853` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `7.5896` n `122` status `ready` deltaP `19.7871` edge `0.592` maxDD `-4.9825`
- `market_context_high->crypto_major_4h` score `6.0612` n `122` status `ready` deltaP `22.1487` edge `0.4896` maxDD `-5.906`
- `risk_on_high->crypto_alt_4h` score `5.3959` n `54` status `ready` deltaP `22.5497` edge `0.344` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `5.3959` n `54` status `ready` deltaP `22.5497` edge `0.344` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `4.15` n `54` status `ready` deltaP `35.5974` edge `0.38` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.15` n `54` status `ready` deltaP `35.5974` edge `0.38` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.4992` n `122` status `ready` deltaP `13.7062` edge `0.14` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `0.9919` n `122` status `ready` deltaP `6.7071` edge `0.1185` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.2736` n `122` status `ready` deltaP `11.9902` edge `0.0474` maxDD `-1.6961`
- `market_context_high->fx_1h` score `-0.2899` n `122` status `ready` deltaP `0.4381` edge `-0.0017` maxDD `-0.4047`
- `market_context_high->metal_1h` score `-0.3234` n `122` status `ready` deltaP `8.0544` edge `0.0063` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.3753` n `54` status `ready` deltaP `3.3489` edge `0.0027` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.3753` n `54` status `ready` deltaP `3.3489` edge `0.0027` maxDD `-0.8513`
- `market_context_high->commodity_24h` score `-0.4274` n `119` status `ready` deltaP `12.4308` edge `0.1405` maxDD `-11.5869`
- `risk_on_high->crypto_major_1h` score `-0.4484` n `54` status `ready` deltaP `2.0016` edge `0.0014` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.4484` n `54` status `ready` deltaP `2.0016` edge `0.0014` maxDD `-3.7781`
- `market_context_high->index_1h` score `-0.4702` n `122` status `ready` deltaP `2.4148` edge `-0.0016` maxDD `-1.3154`
- `risk_on_high->index_1h` score `-0.5005` n `54` status `ready` deltaP `-3.3533` edge `-0.0034` maxDD `-0.7394`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
