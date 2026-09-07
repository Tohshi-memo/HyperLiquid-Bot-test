# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-07T20:07:28.868024+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10171`

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

- `risk_on_high->crypto_major_24h` score `13.1321` n `109` status `ready` deltaP `26.3698` edge `1.174` maxDD `-15.1034`
- `risk_on_and_context->crypto_major_24h` score `13.1321` n `109` status `ready` deltaP `26.3698` edge `1.174` maxDD `-15.1034`
- `risk_on_high->crypto_alt_24h` score `11.5711` n `109` status `ready` deltaP `29.0679` edge `0.7766` maxDD `-0.1572`
- `risk_on_and_context->crypto_alt_24h` score `11.5711` n `109` status `ready` deltaP `29.0679` edge `0.7766` maxDD `-0.1572`
- `market_context_high->crypto_alt_24h` score `6.6762` n `224` status `ready` deltaP `22.8671` edge `0.4614` maxDD `-2.5998`
- `risk_on_high->crypto_alt_4h` score `5.7536` n `117` status `ready` deltaP `30.635` edge `0.3124` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.7536` n `117` status `ready` deltaP `30.635` edge `0.3124` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `4.9595` n `117` status `ready` deltaP `26.4384` edge `0.3229` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.9595` n `117` status `ready` deltaP `26.4384` edge `0.3229` maxDD `-3.8693`
- `market_context_high->equity_24h` score `3.5427` n `224` status `ready` deltaP `14.5833` edge `0.198` maxDD `0.0`
- `risk_on_high->equity_24h` score `2.7699` n `109` status `ready` deltaP `14.5833` edge `0.1336` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `2.7699` n `109` status `ready` deltaP `14.5833` edge `0.1336` maxDD `0.0`
- `risk_on_high->index_24h` score `1.8124` n `109` status `ready` deltaP `16.3449` edge `0.0463` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `1.8124` n `109` status `ready` deltaP `16.3449` edge `0.0463` maxDD `-0.0051`
- `market_context_high->index_24h` score `1.0751` n `224` status `ready` deltaP `11.0615` edge `0.0552` maxDD `-0.1483`
- `risk_on_high->crypto_alt_1h` score `0.9633` n `117` status `ready` deltaP `4.3964` edge `0.0862` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.9633` n `117` status `ready` deltaP `4.3964` edge `0.0862` maxDD `-1.1521`
- `risk_on_high->equity_1h` score `0.5229` n `117` status `ready` deltaP `14.3726` edge `0.0009` maxDD `-2.2516`
- `risk_on_and_context->equity_1h` score `0.5229` n `117` status `ready` deltaP `14.3726` edge `0.0009` maxDD `-2.2516`
- `risk_on_high->metal_1h` score `0.3914` n `117` status `ready` deltaP `11.7752` edge `0.0047` maxDD `-0.3081`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
