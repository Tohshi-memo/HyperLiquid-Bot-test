# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T23:51:01.910695+00:00`
- Price records: `672`
- Market context records: `7824`
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

- `market_context_high->equity_24h` score `9.279` n `132` status `ready` deltaP `28.5507` edge `0.7171` maxDD `-6.0681`
- `market_context_high->metal_24h` score `1.406` n `133` status `ready` deltaP `13.1911` edge `0.2383` maxDD `-2.3927`
- `market_context_high->equity_4h` score `1.3124` n `133` status `ready` deltaP `5.3333` edge `0.324` maxDD `-6.9701`
- `market_context_high->crypto_major_4h` score `1.224` n `133` status `ready` deltaP `14.9562` edge `0.1741` maxDD `-6.7444`
- `market_context_high->crypto_major_1h` score `1.0885` n `133` status `ready` deltaP `13.3076` edge `0.0461` maxDD `-1.5286`
- `market_context_high->crypto_alt_4h` score `0.8883` n `133` status `ready` deltaP `8.9618` edge `0.126` maxDD `-3.9374`
- `market_context_high->fx_24h` score `0.8296` n `132` status `ready` deltaP `25.2187` edge `0.047` maxDD `-3.0343`
- `market_context_high->equity_1h` score `0.7622` n `133` status `ready` deltaP `8.1961` edge `0.0948` maxDD `-4.2072`
- `market_context_high->commodity_24h` score `0.5014` n `132` status `ready` deltaP `16.7747` edge `0.0883` maxDD `-7.0012`
- `market_context_high->commodity_4h` score `0.4493` n `133` status `ready` deltaP `8.6098` edge `0.0394` maxDD `-1.0817`
- `market_context_high->index_1h` score `0.3398` n `133` status `ready` deltaP `8.194` edge `0.0167` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.2911` n `133` status `ready` deltaP `5.3262` edge `0.032` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `0.0653` n `133` status `ready` deltaP `5.7972` edge `0.0127` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.0721` n `133` status `ready` deltaP `12.8521` edge `0.0509` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.399` n `133` status `ready` deltaP `0.8242` edge `0.0` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.889` n `133` status `ready` deltaP `0.968` edge `0.0198` maxDD `-0.6936`
- `market_context_high->fx_4h` score `-1.3397` n `133` status `ready` deltaP `-1.5624` edge `0.0015` maxDD `-1.6936`
- `market_context_high->index_24h` score `-1.4032` n `132` status `ready` deltaP `-7.4005` edge `0.0797` maxDD `-2.1544`
- `market_context_high->metal_4h` score `-1.4261` n `133` status `ready` deltaP `1.443` edge `0.077` maxDD `-1.4368`
- `market_context_high->crypto_alt_24h` score `-2.1461` n `133` status `ready` deltaP `14.7431` edge `0.1561` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
