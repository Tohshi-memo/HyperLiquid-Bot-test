# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T18:52:33.190601+00:00`
- Price records: `672`
- Market context records: `8541`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5925`

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

- `news_risk_high->unknown_24h` score `5835.0872` n `55` status `ready` deltaP `42.7273` edge `486.0145` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.6446` n `64` status `ready` deltaP `20.503` edge `0.3934` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.9609` n `64` status `ready` deltaP `16.0442` edge `0.0755` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.6138` n `64` status `ready` deltaP `15.5034` edge `0.0788` maxDD `-2.4803`
- `market_context_high->crypto_alt_4h` score `1.5874` n `56` status `ready` deltaP `10.453` edge `0.1583` maxDD `-5.323`
- `news_risk_high->crypto_major_4h` score `0.9912` n `64` status `ready` deltaP `6.4405` edge `0.1617` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.7193` n `64` status `ready` deltaP `14.0244` edge `0.1379` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.45` n `64` status `ready` deltaP `8.1119` edge `0.0563` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3298` n `64` status `ready` deltaP `6.6149` edge `0.0494` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.0776` n `64` status `ready` deltaP `5.1366` edge `0.0038` maxDD `-0.2475`
- `news_risk_high->index_1h` score `-0.0127` n `64` status `ready` deltaP `3.3215` edge `0.0079` maxDD `-0.5338`
- `news_risk_high->metal_4h` score `-0.0254` n `64` status `ready` deltaP `1.8674` edge `0.0319` maxDD `-0.8085`
- `news_risk_high->fx_4h` score `-0.0647` n `64` status `ready` deltaP `10.404` edge `0.021` maxDD `-0.6604`
- `news_risk_high->metal_1h` score `-0.1754` n `64` status `ready` deltaP `2.8069` edge `0.007` maxDD `-0.5599`
- `market_context_high->fx_1h` score `-0.2871` n `62` status `ready` deltaP `2.062` edge `-0.0003` maxDD `-0.6874`
- `market_context_high->commodity_1h` score `-0.3176` n `62` status `ready` deltaP `3.7087` edge `-0.0029` maxDD `-2.0038`
- `market_context_high->crypto_alt_1h` score `-0.5267` n `62` status `ready` deltaP `-2.9264` edge `0.0147` maxDD `-3.0178`
- `market_context_high->fx_4h` score `-0.7786` n `56` status `ready` deltaP `1.6986` edge `0.0034` maxDD `-1.3685`
- `market_context_high->index_1h` score `-0.8028` n `62` status `ready` deltaP `0.3477` edge `-0.0163` maxDD `-1.5667`
- `market_context_high->metal_1h` score `-1.0164` n `62` status `ready` deltaP `-3.4431` edge `-0.0123` maxDD `-1.6224`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
