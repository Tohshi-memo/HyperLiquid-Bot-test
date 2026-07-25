# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T09:52:29.863703+00:00`
- Price records: `672`
- Market context records: `7866`
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

- `market_context_high->equity_24h` score `12.0278` n `123` status `ready` deltaP `29.0703` edge `0.9427` maxDD `-6.0681`
- `market_context_high->metal_24h` score `2.0461` n `124` status `ready` deltaP `12.6754` edge `0.2538` maxDD `-2.0904`
- `market_context_high->equity_4h` score `1.9897` n `124` status `ready` deltaP `7.8425` edge `0.3454` maxDD `-6.0745`
- `market_context_high->crypto_major_4h` score `1.5043` n `124` status `ready` deltaP `16.7191` edge `0.1857` maxDD `-6.7444`
- `market_context_high->commodity_24h` score `1.3763` n `123` status `ready` deltaP `21.5313` edge `0.1295` maxDD `-7.0012`
- `market_context_high->crypto_major_1h` score `1.2235` n `124` status `ready` deltaP `13.7097` edge `0.0505` maxDD `-1.5286`
- `market_context_high->crypto_alt_4h` score `1.1628` n `124` status `ready` deltaP `10.833` edge `0.1364` maxDD `-3.9374`
- `market_context_high->fx_24h` score `0.9676` n `123` status `ready` deltaP `27.6762` edge `0.0483` maxDD `-3.0343`
- `market_context_high->equity_1h` score `0.6554` n `124` status `ready` deltaP `9.7331` edge `0.1009` maxDD `-4.2072`
- `market_context_high->crypto_alt_1h` score `0.4057` n `124` status `ready` deltaP `5.5293` edge `0.0402` maxDD `-1.4603`
- `market_context_high->commodity_4h` score `0.3908` n `124` status `ready` deltaP `7.8031` edge `0.0399` maxDD `-1.0817`
- `market_context_high->index_1h` score `0.1789` n `124` status `ready` deltaP `7.447` edge `0.0163` maxDD `-0.7743`
- `market_context_high->commodity_1h` score `0.0487` n `124` status `ready` deltaP `5.3788` edge `0.0141` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.2311` n `124` status `ready` deltaP `9.7194` edge `0.0514` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.3211` n `124` status `ready` deltaP `-0.3173` edge `-0.0003` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.564` n `124` status `ready` deltaP `1.0237` edge `0.0212` maxDD `-0.6936`
- `market_context_high->metal_4h` score `-0.897` n `124` status `ready` deltaP `3.8553` edge `0.0837` maxDD `-1.3989`
- `market_context_high->index_24h` score `-0.9699` n `123` status `ready` deltaP `-4.1668` edge `0.1001` maxDD `-2.0667`
- `market_context_high->fx_4h` score `-1.421` n `124` status `ready` deltaP `-3.0334` edge `0.0005` maxDD `-1.6629`
- `market_context_high->crypto_alt_24h` score `-1.5087` n `124` status `ready` deltaP `14.9704` edge `0.2363` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
