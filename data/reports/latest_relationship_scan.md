# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T16:52:31.350676+00:00`
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

- `news_risk_high->crypto_major_24h` score `23.0094` n `98` status `ready` deltaP `9.492` edge `2.54` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `20.3379` n `98` status `ready` deltaP `15.0935` edge `2.0823` maxDD `-32.7147`
- `market_context_high->unknown_4h` score `14.7219` n `48` status `ready` deltaP `0.1524` edge `1.2408` maxDD `-0.5326`
- `news_risk_high->crypto_alt_4h` score `5.8625` n `101` status `ready` deltaP `23.1873` edge `0.4549` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.4492` n `101` status `ready` deltaP `21.9678` edge `0.3501` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `4.3915` n `48` status `ready` deltaP `36.4329` edge `0.1364` maxDD `-0.0659`
- `market_context_high->commodity_24h` score `3.7009` n `37` status `ready` deltaP `22.2786` edge `0.2124` maxDD `-0.8682`
- `news_risk_high->crypto_alt_1h` score `2.9717` n `101` status `ready` deltaP `16.6805` edge `0.183` maxDD `-2.058`
- `market_context_high->fx_4h` score `2.2918` n `48` status `ready` deltaP `29.624` edge `0.015` maxDD `-0.0543`
- `news_risk_high->crypto_major_1h` score `2.2019` n `101` status `ready` deltaP `18.4769` edge `0.1126` maxDD `-2.8494`
- `market_context_high->fx_24h` score `1.9701` n `37` status `ready` deltaP `20.5612` edge `0.0313` maxDD `-0.0027`
- `market_context_high->commodity_1h` score `1.4784` n `51` status `ready` deltaP `16.5317` edge `0.0405` maxDD `-0.2012`
- `market_context_high->fx_1h` score `1.2953` n `51` status `ready` deltaP `17.6089` edge `0.008` maxDD `-0.063`
- `news_risk_high->commodity_24h` score `1.0674` n `98` status `ready` deltaP `22.775` edge `0.1156` maxDD `-3.4467`
- `news_risk_high->metal_4h` score `0.6896` n `101` status `ready` deltaP `17.861` edge `0.0438` maxDD `-2.0994`
- `news_risk_high->metal_1h` score `0.6413` n `101` status `ready` deltaP `14.7477` edge `0.0153` maxDD `-0.8144`
- `news_risk_high->equity_24h` score `0.5921` n `98` status `ready` deltaP `16.571` edge `0.0798` maxDD `-4.941`
- `market_context_high->metal_1h` score `0.3085` n `51` status `ready` deltaP `8.2247` edge `0.0071` maxDD `-0.4568`
- `news_risk_high->equity_1h` score `0.2209` n `101` status `ready` deltaP `5.2143` edge `0.0242` maxDD `-0.9112`
- `news_risk_high->metal_24h` score `0.1898` n `98` status `ready` deltaP `15.1573` edge `0.0077` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
