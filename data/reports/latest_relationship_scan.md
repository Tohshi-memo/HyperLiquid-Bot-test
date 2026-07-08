# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-08T21:22:26.568620+00:00`
- Price records: `672`
- Market context records: `6125`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11131`

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

- `news_risk_high->crypto_alt_24h` score `10.1793` n `30` status `ready` deltaP `38.2986` edge `0.6077` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `7.8741` n `30` status `ready` deltaP `69.7917` edge `0.1909` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.3201` n `32` status `ready` deltaP `45.0457` edge `0.0643` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3919` n `32` status `ready` deltaP `28.7425` edge `0.0216` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.322` n `32` status `ready` deltaP `14.128` edge `0.122` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.7219` n `32` status `ready` deltaP `9.2253` edge `0.0772` maxDD `-1.6923`
- `market_context_high->equity_4h` score `0.5797` n `195` status `ready` deltaP `4.9695` edge `0.1069` maxDD `-2.671`
- `news_risk_high->index_24h` score `-0.0698` n `30` status `ready` deltaP `8.7152` edge `0.0201` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.2754` n `195` status `ready` deltaP `1.4348` edge `-0.0003` maxDD `-0.5659`
- `news_risk_high->commodity_24h` score `-0.5287` n `30` status `ready` deltaP `14.0973` edge `-0.1175` maxDD `-0.3101`
- `market_context_high->metal_4h` score `-0.7161` n `195` status `ready` deltaP `2.7799` edge `0.0084` maxDD `-3.4996`
- `market_context_high->equity_1h` score `-0.7479` n `195` status `ready` deltaP `0.0399` edge `0.0154` maxDD `-4.2573`
- `market_context_high->commodity_1h` score `-0.7631` n `195` status `ready` deltaP `-2.1388` edge `-0.0047` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.7785` n `32` status `ready` deltaP `-2.994` edge `-0.0301` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.832` n `195` status `ready` deltaP `2.3906` edge `-0.0054` maxDD `-2.0564`
- `market_context_high->crypto_alt_1h` score `-0.854` n `195` status `ready` deltaP `4.2093` edge `0.0377` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.8759` n `195` status `ready` deltaP `4.9133` edge `0.0317` maxDD `-9.807`
- `market_context_high->index_4h` score `-1.021` n `195` status `ready` deltaP `-0.1306` edge `0.0164` maxDD `-1.381`
- `news_risk_high->crypto_major_24h` score `-1.1257` n `30` status `ready` deltaP `8.6458` edge `-0.124` maxDD `-4.2368`
- `news_risk_high->index_1h` score `-1.1365` n `32` status `ready` deltaP `-10.2732` edge `-0.0209` maxDD `-1.1725`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
