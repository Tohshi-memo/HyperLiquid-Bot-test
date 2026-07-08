# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T10:07:31.272814+00:00`
- Price records: `672`
- Market context records: `6076`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11112`

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

- `news_risk_high->fx_24h` score `8.1618` n `30` status `ready` deltaP `72.7431` edge `0.1952` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `4.3883` n `30` status `ready` deltaP `30.4861` edge `0.1772` maxDD `-0.5131`
- `news_risk_high->fx_4h` score `4.3683` n `30` status `ready` deltaP `45.1829` edge `0.0674` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.459` n `32` status `ready` deltaP `29.491` edge `0.0222` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.6949` n `206` status `ready` deltaP `9.0989` edge `0.1723` maxDD `-2.671`
- `news_risk_high->crypto_major_1h` score `1.1918` n `32` status `ready` deltaP `13.8286` edge `0.1073` maxDD `-2.0691`
- `news_risk_high->commodity_24h` score `1.0031` n `30` status `ready` deltaP `20.0` edge `-0.0292` maxDD `-0.3101`
- `news_risk_high->crypto_alt_1h` score `0.6564` n `32` status `ready` deltaP `9.2253` edge `0.0688` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.0961` n `30` status `ready` deltaP `9.2361` edge `0.0379` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.3511` n `206` status `ready` deltaP `3.8791` edge `0.009` maxDD `-2.0564`
- `market_context_high->fx_1h` score `-0.5079` n `206` status `ready` deltaP `0.6075` edge `-0.0007` maxDD `-0.6538`
- `news_risk_high->metal_1h` score `-0.7474` n `32` status `ready` deltaP `-1.9461` edge `-0.0331` maxDD `-1.6464`
- `market_context_high->crypto_alt_1h` score `-0.7604` n `206` status `ready` deltaP `4.7047` edge `0.0464` maxDD `-9.3536`
- `market_context_high->metal_4h` score `-0.7631` n `206` status `ready` deltaP `4.9432` edge `0.0222` maxDD `-3.4996`
- `market_context_high->crypto_major_1h` score `-0.795` n `206` status `ready` deltaP `4.9997` edge `0.0415` maxDD `-9.807`
- `market_context_high->commodity_1h` score `-0.8057` n `206` status `ready` deltaP `-2.4315` edge `-0.0063` maxDD `-0.5708`
- `market_context_high->equity_1h` score `-0.8071` n `206` status `ready` deltaP `1.9781` edge `0.0324` maxDD `-4.3608`
- `market_context_high->index_4h` score `-0.8896` n `206` status `ready` deltaP `2.2629` edge `0.0242` maxDD `-1.9335`
- `news_risk_high->index_1h` score `-0.9489` n `32` status `ready` deltaP `-7.4289` edge `-0.0158` maxDD `-1.1725`
- `market_context_high->index_1h` score `-1.1768` n `206` status `ready` deltaP `-1.9374` edge `0.0047` maxDD `-1.1879`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
