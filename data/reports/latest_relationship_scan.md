# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-13T03:37:34.959957+00:00`
- Price records: `672`
- Market context records: `3751`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13153`

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

- `risk_on_high->crypto_major_24h` score `28.6686` n `32` status `ready` deltaP `29.6875` edge `2.1954` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `28.6686` n `32` status `ready` deltaP `29.6875` edge `2.1954` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `22.7177` n `32` status `ready` deltaP `34.8958` edge `1.6605` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `22.7177` n `32` status `ready` deltaP `34.8958` edge `1.6605` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `21.2745` n `32` status `ready` deltaP `30.9028` edge `1.582` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `21.2745` n `32` status `ready` deltaP `30.9028` edge `1.582` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.4088` n `32` status `ready` deltaP `31.25` edge `0.7424` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.4088` n `32` status `ready` deltaP `31.25` edge `0.7424` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `9.9707` n `32` status `ready` deltaP `17.9878` edge `0.8232` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `9.9707` n `32` status `ready` deltaP `17.9878` edge `0.8232` maxDD `-5.9781`
- `market_context_high->index_24h` score `5.4328` n `164` status `ready` deltaP `26.9817` edge `0.3868` maxDD `-7.1159`
- `market_context_high->equity_24h` score `5.1547` n `164` status `ready` deltaP `15.9934` edge `0.5977` maxDD `-13.6477`
- `market_context_high->metal_24h` score `4.6131` n `164` status `ready` deltaP `27.6296` edge `0.3434` maxDD `-9.1203`
- `market_context_high->crypto_major_24h` score `3.9011` n `164` status `ready` deltaP `6.593` edge `0.7275` maxDD `-31.0425`
- `market_context_high->crypto_major_4h` score `1.7094` n `168` status `ready` deltaP `8.7616` edge `0.2741` maxDD `-10.5381`
- `risk_on_high->metal_24h` score `1.3106` n `32` status `ready` deltaP `14.0625` edge `0.0416` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `1.3106` n `32` status `ready` deltaP `14.0625` edge `0.0416` maxDD `-0.7574`
- `risk_on_high->equity_4h` score `1.1723` n `32` status `ready` deltaP `6.936` edge `0.2175` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `1.1723` n `32` status `ready` deltaP `6.936` edge `0.2175` maxDD `-5.7426`
- `risk_on_high->crypto_major_1h` score `1.018` n `32` status `ready` deltaP `1.9274` edge `0.2246` maxDD `-5.8885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
