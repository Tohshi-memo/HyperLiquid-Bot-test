# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T08:37:30.088726+00:00`
- Price records: `672`
- Market context records: `7861`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14661`

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

- `market_context_high->equity_24h` score `11.3697` n `128` status `ready` deltaP `28.8995` edge `0.889` maxDD `-6.0681`
- `market_context_high->equity_4h` score `1.5127` n `129` status `ready` deltaP `5.5294` edge `0.3283` maxDD `-6.6986`
- `market_context_high->commodity_24h` score `1.4193` n `128` status `ready` deltaP `22.2935` edge `0.128` maxDD `-7.0012`
- `market_context_high->metal_24h` score `1.3604` n `129` status `ready` deltaP `9.8934` edge `0.2394` maxDD `-2.3594`
- `market_context_high->crypto_major_4h` score `1.2253` n `129` status `ready` deltaP `14.8374` edge `0.175` maxDD `-6.7444`
- `market_context_high->crypto_major_1h` score `1.0055` n `129` status `ready` deltaP `12.3149` edge `0.0458` maxDD `-1.5286`
- `market_context_high->fx_24h` score `0.9147` n `128` status `ready` deltaP `26.6155` edge `0.0486` maxDD `-3.0343`
- `market_context_high->crypto_alt_4h` score `0.8738` n `129` status `ready` deltaP `9.0801` edge `0.124` maxDD `-3.9374`
- `market_context_high->commodity_4h` score `0.516` n `129` status `ready` deltaP `9.0534` edge `0.042` maxDD `-1.0817`
- `market_context_high->equity_1h` score `0.4883` n `129` status `ready` deltaP `7.3887` edge `0.0951` maxDD `-4.2072`
- `market_context_high->index_1h` score `0.4115` n `129` status `ready` deltaP `9.016` edge `0.0172` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.2389` n `129` status `ready` deltaP `4.5096` edge `0.0331` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `0.1592` n `129` status `ready` deltaP `6.7602` edge `0.0141` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.1705` n `129` status `ready` deltaP `10.9452` edge `0.051` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.3199` n `129` status `ready` deltaP `-0.3108` edge `-0.0002` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.8889` n `129` status `ready` deltaP `0.8796` edge `0.0204` maxDD `-0.6936`
- `market_context_high->index_24h` score `-1.1263` n `128` status `ready` deltaP `-4.413` edge `0.0947` maxDD `-2.1079`
- `market_context_high->metal_4h` score `-1.3059` n `129` status `ready` deltaP `2.4957` edge `0.08` maxDD `-1.4368`
- `market_context_high->fx_4h` score `-1.4257` n `129` status `ready` deltaP `-3.147` edge `0.0009` maxDD `-1.6833`
- `market_context_high->crypto_alt_24h` score `-1.5589` n `129` status `ready` deltaP `15.7605` edge `0.2246` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
