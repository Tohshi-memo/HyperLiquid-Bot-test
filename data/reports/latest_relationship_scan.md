# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-16T09:07:34.532985+00:00`
- Price records: `672`
- Market context records: `4077`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10224`

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

- `risk_on_high->unknown_4h` score `144.8033` n `40` status `ready` deltaP `-7.7439` edge `12.3002` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `144.8033` n `40` status `ready` deltaP `-7.7439` edge `12.3002` maxDD `-10.864`
- `market_context_high->unknown_1h` score `51.0944` n `172` status `ready` deltaP `1.88` edge `4.4031` maxDD `-9.6211`
- `market_context_high->unknown_24h` score `37.0932` n `144` status `ready` deltaP `-9.0663` edge `3.5544` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `16.8376` n `172` status `ready` deltaP `-1.8718` edge `1.9579` maxDD `-35.7161`
- `risk_on_high->equity_4h` score `3.6806` n `40` status `ready` deltaP `37.8963` edge `0.0588` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `3.6806` n `40` status `ready` deltaP `37.8963` edge `0.0588` maxDD `-0.0446`
- `market_context_high->equity_4h` score `1.3053` n `172` status `ready` deltaP `14.8149` edge `0.1631` maxDD `-6.9137`
- `market_context_high->index_24h` score `1.1968` n `144` status `ready` deltaP `16.9844` edge `-0.0135` maxDD `0.0`
- `risk_on_high->equity_24h` score `1.0088` n `40` status `ready` deltaP `29.2894` edge `-0.1112` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.0088` n `40` status `ready` deltaP `29.2894` edge `-0.1112` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `0.7909` n `40` status `ready` deltaP `18.3841` edge `0.0099` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.7909` n `40` status `ready` deltaP `18.3841` edge `0.0099` maxDD `-2.6576`
- `market_context_high->equity_1h` score `0.7298` n `172` status `ready` deltaP `5.6225` edge `0.0793` maxDD `-2.144`
- `risk_on_high->equity_1h` score `0.434` n `40` status `ready` deltaP `10.9132` edge `0.0025` maxDD `-0.7937`
- `risk_on_and_context->equity_1h` score `0.434` n `40` status `ready` deltaP `10.9132` edge `0.0025` maxDD `-0.7937`
- `risk_on_high->metal_4h` score `0.216` n `40` status `ready` deltaP `11.7073` edge `-0.0168` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.216` n `40` status `ready` deltaP `11.7073` edge `-0.0168` maxDD `-1.3516`
- `risk_on_high->fx_4h` score `0.1872` n `40` status `ready` deltaP `11.9207` edge `0.0036` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.1872` n `40` status `ready` deltaP `11.9207` edge `0.0036` maxDD `-0.3925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
