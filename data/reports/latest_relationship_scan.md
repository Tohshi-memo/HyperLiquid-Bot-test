# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T09:22:30.406956+00:00`
- Price records: `672`
- Market context records: `5130`
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

- `market_context_high->unknown_24h` score `30.7914` n `61` status `ready` deltaP `28.7255` edge `2.4087` maxDD `-1.4072`
- `market_context_high->unknown_1h` score `8.6416` n `127` status `ready` deltaP `9.4323` edge `0.7214` maxDD `-2.7986`
- `market_context_high->unknown_4h` score `7.3512` n `118` status `ready` deltaP `19.8326` edge `0.5826` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `4.885` n `118` status `ready` deltaP `14.1148` edge `0.4729` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.4216` n `118` status `ready` deltaP `11.8773` edge `0.4352` maxDD `-14.0065`
- `market_context_high->commodity_24h` score `1.7989` n `61` status `ready` deltaP `22.2677` edge `0.168` maxDD `-4.1987`
- `market_context_high->equity_4h` score `0.6837` n `118` status `ready` deltaP `7.7615` edge `0.1691` maxDD `-7.4425`
- `market_context_high->equity_1h` score `0.6401` n `127` status `ready` deltaP `7.1031` edge `0.0653` maxDD `-2.745`
- `market_context_high->crypto_alt_1h` score `0.6317` n `127` status `ready` deltaP `4.214` edge `0.1207` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.5622` n `127` status `ready` deltaP `6.5703` edge `0.1276` maxDD `-6.9639`
- `market_context_high->metal_24h` score `0.4023` n `61` status `ready` deltaP `2.1915` edge `0.2199` maxDD `-11.4122`
- `market_context_high->metal_1h` score `0.0636` n `127` status `ready` deltaP `5.8218` edge `0.0208` maxDD `-1.4501`
- `market_context_high->index_1h` score `-0.0576` n `127` status `ready` deltaP `4.6301` edge `0.0147` maxDD `-1.0296`
- `market_context_high->crypto_alt_24h` score `-0.4502` n `61` status `ready` deltaP `14.3244` edge `0.5481` maxDD `-50.438`
- `market_context_high->index_4h` score `-0.5422` n `118` status `ready` deltaP `4.7927` edge `0.0346` maxDD `-2.9391`
- `market_context_high->commodity_1h` score `-0.5474` n `127` status `ready` deltaP `1.1033` edge `-0.0006` maxDD `-2.155`
- `market_context_high->metal_4h` score `-0.5725` n `118` status `ready` deltaP `2.2995` edge `0.0523` maxDD `-4.6157`
- `market_context_high->fx_1h` score `-0.7054` n `127` status `ready` deltaP `-3.6211` edge `-0.0022` maxDD `-0.7944`
- `market_context_high->fx_4h` score `-1.0211` n `118` status `ready` deltaP `-3.5422` edge `0.0` maxDD `-1.9169`
- `market_context_high->crypto_major_24h` score `-1.0324` n `61` status `ready` deltaP `15.1155` edge `0.5484` maxDD `-52.4829`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
