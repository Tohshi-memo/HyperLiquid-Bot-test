# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-15T10:22:28.012779+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11700`

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

- `market_context_high->unknown_24h` score `137.309` n `128` status `ready` deltaP `-26.1956` edge `11.9083` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `33.5298` n `32` status `ready` deltaP `-39.4768` edge `4.6369` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.5298` n `32` status `ready` deltaP `-39.4768` edge `4.6369` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `12.3509` n `36` status `ready` deltaP `23.368` edge `0.9114` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.6459` n `36` status `ready` deltaP `39.8782` edge `0.3713` maxDD `0.0`
- `market_context_high->commodity_24h` score `5.307` n `128` status `ready` deltaP `30.5851` edge `0.2441` maxDD `-0.1266`
- `risk_on_high->commodity_24h` score `4.8831` n `32` status `ready` deltaP `32.9289` edge `0.1874` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.8831` n `32` status `ready` deltaP `32.9289` edge `0.1874` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `4.2276` n `32` status `ready` deltaP `28.2008` edge `0.4696` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `4.2276` n `32` status `ready` deltaP `28.2008` edge `0.4696` maxDD `-6.2481`
- `news_risk_high->index_24h` score `3.3661` n `36` status `ready` deltaP `27.5563` edge `0.0968` maxDD `0.0`
- `risk_on_high->commodity_4h` score `3.0044` n `32` status `ready` deltaP `21.9606` edge `0.1222` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `3.0044` n `32` status `ready` deltaP `21.9606` edge `0.1222` maxDD `-0.1258`
- `market_context_high->commodity_4h` score `2.0565` n `128` status `ready` deltaP `20.3981` edge `0.0825` maxDD `-0.7687`
- `news_risk_high->index_4h` score `1.8782` n `36` status `ready` deltaP `21.6895` edge `0.0251` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.7478` n `36` status `ready` deltaP `8.5829` edge `0.1203` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.2982` n `32` status `ready` deltaP `13.8099` edge `0.0394` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2982` n `32` status `ready` deltaP `13.8099` edge `0.0394` maxDD `-0.1957`
- `market_context_high->commodity_1h` score `0.6617` n `128` status `ready` deltaP `9.1224` edge `0.024` maxDD `-0.3742`
- `risk_on_high->fx_4h` score `0.5496` n `32` status `ready` deltaP `6.7209` edge `0.0151` maxDD `-0.1285`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
