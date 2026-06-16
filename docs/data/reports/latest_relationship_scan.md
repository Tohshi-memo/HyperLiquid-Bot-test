# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-16T02:52:40.586422+00:00`
- Price records: `672`
- Market context records: `4051`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10432`

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

- `risk_on_high->unknown_4h` score `144.9135` n `40` status `ready` deltaP `-7.8963` edge `12.3104` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `144.9135` n `40` status `ready` deltaP `-7.8963` edge `12.3104` maxDD `-10.864`
- `market_context_high->unknown_24h` score `41.0437` n `140` status `ready` deltaP `-7.8795` edge `3.8757` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `21.0731` n `159` status `ready` deltaP `0.6414` edge `2.2941` maxDD `-35.7161`
- `risk_on_high->equity_24h` score `3.8286` n `40` status `ready` deltaP `33.6222` edge `0.0949` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `3.8286` n `40` status `ready` deltaP `33.6222` edge `0.0949` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.723` n `40` status `ready` deltaP `38.2012` edge `0.0603` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `3.723` n `40` status `ready` deltaP `38.2012` edge `0.0603` maxDD `-0.0446`
- `market_context_high->index_24h` score `2.163` n `140` status `ready` deltaP `20.6029` edge `0.0641` maxDD `-1.3629`
- `market_context_high->equity_4h` score `1.6549` n `159` status `ready` deltaP `15.544` edge `0.1707` maxDD `-6.9137`
- `risk_on_high->crypto_major_4h` score `1.2536` n `40` status `ready` deltaP `19.9085` edge `0.0383` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.2536` n `40` status `ready` deltaP `19.9085` edge `0.0383` maxDD `-2.6576`
- `market_context_high->equity_1h` score `0.8236` n `171` status `ready` deltaP `6.4354` edge `0.0817` maxDD `-2.144`
- `risk_on_high->equity_1h` score `0.4687` n `40` status `ready` deltaP `11.3623` edge `0.0024` maxDD `-0.7937`
- `risk_on_and_context->equity_1h` score `0.4687` n `40` status `ready` deltaP `11.3623` edge `0.0024` maxDD `-0.7937`
- `risk_on_high->crypto_major_1h` score `0.2084` n `40` status `ready` deltaP `12.6048` edge `-0.0031` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.2084` n `40` status `ready` deltaP `12.6048` edge `-0.0031` maxDD `-2.3372`
- `risk_on_high->metal_4h` score `0.1247` n `40` status `ready` deltaP `10.7927` edge `-0.0224` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.1247` n `40` status `ready` deltaP `10.7927` edge `-0.0224` maxDD `-1.3516`
- `market_context_high->metal_24h` score `0.0541` n `140` status `ready` deltaP `7.3669` edge `0.0541` maxDD `-4.8962`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
