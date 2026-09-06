# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T07:07:24.820114+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10647`

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

- `news_risk_high->crypto_alt_24h` score `8.424` n `30` status `ready` deltaP `35.5556` edge `0.4694` maxDD `-0.0214`
- `news_risk_high->crypto_major_24h` score `5.7686` n `30` status `ready` deltaP `23.6805` edge `0.4265` maxDD `-6.6257`
- `news_risk_high->crypto_major_4h` score `5.4037` n `30` status `ready` deltaP `28.1301` edge `0.2829` maxDD `-0.6101`
- `news_risk_high->commodity_24h` score `4.0231` n `30` status `ready` deltaP `20.1389` edge `0.201` maxDD `0.0`
- `news_risk_high->commodity_4h` score `2.7354` n `30` status `ready` deltaP `16.5854` edge `0.1333` maxDD `-0.2737`
- `news_risk_high->metal_4h` score `2.4887` n `30` status `ready` deltaP `23.7906` edge `0.0709` maxDD `-0.7692`
- `risk_on_high->crypto_major_24h` score `2.312` n `94` status `ready` deltaP `14.177` edge `0.9345` maxDD `-47.9416`
- `risk_on_and_context->crypto_major_24h` score `2.312` n `94` status `ready` deltaP `14.177` edge `0.9345` maxDD `-47.9416`
- `news_risk_high->fx_24h` score `2.1098` n `30` status `ready` deltaP `30.6945` edge `0.0417` maxDD `-2.9744`
- `news_risk_high->index_1h` score `1.4692` n `30` status `ready` deltaP `17.1557` edge `0.0173` maxDD `-0.0724`
- `market_context_high->equity_24h` score `1.2478` n `177` status `ready` deltaP `13.0827` edge `0.3706` maxDD `-16.9737`
- `news_risk_high->equity_1h` score `1.2134` n `30` status `ready` deltaP `5.8483` edge `0.1012` maxDD `-0.7924`
- `news_risk_high->metal_1h` score `0.7681` n `30` status `ready` deltaP `8.3134` edge `0.0279` maxDD `-0.2118`
- `news_risk_high->crypto_major_1h` score `0.5183` n `30` status `ready` deltaP `-0.5589` edge `0.0652` maxDD `-0.4628`
- `news_risk_high->crypto_alt_1h` score `0.1806` n `30` status `ready` deltaP `3.8623` edge `0.0158` maxDD `-0.7867`
- `news_risk_high->crypto_alt_4h` score `0.1716` n `30` status `ready` deltaP `2.4695` edge `0.0307` maxDD `-1.296`
- `news_risk_high->commodity_1h` score `0.0402` n `30` status `ready` deltaP `6.7465` edge `0.0048` maxDD `-0.9036`
- `risk_on_high->index_1h` score `-0.1084` n `145` status `ready` deltaP `5.0867` edge `-0.0031` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `-0.1084` n `145` status `ready` deltaP `5.0867` edge `-0.0031` maxDD `-0.5764`
- `risk_on_high->metal_1h` score `-0.1286` n `145` status `ready` deltaP `8.1984` edge `0.0001` maxDD `-1.699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
