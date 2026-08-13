# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-13T15:22:26.391962+00:00`
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

- `market_context_high->unknown_24h` score `67.3851` n `161` status `ready` deltaP `-23.6898` edge `6.0646` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `30.0466` n `32` status `ready` deltaP `-42.1875` edge `4.2084` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `30.0466` n `32` status `ready` deltaP `-42.1875` edge `4.2084` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `9.2902` n `36` status `ready` deltaP `10.0694` edge `0.745` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `6.5495` n `36` status `ready` deltaP `35.5183` edge `0.309` maxDD `0.0`
- `risk_on_high->commodity_24h` score `3.9413` n `32` status `ready` deltaP `27.9514` edge `0.1421` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `3.9413` n `32` status `ready` deltaP `27.9514` edge `0.1421` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.688` n `32` status `ready` deltaP `19.1311` edge `0.1147` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.688` n `32` status `ready` deltaP `19.1311` edge `0.1147` maxDD `-0.1258`
- `news_risk_high->index_24h` score `2.5676` n `36` status `ready` deltaP `15.625` edge `0.1098` maxDD `0.0`
- `market_context_high->commodity_24h` score `1.9723` n `161` status `ready` deltaP `18.0135` edge `0.1246` maxDD `-2.4263`
- `risk_on_high->fx_24h` score `1.9511` n `32` status `ready` deltaP `21.875` edge `0.0352` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.9511` n `32` status `ready` deltaP `21.875` edge `0.0352` maxDD `-0.1418`
- `news_risk_high->index_4h` score `1.6845` n `36` status `ready` deltaP `19.6138` edge `0.0228` maxDD `-0.0546`
- `market_context_high->commodity_4h` score `1.5064` n `161` status `ready` deltaP `16.7825` edge `0.0775` maxDD `-2.1077`
- `news_risk_high->equity_1h` score `1.3677` n `36` status `ready` deltaP `6.7865` edge `0.1006` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.2084` n `32` status `ready` deltaP `13.0614` edge `0.0369` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2084` n `32` status `ready` deltaP `13.0614` edge `0.0369` maxDD `-0.1957`
- `risk_on_high->crypto_major_24h` score `1.1325` n `32` status `ready` deltaP `11.4583` edge `0.1844` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `1.1325` n `32` status `ready` deltaP `11.4583` edge `0.1844` maxDD `-6.2481`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
