# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T16:07:23.664303+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9338`

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

- `news_risk_high->crypto_major_24h` score `22.7889` n `98` status `ready` deltaP `8.9711` edge `2.5251` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `20.2729` n `98` status `ready` deltaP `14.7463` edge `2.0792` maxDD `-32.7147`
- `market_context_high->unknown_4h` score `13.7015` n `50` status `ready` deltaP `0.4024` edge `1.1541` maxDD `-0.5326`
- `news_risk_high->crypto_alt_4h` score `5.9585` n `101` status `ready` deltaP `23.1873` edge `0.4629` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.5128` n `101` status `ready` deltaP `21.9678` edge `0.3554` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `4.3846` n `50` status `ready` deltaP `36.7805` edge `0.1335` maxDD `-0.0659`
- `market_context_high->commodity_24h` score `3.9713` n `39` status `ready` deltaP `23.6646` edge `0.2257` maxDD `-0.8682`
- `news_risk_high->crypto_alt_1h` score `3.0317` n `101` status `ready` deltaP `16.6805` edge `0.188` maxDD `-2.058`
- `market_context_high->fx_4h` score `2.3264` n `50` status `ready` deltaP `30.2073` edge `0.014` maxDD `-0.0543`
- `news_risk_high->crypto_major_1h` score `2.2451` n `101` status `ready` deltaP `18.4769` edge `0.1162` maxDD `-2.8494`
- `market_context_high->fx_24h` score `1.8903` n `39` status `ready` deltaP `20.179` edge `0.0272` maxDD `-0.0027`
- `market_context_high->commodity_1h` score `1.4473` n `50` status `ready` deltaP `16.0539` edge `0.0411` maxDD `-0.2012`
- `market_context_high->fx_1h` score `1.0925` n `50` status `ready` deltaP `15.2096` edge `0.0071` maxDD `-0.063`
- `news_risk_high->commodity_24h` score `1.0721` n `98` status `ready` deltaP `22.775` edge `0.1162` maxDD `-3.4467`
- `news_risk_high->metal_4h` score `0.7286` n `101` status `ready` deltaP `18.3183` edge `0.044` maxDD `-2.0994`
- `news_risk_high->metal_1h` score `0.6425` n `101` status `ready` deltaP `14.7477` edge `0.0154` maxDD `-0.8144`
- `news_risk_high->equity_24h` score `0.6053` n `98` status `ready` deltaP `16.571` edge `0.0809` maxDD `-4.941`
- `market_context_high->metal_1h` score `0.2649` n `50` status `ready` deltaP `7.4012` edge `0.007` maxDD `-0.4568`
- `news_risk_high->equity_1h` score `0.2269` n `101` status `ready` deltaP `5.2143` edge `0.0247` maxDD `-0.9112`
- `news_risk_high->metal_24h` score `0.2195` n `98` status `ready` deltaP `15.5046` edge `0.0092` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
