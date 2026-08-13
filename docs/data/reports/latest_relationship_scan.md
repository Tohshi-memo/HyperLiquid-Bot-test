# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-13T09:52:28.270756+00:00`
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

- `market_context_high->unknown_24h` score `16.2519` n `161` status `ready` deltaP `-23.6898` edge `1.8035` maxDD `-9.6329`
- `news_risk_high->equity_4h` score `7.0586` n `36` status `ready` deltaP `37.6524` edge `0.3372` maxDD `0.0`
- `risk_on_high->commodity_24h` score `3.157` n `32` status `ready` deltaP `24.1319` edge `0.1022` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `3.157` n `32` status `ready` deltaP `24.1319` edge `0.1022` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.3533` n `32` status `ready` deltaP `16.3872` edge `0.1051` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.3533` n `32` status `ready` deltaP `16.3872` edge `0.1051` maxDD `-0.1258`
- `risk_on_high->fx_24h` score `2.085` n `32` status `ready` deltaP `23.2639` edge `0.0371` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `2.085` n `32` status `ready` deltaP `23.2639` edge `0.0371` maxDD `-0.1418`
- `news_risk_high->index_4h` score `1.9554` n `36` status `ready` deltaP `22.2053` edge `0.0281` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.641` n `36` status `ready` deltaP `8.2835` edge `0.1134` maxDD `-0.5496`
- `risk_on_high->crypto_major_24h` score `1.4426` n `32` status `ready` deltaP `12.8472` edge `0.2149` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `1.4426` n `32` status `ready` deltaP `12.8472` edge `0.2149` maxDD `-6.2481`
- `market_context_high->commodity_24h` score `1.188` n `161` status `ready` deltaP `14.194` edge `0.0847` maxDD `-2.4263`
- `market_context_high->commodity_4h` score `1.1717` n `161` status `ready` deltaP `14.0386` edge `0.0679` maxDD `-2.1077`
- `risk_on_high->commodity_1h` score `1.1221` n `32` status `ready` deltaP `12.1632` edge `0.0357` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.1221` n `32` status `ready` deltaP `12.1632` edge `0.0357` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `0.8965` n `32` status `ready` deltaP `10.4421` edge `0.0192` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `0.8965` n `32` status `ready` deltaP `10.4421` edge `0.0192` maxDD `-0.1285`
- `market_context_high->commodity_1h` score `0.8482` n `161` status `ready` deltaP `10.4939` edge `0.0304` maxDD `-0.3742`
- `risk_on_high->index_1h` score `0.2462` n `32` status `ready` deltaP `9.2066` edge `0.0077` maxDD `-0.3343`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
