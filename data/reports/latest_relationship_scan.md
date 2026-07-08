# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T02:22:30.557314+00:00`
- Price records: `672`
- Market context records: `6042`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11125`

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

- `news_risk_high->fx_24h` score `7.9904` n `30` status `ready` deltaP `71.875` edge `0.1867` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.2211` n `30` status `ready` deltaP `43.6585` edge `0.0653` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `2.4332` n `30` status `ready` deltaP `25.382` edge `0.0541` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.2849` n `30` status `ready` deltaP `27.3752` edge `0.0218` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.5529` n `206` status `ready` deltaP `8.7941` edge `0.1625` maxDD `-2.671`
- `market_context_high->equity_24h` score `1.1618` n `182` status `ready` deltaP `28.892` edge `0.5575` maxDD `-35.4267`
- `news_risk_high->crypto_major_1h` score `0.9697` n `30` status `ready` deltaP `10.9381` edge `0.0981` maxDD `-2.0691`
- `news_risk_high->crypto_alt_24h` score `0.821` n `30` status `ready` deltaP `25.1041` edge `-0.0842` maxDD `-0.5131`
- `news_risk_high->crypto_alt_1h` score `0.3471` n `30` status `ready` deltaP `6.0679` edge `0.0502` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.1351` n `30` status `ready` deltaP `9.2361` edge `0.0429` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.4158` n `206` status `ready` deltaP `3.43` edge `0.0037` maxDD `-2.0564`
- `news_risk_high->metal_1h` score `-0.4523` n `30` status `ready` deltaP `0.9381` edge `-0.0276` maxDD `-1.2643`
- `market_context_high->index_24h` score `-0.4961` n `182` status `ready` deltaP `4.8039` edge `0.0744` maxDD `-5.6021`
- `market_context_high->fx_1h` score `-0.5474` n `206` status `ready` deltaP `0.1584` edge `-0.001` maxDD `-0.6538`
- `market_context_high->commodity_1h` score `-0.6751` n `206` status `ready` deltaP `-1.683` edge `-0.0004` maxDD `-0.5708`
- `market_context_high->crypto_major_1h` score `-0.848` n `206` status `ready` deltaP `4.4009` edge `0.0387` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-0.8594` n `206` status `ready` deltaP `4.2556` edge `0.0367` maxDD `-9.3536`
- `market_context_high->index_4h` score `-0.9781` n `206` status `ready` deltaP `1.8056` edge `0.0159` maxDD `-1.9335`
- `market_context_high->metal_4h` score `-1.0049` n `206` status `ready` deltaP `4.4859` edge `0.0051` maxDD `-3.4996`
- `news_risk_high->index_1h` score `-1.0633` n `30` status `ready` deltaP `-9.7006` edge `-0.0202` maxDD `-1.1161`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
