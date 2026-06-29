# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T10:52:31.547751+00:00`
- Price records: `672`
- Market context records: `5137`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5588`

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

- `market_context_high->unknown_24h` score `28.3464` n `64` status `ready` deltaP `29.5139` edge `2.1997` maxDD `-1.4072`
- `market_context_high->unknown_4h` score `7.2838` n `121` status `ready` deltaP `20.5049` edge `0.5725` maxDD `-5.5109`
- `market_context_high->unknown_1h` score `7.1922` n `133` status `ready` deltaP `9.8544` edge `0.5978` maxDD `-2.7986`
- `market_context_high->crypto_alt_4h` score `5.0537` n `121` status `ready` deltaP `15.1443` edge `0.4801` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.623` n `121` status `ready` deltaP `12.9699` edge `0.4447` maxDD `-14.0065`
- `market_context_high->commodity_24h` score `1.4398` n `64` status `ready` deltaP `19.2708` edge `0.1461` maxDD `-4.1987`
- `market_context_high->crypto_alt_1h` score `0.8854` n `133` status `ready` deltaP `6.3808` edge `0.1274` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.8668` n `133` status `ready` deltaP `8.7727` edge `0.1383` maxDD `-6.9639`
- `market_context_high->equity_4h` score `0.8176` n `121` status `ready` deltaP `8.5492` edge `0.175` maxDD `-7.4425`
- `market_context_high->equity_1h` score `0.7173` n `133` status `ready` deltaP `7.888` edge `0.0665` maxDD `-2.745`
- `market_context_high->index_1h` score `0.0108` n `133` status `ready` deltaP `5.486` edge `0.0147` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.0994` n `133` status `ready` deltaP `4.4145` edge `0.0144` maxDD `-1.8592`
- `market_context_high->metal_24h` score `-0.1065` n `64` status `ready` deltaP `0.3472` edge `0.1898` maxDD `-11.4122`
- `market_context_high->index_4h` score `-0.421` n `121` status `ready` deltaP `6.0534` edge `0.0363` maxDD `-2.9391`
- `market_context_high->crypto_alt_24h` score `-0.4568` n `64` status `ready` deltaP `16.1458` edge `0.5351` maxDD `-50.438`
- `market_context_high->commodity_1h` score `-0.5543` n `133` status `ready` deltaP `0.9714` edge `-0.0006` maxDD `-2.155`
- `market_context_high->fx_1h` score `-0.6331` n `133` status `ready` deltaP `-2.3356` edge `-0.0015` maxDD `-0.7944`
- `market_context_high->metal_4h` score `-0.636` n `121` status `ready` deltaP `2.0334` edge `0.0492` maxDD `-4.8772`
- `market_context_high->fx_4h` score `-0.9888` n `121` status `ready` deltaP `-2.9807` edge `0.0004` maxDD `-1.9169`
- `market_context_high->fx_24h` score `-1.0539` n `64` status `ready` deltaP `1.2153` edge `-0.0044` maxDD `-0.9885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
