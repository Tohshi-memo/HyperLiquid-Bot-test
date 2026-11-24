# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-24T20:52:29.997836+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4092`

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

- `market_context_high->unknown_1h` score `32267.7482` n `45` status `ready` deltaP `1.4171` edge `2688.979` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `22053.3253` n `45` status `ready` deltaP `3.1776` edge `1837.7698` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `1032.7933` n `31` status `ready` deltaP `1.6322` edge `86.0728` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `800.3778` n `31` status `ready` deltaP `4.3962` edge `66.6745` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `38.5571` n `31` status `ready` deltaP `50.1736` edge `2.8786` maxDD `0.0`
- `news_risk_high->equity_24h` score `37.0503` n `31` status `ready` deltaP `43.9236` edge `2.7947` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `34.1099` n `31` status `ready` deltaP `48.9583` edge `2.5161` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `11.7535` n `31` status `ready` deltaP `26.6079` edge `0.8891` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.1014` n `31` status `ready` deltaP `41.2355` edge `0.6777` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `10.4056` n `31` status `ready` deltaP `34.6332` edge `0.6843` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.3032` n `31` status `ready` deltaP `17.5403` edge `0.9611` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `5.998` n `31` status `ready` deltaP `50.7393` edge `0.1744` maxDD `-0.0262`
- `news_risk_high->index_24h` score `5.5636` n `31` status `ready` deltaP `41.8403` edge `0.1847` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.5864` n `31` status `ready` deltaP `18.9395` edge `0.1913` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.0671` n `31` status `ready` deltaP `32.9564` edge `0.0619` maxDD `-0.4146`
- `market_context_high->fx_4h` score `2.7379` n `45` status `ready` deltaP `33.2893` edge `0.0347` maxDD `-0.2774`
- `news_risk_high->crypto_major_1h` score `2.7002` n `31` status `ready` deltaP `12.4058` edge `0.3096` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.5596` n `31` status `ready` deltaP `30.3458` edge `0.0195` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.3611` n `31` status `ready` deltaP `12.1064` edge `0.2577` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.6521` n `31` status `ready` deltaP `30.93` edge `0.0335` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
