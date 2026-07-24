# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T17:07:30.392433+00:00`
- Price records: `672`
- Market context records: `7793`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14661`

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

- `market_context_high->equity_24h` score `7.9038` n `132` status `ready` deltaP `28.5507` edge `0.6025` maxDD `-6.0681`
- `market_context_high->metal_24h` score `1.4933` n `133` status `ready` deltaP `14.0577` edge `0.2398` maxDD `-2.3927`
- `market_context_high->crypto_major_4h` score `1.2132` n `133` status `ready` deltaP `14.8808` edge `0.1737` maxDD `-6.7444`
- `market_context_high->equity_4h` score `1.1773` n `133` status `ready` deltaP `4.1887` edge `0.3143` maxDD `-6.9701`
- `market_context_high->crypto_major_1h` score `1.0813` n `133` status `ready` deltaP `13.3821` edge `0.045` maxDD `-1.5286`
- `market_context_high->crypto_alt_4h` score `0.9749` n `133` status `ready` deltaP `9.1885` edge `0.1317` maxDD `-3.9374`
- `market_context_high->fx_24h` score `0.8117` n `132` status `ready` deltaP `25.2187` edge `0.0447` maxDD `-3.0343`
- `market_context_high->equity_1h` score `0.7179` n `133` status `ready` deltaP `7.9719` edge `0.0926` maxDD `-4.2072`
- `market_context_high->index_1h` score `0.3792` n `133` status `ready` deltaP `8.7171` edge `0.0165` maxDD `-0.7743`
- `market_context_high->commodity_4h` score `0.3787` n `133` status `ready` deltaP `7.7874` edge `0.039` maxDD `-1.0817`
- `market_context_high->crypto_alt_1h` score `0.2513` n `133` status `ready` deltaP `4.799` edge `0.0322` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `0.054` n `133` status `ready` deltaP `5.58` edge `0.0132` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.1156` n `133` status `ready` deltaP `12.1655` edge `0.0499` maxDD `-1.3325`
- `market_context_high->commodity_24h` score `-0.3183` n `132` status `ready` deltaP `12.0791` edge `0.0513` maxDD `-7.0012`
- `market_context_high->fx_1h` score `-0.3285` n `133` status `ready` deltaP `1.6458` edge `0.0004` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.8905` n `133` status `ready` deltaP `1.0396` edge `0.0192` maxDD `-0.6936`
- `market_context_high->fx_4h` score `-1.3382` n `133` status `ready` deltaP `-1.6541` edge `0.0023` maxDD `-1.6936`
- `market_context_high->metal_4h` score `-1.5499` n `133` status `ready` deltaP `0.2998` edge `0.0743` maxDD `-1.4368`
- `market_context_high->index_24h` score `-1.6537` n `132` status `ready` deltaP `-9.4875` edge `0.0615` maxDD `-2.1544`
- `market_context_high->crypto_alt_24h` score `-2.3208` n `133` status `ready` deltaP `14.7431` edge `0.1337` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
