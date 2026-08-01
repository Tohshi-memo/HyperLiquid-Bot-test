# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T03:07:29.893635+00:00`
- Price records: `672`
- Market context records: `8579`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5919`

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

- `news_risk_high->unknown_24h` score `4751.0051` n `64` status `ready` deltaP `38.0208` edge `395.7057` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.9826` n `64` status `ready` deltaP `22.0274` edge `0.4114` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.1786` n `64` status `ready` deltaP `18.3308` edge `0.0784` maxDD `-0.191`
- `market_context_high->crypto_alt_4h` score `1.8098` n `62` status `ready` deltaP `12.9032` edge `0.1605` maxDD `-5.323`
- `news_risk_high->equity_1h` score `1.7816` n `64` status `ready` deltaP `16.701` edge `0.0848` maxDD `-2.4803`
- `news_risk_high->crypto_major_4h` score `1.0784` n `64` status `ready` deltaP `7.2027` edge `0.1678` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.5854` n `64` status `ready` deltaP `12.5` edge `0.1309` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.4368` n `64` status `ready` deltaP `8.1119` edge `0.0546` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3625` n `64` status `ready` deltaP `7.064` edge `0.0506` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.0893` n `64` status `ready` deltaP `5.2863` edge `0.0043` maxDD `-0.2475`
- `news_risk_high->fx_4h` score `0.0594` n `64` status `ready` deltaP `11.7759` edge `0.0222` maxDD `-0.6604`
- `news_risk_high->index_1h` score `0.0169` n `64` status `ready` deltaP `3.7706` edge `0.0087` maxDD `-0.5338`
- `news_risk_high->metal_4h` score `-0.0341` n `64` status `ready` deltaP `1.7149` edge `0.0318` maxDD `-0.8085`
- `market_context_high->fx_4h` score `-0.1088` n `62` status `ready` deltaP `8.6005` edge `0.0132` maxDD `-1.3685`
- `news_risk_high->metal_1h` score `-0.1455` n `64` status `ready` deltaP `3.1063` edge `0.0075` maxDD `-0.5599`
- `market_context_high->fx_1h` score `-0.2755` n `62` status `ready` deltaP `2.2117` edge `0.0002` maxDD `-0.6874`
- `market_context_high->commodity_1h` score `-0.3309` n `62` status `ready` deltaP `3.8584` edge `-0.0056` maxDD `-2.0038`
- `market_context_high->crypto_alt_1h` score `-0.54` n `62` status `ready` deltaP `-2.9264` edge `0.013` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.7573` n `62` status `ready` deltaP `0.7968` edge `-0.0155` maxDD `-1.5667`
- `market_context_high->metal_1h` score `-0.9865` n `62` status `ready` deltaP `-3.1437` edge `-0.0118` maxDD `-1.6224`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
