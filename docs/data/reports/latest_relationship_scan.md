# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-13T10:22:26.804007+00:00`
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

- `market_context_high->unknown_24h` score `20.9703` n `161` status `ready` deltaP `-23.6898` edge `2.1967` maxDD `-9.6329`
- `news_risk_high->equity_4h` score `7.0658` n `36` status `ready` deltaP `37.6524` edge `0.3378` maxDD `0.0`
- `risk_on_high->commodity_24h` score `3.2219` n `32` status `ready` deltaP `24.4792` edge `0.1053` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `3.2219` n `32` status `ready` deltaP `24.4792` edge `0.1053` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.3921` n `32` status `ready` deltaP `16.6921` edge `0.1063` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.3921` n `32` status `ready` deltaP `16.6921` edge `0.1063` maxDD `-0.1258`
- `risk_on_high->fx_24h` score `2.0838` n `32` status `ready` deltaP `23.2639` edge `0.037` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `2.0838` n `32` status `ready` deltaP `23.2639` edge `0.037` maxDD `-0.1418`
- `news_risk_high->index_4h` score `1.9542` n `36` status `ready` deltaP `22.2053` edge `0.028` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.641` n `36` status `ready` deltaP `8.2835` edge `0.1134` maxDD `-0.5496`
- `risk_on_high->crypto_major_24h` score `1.4348` n `32` status `ready` deltaP `12.8472` edge `0.2139` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `1.4348` n `32` status `ready` deltaP `12.8472` edge `0.2139` maxDD `-6.2481`
- `market_context_high->commodity_24h` score `1.253` n `161` status `ready` deltaP `14.5413` edge `0.0878` maxDD `-2.4263`
- `market_context_high->commodity_4h` score `1.2105` n `161` status `ready` deltaP `14.3435` edge `0.0691` maxDD `-2.1077`
- `risk_on_high->commodity_1h` score `1.0945` n `32` status `ready` deltaP `11.8638` edge `0.0354` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.0945` n `32` status `ready` deltaP `11.8638` edge `0.0354` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `0.8977` n `32` status `ready` deltaP `10.4421` edge `0.0193` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `0.8977` n `32` status `ready` deltaP `10.4421` edge `0.0193` maxDD `-0.1285`
- `market_context_high->commodity_1h` score `0.8206` n `161` status `ready` deltaP `10.1945` edge `0.0301` maxDD `-0.3742`
- `risk_on_high->index_1h` score `0.2462` n `32` status `ready` deltaP `9.2066` edge `0.0077` maxDD `-0.3343`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
