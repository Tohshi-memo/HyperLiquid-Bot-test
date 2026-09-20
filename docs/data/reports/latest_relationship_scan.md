# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T16:37:26.645652+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9886`

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

- `news_risk_high->crypto_major_24h` score `22.9379` n `98` status `ready` deltaP `9.3184` edge `2.5352` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `20.3144` n `98` status `ready` deltaP `14.9199` edge `2.0815` maxDD `-32.7147`
- `market_context_high->unknown_4h` score `14.6571` n `48` status `ready` deltaP `0.1524` edge `1.2354` maxDD `-0.5326`
- `news_risk_high->crypto_alt_4h` score `5.9009` n `101` status `ready` deltaP `23.1873` edge `0.4581` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.4744` n `101` status `ready` deltaP `21.9678` edge `0.3522` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `4.3891` n `48` status `ready` deltaP `36.4329` edge `0.1362` maxDD `-0.0659`
- `market_context_high->commodity_24h` score `3.7069` n `37` status `ready` deltaP `22.2786` edge `0.2129` maxDD `-0.8682`
- `news_risk_high->crypto_alt_1h` score `2.9969` n `101` status `ready` deltaP `16.6805` edge `0.1851` maxDD `-2.058`
- `market_context_high->fx_4h` score `2.2918` n `48` status `ready` deltaP `29.624` edge `0.015` maxDD `-0.0543`
- `news_risk_high->crypto_major_1h` score `2.2187` n `101` status `ready` deltaP `18.4769` edge `0.114` maxDD `-2.8494`
- `market_context_high->fx_24h` score `1.955` n `37` status `ready` deltaP `20.3876` edge `0.0312` maxDD `-0.0027`
- `market_context_high->commodity_1h` score `1.599` n `50` status `ready` deltaP `17.9042` edge `0.0414` maxDD `-0.2012`
- `market_context_high->fx_1h` score `1.2537` n `50` status `ready` deltaP `17.0599` edge `0.0082` maxDD `-0.063`
- `news_risk_high->commodity_24h` score `1.0713` n `98` status `ready` deltaP `22.775` edge `0.1161` maxDD `-3.4467`
- `news_risk_high->metal_4h` score `0.703` n `101` status `ready` deltaP `18.0134` edge `0.0439` maxDD `-2.0994`
- `news_risk_high->metal_1h` score `0.6425` n `101` status `ready` deltaP `14.7477` edge `0.0154` maxDD `-0.8144`
- `news_risk_high->equity_24h` score `0.5933` n `98` status `ready` deltaP `16.571` edge `0.0799` maxDD `-4.941`
- `market_context_high->metal_1h` score `0.2634` n `50` status `ready` deltaP `7.4012` edge `0.0068` maxDD `-0.4568`
- `news_risk_high->equity_1h` score `0.2209` n `101` status `ready` deltaP `5.2143` edge `0.0242` maxDD `-0.9112`
- `news_risk_high->metal_24h` score `0.2019` n `98` status `ready` deltaP `15.3309` edge `0.0081` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
