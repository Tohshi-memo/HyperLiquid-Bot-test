# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T06:52:33.267638+00:00`
- Price records: `672`
- Market context records: `7751`
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

- `market_context_high->equity_24h` score `5.1411` n `132` status `ready` deltaP `22.5319` edge `0.4124` maxDD `-6.0681`
- `market_context_high->crypto_major_1h` score `0.8547` n `133` status `ready` deltaP `12.11` edge `0.0346` maxDD `-1.5286`
- `market_context_high->metal_24h` score `0.6906` n `133` status `ready` deltaP `8.584` edge `0.2094` maxDD `-2.3927`
- `market_context_high->equity_1h` score `0.5042` n `133` status `ready` deltaP `8.3463` edge `0.0723` maxDD `-4.2072`
- `market_context_high->crypto_major_4h` score `0.4781` n `133` status `ready` deltaP `12.5172` edge `0.1282` maxDD `-6.7444`
- `market_context_high->fx_24h` score `0.4063` n `132` status `ready` deltaP `19.0872` edge `0.0336` maxDD `-3.0343`
- `market_context_high->index_1h` score `0.3914` n `133` status `ready` deltaP `9.0949` edge `0.015` maxDD `-0.7743`
- `market_context_high->equity_4h` score `0.3864` n `133` status `ready` deltaP `1.9694` edge `0.2277` maxDD `-6.9701`
- `market_context_high->crypto_alt_4h` score `0.2292` n `133` status `ready` deltaP `6.8276` edge `0.0853` maxDD `-3.9374`
- `market_context_high->crypto_alt_1h` score `0.0201` n `133` status `ready` deltaP `3.5298` edge `0.0214` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `-0.194` n `133` status `ready` deltaP `3.5449` edge `0.0061` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.2561` n `133` status `ready` deltaP `10.5585` edge `0.0426` maxDD `-1.3325`
- `market_context_high->commodity_4h` score `-0.2908` n `133` status `ready` deltaP `3.2581` edge `0.0134` maxDD `-1.0817`
- `market_context_high->fx_1h` score `-0.4639` n `133` status `ready` deltaP `0.0734` edge `-0.0004` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.7896` n `133` status `ready` deltaP `2.1656` edge `0.0201` maxDD `-0.6936`
- `market_context_high->metal_4h` score `-1.4163` n `133` status `ready` deltaP `1.5954` edge `0.0768` maxDD `-1.4368`
- `market_context_high->fx_4h` score `-1.4761` n `133` status `ready` deltaP `-3.8559` edge `-0.0007` maxDD `-1.6936`
- `market_context_high->commodity_24h` score `-1.6313` n `132` status `ready` deltaP `5.6858` edge `-0.0155` maxDD `-7.0012`
- `market_context_high->unknown_1h` score `-2.268` n `133` status `ready` deltaP `-1.4238` edge `-0.1205` maxDD `-1.054`
- `market_context_high->index_24h` score `-2.2975` n `132` status `ready` deltaP `-16.3631` edge `0.0248` maxDD `-2.1544`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
