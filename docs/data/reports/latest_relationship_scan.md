# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T08:37:27.340100+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8486`

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

- `news_risk_high->crypto_major_24h` score `55.6356` n `71` status `ready` deltaP `35.3384` edge `4.4899` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `48.6951` n `71` status `ready` deltaP `39.4855` edge `3.9326` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `35.9407` n `146` status `ready` deltaP `-2.0423` edge `3.032` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `11.6449` n `71` status `ready` deltaP `44.9457` edge `0.675` maxDD `-0.0053`
- `risk_on_high->unknown_4h` score `8.3047` n `52` status `ready` deltaP `-9.076` edge `0.7751` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `8.3047` n `52` status `ready` deltaP `-9.076` edge `0.7751` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.2412` n `52` status `ready` deltaP `44.9653` edge `0.387` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.2412` n `52` status `ready` deltaP `44.9653` edge `0.387` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.9874` n `146` status `ready` deltaP `38.116` edge `0.3807` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `6.7385` n `81` status `ready` deltaP `23.0974` edge `0.5285` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.6125` n `81` status `ready` deltaP `19.9883` edge `0.3769` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `3.3741` n `81` status `ready` deltaP `17.7497` edge `0.2094` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.7204` n `81` status `ready` deltaP `20.9673` edge `0.1392` maxDD `-2.8494`
- `risk_on_high->commodity_4h` score `2.6307` n `52` status `ready` deltaP `31.3203` edge `0.0454` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.6307` n `52` status `ready` deltaP `31.3203` edge `0.0454` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.5011` n `146` status `ready` deltaP `27.3951` edge `0.0676` maxDD `-0.345`
- `news_risk_high->metal_24h` score `2.0618` n `71` status `ready` deltaP `25.0146` edge `0.0823` maxDD `-2.1797`
- `news_risk_high->fx_4h` score `1.2838` n `81` status `ready` deltaP `14.4554` edge `0.0325` maxDD `-0.084`
- `market_context_high->commodity_1h` score `0.9896` n `146` status `ready` deltaP `14.8142` edge `0.0214` maxDD `-0.3491`
- `news_risk_high->equity_1h` score `0.8119` n `81` status `ready` deltaP `10.0078` edge `0.0415` maxDD `-0.9112`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
