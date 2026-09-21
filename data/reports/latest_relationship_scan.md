# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T23:52:27.132706+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9940`

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

- `market_context_high->unknown_4h` score `29.4553` n `56` status `ready` deltaP `2.2649` edge `2.4545` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `11.4664` n `101` status `ready` deltaP `0.5053` edge `1.638` maxDD `-46.1999`
- `market_context_high->crypto_major_24h` score `10.5803` n `51` status `ready` deltaP `6.6789` edge `1.394` maxDD `-40.5469`
- `news_risk_high->crypto_alt_24h` score `6.856` n `101` status `ready` deltaP `0.8904` edge `1.0535` maxDD `-32.7147`
- `market_context_high->equity_24h` score `5.4082` n `51` status `ready` deltaP `-0.0919` edge `0.6903` maxDD `-15.1201`
- `news_risk_high->crypto_alt_4h` score `3.1766` n `101` status `ready` deltaP `15.4129` edge `0.2829` maxDD `-7.675`
- `news_risk_high->commodity_24h` score `2.4658` n `101` status `ready` deltaP `30.6621` edge `0.2423` maxDD `-3.4467`
- `news_risk_high->crypto_alt_1h` score `2.3805` n `101` status `ready` deltaP `14.5847` edge `0.1477` maxDD `-2.058`
- `market_context_high->index_24h` score `2.3124` n `51` status `ready` deltaP `3.9012` edge `0.2354` maxDD `-1.4969`
- `news_risk_high->crypto_major_4h` score `2.1996` n `101` status `ready` deltaP `16.6324` edge `0.1982` maxDD `-8.0625`
- `news_risk_high->crypto_major_1h` score `1.6156` n `101` status `ready` deltaP `15.932` edge `0.0807` maxDD `-2.8494`
- `news_risk_high->fx_4h` score `0.4826` n `101` status `ready` deltaP `11.537` edge `0.0269` maxDD `-0.421`
- `news_risk_high->metal_1h` score `0.4256` n `101` status `ready` deltaP `12.6519` edge `0.0113` maxDD `-0.8144`
- `market_context_high->equity_1h` score `0.4251` n `56` status `ready` deltaP `2.9192` edge `0.0413` maxDD `-0.36`
- `market_context_high->fx_1h` score `0.3816` n `56` status `ready` deltaP `9.2173` edge `0.006` maxDD `-0.1854`
- `market_context_high->index_1h` score `0.3743` n `56` status `ready` deltaP `6.9504` edge `0.0104` maxDD `-0.0435`
- `market_context_high->metal_1h` score `0.3378` n `56` status `ready` deltaP `6.234` edge `0.0174` maxDD `-0.1314`
- `market_context_high->metal_24h` score `0.2377` n `51` status `ready` deltaP `17.0241` edge `-0.0703` maxDD `-0.2042`
- `news_risk_high->metal_4h` score `0.1967` n `101` status `ready` deltaP `13.4403` edge `0.0322` maxDD `-2.0994`
- `market_context_high->index_4h` score `0.044` n `56` status `ready` deltaP `10.4747` edge `-0.0005` maxDD `-1.0949`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
