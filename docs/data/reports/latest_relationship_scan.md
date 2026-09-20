# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T12:07:25.815330+00:00`
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

- `news_risk_high->crypto_major_24h` score `22.4532` n `97` status `ready` deltaP `6.9087` edge `2.4797` maxDD `-44.039`
- `news_risk_high->crypto_alt_24h` score `20.8645` n `97` status `ready` deltaP `15.3512` edge `2.0923` maxDD `-30.4749`
- `market_context_high->unknown_4h` score `19.6927` n `60` status `ready` deltaP `1.4024` edge `1.6467` maxDD `-0.5326`
- `news_risk_high->crypto_alt_4h` score `5.8618` n `101` status `ready` deltaP `22.5776` edge `0.4589` maxDD `-7.675`
- `market_context_high->commodity_24h` score `5.6991` n `54` status `ready` deltaP `30.7871` edge `0.3222` maxDD `-0.8682`
- `news_risk_high->crypto_major_4h` score `4.3573` n `101` status `ready` deltaP `21.358` edge `0.3465` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `3.9891` n `60` status `ready` deltaP `34.2378` edge `0.1175` maxDD `-0.0659`
- `news_risk_high->crypto_alt_1h` score `3.0462` n `101` status `ready` deltaP `16.5308` edge `0.1902` maxDD `-2.058`
- `market_context_high->fx_4h` score `2.2914` n `60` status `ready` deltaP `29.6545` edge `0.0106` maxDD `-0.0543`
- `news_risk_high->crypto_major_1h` score `2.2056` n `101` status `ready` deltaP `18.1775` edge `0.1149` maxDD `-2.8494`
- `market_context_high->fx_24h` score `1.5223` n `54` status `ready` deltaP `18.1134` edge `0.0103` maxDD `-0.0027`
- `market_context_high->commodity_1h` score `1.2638` n `65` status `ready` deltaP `15.4468` edge `0.0317` maxDD `-0.3491`
- `news_risk_high->equity_24h` score `1.0518` n `97` status `ready` deltaP `17.3916` edge `0.1053` maxDD `-4.6876`
- `news_risk_high->commodity_24h` score `0.9861` n `97` status `ready` deltaP `22.5015` edge `0.107` maxDD `-3.4467`
- `market_context_high->fx_1h` score `0.6617` n `65` status `ready` deltaP `10.7646` edge `0.005` maxDD `-0.063`
- `news_risk_high->metal_1h` score `0.6173` n `101` status `ready` deltaP `14.4483` edge `0.0153` maxDD `-0.8144`
- `news_risk_high->metal_4h` score `0.586` n `101` status `ready` deltaP `16.6415` edge `0.0433` maxDD `-2.0994`
- `news_risk_high->metal_24h` score `0.3637` n `97` status `ready` deltaP `16.2515` edge `0.0227` maxDD `-2.4203`
- `market_context_high->metal_1h` score `0.2632` n `65` status `ready` deltaP `7.5633` edge `0.0057` maxDD `-0.4568`
- `news_risk_high->equity_1h` score `0.2196` n `101` status `ready` deltaP `5.364` edge `0.0231` maxDD `-0.9112`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
