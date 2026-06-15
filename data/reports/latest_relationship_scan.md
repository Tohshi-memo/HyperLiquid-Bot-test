# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T11:52:34.610263+00:00`
- Price records: `672`
- Market context records: `3989`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10092`

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

- `risk_on_high->unknown_4h` score `147.1538` n `40` status `ready` deltaP `-1.6463` edge `12.455` maxDD `-10.8303`
- `risk_on_and_context->unknown_4h` score `147.1538` n `40` status `ready` deltaP `-1.6463` edge `12.455` maxDD `-10.8303`
- `market_context_high->unknown_24h` score `36.1733` n `148` status `ready` deltaP `-6.1655` edge `3.4574` maxDD `-24.1486`
- `market_context_high->unknown_4h` score `21.4651` n `160` status `ready` deltaP `1.4787` edge `2.3198` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `9.3347` n `40` status `ready` deltaP `42.0139` edge `0.4978` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.3347` n `40` status `ready` deltaP `42.0139` edge `0.4978` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.8841` n `40` status `ready` deltaP `37.5915` edge `0.0778` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `3.8841` n `40` status `ready` deltaP `37.5915` edge `0.0778` maxDD `-0.0458`
- `market_context_high->metal_24h` score `3.3924` n `148` status `ready` deltaP `16.4556` edge `0.3245` maxDD `-9.1203`
- `market_context_high->index_24h` score `3.198` n `148` status `ready` deltaP `25.807` edge `0.2084` maxDD `-7.1159`
- `risk_on_high->index_24h` score `2.8077` n `40` status `ready` deltaP `29.8611` edge `0.0349` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.8077` n `40` status `ready` deltaP `29.8611` edge `0.0349` maxDD `0.0`
- `market_context_high->equity_24h` score `2.5807` n `148` status `ready` deltaP `18.3653` edge `0.3956` maxDD `-14.5715`
- `market_context_high->equity_4h` score `2.3085` n `160` status `ready` deltaP `20.0915` edge `0.1887` maxDD `-7.0879`
- `risk_on_high->crypto_major_4h` score `1.9402` n `40` status `ready` deltaP `20.9756` edge `0.0884` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.9402` n `40` status `ready` deltaP `20.9756` edge `0.0884` maxDD `-2.6576`
- `market_context_high->crypto_major_4h` score `1.8001` n `160` status `ready` deltaP `18.4756` edge `0.1835` maxDD `-7.8662`
- `market_context_high->crypto_major_1h` score `1.4685` n `160` status `ready` deltaP `11.9536` edge `0.0969` maxDD `-2.3372`
- `market_context_high->equity_1h` score `0.9797` n `160` status `ready` deltaP `8.8885` edge `0.0788` maxDD `-2.1799`
- `risk_on_high->commodity_24h` score `0.8883` n `40` status `ready` deltaP `4.1667` edge `0.2744` maxDD `-12.9187`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
