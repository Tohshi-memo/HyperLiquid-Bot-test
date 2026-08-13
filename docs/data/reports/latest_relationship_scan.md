# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-13T14:52:31.049528+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11712`

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

- `market_context_high->unknown_24h` score `62.7759` n `161` status `ready` deltaP `-23.6898` edge `5.6805` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `27.0506` n `32` status `ready` deltaP `-42.1875` edge `3.8243` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `27.0506` n `32` status `ready` deltaP `-42.1875` edge `3.8243` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `9.1033` n `35` status `ready` deltaP `9.5932` edge `0.7326` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `6.6579` n `36` status `ready` deltaP `35.8232` edge `0.316` maxDD `0.0`
- `risk_on_high->commodity_24h` score `3.8763` n `32` status `ready` deltaP `27.6042` edge `0.139` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `3.8763` n `32` status `ready` deltaP `27.6042` edge `0.139` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.6796` n `32` status `ready` deltaP `19.1311` edge `0.114` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.6796` n `32` status `ready` deltaP `19.1311` edge `0.114` maxDD `-0.1258`
- `news_risk_high->index_24h` score `2.5316` n `35` status `ready` deltaP `15.625` edge `0.1068` maxDD `0.0`
- `risk_on_high->fx_24h` score `1.9825` n `32` status `ready` deltaP `22.2222` edge `0.0355` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.9825` n `32` status `ready` deltaP `22.2222` edge `0.0355` maxDD `-0.1418`
- `market_context_high->commodity_24h` score `1.9074` n `161` status `ready` deltaP `17.6663` edge `0.1215` maxDD `-2.4263`
- `news_risk_high->index_4h` score `1.7233` n `36` status `ready` deltaP `19.9187` edge `0.024` maxDD `-0.0546`
- `market_context_high->commodity_4h` score `1.498` n `161` status `ready` deltaP `16.7825` edge `0.0768` maxDD `-2.1077`
- `news_risk_high->equity_1h` score `1.3857` n `36` status `ready` deltaP `6.9362` edge `0.1011` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.2299` n `32` status `ready` deltaP `13.2111` edge `0.0377` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2299` n `32` status `ready` deltaP `13.2111` edge `0.0377` maxDD `-0.1957`
- `risk_on_high->crypto_major_24h` score `1.1833` n `32` status `ready` deltaP `11.8056` edge `0.1886` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `1.1833` n `32` status `ready` deltaP `11.8056` edge `0.1886` maxDD `-6.2481`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
