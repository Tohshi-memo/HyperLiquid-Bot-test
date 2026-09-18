# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T21:07:28.034977+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8194`

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

- `market_context_high->unknown_4h` score `37.8232` n `149` status `ready` deltaP `-0.9208` edge `3.1814` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `36.858` n `39` status `ready` deltaP `15.5449` edge `3.0733` maxDD `-6.1014`
- `news_risk_high->crypto_alt_24h` score `36.8161` n `39` status `ready` deltaP `33.7073` edge `2.9812` maxDD `-9.3661`
- `risk_on_high->unknown_4h` score `11.7019` n `52` status `ready` deltaP `-8.1614` edge `1.0521` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `11.7019` n `52` status `ready` deltaP `-8.1614` edge `1.0521` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.5865` n `52` status `ready` deltaP `47.9167` edge `0.3961` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.5865` n `52` status `ready` deltaP `47.9167` edge `0.3961` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.4153` n `84` status `ready` deltaP `27.8818` edge `0.628` maxDD `-7.675`
- `market_context_high->commodity_24h` score `7.2874` n `149` status `ready` deltaP `41.2053` edge `0.3851` maxDD `-0.8682`
- `news_risk_high->equity_24h` score `6.0764` n `39` status `ready` deltaP `23.3975` edge `0.4402` maxDD `-3.1851`
- `risk_on_high->commodity_4h` score `2.8441` n `52` status `ready` deltaP `32.9972` edge `0.052` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.8441` n `52` status `ready` deltaP `32.9972` edge `0.052` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.7438` n `149` status `ready` deltaP `29.4995` edge `0.0738` maxDD `-0.345`
- `news_risk_high->crypto_major_4h` score `2.5265` n `84` status `ready` deltaP `18.5685` edge `0.3561` maxDD `-10.1452`
- `news_risk_high->equity_4h` score `1.8755` n `84` status `ready` deltaP `17.0079` edge `0.1329` maxDD `-4.1995`
- `news_risk_high->crypto_alt_1h` score `1.7578` n `84` status `ready` deltaP `12.4679` edge `0.1398` maxDD `-3.4483`
- `news_risk_high->metal_24h` score `1.6947` n `39` status `ready` deltaP `12.8873` edge `0.0836` maxDD `-0.2629`
- `market_context_high->commodity_1h` score `1.1505` n `149` status `ready` deltaP `16.5103` edge `0.0235` maxDD `-0.3491`
- `news_risk_high->equity_1h` score `1.0236` n `84` status `ready` deltaP `12.6533` edge `0.0415` maxDD `-0.9112`
- `news_risk_high->fx_4h` score `1.0208` n `84` status `ready` deltaP `11.5781` edge `0.0307` maxDD `-0.1589`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
