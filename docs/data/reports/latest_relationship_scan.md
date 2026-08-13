# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-13T11:07:29.791342+00:00`
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

- `market_context_high->unknown_24h` score `28.0419` n `161` status `ready` deltaP `-23.6898` edge `2.786` maxDD `-9.6329`
- `news_risk_high->equity_4h` score `7.05` n `36` status `ready` deltaP `37.5` edge `0.3375` maxDD `0.0`
- `risk_on_high->unknown_24h` score `4.4735` n `32` status `ready` deltaP `-42.1875` edge `0.9298` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `4.4735` n `32` status `ready` deltaP `-42.1875` edge `0.9298` maxDD `-1.6689`
- `risk_on_high->commodity_24h` score `3.3368` n `32` status `ready` deltaP `25.0` edge `0.1114` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `3.3368` n `32` status `ready` deltaP `25.0` edge `0.1114` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.4551` n `32` status `ready` deltaP `17.1494` edge `0.1085` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.4551` n `32` status `ready` deltaP `17.1494` edge `0.1085` maxDD `-0.1258`
- `risk_on_high->fx_24h` score `2.0826` n `32` status `ready` deltaP `23.2639` edge `0.0369` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `2.0826` n `32` status `ready` deltaP `23.2639` edge `0.0369` maxDD `-0.1418`
- `news_risk_high->index_4h` score `1.9396` n `36` status `ready` deltaP `22.0528` edge `0.0278` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.6159` n `36` status `ready` deltaP `7.9841` edge `0.1133` maxDD `-0.5496`
- `risk_on_high->crypto_major_24h` score `1.4114` n `32` status `ready` deltaP `12.8472` edge `0.2109` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `1.4114` n `32` status `ready` deltaP `12.8472` edge `0.2109` maxDD `-6.2481`
- `market_context_high->commodity_24h` score `1.3678` n `161` status `ready` deltaP `15.0621` edge `0.0939` maxDD `-2.4263`
- `market_context_high->commodity_4h` score `1.2735` n `161` status `ready` deltaP `14.8008` edge `0.0713` maxDD `-2.1077`
- `risk_on_high->commodity_1h` score `1.1353` n `32` status `ready` deltaP `12.3129` edge `0.0358` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.1353` n `32` status `ready` deltaP `12.3129` edge `0.0358` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `0.9147` n `32` status `ready` deltaP `10.5945` edge `0.0197` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `0.9147` n `32` status `ready` deltaP `10.5945` edge `0.0197` maxDD `-0.1285`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
