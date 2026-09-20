# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T17:52:25.478248+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9862`

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

- `news_risk_high->crypto_major_24h` score `23.2809` n `98` status `ready` deltaP `10.1864` edge `2.558` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `20.3379` n `98` status `ready` deltaP `15.0935` edge `2.0823` maxDD `-32.7147`
- `market_context_high->unknown_4h` score `16.509` n `45` status `ready` deltaP `-0.2643` edge `1.3925` maxDD `-0.5326`
- `news_risk_high->crypto_alt_4h` score `5.6365` n `101` status `ready` deltaP `22.8824` edge `0.4381` maxDD `-7.675`
- `market_context_high->commodity_4h` score `4.6145` n `45` status `ready` deltaP `37.9743` edge `0.1447` maxDD `-0.0659`
- `news_risk_high->crypto_major_4h` score `4.3388` n `101` status `ready` deltaP `21.9678` edge `0.3409` maxDD `-8.0625`
- `market_context_high->commodity_24h` score `3.3889` n `34` status `ready` deltaP `19.8938` edge `0.2023` maxDD `-0.8682`
- `news_risk_high->crypto_alt_1h` score `2.9225` n `101` status `ready` deltaP `16.6805` edge `0.1789` maxDD `-2.058`
- `market_context_high->fx_4h` score `2.2092` n `45` status `ready` deltaP `28.6517` edge `0.0146` maxDD `-0.0543`
- `news_risk_high->crypto_major_1h` score `2.2079` n `101` status `ready` deltaP `18.7763` edge `0.1111` maxDD `-2.8494`
- `market_context_high->fx_24h` score `2.0654` n `34` status `ready` deltaP `21.0171` edge `0.0362` maxDD `-0.0027`
- `market_context_high->commodity_1h` score `1.5134` n `52` status `ready` deltaP `17.135` edge `0.0394` maxDD `-0.2012`
- `news_risk_high->commodity_24h` score `1.0612` n `98` status `ready` deltaP `22.775` edge `0.1148` maxDD `-3.4467`
- `market_context_high->fx_1h` score `1.0346` n `52` status `ready` deltaP `14.4404` edge `0.0074` maxDD `-0.063`
- `news_risk_high->metal_4h` score `0.6506` n `101` status `ready` deltaP `17.4037` edge `0.0436` maxDD `-2.0994`
- `news_risk_high->metal_1h` score `0.6293` n `101` status `ready` deltaP `14.598` edge `0.0153` maxDD `-0.8144`
- `news_risk_high->equity_24h` score `0.5662` n `98` status `ready` deltaP `16.3974` edge `0.0788` maxDD `-4.941`
- `market_context_high->metal_1h` score `0.3419` n `52` status `ready` deltaP `8.8669` edge `0.0071` maxDD `-0.4568`
- `news_risk_high->equity_1h` score `0.2328` n `101` status `ready` deltaP `5.364` edge `0.0242` maxDD `-0.9112`
- `news_risk_high->metal_24h` score `0.1644` n `98` status `ready` deltaP `14.9837` edge `0.0056` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
