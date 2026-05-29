# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T21:22:18.594216+00:00`
- Price records: `672`
- Market context records: `2282`
- Flow alert records: `8463`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9287`

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

- `news_risk_high->crypto_alt_24h` score `20.4067` n `43` status `ready` deltaP `49.8627` edge `1.427` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `15.5107` n `43` status `ready` deltaP `40.3827` edge `1.0673` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `13.6557` n `43` status `ready` deltaP `30.1397` edge `0.9685` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.3252` n `43` status `ready` deltaP `20.1146` edge `0.7844` maxDD `-3.3119`
- `market_context_high->unknown_24h` score `7.868` n `115` status `ready` deltaP `26.3737` edge `0.521` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `7.8429` n `159` status `ready` deltaP `25.3758` edge `0.7523` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `7.6918` n `159` status `ready` deltaP `29.8933` edge `0.6227` maxDD `-10.1468`
- `news_risk_high->unknown_24h` score `7.4315` n `43` status `ready` deltaP `30.4182` edge `0.4391` maxDD `-1.4744`
- `market_context_high->unknown_4h` score `5.6512` n `159` status `ready` deltaP `22.1554` edge `0.3842` maxDD `-1.8773`
- `market_context_high->crypto_major_24h` score `4.9897` n `115` status `ready` deltaP `13.8255` edge `0.9368` maxDD `-25.1408`
- `news_risk_high->commodity_4h` score `3.8119` n `43` status `ready` deltaP `32.6148` edge `0.3384` maxDD `-3.0367`
- `news_risk_high->index_24h` score `3.6266` n `43` status `ready` deltaP `11.5351` edge `0.2672` maxDD `-1.3507`
- `news_risk_high->fx_24h` score `3.5763` n `43` status `ready` deltaP `37.2295` edge `0.0683` maxDD `-0.1442`
- `news_risk_high->commodity_24h` score `3.5634` n `43` status `ready` deltaP `4.4614` edge `0.3489` maxDD `-3.202`
- `market_context_high->index_24h` score `3.2369` n `115` status `ready` deltaP `13.3349` edge `0.2326` maxDD `-1.4737`
- `market_context_high->index_4h` score `2.4773` n `159` status `ready` deltaP `23.8533` edge `0.13` maxDD `-2.2732`
- `market_context_high->crypto_alt_1h` score `2.1494` n `159` status `ready` deltaP `13.2226` edge `0.2097` maxDD `-6.1656`
- `market_context_high->equity_4h` score `2.1288` n `159` status `ready` deltaP `18.2323` edge `0.1963` maxDD `-5.9024`
- `news_risk_high->fx_4h` score `2.1258` n `43` status `ready` deltaP `27.127` edge `0.0147` maxDD `-0.1382`
- `market_context_high->crypto_major_1h` score `1.9012` n `159` status `ready` deltaP `13.6717` edge `0.1867` maxDD `-4.2199`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
