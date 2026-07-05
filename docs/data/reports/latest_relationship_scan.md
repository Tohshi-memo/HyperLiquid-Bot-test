# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T18:52:27.329690+00:00`
- Price records: `672`
- Market context records: `5801`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9058`

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

- `market_context_high->equity_24h` score `0.4553` n `248` status `ready` deltaP `15.3954` edge `0.4432` maxDD `-31.6316`
- `market_context_high->equity_4h` score `-0.0788` n `298` status `ready` deltaP `5.985` edge `0.1174` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2323` n `298` status `ready` deltaP `2.6484` edge `0.0011` maxDD `-0.5499`
- `market_context_high->equity_1h` score `-0.6159` n `298` status `ready` deltaP `3.3256` edge `0.0272` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.6277` n `298` status `ready` deltaP `2.4163` edge `-0.0009` maxDD `-2.0682`
- `market_context_high->index_1h` score `-0.6278` n `298` status `ready` deltaP `0.3979` edge `0.0037` maxDD `-0.9472`
- `market_context_high->commodity_1h` score `-0.7859` n `298` status `ready` deltaP `-2.2304` edge `-0.0054` maxDD `-3.7721`
- `market_context_high->crypto_major_1h` score `-0.9098` n `298` status `ready` deltaP `3.2372` edge `0.0347` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-1.1132` n `298` status `ready` deltaP `1.4819` edge `0.0308` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.222` n `298` status `ready` deltaP `0.3386` edge `0.0098` maxDD `-3.165`
- `market_context_high->fx_24h` score `-1.2326` n `248` status `ready` deltaP `12.1976` edge `0.0356` maxDD `-4.9958`
- `market_context_high->fx_4h` score `-1.4478` n `298` status `ready` deltaP `0.8246` edge `0.0038` maxDD `-2.2593`
- `market_context_high->commodity_4h` score `-2.2078` n `298` status `ready` deltaP `-2.8432` edge `-0.0235` maxDD `-11.9144`
- `market_context_high->metal_4h` score `-2.4162` n `298` status `ready` deltaP `-4.9998` edge `-0.0467` maxDD `-11.0457`
- `market_context_high->index_24h` score `-2.7995` n `248` status `ready` deltaP `3.7131` edge `0.0308` maxDD `-18.1572`
- `market_context_high->crypto_major_4h` score `-2.8674` n `298` status `ready` deltaP `7.8133` edge `0.1462` maxDD `-25.6458`
- `market_context_high->crypto_alt_4h` score `-4.4906` n `298` status `ready` deltaP `5.5554` edge `0.0896` maxDD `-28.7346`
- `market_context_high->metal_24h` score `-6.4152` n `248` status `ready` deltaP `-6.3732` edge `-0.2461` maxDD `-24.0436`
- `market_context_high->crypto_major_24h` score `-9.4837` n `248` status `ready` deltaP `-0.6161` edge `-0.1991` maxDD `-31.635`
- `market_context_high->commodity_24h` score `-10.1787` n `248` status `ready` deltaP `-13.8385` edge `-0.0765` maxDD `-37.024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
