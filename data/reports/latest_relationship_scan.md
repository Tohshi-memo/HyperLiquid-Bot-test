# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T19:37:26.568876+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8314`

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

- `market_context_high->unknown_4h` score `38.62` n `149` status `ready` deltaP `-0.9208` edge `3.2478` maxDD `-0.5326`
- `news_risk_high->crypto_alt_24h` score `33.5182` n `37` status `ready` deltaP `33.0143` edge `2.711` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `21.1225` n `37` status `ready` deltaP `11.8384` edge `2.745` maxDD `-6.6058`
- `risk_on_high->unknown_4h` score `12.4987` n `52` status `ready` deltaP `-8.1614` edge `1.1185` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `12.4987` n `52` status `ready` deltaP `-8.1614` edge `1.1185` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.6021` n `52` status `ready` deltaP `47.9167` edge `0.3974` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.6021` n `52` status `ready` deltaP `47.9167` edge `0.3974` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.366` n `85` status `ready` deltaP `27.76` edge `0.6247` maxDD `-7.675`
- `market_context_high->commodity_24h` score `7.303` n `149` status `ready` deltaP `41.2053` edge `0.3864` maxDD `-0.8682`
- `news_risk_high->equity_24h` score `4.9184` n `37` status `ready` deltaP `20.0732` edge `0.373` maxDD `-3.4232`
- `risk_on_high->commodity_4h` score `2.8405` n `52` status `ready` deltaP `32.9972` edge `0.0517` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.8405` n `52` status `ready` deltaP `32.9972` edge `0.0517` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.7402` n `149` status `ready` deltaP `29.4995` edge `0.0735` maxDD `-0.345`
- `news_risk_high->crypto_major_4h` score `2.3961` n `85` status `ready` deltaP `18.5868` edge `0.353` maxDD `-10.9113`
- `news_risk_high->equity_4h` score `2.0268` n `85` status `ready` deltaP `17.9537` edge `0.1392` maxDD `-4.1995`
- `market_context_high->commodity_1h` score `1.1912` n `149` status `ready` deltaP `16.9594` edge `0.0239` maxDD `-0.3491`
- `news_risk_high->equity_1h` score `1.1313` n `85` status `ready` deltaP `13.7002` edge `0.0435` maxDD `-0.9112`
- `news_risk_high->metal_24h` score `1.0936` n `37` status `ready` deltaP `8.4178` edge `0.0633` maxDD `-0.2629`
- `news_risk_high->crypto_alt_1h` score `1.0504` n `85` status `ready` deltaP `11.8193` edge `0.1346` maxDD `-3.6312`
- `news_risk_high->fx_4h` score `0.9672` n `85` status `ready` deltaP `11.6804` edge `0.0302` maxDD `-0.1976`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
