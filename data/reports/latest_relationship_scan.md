# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T04:52:29.617669+00:00`
- Price records: `672`
- Market context records: `7743`
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

- `market_context_high->equity_24h` score `4.5148` n `132` status `ready` deltaP `21.1382` edge `0.3695` maxDD `-6.0681`
- `market_context_high->crypto_major_1h` score `0.9782` n `133` status `ready` deltaP `12.8585` edge `0.0399` maxDD `-1.5286`
- `market_context_high->crypto_major_4h` score `0.6713` n `133` status `ready` deltaP `13.4318` edge `0.1382` maxDD `-6.7444`
- `market_context_high->equity_1h` score `0.5546` n `133` status `ready` deltaP `8.4964` edge `0.0755` maxDD `-4.2072`
- `market_context_high->crypto_alt_4h` score `0.449` n `133` status `ready` deltaP `7.8947` edge `0.0965` maxDD `-3.9374`
- `market_context_high->equity_4h` score `0.4017` n `133` status `ready` deltaP `1.6636` edge `0.2317` maxDD `-6.9701`
- `market_context_high->index_1h` score `0.3938` n `133` status `ready` deltaP `9.0949` edge `0.0152` maxDD `-0.7743`
- `market_context_high->metal_24h` score `0.3791` n `133` status `ready` deltaP `7.1951` edge `0.1927` maxDD `-2.3927`
- `market_context_high->fx_24h` score `0.3166` n `132` status `ready` deltaP `17.6935` edge `0.0314` maxDD `-3.0343`
- `market_context_high->crypto_alt_1h` score `0.1053` n `133` status `ready` deltaP `3.9789` edge `0.0255` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `-0.2024` n `133` status `ready` deltaP `3.3948` edge `0.0064` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.2569` n `133` status `ready` deltaP `10.5585` edge `0.0425` maxDD `-1.3325`
- `market_context_high->commodity_4h` score `-0.3126` n `133` status `ready` deltaP `3.1052` edge `0.0126` maxDD `-1.0817`
- `market_context_high->fx_1h` score `-0.4639` n `133` status `ready` deltaP `0.0734` edge `-0.0004` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.7656` n `133` status `ready` deltaP `2.465` edge `0.0201` maxDD `-0.6936`
- `market_context_high->metal_4h` score `-1.4661` n `133` status `ready` deltaP `1.1381` edge `0.0757` maxDD `-1.4368`
- `market_context_high->fx_4h` score `-1.5031` n `133` status `ready` deltaP `-4.3147` edge `-0.0011` maxDD `-1.6936`
- `market_context_high->commodity_24h` score `-1.6853` n `132` status `ready` deltaP `5.6858` edge `-0.02` maxDD `-7.0012`
- `market_context_high->unknown_1h` score `-2.2392` n `133` status `ready` deltaP `-1.2741` edge `-0.1191` maxDD `-1.054`
- `market_context_high->index_24h` score `-2.4503` n `132` status `ready` deltaP `-17.7568` edge `0.0145` maxDD `-2.1544`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
