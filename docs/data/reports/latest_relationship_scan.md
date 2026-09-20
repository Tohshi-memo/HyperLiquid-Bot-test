# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T10:37:33.937306+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9300`

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

- `news_risk_high->crypto_major_24h` score `29.0208` n `91` status `ready` deltaP `10.4892` edge `2.8137` maxDD `-30.885`
- `news_risk_high->crypto_alt_24h` score `27.6614` n `91` status `ready` deltaP `19.3395` edge `2.4388` maxDD `-17.0092`
- `market_context_high->unknown_4h` score `16.8077` n `63` status `ready` deltaP `1.6405` edge `1.4047` maxDD `-0.5326`
- `news_risk_high->crypto_alt_4h` score `6.3785` n `98` status `ready` deltaP `24.0573` edge `0.4921` maxDD `-7.675`
- `market_context_high->commodity_24h` score `6.1221` n `60` status `ready` deltaP `32.6389` edge `0.3451` maxDD `-0.8682`
- `news_risk_high->crypto_major_4h` score `4.7112` n `98` status `ready` deltaP `23.1427` edge `0.3641` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `4.0271` n `63` status `ready` deltaP `34.9521` edge `0.1159` maxDD `-0.0659`
- `news_risk_high->crypto_alt_1h` score `3.0306` n `101` status `ready` deltaP `16.3811` edge `0.1899` maxDD `-2.058`
- `news_risk_high->equity_24h` score `2.7729` n `91` status `ready` deltaP `22.6935` edge `0.1683` maxDD `-3.081`
- `news_risk_high->crypto_major_1h` score `2.2248` n `101` status `ready` deltaP `18.3272` edge `0.1155` maxDD `-2.8494`
- `market_context_high->fx_4h` score `2.213` n `63` status `ready` deltaP `28.8545` edge `0.0094` maxDD `-0.0543`
- `market_context_high->commodity_1h` score `1.4738` n `71` status `ready` deltaP `17.8776` edge `0.033` maxDD `-0.3491`
- `market_context_high->fx_24h` score `1.3853` n `60` status `ready` deltaP `17.2569` edge `0.0046` maxDD `-0.0027`
- `news_risk_high->commodity_24h` score `0.7811` n `91` status `ready` deltaP `20.7342` edge `0.0925` maxDD `-3.4467`
- `news_risk_high->metal_4h` score `0.7457` n `98` status `ready` deltaP `18.3673` edge `0.0451` maxDD `-2.0994`
- `news_risk_high->metal_24h` score `0.7129` n `91` status `ready` deltaP `21.0776` edge `0.0353` maxDD `-2.4203`
- `news_risk_high->metal_1h` score `0.6161` n `101` status `ready` deltaP `14.4483` edge `0.0152` maxDD `-0.8144`
- `market_context_high->fx_1h` score `0.3155` n `71` status `ready` deltaP `7.1814` edge `0.0042` maxDD `-0.063`
- `news_risk_high->equity_1h` score `0.2771` n `101` status `ready` deltaP `5.9628` edge `0.0239` maxDD `-0.9112`
- `news_risk_high->fx_4h` score `-0.0671` n `98` status `ready` deltaP `5.3851` edge `0.0221` maxDD `-0.421`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
