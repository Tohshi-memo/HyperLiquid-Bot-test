# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T07:52:27.100501+00:00`
- Price records: `672`
- Market context records: `7755`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14676`

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

- `market_context_high->equity_24h` score `5.4093` n `132` status `ready` deltaP `23.2288` edge `0.4301` maxDD `-6.0681`
- `market_context_high->metal_24h` score `0.805` n `133` status `ready` deltaP `9.2784` edge `0.2143` maxDD `-2.3927`
- `market_context_high->crypto_major_1h` score `0.7876` n `133` status `ready` deltaP `11.6609` edge `0.032` maxDD `-1.5286`
- `market_context_high->crypto_major_4h` score `0.4673` n `133` status `ready` deltaP `12.5172` edge `0.1273` maxDD `-6.7444`
- `market_context_high->fx_24h` score `0.4495` n `132` status `ready` deltaP `19.7841` edge `0.0345` maxDD `-3.0343`
- `market_context_high->equity_1h` score `0.4286` n `133` status `ready` deltaP `7.8958` edge `0.069` maxDD `-4.2072`
- `market_context_high->equity_4h` score `0.3911` n `133` status `ready` deltaP `1.9694` edge `0.2283` maxDD `-6.9701`
- `market_context_high->index_1h` score `0.3482` n `133` status `ready` deltaP `8.6444` edge `0.0144` maxDD `-0.7743`
- `market_context_high->crypto_alt_4h` score `0.2112` n `133` status `ready` deltaP `6.8276` edge `0.0838` maxDD `-3.9374`
- `market_context_high->crypto_alt_1h` score `-0.0422` n `133` status `ready` deltaP `3.0807` edge `0.0192` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `-0.1292` n `133` status `ready` deltaP `4.1455` edge `0.0075` maxDD `-0.6722`
- `market_context_high->commodity_4h` score `-0.1927` n `133` status `ready` deltaP `3.8698` edge `0.0175` maxDD `-1.0817`
- `market_context_high->index_4h` score `-0.2584` n `133` status `ready` deltaP `10.5585` edge `0.0423` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.5023` n `133` status `ready` deltaP `-0.377` edge `-0.0006` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.8423` n `133` status `ready` deltaP `1.7165` edge `0.0187` maxDD `-0.6936`
- `market_context_high->metal_4h` score `-1.4673` n `133` status `ready` deltaP `1.1381` edge `0.0756` maxDD `-1.4368`
- `market_context_high->fx_4h` score `-1.4936` n `133` status `ready` deltaP `-4.1617` edge `-0.0009` maxDD `-1.6936`
- `market_context_high->commodity_24h` score `-1.5266` n `132` status `ready` deltaP `6.0342` edge `-0.0091` maxDD `-7.0012`
- `market_context_high->index_24h` score `-2.2293` n `132` status `ready` deltaP `-15.6663` edge `0.0289` maxDD `-2.1544`
- `market_context_high->unknown_1h` score `-2.2824` n `133` status `ready` deltaP `-1.5735` edge `-0.1207` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
