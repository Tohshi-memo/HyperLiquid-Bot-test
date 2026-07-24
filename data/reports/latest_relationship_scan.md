# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T07:07:26.181737+00:00`
- Price records: `672`
- Market context records: `7752`
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

- `market_context_high->equity_24h` score `5.2211` n `132` status `ready` deltaP `22.7061` edge `0.4179` maxDD `-6.0681`
- `market_context_high->crypto_major_1h` score `0.8499` n `133` status `ready` deltaP `12.11` edge `0.0342` maxDD `-1.5286`
- `market_context_high->metal_24h` score `0.7237` n `133` status `ready` deltaP `8.7576` edge `0.211` maxDD `-2.3927`
- `market_context_high->equity_1h` score `0.5018` n `133` status `ready` deltaP `8.3463` edge `0.0721` maxDD `-4.2072`
- `market_context_high->crypto_major_4h` score `0.4745` n `133` status `ready` deltaP `12.5172` edge `0.1279` maxDD `-6.7444`
- `market_context_high->fx_24h` score `0.4177` n `132` status `ready` deltaP `19.2615` edge `0.0339` maxDD `-3.0343`
- `market_context_high->index_1h` score `0.3902` n `133` status `ready` deltaP `9.0949` edge `0.0149` maxDD `-0.7743`
- `market_context_high->equity_4h` score `0.3895` n `133` status `ready` deltaP `1.9694` edge `0.2281` maxDD `-6.9701`
- `market_context_high->crypto_alt_4h` score `0.2256` n `133` status `ready` deltaP `6.8276` edge `0.085` maxDD `-3.9374`
- `market_context_high->crypto_alt_1h` score `0.0189` n `133` status `ready` deltaP `3.5298` edge `0.0213` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `-0.1772` n `133` status `ready` deltaP `3.6951` edge `0.0065` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.2569` n `133` status `ready` deltaP `10.5585` edge `0.0425` maxDD `-1.3325`
- `market_context_high->commodity_4h` score `-0.2666` n `133` status `ready` deltaP `3.411` edge `0.0144` maxDD `-1.0817`
- `market_context_high->fx_1h` score `-0.4639` n `133` status `ready` deltaP `0.0734` edge `-0.0004` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.8052` n `133` status `ready` deltaP `2.0159` edge `0.0198` maxDD `-0.6936`
- `market_context_high->metal_4h` score `-1.4175` n `133` status `ready` deltaP `1.5954` edge `0.0767` maxDD `-1.4368`
- `market_context_high->fx_4h` score `-1.4761` n `133` status `ready` deltaP `-3.8559` edge `-0.0007` maxDD `-1.6936`
- `market_context_high->commodity_24h` score `-1.6133` n `132` status `ready` deltaP `5.6858` edge `-0.014` maxDD `-7.0012`
- `market_context_high->index_24h` score `-2.2791` n `132` status `ready` deltaP `-16.1889` edge `0.026` maxDD `-2.1544`
- `market_context_high->unknown_1h` score `-2.2836` n `133` status `ready` deltaP `-1.5735` edge `-0.1208` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
