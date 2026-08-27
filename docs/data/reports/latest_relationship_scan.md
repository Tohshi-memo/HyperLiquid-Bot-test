# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-27T13:37:32.984530+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14748`

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

- `news_risk_high->unknown_24h` score `51.4601` n `50` status `ready` deltaP `11.5717` edge `4.2112` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.59` n `50` status `ready` deltaP `37.6235` edge `1.4258` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.6482` n `50` status `ready` deltaP `26.3171` edge `0.8885` maxDD `-0.1279`
- `news_risk_high->equity_24h` score `4.6165` n `50` status `ready` deltaP `25.6235` edge `0.3067` maxDD `-4.7584`
- `news_risk_high->metal_24h` score `4.4366` n `50` status `ready` deltaP `44.9775` edge `0.0741` maxDD `-0.0053`
- `news_risk_high->fx_4h` score `4.0211` n `50` status `ready` deltaP `46.878` edge `0.0316` maxDD `-0.0559`
- `market_context_high->unknown_4h` score `3.2535` n `135` status `ready` deltaP `24.169` edge `0.1507` maxDD `-0.5894`
- `news_risk_high->unknown_1h` score `2.997` n `50` status `ready` deltaP `17.2754` edge `0.1702` maxDD `-0.8495`
- `news_risk_high->index_24h` score `2.6864` n `50` status `ready` deltaP `30.1416` edge `0.038` maxDD `-0.2064`
- `market_context_high->unknown_24h` score `2.0358` n `128` status `ready` deltaP `5.3217` edge `0.2074` maxDD `-3.1917`
- `news_risk_high->fx_1h` score `1.542` n `50` status `ready` deltaP `20.6527` edge `0.0078` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.1978` n `50` status `ready` deltaP `17.2635` edge `0.0126` maxDD `-0.2301`
- `market_context_high->unknown_1h` score `0.9429` n `147` status `ready` deltaP `10.0645` edge `0.0565` maxDD `-1.6015`
- `news_risk_high->equity_4h` score `0.6125` n `50` status `ready` deltaP `17.7683` edge `0.0089` maxDD `-2.105`
- `news_risk_high->commodity_1h` score `0.5619` n `50` status `ready` deltaP `15.0479` edge `0.003` maxDD `-0.5024`
- `news_risk_high->index_1h` score `0.1623` n `50` status `ready` deltaP `8.1078` edge `0.0007` maxDD `-0.0486`
- `news_risk_high->metal_1h` score `0.1194` n `50` status `ready` deltaP `5.8503` edge `-0.0011` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.0471` n `50` status `ready` deltaP `7.7683` edge `-0.0026` maxDD `-0.249`
- `news_risk_high->index_4h` score `-0.1135` n `50` status `ready` deltaP `4.7988` edge `-0.0018` maxDD `-0.1719`
- `market_context_high->fx_1h` score `-0.5214` n `147` status `ready` deltaP `1.0337` edge `-0.0005` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
