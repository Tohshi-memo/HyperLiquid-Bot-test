# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-13T14:22:26.455754+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9708`

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

- `market_context_high->crypto_alt_4h` score `8.276` n `117` status `ready` deltaP `21.3376` edge `0.6923` maxDD `-9.2574`
- `market_context_high->crypto_major_4h` score `7.2446` n `117` status `ready` deltaP `25.0834` edge `0.5924` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `6.8649` n `54` status `ready` deltaP `23.6168` edge `0.4594` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `6.8649` n `54` status `ready` deltaP `23.6168` edge `0.4594` maxDD `-1.9151`
- `risk_on_high->commodity_24h` score `6.0988` n `48` status `ready` deltaP `32.0` edge `0.2949` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.0988` n `48` status `ready` deltaP `32.0` edge `0.2949` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `5.2488` n `54` status `ready` deltaP `38.1888` edge `0.5036` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `5.2488` n `54` status `ready` deltaP `38.1888` edge `0.5036` maxDD `-4.1548`
- `market_context_high->unknown_4h` score `3.8334` n `117` status `ready` deltaP `-3.467` edge `0.4072` maxDD `-1.8373`
- `market_context_high->crypto_alt_1h` score `2.0733` n `117` status `ready` deltaP `14.6144` edge `0.1821` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.587` n `117` status `ready` deltaP `8.057` edge `0.1591` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.1274` n `117` status `ready` deltaP `12.6981` edge `0.0305` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.1248` n `54` status `ready` deltaP `3.4986` edge `0.0329` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.1248` n `54` status `ready` deltaP `3.4986` edge `0.0329` maxDD `-3.7781`
- `market_context_high->fx_1h` score `-0.3419` n `117` status `ready` deltaP `1.0973` edge `0.0022` maxDD `-0.3742`
- `risk_on_high->crypto_alt_1h` score `-0.3856` n `54` status `ready` deltaP `4.358` edge `0.0241` maxDD `-5.8734`
- `risk_on_and_context->crypto_alt_1h` score `-0.3856` n `54` status `ready` deltaP `4.358` edge `0.0241` maxDD `-5.8734`
- `market_context_high->metal_1h` score `-0.4285` n `117` status `ready` deltaP `6.8159` edge `0.0058` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.4929` n `54` status `ready` deltaP `1.4028` edge `0.0006` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4929` n `54` status `ready` deltaP `1.4028` edge `0.0006` maxDD `-0.8513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
