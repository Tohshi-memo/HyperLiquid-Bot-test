# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-10T14:13:12.747201+00:00`
- Price records: `672`
- Market context records: `984`
- Flow alert records: `2753`
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

- `market_context_high->crypto_major_24h` score `15.3972` n `150` status `ready` deltaP `35.7292` edge `1.0783` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `9.8865` n `150` status `ready` deltaP `12.3264` edge `0.7417` maxDD `0.0`
- `market_context_high->equity_24h` score `1.1932` n `150` status `ready` deltaP `0.8264` edge `0.3544` maxDD `-10.5047`
- `market_context_high->index_24h` score `0.5042` n `150` status `ready` deltaP `-1.4652` edge `0.2513` maxDD `-5.9609`
- `market_context_high->commodity_1h` score `-0.196` n `210` status `ready` deltaP `3.7425` edge `0.0395` maxDD `-3.7959`
- `market_context_high->fx_1h` score `-0.5303` n `210` status `ready` deltaP `1.9176` edge `0.0011` maxDD `-0.3124`
- `market_context_high->equity_1h` score `-0.6512` n `210` status `ready` deltaP `1.1249` edge `0.0151` maxDD `-4.4826`
- `market_context_high->fx_4h` score `-0.6894` n `206` status `ready` deltaP `1.3439` edge `0.0023` maxDD `-1.6381`
- `market_context_high->index_1h` score `-0.7186` n `210` status `ready` deltaP `3.071` edge `0.005` maxDD `-2.8282`
- `market_context_high->crypto_major_1h` score `-1.1581` n `210` status `ready` deltaP `5.0741` edge `-0.01` maxDD `-11.4508`
- `market_context_high->unknown_1h` score `-1.1752` n `210` status `ready` deltaP `-1.075` edge `-0.0136` maxDD `-3.5069`
- `market_context_high->equity_4h` score `-1.5692` n `206` status `ready` deltaP `1.4904` edge `0.0745` maxDD `-10.5498`
- `market_context_high->index_4h` score `-1.7889` n `206` status `ready` deltaP `-2.1164` edge `0.0173` maxDD `-6.5149`
- `market_context_high->metal_1h` score `-1.8441` n `210` status `ready` deltaP `-1.4984` edge `-0.0305` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-1.998` n `206` status `ready` deltaP `-1.7538` edge `0.0723` maxDD `-13.0076`
- `market_context_high->crypto_alt_1h` score `-2.1392` n `210` status `ready` deltaP `-0.4648` edge `-0.0312` maxDD `-8.1842`
- `market_context_high->crypto_major_4h` score `-2.817` n `206` status `ready` deltaP `7.2979` edge `0.0872` maxDD `-22.648`
- `market_context_high->unknown_4h` score `-3.2586` n `206` status `ready` deltaP `7.4503` edge `-0.1334` maxDD `-8.3588`
- `market_context_high->crypto_alt_4h` score `-3.4503` n `206` status `ready` deltaP `-2.3576` edge `0.006` maxDD `-15.2248`
- `market_context_high->unknown_24h` score `-4.0839` n `150` status `ready` deltaP `4.3194` edge `-0.0018` maxDD `-33.7129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
