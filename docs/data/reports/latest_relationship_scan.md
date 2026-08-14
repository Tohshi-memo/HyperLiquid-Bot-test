# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-14T06:52:24.843830+00:00`
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

- `market_context_high->unknown_24h` score `90.2544` n `150` status `ready` deltaP `-29.7986` edge `8.0111` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.1246` n `32` status `ready` deltaP `-43.9236` edge `4.6146` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.1246` n `32` status `ready` deltaP `-43.9236` edge `4.6146` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `10.0402` n `36` status `ready` deltaP `10.0694` edge `0.8075` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.21` n `36` status `ready` deltaP `38.7195` edge `0.3427` maxDD `0.0`
- `risk_on_high->commodity_24h` score `4.7877` n `32` status `ready` deltaP `32.2917` edge `0.1837` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.7877` n `32` status `ready` deltaP `32.2917` edge `0.1837` maxDD `0.0`
- `market_context_high->commodity_24h` score `2.8606` n `150` status `ready` deltaP `22.2917` edge `0.1701` maxDD `-2.4263`
- `risk_on_high->commodity_4h` score `2.834` n `32` status `ready` deltaP `19.7409` edge `0.1228` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.834` n `32` status `ready` deltaP `19.7409` edge `0.1228` maxDD `-0.1258`
- `news_risk_high->index_24h` score `2.2791` n `36` status `ready` deltaP `14.5833` edge `0.0927` maxDD `0.0`
- `news_risk_high->index_4h` score `1.7213` n `36` status `ready` deltaP `20.2235` edge `0.0218` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.6614` n `36` status `ready` deltaP `8.7326` edge `0.1121` maxDD `-0.5496`
- `market_context_high->commodity_4h` score `1.4725` n `150` status `ready` deltaP `16.2826` edge `0.078` maxDD `-2.1077`
- `risk_on_high->crypto_major_24h` score `1.3082` n `32` status `ready` deltaP `12.1528` edge `0.2023` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `1.3082` n `32` status `ready` deltaP `12.1528` edge `0.2023` maxDD `-6.2481`
- `risk_on_high->commodity_1h` score `1.2875` n `32` status `ready` deltaP `13.6602` edge `0.0395` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2875` n `32` status `ready` deltaP `13.6602` edge `0.0395` maxDD `-0.1957`
- `risk_on_high->fx_24h` score `1.1948` n `32` status `ready` deltaP `14.2361` edge `0.0231` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.1948` n `32` status `ready` deltaP `14.2361` edge `0.0231` maxDD `-0.1418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
