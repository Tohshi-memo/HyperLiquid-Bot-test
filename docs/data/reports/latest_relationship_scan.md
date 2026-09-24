# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T13:22:33.424125+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10092`

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

- `market_context_high->unknown_1h` score `99.4651` n `47` status `ready` deltaP `10.116` edge `8.2284` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `41.7863` n `47` status `ready` deltaP `29.3809` edge `3.3256` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `27.7555` n `47` status `ready` deltaP `24.2612` edge `2.1892` maxDD `-2.7051`
- `market_context_high->equity_24h` score `23.7341` n `47` status `ready` deltaP `26.7767` edge `1.8349` maxDD `-2.1786`
- `news_risk_high->crypto_major_24h` score `10.3749` n `103` status `ready` deltaP `3.7251` edge `1.744` maxDD `-63.6743`
- `news_risk_high->crypto_alt_24h` score `7.8546` n `103` status `ready` deltaP `1.1462` edge `1.3482` maxDD `-49.7699`
- `market_context_high->index_24h` score `7.8137` n `47` status `ready` deltaP `34.9364` edge `0.4312` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.487` n `47` status `ready` deltaP `30.1973` edge `0.1131` maxDD `-0.2401`
- `market_context_high->index_4h` score `3.0748` n `47` status `ready` deltaP `34.941` edge `0.0387` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.6865` n `47` status `ready` deltaP `17.9067` edge `0.1463` maxDD `-1.3444`
- `news_risk_high->crypto_alt_1h` score `2.4363` n `120` status `ready` deltaP `12.8344` edge `0.1665` maxDD `-1.5895`
- `news_risk_high->crypto_major_1h` score `2.0751` n `120` status `ready` deltaP `15.0799` edge `0.1159` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.6851` n `114` status `ready` deltaP `24.7085` edge `0.0393` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.3713` n `103` status `ready` deltaP `31.0528` edge `0.1319` maxDD `-1.7159`
- `news_risk_high->commodity_24h` score `1.3148` n `103` status `ready` deltaP `17.4976` edge `0.1108` maxDD `-2.431`
- `news_risk_high->metal_24h` score `1.0663` n `103` status `ready` deltaP `23.6904` edge `0.1236` maxDD `-7.2536`
- `market_context_high->index_1h` score `0.9906` n `47` status `ready` deltaP `14.9095` edge `0.011` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.9499` n `47` status `ready` deltaP `11.167` edge `0.045` maxDD `-1.5564`
- `news_risk_high->crypto_major_4h` score `0.886` n `114` status `ready` deltaP `13.2435` edge `0.1987` maxDD `-13.719`
- `market_context_high->crypto_alt_4h` score `0.5071` n `47` status `ready` deltaP `6.3343` edge `0.0668` maxDD `-3.3417`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
