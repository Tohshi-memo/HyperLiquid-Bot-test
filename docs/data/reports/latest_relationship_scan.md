# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T08:22:17.851360+00:00`
- Price records: `672`
- Market context records: `1928`
- Flow alert records: `7449`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7540`

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

- `market_context_high->crypto_alt_4h` score `7.4608` n `207` status `ready` deltaP `23.5353` edge `0.5793` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.9589` n `207` status `ready` deltaP `28.6218` edge `0.5137` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `3.5976` n `207` status `ready` deltaP `17.2035` edge `0.3875` maxDD `-9.8581`
- `market_context_high->equity_4h` score `2.2282` n `207` status `ready` deltaP `13.9552` edge `0.2021` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `0.6799` n `219` status `ready` deltaP `8.1556` edge `0.1009` maxDD `-3.2225`
- `market_context_high->unknown_24h` score `0.6364` n `196` status `ready` deltaP `13.9916` edge `0.4918` maxDD `-35.8966`
- `market_context_high->crypto_alt_1h` score `0.4922` n `219` status `ready` deltaP `7.1228` edge `0.1049` maxDD `-4.9097`
- `market_context_high->metal_24h` score `0.3474` n `196` status `ready` deltaP `12.2626` edge `0.1898` maxDD `-12.7414`
- `market_context_high->index_4h` score `0.2441` n `207` status `ready` deltaP `8.6905` edge `0.0713` maxDD `-3.7119`
- `market_context_high->index_24h` score `0.1838` n `196` status `ready` deltaP `4.2233` edge `0.11` maxDD `-4.1604`
- `market_context_high->equity_1h` score `-0.1981` n `219` status `ready` deltaP `4.4808` edge `0.033` maxDD `-2.6836`
- `market_context_high->fx_24h` score `-0.2429` n `196` status `ready` deltaP `10.1793` edge `0.0168` maxDD `-1.3925`
- `market_context_high->fx_1h` score `-0.6588` n `219` status `ready` deltaP `-3.275` edge `0.0006` maxDD `-0.3914`
- `market_context_high->metal_1h` score `-0.6667` n `219` status `ready` deltaP `4.802` edge `0.0161` maxDD `-6.3532`
- `market_context_high->index_1h` score `-0.6905` n `219` status `ready` deltaP `-0.2802` edge `0.0075` maxDD `-1.7205`
- `market_context_high->fx_4h` score `-0.9037` n `207` status `ready` deltaP `-3.9516` edge `-0.0007` maxDD `-1.1056`
- `market_context_high->metal_4h` score `-1.0337` n `207` status `ready` deltaP `9.622` edge `0.1189` maxDD `-12.5349`
- `market_context_high->unknown_1h` score `-1.252` n `219` status `ready` deltaP `1.808` edge `-0.0212` maxDD `-3.6151`
- `market_context_high->equity_24h` score `-1.2935` n `196` status `ready` deltaP `6.9374` edge `0.3358` maxDD `-33.1875`
- `market_context_high->commodity_1h` score `-1.9905` n `219` status `ready` deltaP `1.1566` edge `-0.0071` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
