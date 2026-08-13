# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-13T04:52:25.093932+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11840`

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

- `news_risk_high->equity_4h` score `6.867` n `36` status `ready` deltaP `37.0427` edge `0.3253` maxDD `0.0`
- `risk_on_high->commodity_24h` score `2.5715` n `32` status `ready` deltaP `20.8333` edge `0.0754` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `2.5715` n `32` status `ready` deltaP `20.8333` edge `0.0754` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.3217` n `32` status `ready` deltaP `16.0823` edge `0.1045` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.3217` n `32` status `ready` deltaP `16.0823` edge `0.1045` maxDD `-0.1258`
- `news_risk_high->index_4h` score `1.948` n `36` status `ready` deltaP `22.0528` edge `0.0285` maxDD `-0.0546`
- `risk_on_high->fx_24h` score `1.9456` n `32` status `ready` deltaP `21.7014` edge `0.0359` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.9456` n `32` status `ready` deltaP `21.7014` edge `0.0359` maxDD `-0.1418`
- `risk_on_high->crypto_major_24h` score `1.8987` n `32` status `ready` deltaP `15.7986` edge `0.2537` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `1.8987` n `32` status `ready` deltaP `15.7986` edge `0.2537` maxDD `-6.2481`
- `news_risk_high->equity_1h` score `1.5895` n `36` status `ready` deltaP `7.9841` edge `0.1111` maxDD `-0.5496`
- `market_context_high->commodity_4h` score `1.1401` n `161` status `ready` deltaP `13.7337` edge `0.0673` maxDD `-2.1077`
- `risk_on_high->commodity_1h` score `1.1053` n `32` status `ready` deltaP `12.1632` edge `0.0343` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.1053` n `32` status `ready` deltaP `12.1632` edge `0.0343` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `1.0242` n `32` status `ready` deltaP `11.814` edge `0.0207` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `1.0242` n `32` status `ready` deltaP `11.814` edge `0.0207` maxDD `-0.1285`
- `market_context_high->commodity_1h` score `0.8314` n `161` status `ready` deltaP `10.4939` edge `0.029` maxDD `-0.3742`
- `market_context_high->commodity_24h` score `0.6025` n `161` status `ready` deltaP `10.8954` edge `0.0579` maxDD `-2.4263`
- `risk_on_high->index_1h` score `0.2268` n `32` status `ready` deltaP `8.7575` edge `0.0082` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.2268` n `32` status `ready` deltaP `8.7575` edge `0.0082` maxDD `-0.3343`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
