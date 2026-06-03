# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T15:37:25.028136+00:00`
- Price records: `672`
- Market context records: `2777`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9237`

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

- `market_context_high->unknown_24h` score `3.7903` n `139` status `ready` deltaP `7.9087` edge `0.3096` maxDD `-1.7175`
- `market_context_high->crypto_alt_24h` score `3.5681` n `139` status `ready` deltaP `4.5776` edge `0.6585` maxDD `-22.6673`
- `market_context_high->unknown_4h` score `0.9494` n `142` status `ready` deltaP `6.338` edge `0.1422` maxDD `-3.7602`
- `market_context_high->commodity_24h` score `0.3139` n `139` status `ready` deltaP `10.3841` edge `0.2804` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.1423` n `142` status `ready` deltaP `11.624` edge `0.0249` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.0481` n `142` status `ready` deltaP `3.8817` edge `0.0432` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.1475` n `142` status `ready` deltaP `3.4495` edge `0.0075` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.5874` n `142` status `ready` deltaP `-1.1364` edge `0.003` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.6117` n `142` status `ready` deltaP `0.0169` edge `-0.0032` maxDD `-4.3601`
- `market_context_high->metal_1h` score `-0.6746` n `142` status `ready` deltaP `0.1328` edge `-0.0028` maxDD `-3.0996`
- `market_context_high->crypto_alt_1h` score `-0.7132` n `142` status `ready` deltaP `5.0962` edge `0.0506` maxDD `-10.747`
- `market_context_high->crypto_major_1h` score `-0.9295` n `142` status `ready` deltaP `3.926` edge `0.0416` maxDD `-9.622`
- `market_context_high->equity_1h` score `-1.1353` n `142` status `ready` deltaP `-3.7973` edge `0.014` maxDD `-2.6634`
- `market_context_high->fx_4h` score `-1.1483` n `142` status `ready` deltaP `-3.753` edge `0.0072` maxDD `-0.5631`
- `market_context_high->fx_24h` score `-1.3908` n `139` status `ready` deltaP `-1.1716` edge `-0.0209` maxDD `-0.6418`
- `market_context_high->crypto_alt_4h` score `-1.4031` n `142` status `ready` deltaP `14.0329` edge `0.2236` maxDD `-28.7261`
- `market_context_high->commodity_4h` score `-1.5541` n `142` status `ready` deltaP `0.161` edge `-0.0083` maxDD `-10.0279`
- `market_context_high->equity_4h` score `-1.7863` n `142` status `ready` deltaP `0.2855` edge `-0.0128` maxDD `-5.7037`
- `market_context_high->metal_4h` score `-2.3166` n `142` status `ready` deltaP `-1.8378` edge `-0.0297` maxDD `-11.4038`
- `market_context_high->crypto_major_4h` score `-2.5913` n `142` status `ready` deltaP `5.1249` edge `0.1242` maxDD `-32.2466`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
