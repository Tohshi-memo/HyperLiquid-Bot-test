# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T09:07:30.482584+00:00`
- Price records: `672`
- Market context records: `6071`
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

- `news_risk_high->fx_24h` score `8.1582` n `30` status `ready` deltaP `72.7431` edge `0.1949` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.4084` n `30` status `ready` deltaP `45.6402` edge `0.0677` maxDD `-0.0345`
- `news_risk_high->crypto_alt_24h` score `3.7916` n `30` status `ready` deltaP `29.7916` edge `0.1321` maxDD `-0.5131`
- `news_risk_high->fx_1h` score `2.4195` n `32` status `ready` deltaP `29.0419` edge `0.0219` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.5893` n `206` status `ready` deltaP `9.0989` edge `0.1635` maxDD `-2.671`
- `news_risk_high->crypto_major_1h` score `1.2167` n `32` status `ready` deltaP `13.9783` edge `0.1095` maxDD `-2.0691`
- `news_risk_high->commodity_24h` score `1.2122` n `30` status `ready` deltaP `20.6945` edge `-0.0164` maxDD `-0.3101`
- `news_risk_high->crypto_alt_1h` score `0.6431` n `32` status `ready` deltaP `9.2253` edge `0.0671` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.0844` n `30` status `ready` deltaP `9.2361` edge `0.0364` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.3916` n `206` status `ready` deltaP `3.43` edge `0.0068` maxDD `-2.0564`
- `market_context_high->fx_1h` score `-0.5474` n `206` status `ready` deltaP `0.1584` edge `-0.001` maxDD `-0.6538`
- `market_context_high->crypto_major_1h` score `-0.7701` n `206` status `ready` deltaP `5.1494` edge `0.0437` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-0.7737` n `206` status `ready` deltaP `4.7047` edge `0.0447` maxDD `-9.3536`
- `news_risk_high->metal_1h` score `-0.7879` n `32` status `ready` deltaP `-2.3952` edge `-0.0353` maxDD `-1.6464`
- `market_context_high->commodity_1h` score `-0.8153` n `206` status `ready` deltaP `-2.5812` edge `-0.0061` maxDD `-0.5708`
- `market_context_high->index_4h` score `-0.9067` n `206` status `ready` deltaP `2.2629` edge `0.022` maxDD `-1.9335`
- `market_context_high->equity_1h` score `-0.9078` n `206` status `ready` deltaP `1.3793` edge `0.028` maxDD `-4.3608`
- `market_context_high->metal_4h` score `-0.9595` n `206` status `ready` deltaP `4.3334` edge `0.0099` maxDD `-3.4996`
- `news_risk_high->index_1h` score `-0.987` n `32` status `ready` deltaP `-8.0277` edge `-0.0167` maxDD `-1.1725`
- `market_context_high->index_1h` score `-1.2355` n `206` status `ready` deltaP `-2.5362` edge `0.0038` maxDD `-1.1879`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
