# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T09:22:33.885371+00:00`
- Price records: `672`
- Market context records: `6072`
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

- `news_risk_high->fx_24h` score `8.1594` n `30` status `ready` deltaP `72.7431` edge `0.195` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.395` n `30` status `ready` deltaP `45.4878` edge `0.0676` maxDD `-0.0345`
- `news_risk_high->crypto_alt_24h` score `3.9291` n `30` status `ready` deltaP `29.9652` edge `0.1424` maxDD `-0.5131`
- `news_risk_high->fx_1h` score `2.4195` n `32` status `ready` deltaP `29.0419` edge `0.0219` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.6133` n `206` status `ready` deltaP `9.0989` edge `0.1655` maxDD `-2.671`
- `news_risk_high->crypto_major_1h` score `1.2199` n `32` status `ready` deltaP `13.9783` edge `0.1099` maxDD `-2.0691`
- `news_risk_high->commodity_24h` score `1.1612` n `30` status `ready` deltaP `20.5209` edge `-0.0195` maxDD `-0.3101`
- `news_risk_high->crypto_alt_1h` score `0.6501` n `32` status `ready` deltaP `9.2253` edge `0.068` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.0875` n `30` status `ready` deltaP `9.2361` edge `0.0368` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.3768` n `206` status `ready` deltaP `3.5797` edge `0.0077` maxDD `-2.0564`
- `market_context_high->fx_1h` score `-0.5474` n `206` status `ready` deltaP `0.1584` edge `-0.001` maxDD `-0.6538`
- `market_context_high->crypto_alt_1h` score `-0.7667` n `206` status `ready` deltaP `4.7047` edge `0.0456` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.7669` n `206` status `ready` deltaP `5.1494` edge `0.0441` maxDD `-9.807`
- `news_risk_high->metal_1h` score `-0.7731` n `32` status `ready` deltaP `-2.2455` edge `-0.0344` maxDD `-1.6464`
- `market_context_high->commodity_1h` score `-0.8177` n `206` status `ready` deltaP `-2.5812` edge `-0.0063` maxDD `-0.5708`
- `market_context_high->equity_1h` score `-0.8646` n `206` status `ready` deltaP `1.529` edge `0.0306` maxDD `-4.3608`
- `market_context_high->index_4h` score `-0.9013` n `206` status `ready` deltaP `2.2629` edge `0.0227` maxDD `-1.9335`
- `market_context_high->metal_4h` score `-0.9173` n `206` status `ready` deltaP `4.4859` edge `0.0124` maxDD `-3.4996`
- `news_risk_high->index_1h` score `-0.9753` n `32` status `ready` deltaP `-7.878` edge `-0.0162` maxDD `-1.1725`
- `market_context_high->index_1h` score `-1.2175` n `206` status `ready` deltaP `-2.3865` edge `0.0043` maxDD `-1.1879`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
