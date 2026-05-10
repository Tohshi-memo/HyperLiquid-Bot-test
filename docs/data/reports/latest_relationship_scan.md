# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-10T13:52:16.644519+00:00`
- Price records: `672`
- Market context records: `982`
- Flow alert records: `2748`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1440`

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

- `market_context_high->crypto_major_24h` score `15.3936` n `150` status `ready` deltaP `35.7292` edge `1.078` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `9.8841` n `150` status `ready` deltaP `12.3264` edge `0.7415` maxDD `0.0`
- `market_context_high->equity_24h` score `1.2028` n `150` status `ready` deltaP `0.8264` edge `0.3552` maxDD `-10.5047`
- `market_context_high->index_24h` score `0.509` n `150` status `ready` deltaP `-1.4652` edge `0.2517` maxDD `-5.9609`
- `market_context_high->commodity_1h` score `-0.196` n `210` status `ready` deltaP `3.7425` edge `0.0395` maxDD `-3.7959`
- `market_context_high->fx_1h` score `-0.5434` n `210` status `ready` deltaP `1.7679` edge `0.001` maxDD `-0.3124`
- `market_context_high->equity_1h` score `-0.6512` n `210` status `ready` deltaP `1.1249` edge `0.0151` maxDD `-4.4826`
- `market_context_high->fx_4h` score `-0.684` n `205` status `ready` deltaP `1.4329` edge `0.0024` maxDD `-1.6381`
- `market_context_high->index_1h` score `-0.7054` n `210` status `ready` deltaP `3.2207` edge `0.0051` maxDD `-2.8282`
- `market_context_high->crypto_major_1h` score `-1.1449` n `210` status `ready` deltaP `5.2238` edge `-0.0093` maxDD `-11.4508`
- `market_context_high->unknown_1h` score `-1.174` n `210` status `ready` deltaP `-1.075` edge `-0.0135` maxDD `-3.5069`
- `market_context_high->equity_4h` score `-1.5679` n `205` status `ready` deltaP `1.372` edge `0.0754` maxDD `-10.5498`
- `market_context_high->index_4h` score `-1.7673` n `205` status `ready` deltaP `-1.9207` edge `0.0178` maxDD `-6.5149`
- `market_context_high->metal_1h` score `-1.8441` n `210` status `ready` deltaP `-1.4984` edge `-0.0305` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-1.9806` n `205` status `ready` deltaP `-1.5549` edge `0.0732` maxDD `-13.0076`
- `market_context_high->crypto_alt_1h` score `-2.12` n `210` status `ready` deltaP `-0.3151` edge `-0.0306` maxDD `-8.1842`
- `market_context_high->crypto_major_4h` score `-2.8179` n `205` status `ready` deltaP `7.2561` edge `0.0874` maxDD `-22.648`
- `market_context_high->unknown_4h` score `-3.2317` n `205` status `ready` deltaP `7.5915` edge `-0.1321` maxDD `-8.3588`
- `market_context_high->crypto_alt_4h` score `-3.4616` n `205` status `ready` deltaP `-2.3781` edge `0.0052` maxDD `-15.2248`
- `market_context_high->unknown_24h` score `-4.0687` n `150` status `ready` deltaP `4.493` edge `-0.001` maxDD `-33.7129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
