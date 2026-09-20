# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T17:37:28.011038+00:00`
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

- `news_risk_high->crypto_major_24h` score `23.2118` n `98` status `ready` deltaP `10.0128` edge `2.5534` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `20.3403` n `98` status `ready` deltaP `15.0935` edge `2.0825` maxDD `-32.7147`
- `market_context_high->unknown_4h` score `16.5614` n `46` status `ready` deltaP `-0.1193` edge `1.3959` maxDD `-0.5326`
- `news_risk_high->crypto_alt_4h` score `5.7051` n `101` status `ready` deltaP `23.0349` edge `0.4428` maxDD `-7.675`
- `market_context_high->commodity_4h` score `4.4193` n `46` status `ready` deltaP `36.1943` edge `0.1403` maxDD `-0.0659`
- `news_risk_high->crypto_major_4h` score `4.3676` n `101` status `ready` deltaP `21.9678` edge `0.3433` maxDD `-8.0625`
- `market_context_high->commodity_24h` score `3.4885` n `35` status `ready` deltaP `20.7342` edge `0.205` maxDD `-0.8682`
- `news_risk_high->crypto_alt_1h` score `2.9225` n `101` status `ready` deltaP `16.6805` edge `0.1789` maxDD `-2.058`
- `market_context_high->fx_4h` score `2.2386` n `46` status `ready` deltaP `28.9899` edge `0.0148` maxDD `-0.0543`
- `news_risk_high->crypto_major_1h` score `2.1923` n `101` status `ready` deltaP `18.6266` edge `0.1108` maxDD `-2.8494`
- `market_context_high->fx_24h` score `2.039` n `35` status `ready` deltaP `20.9276` edge `0.0346` maxDD `-0.0027`
- `market_context_high->commodity_1h` score `1.3703` n `52` status `ready` deltaP `15.3616` edge `0.0393` maxDD `-0.2012`
- `market_context_high->fx_1h` score `1.18` n `52` status `ready` deltaP `16.2137` edge `0.0077` maxDD `-0.063`
- `news_risk_high->commodity_24h` score `1.0627` n `98` status `ready` deltaP `22.775` edge `0.115` maxDD `-3.4467`
- `news_risk_high->metal_4h` score `0.6506` n `101` status `ready` deltaP `17.4037` edge `0.0436` maxDD `-2.0994`
- `news_risk_high->metal_1h` score `0.6173` n `101` status `ready` deltaP `14.4483` edge `0.0153` maxDD `-0.8144`
- `news_risk_high->equity_24h` score `0.5686` n `98` status `ready` deltaP `16.3974` edge `0.079` maxDD `-4.941`
- `market_context_high->metal_1h` score `0.4357` n `52` status `ready` deltaP `10.6403` edge `0.0073` maxDD `-0.4568`
- `news_risk_high->equity_1h` score `0.2328` n `101` status `ready` deltaP `5.364` edge `0.0242` maxDD `-0.9112`
- `news_risk_high->metal_24h` score `0.1683` n `98` status `ready` deltaP `14.9837` edge `0.0061` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
