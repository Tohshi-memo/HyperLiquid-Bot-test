# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T22:52:28.373268+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8684`

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

- `news_risk_high->unknown_4h` score `467.9291` n `71` status `ready` deltaP `-12.3218` edge `39.1532` maxDD `-4.1571`
- `risk_on_high->commodity_24h` score `9.1852` n `52` status `ready` deltaP `50.0` edge `0.4321` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.1852` n `52` status `ready` deltaP `50.0` edge `0.4321` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `8.1524` n `55` status `ready` deltaP `26.9665` edge `0.6375` maxDD `-9.3661`
- `market_context_high->commodity_24h` score `7.8861` n `149` status `ready` deltaP `43.2886` edge `0.4211` maxDD `-0.8682`
- `news_risk_high->index_24h` score `4.5733` n `55` status `ready` deltaP `31.5625` edge `0.1883` maxDD `-0.075`
- `news_risk_high->equity_24h` score `3.689` n `55` status `ready` deltaP `17.904` edge `0.531` maxDD `-6.5262`
- `news_risk_high->crypto_major_24h` score `3.3833` n `55` status `ready` deltaP `11.0322` edge `0.5597` maxDD `-13.2931`
- `risk_on_high->commodity_4h` score `3.0777` n `52` status `ready` deltaP `33.6069` edge `0.0674` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `3.0777` n `52` status `ready` deltaP `33.6069` edge `0.0674` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.9774` n `149` status `ready` deltaP `30.1092` edge `0.0892` maxDD `-0.345`
- `risk_on_high->fx_24h` score `1.8221` n `52` status `ready` deltaP `26.2019` edge `-0.0186` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `1.8221` n `52` status `ready` deltaP `26.2019` edge `-0.0186` maxDD `-0.0054`
- `market_context_high->fx_24h` score `1.6873` n `149` status `ready` deltaP `23.427` edge `0.006` maxDD `-0.0593`
- `news_risk_high->metal_24h` score `1.555` n `55` status `ready` deltaP `17.5474` edge `0.1278` maxDD `-0.6334`
- `news_risk_high->index_4h` score `1.3245` n `71` status `ready` deltaP `19.0441` edge `0.03` maxDD `-0.3938`
- `market_context_high->commodity_1h` score `1.2811` n `149` status `ready` deltaP `17.5582` edge `0.0274` maxDD `-0.3491`
- `risk_on_high->commodity_1h` score `0.6578` n `52` status `ready` deltaP `10.6403` edge `0.0191` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.6578` n `52` status `ready` deltaP `10.6403` edge `0.0191` maxDD `-0.1507`
- `market_context_high->fx_4h` score `0.2389` n `149` status `ready` deltaP `10.9531` edge `0.0052` maxDD `-0.1412`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
