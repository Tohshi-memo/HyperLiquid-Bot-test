# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-14T06:37:27.944897+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11808`

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

- `market_context_high->unknown_24h` score `90.2887` n `150` status `ready` deltaP `-29.625` edge `8.0128` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.1469` n `32` status `ready` deltaP `-43.75` edge `4.6163` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.1469` n `32` status `ready` deltaP `-43.75` edge `4.6163` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `10.0366` n `36` status `ready` deltaP `10.0694` edge `0.8072` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.187` n `36` status `ready` deltaP `38.5671` edge `0.3418` maxDD `0.0`
- `risk_on_high->commodity_24h` score `4.7865` n `32` status `ready` deltaP `32.2917` edge `0.1836` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.7865` n `32` status `ready` deltaP `32.2917` edge `0.1836` maxDD `0.0`
- `market_context_high->commodity_24h` score `2.8594` n `150` status `ready` deltaP `22.2917` edge `0.17` maxDD `-2.4263`
- `risk_on_high->commodity_4h` score `2.8534` n `32` status `ready` deltaP `19.8933` edge `0.1234` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.8534` n `32` status `ready` deltaP `19.8933` edge `0.1234` maxDD `-0.1258`
- `news_risk_high->index_24h` score `2.2827` n `36` status `ready` deltaP `14.5833` edge `0.093` maxDD `0.0`
- `news_risk_high->index_4h` score `1.7201` n `36` status `ready` deltaP `20.2235` edge `0.0217` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.647` n `36` status `ready` deltaP `8.5829` edge `0.1119` maxDD `-0.5496`
- `market_context_high->commodity_4h` score `1.4918` n `150` status `ready` deltaP `16.435` edge `0.0786` maxDD `-2.1077`
- `risk_on_high->commodity_1h` score `1.3006` n `32` status `ready` deltaP `13.8099` edge `0.0396` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.3006` n `32` status `ready` deltaP `13.8099` edge `0.0396` maxDD `-0.1957`
- `risk_on_high->crypto_major_24h` score `1.2789` n `32` status `ready` deltaP `11.9792` edge `0.1997` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `1.2789` n `32` status `ready` deltaP `11.9792` edge `0.1997` maxDD `-6.2481`
- `risk_on_high->fx_24h` score `1.1948` n `32` status `ready` deltaP `14.2361` edge `0.0231` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.1948` n `32` status `ready` deltaP `14.2361` edge `0.0231` maxDD `-0.1418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
