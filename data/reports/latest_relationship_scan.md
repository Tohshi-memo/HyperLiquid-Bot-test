# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T13:52:26.998584+00:00`
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

- `news_risk_high->crypto_major_24h` score `21.9967` n `98` status `ready` deltaP `7.4086` edge `2.4695` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `20.0173` n `98` status `ready` deltaP `14.7463` edge `2.0579` maxDD `-32.7147`
- `market_context_high->unknown_4h` score `18.3371` n `59` status `ready` deltaP `1.3177` edge `1.5343` maxDD `-0.5326`
- `news_risk_high->crypto_alt_4h` score `6.0139` n `101` status `ready` deltaP `23.3398` edge `0.4665` maxDD `-7.675`
- `market_context_high->commodity_24h` score `5.1288` n `48` status `ready` deltaP `28.4723` edge `0.2901` maxDD `-0.8682`
- `news_risk_high->crypto_major_4h` score `4.5104` n `101` status `ready` deltaP `21.9678` edge `0.3552` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `4.3892` n `59` status `ready` deltaP `38.4585` edge `0.1227` maxDD `-0.0659`
- `news_risk_high->crypto_alt_1h` score `3.1469` n `101` status `ready` deltaP `17.1296` edge `0.1946` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.2907` n `101` status `ready` deltaP `18.7763` edge `0.118` maxDD `-2.8494`
- `market_context_high->fx_24h` score `1.6478` n `48` status `ready` deltaP `19.0973` edge `0.0142` maxDD `-0.0027`
- `market_context_high->fx_4h` score `1.6211` n `59` status `ready` deltaP `22.021` edge `0.0098` maxDD `-0.0543`
- `market_context_high->commodity_1h` score `1.5007` n `59` status `ready` deltaP `16.9466` edge `0.0396` maxDD `-0.2012`
- `news_risk_high->commodity_24h` score `1.0464` n `98` status `ready` deltaP `22.775` edge `0.1129` maxDD `-3.4467`
- `market_context_high->fx_1h` score `0.7258` n `59` status `ready` deltaP `11.461` edge `0.0057` maxDD `-0.063`
- `news_risk_high->equity_24h` score `0.6809` n `98` status `ready` deltaP `16.571` edge `0.0872` maxDD `-4.941`
- `news_risk_high->metal_4h` score `0.6774` n `101` status `ready` deltaP `17.7086` edge `0.0438` maxDD `-2.0994`
- `news_risk_high->metal_1h` score `0.6544` n `101` status `ready` deltaP `14.8974` edge `0.0154` maxDD `-0.8144`
- `news_risk_high->metal_24h` score `0.2726` n `98` status `ready` deltaP `15.5046` edge `0.016` maxDD `-2.4203`
- `market_context_high->metal_1h` score `0.244` n `59` status `ready` deltaP `7.178` edge `0.0058` maxDD `-0.4568`
- `news_risk_high->equity_1h` score `0.2376` n `101` status `ready` deltaP `5.364` edge `0.0246` maxDD `-0.9112`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
