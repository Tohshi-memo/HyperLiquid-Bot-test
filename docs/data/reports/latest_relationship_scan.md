# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-14T07:07:58.073215+00:00`
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

- `market_context_high->unknown_24h` score `90.2352` n `150` status `ready` deltaP `-29.7986` edge `8.0095` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.1122` n `32` status `ready` deltaP `-43.9236` edge `4.613` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.1122` n `32` status `ready` deltaP `-43.9236` edge `4.613` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `10.0366` n `36` status `ready` deltaP `10.0694` edge `0.8072` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.2172` n `36` status `ready` deltaP `38.7195` edge `0.3433` maxDD `0.0`
- `risk_on_high->commodity_24h` score `4.7865` n `32` status `ready` deltaP `32.2917` edge `0.1836` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.7865` n `32` status `ready` deltaP `32.2917` edge `0.1836` maxDD `0.0`
- `market_context_high->commodity_24h` score `2.8594` n `150` status `ready` deltaP `22.2917` edge `0.17` maxDD `-2.4263`
- `risk_on_high->commodity_4h` score `2.811` n `32` status `ready` deltaP `19.5884` edge `0.1219` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.811` n `32` status `ready` deltaP `19.5884` edge `0.1219` maxDD `-0.1258`
- `news_risk_high->index_24h` score `2.2755` n `36` status `ready` deltaP `14.5833` edge `0.0924` maxDD `0.0`
- `news_risk_high->index_4h` score `1.7213` n `36` status `ready` deltaP `20.2235` edge `0.0218` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.6602` n `36` status `ready` deltaP `8.7326` edge `0.112` maxDD `-0.5496`
- `market_context_high->commodity_4h` score `1.4495` n `150` status `ready` deltaP `16.1301` edge `0.0771` maxDD `-2.1077`
- `risk_on_high->crypto_major_24h` score `1.3398` n `32` status `ready` deltaP `12.3264` edge `0.2052` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `1.3398` n `32` status `ready` deltaP `12.3264` edge `0.2052` maxDD `-6.2481`
- `risk_on_high->commodity_1h` score `1.2875` n `32` status `ready` deltaP `13.6602` edge `0.0395` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2875` n `32` status `ready` deltaP `13.6602` edge `0.0395` maxDD `-0.1957`
- `risk_on_high->fx_24h` score `1.1936` n `32` status `ready` deltaP `14.2361` edge `0.023` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.1936` n `32` status `ready` deltaP `14.2361` edge `0.023` maxDD `-0.1418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
