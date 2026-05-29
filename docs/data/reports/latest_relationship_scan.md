# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T09:22:22.115177+00:00`
- Price records: `672`
- Market context records: `2231`
- Flow alert records: `8316`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9178`

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

- `news_risk_high->crypto_alt_24h` score `25.7856` n `33` status `ready` deltaP `56.4394` edge `1.8314` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `14.5357` n `33` status `ready` deltaP `46.7961` edge `0.9433` maxDD `-3.1836`
- `market_context_high->crypto_alt_4h` score `12.9152` n `131` status `ready` deltaP `37.1695` edge `0.9221` maxDD `-5.1574`
- `news_risk_high->equity_24h` score `12.5824` n `33` status `ready` deltaP `37.7683` edge `0.8282` maxDD `-2.1831`
- `market_context_high->crypto_major_4h` score `11.7291` n `131` status `ready` deltaP `42.2129` edge `0.749` maxDD `-1.9063`
- `news_risk_high->unknown_24h` score `9.4926` n `33` status `ready` deltaP `37.3422` edge `0.5647` maxDD `-1.4744`
- `news_risk_high->crypto_major_24h` score `7.4725` n `33` status `ready` deltaP `19.2867` edge `0.8875` maxDD `-3.3119`
- `market_context_high->unknown_4h` score `5.486` n `131` status `ready` deltaP `20.8388` edge `0.3747` maxDD `-1.8499`
- `news_risk_high->commodity_4h` score `3.9418` n `43` status `ready` deltaP `33.0721` edge `0.352` maxDD `-3.0367`
- `market_context_high->equity_4h` score `3.4568` n `131` status `ready` deltaP `23.1486` edge `0.2329` maxDD `-4.5993`
- `market_context_high->index_4h` score `3.3159` n `131` status `ready` deltaP `26.6535` edge `0.1606` maxDD `-1.6242`
- `market_context_high->crypto_major_1h` score `3.1425` n `143` status `ready` deltaP `17.3831` edge `0.1937` maxDD `-1.817`
- `news_risk_high->fx_24h` score `2.9604` n `33` status `ready` deltaP `31.0606` edge `0.0581` maxDD `-0.1442`
- `market_context_high->crypto_alt_1h` score `2.9147` n `143` status `ready` deltaP `16.2839` edge `0.2207` maxDD `-4.9097`
- `news_risk_high->commodity_24h` score `2.3667` n `33` status `ready` deltaP `-1.7677` edge `0.2907` maxDD `-3.202`
- `news_risk_high->fx_4h` score `2.1622` n `43` status `ready` deltaP `27.4319` edge `0.0157` maxDD `-0.1382`
- `market_context_high->unknown_24h` score `1.9454` n `131` status `ready` deltaP `23.5555` edge `0.4508` maxDD `-30.3243`
- `market_context_high->index_24h` score `1.6514` n `131` status `ready` deltaP `8.4924` edge `0.1961` maxDD `-3.8749`
- `news_risk_high->index_24h` score `1.374` n `33` status `ready` deltaP `10.2273` edge `0.0882` maxDD `-1.3507`
- `market_context_high->metal_4h` score `1.2985` n `131` status `ready` deltaP `16.8684` edge `0.1345` maxDD `-4.7664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
