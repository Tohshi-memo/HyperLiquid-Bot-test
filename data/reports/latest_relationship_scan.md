# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T13:08:02.852566+00:00`
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

- `news_risk_high->crypto_major_24h` score `21.7018` n `98` status `ready` deltaP `6.8878` edge `2.4484` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `19.8973` n `98` status `ready` deltaP `14.7463` edge `2.0479` maxDD `-32.7147`
- `market_context_high->unknown_4h` score `17.3821` n `61` status `ready` deltaP `1.4844` edge `1.4536` maxDD `-0.5326`
- `news_risk_high->crypto_alt_4h` score `5.9113` n `101` status `ready` deltaP `22.8824` edge `0.461` maxDD `-7.675`
- `market_context_high->commodity_24h` score `5.402` n `51` status `ready` deltaP `29.6978` edge `0.3047` maxDD `-0.8682`
- `news_risk_high->crypto_major_4h` score `4.4115` n `101` status `ready` deltaP `21.5105` edge `0.35` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `4.1108` n `61` status `ready` deltaP `35.8181` edge `0.1171` maxDD `-0.0659`
- `news_risk_high->crypto_alt_1h` score `3.0653` n `101` status `ready` deltaP `16.6805` edge `0.1908` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.2212` n `101` status `ready` deltaP `18.3272` edge `0.1152` maxDD `-2.8494`
- `market_context_high->fx_4h` score `1.8187` n `61` status `ready` deltaP `23.9255` edge `0.0094` maxDD `-0.0543`
- `market_context_high->fx_24h` score `1.6015` n `51` status `ready` deltaP `18.6989` edge `0.013` maxDD `-0.0027`
- `market_context_high->commodity_1h` score `1.1363` n `62` status `ready` deltaP `13.7338` edge `0.0325` maxDD `-0.3491`
- `news_risk_high->commodity_24h` score `1.0347` n `98` status `ready` deltaP `22.775` edge `0.1114` maxDD `-3.4467`
- `market_context_high->fx_1h` score `0.8187` n `62` status `ready` deltaP `12.6521` edge `0.0055` maxDD `-0.063`
- `news_risk_high->equity_24h` score `0.7217` n `98` status `ready` deltaP `16.571` edge `0.0906` maxDD `-4.941`
- `news_risk_high->metal_4h` score `0.6372` n `101` status `ready` deltaP `17.2512` edge `0.0435` maxDD `-2.0994`
- `news_risk_high->metal_1h` score `0.6293` n `101` status `ready` deltaP `14.598` edge `0.0153` maxDD `-0.8144`
- `market_context_high->metal_1h` score `0.3389` n `62` status `ready` deltaP `8.9289` edge `0.0063` maxDD `-0.4568`
- `news_risk_high->metal_24h` score `0.2905` n `98` status `ready` deltaP `15.5046` edge `0.0183` maxDD `-2.4203`
- `news_risk_high->equity_1h` score `0.2101` n `101` status `ready` deltaP `5.2143` edge `0.0233` maxDD `-0.9112`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
