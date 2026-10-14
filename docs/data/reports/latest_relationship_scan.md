# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-14T02:22:32.404415+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9807`

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

- `market_context_high->crypto_alt_4h` score `6.6939` n `117` status `ready` deltaP `16.696` edge `0.5914` maxDD `-9.2574`
- `risk_on_high->commodity_24h` score `6.28` n `52` status `ready` deltaP `32.0` edge `0.31` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.28` n `52` status `ready` deltaP `32.0` edge `0.31` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `6.1293` n `117` status `ready` deltaP `21.1919` edge `0.5254` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `5.2828` n `54` status `ready` deltaP `18.9752` edge `0.3585` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `5.2828` n `54` status `ready` deltaP `18.9752` edge `0.3585` maxDD `-1.9151`
- `risk_on_high->crypto_major_4h` score `4.5238` n `54` status `ready` deltaP `34.2973` edge `0.4366` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.5238` n `54` status `ready` deltaP `34.2973` edge `0.4366` maxDD `-4.1548`
- `market_context_high->unknown_4h` score `4.4049` n `117` status `ready` deltaP `-3.7934` edge `0.457` maxDD `-1.8373`
- `market_context_high->crypto_alt_1h` score `1.8634` n `117` status `ready` deltaP `14.1653` edge `0.1676` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.37` n `117` status `ready` deltaP `7.0091` edge `0.148` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.337` n `117` status `ready` deltaP `14.448` edge `0.0363` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.2659` n `54` status `ready` deltaP `2.4507` edge `0.0218` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.2659` n `54` status `ready` deltaP `2.4507` edge `0.0218` maxDD `-3.7781`
- `market_context_high->fx_1h` score `-0.3179` n `117` status `ready` deltaP `1.3976` edge `0.0022` maxDD `-0.3742`
- `market_context_high->metal_1h` score `-0.3506` n `117` status `ready` deltaP `7.5644` edge `0.0073` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.4423` n `54` status `ready` deltaP `2.1513` edge `0.0021` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4423` n `54` status `ready` deltaP `2.1513` edge `0.0021` maxDD `-0.8513`
- `risk_on_high->crypto_alt_1h` score `-0.522` n `54` status `ready` deltaP `3.9089` edge `0.0096` maxDD `-5.8734`
- `risk_on_and_context->crypto_alt_1h` score `-0.522` n `54` status `ready` deltaP `3.9089` edge `0.0096` maxDD `-5.8734`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
