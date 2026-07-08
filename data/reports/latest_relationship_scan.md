# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T01:37:24.582422+00:00`
- Price records: `672`
- Market context records: `6039`
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

- `news_risk_high->fx_24h` score `7.9796` n `30` status `ready` deltaP `71.875` edge `0.1858` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.2491` n `30` status `ready` deltaP `43.9634` edge `0.0656` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `2.5625` n `30` status `ready` deltaP `25.9028` edge `0.0614` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.2705` n `30` status `ready` deltaP `27.2255` edge `0.0216` maxDD `-0.1113`
- `market_context_high->equity_24h` score `1.7528` n `180` status `ready` deltaP `29.7223` edge `0.5717` maxDD `-31.6107`
- `market_context_high->equity_4h` score `1.5733` n `206` status `ready` deltaP `8.7941` edge `0.1642` maxDD `-2.671`
- `news_risk_high->crypto_major_1h` score `0.8964` n `30` status `ready` deltaP `10.6387` edge `0.0907` maxDD `-2.0691`
- `news_risk_high->crypto_alt_24h` score `0.4277` n `30` status `ready` deltaP `24.5833` edge `-0.1135` maxDD `-0.5131`
- `news_risk_high->crypto_alt_1h` score `0.259` n `30` status `ready` deltaP `5.6188` edge `0.0419` maxDD `-1.6923`
- `news_risk_high->index_24h` score `0.1312` n `30` status `ready` deltaP `9.2361` edge `0.0424` maxDD `-2.3058`
- `market_context_high->metal_1h` score `-0.4243` n `206` status `ready` deltaP `3.2803` edge `0.0036` maxDD `-2.0564`
- `market_context_high->index_24h` score `-0.4483` n `180` status `ready` deltaP `5.3472` edge `0.0769` maxDD `-5.6021`
- `news_risk_high->metal_1h` score `-0.4608` n `30` status `ready` deltaP `0.7884` edge `-0.0277` maxDD `-1.2643`
- `market_context_high->fx_1h` score `-0.5618` n `206` status `ready` deltaP `0.0087` edge `-0.0012` maxDD `-0.6538`
- `market_context_high->commodity_1h` score `-0.6739` n `206` status `ready` deltaP `-1.683` edge `-0.0003` maxDD `-0.5708`
- `market_context_high->crypto_major_1h` score `-0.9213` n `206` status `ready` deltaP `4.1015` edge `0.0313` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-0.9475` n `206` status `ready` deltaP `3.8065` edge `0.0284` maxDD `-9.3536`
- `market_context_high->metal_4h` score `-0.9745` n `206` status `ready` deltaP `4.7907` edge `0.0056` maxDD `-3.4996`
- `market_context_high->index_4h` score `-0.9852` n `206` status `ready` deltaP `1.6532` edge `0.016` maxDD `-1.9335`
- `news_risk_high->index_1h` score `-1.0851` n `30` status `ready` deltaP `-10.0` edge `-0.021` maxDD `-1.1161`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
