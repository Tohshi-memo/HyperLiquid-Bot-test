# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T08:37:28.957408+00:00`
- Price records: `672`
- Market context records: `3975`
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

- `risk_on_high->unknown_4h` score `147.9687` n `40` status `ready` deltaP `0.3354` edge `12.5097` maxDD `-10.8303`
- `risk_on_and_context->unknown_4h` score `147.9687` n `40` status `ready` deltaP `0.3354` edge `12.5097` maxDD `-10.8303`
- `market_context_high->unknown_24h` score `29.7994` n `153` status `ready` deltaP `-6.5054` edge `3.1009` maxDD `-37.9399`
- `market_context_high->unknown_4h` score `19.5151` n `166` status `ready` deltaP `1.2691` edge `2.1587` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `9.1811` n `40` status `ready` deltaP `42.0139` edge `0.485` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `9.1811` n `40` status `ready` deltaP `42.0139` edge `0.485` maxDD `0.0`
- `market_context_high->metal_24h` score `3.8274` n `153` status `ready` deltaP `17.2284` edge `0.3556` maxDD `-9.1203`
- `risk_on_high->equity_4h` score `3.5875` n `40` status `ready` deltaP `37.439` edge `0.0541` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `3.5875` n `40` status `ready` deltaP `37.439` edge `0.0541` maxDD `-0.0458`
- `market_context_high->index_24h` score `3.4162` n `153` status `ready` deltaP `25.9395` edge `0.2257` maxDD `-7.1159`
- `market_context_high->equity_24h` score `3.0781` n `153` status `ready` deltaP `19.1381` edge `0.4319` maxDD `-14.5715`
- `risk_on_high->index_24h` score `2.7657` n `40` status `ready` deltaP `29.8611` edge `0.0314` maxDD `0.0`
- `risk_on_and_context->index_24h` score `2.7657` n `40` status `ready` deltaP `29.8611` edge `0.0314` maxDD `0.0`
- `market_context_high->equity_4h` score `2.4646` n `166` status `ready` deltaP `20.6619` edge `0.1979` maxDD `-7.0879`
- `market_context_high->crypto_major_4h` score `2.1699` n `166` status `ready` deltaP `19.4075` edge `0.2081` maxDD `-7.8662`
- `risk_on_high->crypto_major_4h` score `1.7864` n `40` status `ready` deltaP `20.8232` edge `0.0766` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.7864` n `40` status `ready` deltaP `20.8232` edge `0.0766` maxDD `-2.6576`
- `market_context_high->crypto_major_1h` score `1.6029` n `166` status `ready` deltaP `12.5081` edge `0.1044` maxDD `-2.3372`
- `market_context_high->equity_1h` score `1.1452` n `166` status `ready` deltaP `9.6819` edge `0.0873` maxDD `-2.1799`
- `market_context_high->metal_1h` score `1.0438` n `166` status `ready` deltaP `12.3404` edge `0.0641` maxDD `-2.751`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
