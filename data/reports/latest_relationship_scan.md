# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T06:07:26.647938+00:00`
- Price records: `672`
- Market context records: `5117`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5560`

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

- `market_context_high->unknown_24h` score `24.1058` n `70` status `ready` deltaP `28.6756` edge `1.8519` maxDD `-1.4072`
- `market_context_high->unknown_1h` score `8.2593` n `126` status `ready` deltaP `6.6938` edge `0.7078` maxDD `-2.7986`
- `market_context_high->unknown_4h` score `7.3944` n `114` status `ready` deltaP `19.7582` edge `0.5867` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `5.4011` n `114` status `ready` deltaP `15.5568` edge `0.5063` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.8526` n `114` status `ready` deltaP `13.2301` edge `0.4621` maxDD `-14.0065`
- `market_context_high->crypto_alt_1h` score `0.8264` n `126` status `ready` deltaP `6.5583` edge `0.1213` maxDD `-5.0257`
- `market_context_high->equity_1h` score `0.404` n `126` status `ready` deltaP `7.5468` edge `0.0608` maxDD `-2.745`
- `market_context_high->crypto_major_1h` score `0.3975` n `126` status `ready` deltaP `7.4708` edge `0.1257` maxDD `-6.9639`
- `market_context_high->equity_4h` score `0.1222` n `114` status `ready` deltaP `6.2153` edge `0.1381` maxDD `-7.4425`
- `market_context_high->metal_1h` score `0.105` n `126` status `ready` deltaP `6.7223` edge `0.0201` maxDD `-1.4501`
- `market_context_high->index_1h` score `-0.0221` n `126` status `ready` deltaP `5.0613` edge `0.0138` maxDD `-1.0296`
- `market_context_high->commodity_24h` score `-0.182` n `70` status `ready` deltaP `14.0476` edge `0.0814` maxDD `-10.2036`
- `market_context_high->index_4h` score `-0.5232` n `114` status `ready` deltaP `3.0086` edge `0.0246` maxDD `-2.9391`
- `market_context_high->metal_4h` score `-0.5632` n `114` status `ready` deltaP `1.9389` edge `0.0559` maxDD `-4.6157`
- `market_context_high->fx_1h` score `-0.6744` n `126` status `ready` deltaP `-3.1152` edge `-0.0016` maxDD `-0.7944`
- `market_context_high->commodity_1h` score `-0.9509` n `126` status `ready` deltaP `0.0594` edge `-0.0027` maxDD `-2.155`
- `market_context_high->fx_4h` score `-1.0667` n `114` status `ready` deltaP `-4.5384` edge `0.0008` maxDD `-1.9169`
- `market_context_high->fx_24h` score `-1.4102` n `70` status `ready` deltaP `-1.8154` edge `-0.008` maxDD `-1.4601`
- `market_context_high->commodity_4h` score `-2.4846` n `114` status `ready` deltaP `-0.6552` edge `-0.0301` maxDD `-7.4732`
- `market_context_high->metal_24h` score `-2.7948` n `70` status `ready` deltaP `-2.8671` edge `0.0664` maxDD `-24.7811`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
