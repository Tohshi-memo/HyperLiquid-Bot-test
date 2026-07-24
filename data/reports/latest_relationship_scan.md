# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T09:58:58.354327+00:00`
- Price records: `672`
- Market context records: `7764`
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

- `market_context_high->equity_24h` score `6.074` n `132` status `ready` deltaP `24.6225` edge `0.4762` maxDD `-6.0681`
- `market_context_high->metal_24h` score `1.0313` n `133` status `ready` deltaP `10.6673` edge `0.2239` maxDD `-2.3927`
- `market_context_high->crypto_major_1h` score `0.8703` n `133` status `ready` deltaP `12.11` edge `0.0359` maxDD `-1.5286`
- `market_context_high->fx_24h` score `0.5415` n `132` status `ready` deltaP `21.1778` edge `0.037` maxDD `-3.0343`
- `market_context_high->crypto_major_4h` score `0.4805` n `133` status `ready` deltaP `12.5172` edge `0.1284` maxDD `-6.7444`
- `market_context_high->equity_4h` score `0.4113` n `133` status `ready` deltaP `1.9694` edge `0.2309` maxDD `-6.9701`
- `market_context_high->equity_1h` score `0.3734` n `133` status `ready` deltaP `7.4454` edge `0.0674` maxDD `-4.2072`
- `market_context_high->index_1h` score `0.305` n `133` status `ready` deltaP `8.194` edge `0.0138` maxDD `-0.7743`
- `market_context_high->crypto_alt_4h` score `0.2426` n `133` status `ready` deltaP `6.9801` edge `0.0854` maxDD `-3.9374`
- `market_context_high->crypto_alt_1h` score `0.0417` n `133` status `ready` deltaP `3.6795` edge `0.0222` maxDD `-1.4603`
- `market_context_high->commodity_4h` score `0.0096` n `133` status `ready` deltaP `5.093` edge `0.0262` maxDD `-1.0817`
- `market_context_high->commodity_1h` score `-0.0379` n `133` status `ready` deltaP `4.8963` edge `0.0101` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.26` n `133` status `ready` deltaP `10.5585` edge `0.0421` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.399` n `133` status `ready` deltaP `0.8242` edge `0.0` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.8794` n `133` status `ready` deltaP `1.2674` edge `0.0186` maxDD `-0.6936`
- `market_context_high->commodity_24h` score `-1.2762` n `132` status `ready` deltaP `7.0795` edge `0.0048` maxDD `-7.0012`
- `market_context_high->fx_4h` score `-1.4769` n `133` status `ready` deltaP `-3.8559` edge `-0.0008` maxDD `-1.6936`
- `market_context_high->metal_4h` score `-1.5836` n `133` status `ready` deltaP `0.2235` edge `0.072` maxDD `-1.4368`
- `market_context_high->index_24h` score `-2.085` n `132` status `ready` deltaP `-14.2725` edge `0.0381` maxDD `-2.1544`
- `market_context_high->unknown_1h` score `-2.3255` n `133` status `ready` deltaP `-2.0226` edge `-0.1213` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
