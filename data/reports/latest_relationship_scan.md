# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T08:37:24.771236+00:00`
- Price records: `672`
- Market context records: `7758`
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

- `market_context_high->equity_24h` score `5.6383` n `132` status `ready` deltaP `23.7514` edge `0.4457` maxDD `-6.0681`
- `market_context_high->metal_24h` score `0.8946` n `133` status `ready` deltaP `9.7992` edge `0.2183` maxDD `-2.3927`
- `market_context_high->crypto_major_1h` score `0.7624` n `133` status `ready` deltaP `11.3615` edge `0.0319` maxDD `-1.5286`
- `market_context_high->fx_24h` score `0.4845` n `132` status `ready` deltaP `20.3068` edge `0.0355` maxDD `-3.0343`
- `market_context_high->crypto_major_4h` score `0.4661` n `133` status `ready` deltaP `12.5172` edge `0.1272` maxDD `-6.7444`
- `market_context_high->equity_4h` score `0.3965` n `133` status `ready` deltaP `1.9694` edge `0.229` maxDD `-6.9701`
- `market_context_high->equity_1h` score `0.3806` n `133` status `ready` deltaP `7.5955` edge `0.067` maxDD `-4.2072`
- `market_context_high->index_1h` score `0.3326` n `133` status `ready` deltaP `8.4943` edge `0.0141` maxDD `-0.7743`
- `market_context_high->crypto_alt_4h` score `0.2088` n `133` status `ready` deltaP `6.8276` edge `0.0836` maxDD `-3.9374`
- `market_context_high->crypto_alt_1h` score `-0.0482` n `133` status `ready` deltaP `3.0807` edge `0.0187` maxDD `-1.4603`
- `market_context_high->commodity_4h` score `-0.1236` n `133` status `ready` deltaP `4.3285` edge `0.0202` maxDD `-1.0817`
- `market_context_high->commodity_1h` score `-0.128` n `133` status `ready` deltaP `4.1455` edge `0.0076` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.2592` n `133` status `ready` deltaP `10.5585` edge `0.0422` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.4627` n `133` status `ready` deltaP `0.0734` edge `-0.0003` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.8543` n `133` status `ready` deltaP `1.5668` edge `0.0187` maxDD `-0.6936`
- `market_context_high->commodity_24h` score `-1.4611` n `132` status `ready` deltaP `6.2084` edge `-0.0048` maxDD `-7.0012`
- `market_context_high->fx_4h` score `-1.4848` n `133` status `ready` deltaP `-4.0088` edge `-0.0008` maxDD `-1.6936`
- `market_context_high->metal_4h` score `-1.4891` n `133` status `ready` deltaP `0.9857` edge `0.0748` maxDD `-1.4368`
- `market_context_high->index_24h` score `-2.1771` n `132` status `ready` deltaP `-15.1436` edge `0.0321` maxDD `-2.1544`
- `market_context_high->unknown_1h` score `-2.2944` n `133` status `ready` deltaP `-1.7232` edge `-0.1207` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
