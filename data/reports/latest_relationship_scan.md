# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T15:52:29.678410+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9386`

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

- `news_risk_high->crypto_major_24h` score `22.7138` n `98` status `ready` deltaP `8.7975` edge `2.52` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `20.2585` n `98` status `ready` deltaP `14.7463` edge `2.078` maxDD `-32.7147`
- `market_context_high->unknown_4h` score `12.5781` n `51` status `ready` deltaP `0.52` edge `1.0597` maxDD `-0.5326`
- `news_risk_high->crypto_alt_4h` score `5.9693` n `101` status `ready` deltaP `23.1873` edge `0.4638` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.5188` n `101` status `ready` deltaP `21.9678` edge `0.3559` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `4.3744` n `51` status `ready` deltaP `36.8633` edge `0.1321` maxDD `-0.0659`
- `market_context_high->commodity_24h` score `4.085` n `40` status `ready` deltaP `24.3056` edge `0.2309` maxDD `-0.8682`
- `news_risk_high->crypto_alt_1h` score `3.0389` n `101` status `ready` deltaP `16.6805` edge `0.1886` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.2463` n `101` status `ready` deltaP `18.4769` edge `0.1163` maxDD `-2.8494`
- `market_context_high->fx_4h` score `2.1855` n `51` status `ready` deltaP `28.521` edge `0.0135` maxDD `-0.0543`
- `market_context_high->fx_24h` score `1.8575` n `40` status `ready` deltaP `20.0694` edge `0.0252` maxDD `-0.0027`
- `market_context_high->commodity_1h` score `1.4772` n `51` status `ready` deltaP `16.5317` edge `0.0404` maxDD `-0.2012`
- `news_risk_high->commodity_24h` score `1.0721` n `98` status `ready` deltaP `22.775` edge `0.1162` maxDD `-3.4467`
- `market_context_high->fx_1h` score `0.9803` n `51` status `ready` deltaP `13.8371` edge `0.0069` maxDD `-0.063`
- `news_risk_high->metal_4h` score `0.7286` n `101` status `ready` deltaP `18.3183` edge `0.044` maxDD `-2.0994`
- `news_risk_high->metal_1h` score `0.6293` n `101` status `ready` deltaP `14.598` edge `0.0153` maxDD `-0.8144`
- `news_risk_high->equity_24h` score `0.6137` n `98` status `ready` deltaP `16.571` edge `0.0816` maxDD `-4.941`
- `market_context_high->metal_1h` score `0.3015` n `51` status `ready` deltaP `8.075` edge `0.0072` maxDD `-0.4568`
- `news_risk_high->equity_1h` score `0.2257` n `101` status `ready` deltaP `5.2143` edge `0.0246` maxDD `-0.9112`
- `news_risk_high->metal_24h` score `0.225` n `98` status `ready` deltaP `15.5046` edge `0.0099` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
