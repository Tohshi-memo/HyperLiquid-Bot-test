# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-10T07:22:25.504151+00:00`
- Price records: `672`
- Market context records: `6261`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11082`

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

- `news_risk_high->crypto_alt_24h` score `14.6998` n `32` status `ready` deltaP `42.6351` edge `0.9555` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `5.971` n `32` status `ready` deltaP `50.7719` edge `0.1591` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1829` n `32` status `ready` deltaP `43.8262` edge `0.061` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `3.6603` n `32` status `ready` deltaP `16.0538` edge `0.4402` maxDD `-4.2368`
- `news_risk_high->commodity_24h` score `2.4524` n `32` status `ready` deltaP `26.056` edge `0.0512` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.3452` n `32` status `ready` deltaP `28.1437` edge `0.0217` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `2.2111` n `192` status `ready` deltaP `2.2611` edge `0.27` maxDD `-3.7317`
- `market_context_high->unknown_4h` score `1.3867` n `192` status `ready` deltaP `-1.2322` edge `0.377` maxDD `-11.925`
- `news_risk_high->crypto_major_1h` score `1.3345` n `32` status `ready` deltaP `13.8286` edge `0.1256` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.7857` n `32` status `ready` deltaP `10.5726` edge `0.0764` maxDD `-1.6923`
- `news_risk_high->index_24h` score `-0.1574` n `32` status `ready` deltaP `9.2517` edge `0.0053` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.2723` n `192` status `ready` deltaP `4.0396` edge `0.0421` maxDD `-2.671`
- `market_context_high->metal_24h` score `-0.2901` n `192` status `ready` deltaP `18.0684` edge `0.0992` maxDD `-11.8809`
- `market_context_high->fx_1h` score `-0.2925` n `192` status `ready` deltaP `1.0604` edge `0.0` maxDD `-0.5659`
- `market_context_high->commodity_1h` score `-0.5283` n `192` status `ready` deltaP `-0.4491` edge `0.0036` maxDD `-0.5708`
- `market_context_high->metal_4h` score `-0.5348` n `192` status `ready` deltaP `3.6713` edge `0.0257` maxDD `-3.4996`
- `news_risk_high->metal_1h` score `-0.7115` n `32` status `ready` deltaP `-2.5449` edge `-0.0245` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.7538` n `192` status `ready` deltaP `2.6634` edge `-0.0007` maxDD `-2.0564`
- `market_context_high->crypto_alt_1h` score `-0.878` n `192` status `ready` deltaP `4.8434` edge `0.0304` maxDD `-9.3536`
- `market_context_high->equity_1h` score `-0.9536` n `192` status `ready` deltaP `-1.8151` edge `0.0014` maxDD `-4.2573`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
