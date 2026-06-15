# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T14:22:45.433706+00:00`
- Price records: `672`
- Market context records: `3999`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10252`

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

- `risk_on_high->unknown_4h` score `146.9076` n `40` status `ready` deltaP `-2.7134` edge `12.4416` maxDD `-10.8303`
- `risk_on_and_context->unknown_4h` score `146.9076` n `40` status `ready` deltaP `-2.7134` edge `12.4416` maxDD `-10.8303`
- `market_context_high->unknown_24h` score `45.7583` n `138` status `ready` deltaP `-3.593` edge `4.239` maxDD `-24.1486`
- `market_context_high->unknown_4h` score `25.1455` n `150` status `ready` deltaP `2.4533` edge `2.62` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `9.1967` n `40` status `ready` deltaP `42.0139` edge `0.4863` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.1967` n `40` status `ready` deltaP `42.0139` edge `0.4863` maxDD `0.0`
- `risk_on_high->equity_4h` score `4.036` n `40` status `ready` deltaP `38.2012` edge `0.0864` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `4.036` n `40` status `ready` deltaP `38.2012` edge `0.0864` maxDD `-0.0458`
- `market_context_high->index_24h` score `2.9681` n `138` status `ready` deltaP `25.5133` edge `0.1912` maxDD `-7.1159`
- `market_context_high->metal_24h` score `2.8425` n `138` status `ready` deltaP `14.7419` edge `0.2901` maxDD `-9.1203`
- `risk_on_high->index_24h` score `2.7033` n `40` status `ready` deltaP `29.8611` edge `0.0262` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.7033` n `40` status `ready` deltaP `29.8611` edge `0.0262` maxDD `0.0`
- `market_context_high->equity_4h` score `2.082` n `150` status `ready` deltaP `20.0345` edge `0.1702` maxDD `-7.0879`
- `market_context_high->equity_24h` score `1.8088` n `138` status `ready` deltaP `16.6516` edge `0.3427` maxDD `-14.5715`
- `risk_on_high->crypto_major_4h` score `1.6122` n `40` status `ready` deltaP `20.6707` edge `0.0631` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.6122` n `40` status `ready` deltaP `20.6707` edge `0.0631` maxDD `-2.6576`
- `market_context_high->metal_1h` score `1.2421` n `150` status `ready` deltaP `12.7485` edge `0.066` maxDD `-1.7983`
- `market_context_high->crypto_major_1h` score `1.149` n `150` status `ready` deltaP `10.8703` edge `0.0775` maxDD `-2.3372`
- `market_context_high->crypto_major_4h` score `1.1092` n `150` status `ready` deltaP `17.504` edge `0.1324` maxDD `-7.8662`
- `risk_on_high->commodity_24h` score `1.0395` n `40` status `ready` deltaP `4.1667` edge `0.287` maxDD `-12.9187`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
