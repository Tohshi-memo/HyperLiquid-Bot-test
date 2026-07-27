# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T07:37:33.337508+00:00`
- Price records: `672`
- Market context records: `8070`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11784`

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

- `market_context_high->equity_24h` score `20.0616` n `79` status `ready` deltaP `35.9739` edge `1.523` maxDD `-4.9489`
- `market_context_high->equity_4h` score `8.3542` n `87` status `ready` deltaP `32.4205` edge `0.528` maxDD `-2.5032`
- `market_context_high->metal_24h` score `8.288` n `79` status `ready` deltaP `35.8752` edge `0.4515` maxDD `0.0`
- `news_risk_high->equity_1h` score `3.8657` n `39` status `ready` deltaP `31.7903` edge `0.1418` maxDD `-1.1944`
- `market_context_high->commodity_24h` score `3.8571` n `79` status `ready` deltaP `31.4986` edge `0.2864` maxDD `-9.3304`
- `news_risk_high->unknown_1h` score `3.4778` n `39` status `ready` deltaP `5.942` edge `0.2779` maxDD `-0.8826`
- `market_context_high->index_4h` score `3.2809` n `87` status `ready` deltaP `31.5881` edge `0.0816` maxDD `-0.5022`
- `market_context_high->index_24h` score `2.7763` n `79` status `ready` deltaP `16.6027` edge `0.1877` maxDD `-1.3621`
- `market_context_high->metal_4h` score `2.4092` n `87` status `ready` deltaP `22.2158` edge `0.1149` maxDD `-0.979`
- `market_context_high->equity_1h` score `2.3382` n `87` status `ready` deltaP `14.7257` edge `0.14` maxDD `-2.1322`
- `market_context_high->fx_24h` score `2.1611` n `79` status `ready` deltaP `29.6163` edge `0.053` maxDD `-0.6283`
- `news_risk_high->crypto_major_1h` score `1.2245` n `39` status `ready` deltaP `5.3624` edge `0.09` maxDD `-0.5636`
- `market_context_high->index_1h` score `1.1015` n `87` status `ready` deltaP `14.6724` edge `0.0207` maxDD `-0.4716`
- `news_risk_high->crypto_alt_1h` score `0.9879` n `39` status `ready` deltaP `6.8594` edge `0.0601` maxDD `-0.5468`
- `market_context_high->metal_1h` score `0.7476` n `87` status `ready` deltaP `10.775` edge `0.0283` maxDD `-0.6936`
- `news_risk_high->index_1h` score `0.6796` n `39` status `ready` deltaP `8.3948` edge `0.0212` maxDD `-0.3089`
- `market_context_high->crypto_major_1h` score `0.4464` n `87` status `ready` deltaP `8.7222` edge `0.0201` maxDD `-1.6171`
- `news_risk_high->fx_1h` score `0.4311` n `39` status `ready` deltaP `8.2067` edge `0.007` maxDD `-0.0632`
- `market_context_high->crypto_alt_4h` score `0.3374` n `87` status `ready` deltaP `3.5902` edge `0.1159` maxDD `-3.9374`
- `market_context_high->crypto_major_4h` score `0.1988` n `87` status `ready` deltaP `6.5812` edge `0.1445` maxDD `-6.7444`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
