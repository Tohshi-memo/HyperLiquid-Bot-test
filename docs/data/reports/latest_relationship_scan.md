# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T12:37:27.237749+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9354`

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

- `news_risk_high->crypto_major_24h` score `21.5241` n `98` status `ready` deltaP `6.5406` edge `2.4359` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `19.8325` n `98` status `ready` deltaP `14.7463` edge `2.0425` maxDD `-32.7147`
- `market_context_high->unknown_4h` score `19.2751` n `60` status `ready` deltaP `1.4024` edge `1.6119` maxDD `-0.5326`
- `news_risk_high->crypto_alt_4h` score `5.9005` n `101` status `ready` deltaP `22.8824` edge `0.4601` maxDD `-7.675`
- `market_context_high->commodity_24h` score `5.491` n `52` status `ready` deltaP `30.0748` edge `0.3096` maxDD `-0.8682`
- `news_risk_high->crypto_major_4h` score `4.3923` n `101` status `ready` deltaP `21.5105` edge `0.3484` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `4.1175` n `60` status `ready` deltaP `35.7521` edge `0.1181` maxDD `-0.0659`
- `news_risk_high->crypto_alt_1h` score `3.0222` n `101` status `ready` deltaP `16.3811` edge `0.1892` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.1828` n `101` status `ready` deltaP `18.0278` edge `0.114` maxDD `-2.8494`
- `market_context_high->fx_4h` score `2.0431` n `60` status `ready` deltaP `26.626` edge `0.0101` maxDD `-0.0543`
- `market_context_high->fx_24h` score `1.5683` n `52` status `ready` deltaP `18.3894` edge `0.0123` maxDD `-0.0027`
- `market_context_high->commodity_1h` score `1.1853` n `63` status `ready` deltaP `14.4212` edge `0.032` maxDD `-0.3491`
- `news_risk_high->commodity_24h` score `1.0269` n `98` status `ready` deltaP `22.775` edge `0.1104` maxDD `-3.4467`
- `news_risk_high->equity_24h` score `0.7613` n `98` status `ready` deltaP `16.571` edge `0.0939` maxDD `-4.941`
- `market_context_high->fx_1h` score `0.7183` n `63` status `ready` deltaP `11.4272` edge `0.0053` maxDD `-0.063`
- `news_risk_high->metal_1h` score `0.6173` n `101` status `ready` deltaP `14.4483` edge `0.0153` maxDD `-0.8144`
- `news_risk_high->metal_4h` score `0.6116` n `101` status `ready` deltaP `16.9464` edge `0.0434` maxDD `-2.0994`
- `news_risk_high->metal_24h` score `0.303` n `98` status `ready` deltaP `15.5046` edge `0.0199` maxDD `-2.4203`
- `market_context_high->metal_1h` score `0.2803` n `63` status `ready` deltaP `7.832` edge `0.0061` maxDD `-0.4568`
- `news_risk_high->equity_1h` score `0.1909` n `101` status `ready` deltaP `5.0646` edge `0.0227` maxDD `-0.9112`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
