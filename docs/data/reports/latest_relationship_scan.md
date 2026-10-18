# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-18T01:52:26.273367+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9622`

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

- `risk_on_high->commodity_24h` score `7.0882` n `54` status `ready` deltaP `39.3728` edge `0.3282` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.0882` n `54` status `ready` deltaP `39.3728` edge `0.3282` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `1.2326` n `169` status `ready` deltaP `13.9153` edge `0.3504` maxDD `-15.2359`
- `risk_on_high->crypto_major_4h` score `0.3391` n `91` status `ready` deltaP `14.6761` edge `0.1937` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `0.3391` n `91` status `ready` deltaP `14.6761` edge `0.1937` maxDD `-11.1788`
- `market_context_high->crypto_major_1h` score `0.2617` n `169` status `ready` deltaP `2.8053` edge `0.092` maxDD `-3.7781`
- `risk_on_high->index_1h` score `-0.0004` n `91` status `ready` deltaP `4.8559` edge `0.006` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.0004` n `91` status `ready` deltaP `4.8559` edge `0.006` maxDD `-0.7394`
- `market_context_high->crypto_alt_1h` score `-0.1114` n `169` status `ready` deltaP `6.2414` edge `0.0991` maxDD `-7.3329`
- `market_context_high->index_1h` score `-0.2159` n `169` status `ready` deltaP `6.293` edge `0.0052` maxDD `-1.3195`
- `risk_on_high->fx_1h` score `-0.2804` n `91` status `ready` deltaP `0.7475` edge `-0.0029` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.2804` n `91` status `ready` deltaP `0.7475` edge `-0.0029` maxDD `-0.376`
- `market_context_high->commodity_24h` score `-0.2976` n `120` status `ready` deltaP `12.7061` edge `0.119` maxDD `-9.6139`
- `market_context_high->metal_1h` score `-0.3649` n `169` status `ready` deltaP `4.7798` edge `0.0083` maxDD `-0.9556`
- `market_context_high->metal_4h` score `-0.4137` n `169` status `ready` deltaP `8.5538` edge `0.0422` maxDD `-1.6961`
- `risk_on_high->equity_1h` score `-0.4188` n `91` status `ready` deltaP `9.5585` edge `0.031` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.4188` n `91` status `ready` deltaP `9.5585` edge `0.031` maxDD `-5.3696`
- `risk_on_high->metal_1h` score `-0.4782` n `91` status `ready` deltaP `1.1449` edge `0.0042` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4782` n `91` status `ready` deltaP `1.1449` edge `0.0042` maxDD `-0.8513`
- `market_context_high->fx_1h` score `-0.5436` n `169` status `ready` deltaP `-2.3802` edge `-0.0017` maxDD `-0.503`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
