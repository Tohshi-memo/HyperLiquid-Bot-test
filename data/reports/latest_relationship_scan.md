# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-15T06:52:27.642634+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9709`

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

- `market_context_high->crypto_alt_4h` score `7.9575` n `119` status `ready` deltaP `19.5211` edge `0.6774` maxDD `-9.2196`
- `risk_on_high->commodity_24h` score `7.9111` n `54` status `ready` deltaP `41.2892` edge `0.384` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.9111` n `54` status `ready` deltaP `41.2892` edge `0.384` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `6.8557` n `54` status `ready` deltaP `23.007` edge `0.4626` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `6.8557` n `54` status `ready` deltaP `23.007` edge `0.4626` maxDD `-1.907`
- `market_context_high->crypto_major_4h` score `6.4716` n `119` status `ready` deltaP `21.4952` edge `0.5519` maxDD `-7.4722`
- `risk_on_high->crypto_major_4h` score `4.8919` n `54` status `ready` deltaP `35.7498` edge `0.4741` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.8919` n `54` status `ready` deltaP `35.7498` edge `0.4741` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.8284` n `122` status `ready` deltaP `13.3356` edge `0.1699` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `1.14` n `122` status `ready` deltaP `5.2886` edge `0.1403` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.2549` n `119` status `ready` deltaP `12.7165` edge `0.041` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.2814` n `54` status `ready` deltaP `1.4028` edge `0.0268` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.2814` n `54` status `ready` deltaP `1.4028` edge `0.0268` maxDD `-3.7781`
- `risk_on_high->crypto_alt_1h` score `-0.3208` n `54` status `ready` deltaP `4.9568` edge `0.0281` maxDD `-5.8485`
- `risk_on_and_context->crypto_alt_1h` score `-0.3208` n `54` status `ready` deltaP `4.9568` edge `0.0281` maxDD `-5.8485`
- `market_context_high->fx_1h` score `-0.3349` n `122` status `ready` deltaP `-0.544` edge `-0.0013` maxDD `-0.3742`
- `market_context_high->metal_1h` score `-0.4168` n `122` status `ready` deltaP `6.8568` edge `0.0065` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.4321` n `54` status `ready` deltaP `2.1513` edge `0.0034` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4321` n `54` status `ready` deltaP `2.1513` edge `0.0034` maxDD `-0.8513`
- `market_context_high->commodity_24h` score `-0.4476` n `116` status `ready` deltaP `12.8409` edge `0.1455` maxDD `-12.0788`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
