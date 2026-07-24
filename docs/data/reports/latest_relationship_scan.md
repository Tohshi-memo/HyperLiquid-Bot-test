# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T09:22:29.370423+00:00`
- Price records: `672`
- Market context records: `7761`
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

- `market_context_high->equity_24h` score `5.8961` n `132` status `ready` deltaP `24.2741` edge `0.4637` maxDD `-6.0681`
- `market_context_high->metal_24h` score `0.9771` n `133` status `ready` deltaP `10.3201` edge `0.2217` maxDD `-2.3927`
- `market_context_high->crypto_major_1h` score `0.8188` n `133` status `ready` deltaP `11.8106` edge `0.0336` maxDD `-1.5286`
- `market_context_high->fx_24h` score `0.5187` n `132` status `ready` deltaP `20.8294` edge `0.0364` maxDD `-3.0343`
- `market_context_high->crypto_major_4h` score `0.4781` n `133` status `ready` deltaP `12.5172` edge `0.1282` maxDD `-6.7444`
- `market_context_high->equity_4h` score `0.4074` n `133` status `ready` deltaP `1.9694` edge `0.2304` maxDD `-6.9701`
- `market_context_high->equity_1h` score `0.3542` n `133` status `ready` deltaP `7.4454` edge `0.0658` maxDD `-4.2072`
- `market_context_high->index_1h` score `0.3038` n `133` status `ready` deltaP `8.194` edge `0.0137` maxDD `-0.7743`
- `market_context_high->crypto_alt_4h` score `0.2366` n `133` status `ready` deltaP `6.9801` edge `0.0849` maxDD `-3.9374`
- `market_context_high->crypto_alt_1h` score `-0.005` n `133` status `ready` deltaP `3.3801` edge `0.0203` maxDD `-1.4603`
- `market_context_high->commodity_4h` score `-0.0449` n `133` status `ready` deltaP `4.7872` edge `0.0237` maxDD `-1.0817`
- `market_context_high->commodity_1h` score `-0.074` n `133` status `ready` deltaP `4.596` edge `0.0091` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.26` n `133` status `ready` deltaP `10.5585` edge `0.0421` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.4243` n `133` status `ready` deltaP `0.5239` edge `-0.0001` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.8818` n `133` status `ready` deltaP `1.2674` edge `0.0184` maxDD `-0.6936`
- `market_context_high->commodity_24h` score `-1.3521` n `132` status `ready` deltaP `6.7311` edge `0.0008` maxDD `-7.0012`
- `market_context_high->fx_4h` score `-1.4769` n `133` status `ready` deltaP `-3.8559` edge `-0.0008` maxDD `-1.6936`
- `market_context_high->metal_4h` score `-1.5449` n `133` status `ready` deltaP `0.5283` edge `0.0732` maxDD `-1.4368`
- `market_context_high->index_24h` score `-2.1234` n `132` status `ready` deltaP `-14.621` edge `0.0355` maxDD `-2.1544`
- `market_context_high->unknown_1h` score `-2.3219` n `133` status `ready` deltaP `-2.0226` edge `-0.121` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
