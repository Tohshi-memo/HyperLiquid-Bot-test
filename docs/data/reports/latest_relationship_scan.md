# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-17T09:07:25.012022+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9372`

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

- `market_context_high->crypto_alt_4h` score `7.0802` n `136` status `ready` deltaP `16.58` edge `0.5751` maxDD `-4.9825`
- `risk_on_high->commodity_24h` score `7.0341` n `54` status `ready` deltaP `38.5017` edge `0.3295` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.0341` n `54` status `ready` deltaP `38.5017` edge `0.3295` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `6.4542` n `62` status `ready` deltaP `36.7673` edge `0.378` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `6.4542` n `62` status `ready` deltaP `36.7673` edge `0.378` maxDD `-4.1548`
- `market_context_high->crypto_major_4h` score `6.1081` n `136` status `ready` deltaP `24.2198` edge `0.4797` maxDD `-5.906`
- `risk_on_high->crypto_alt_4h` score `3.9718` n `62` status `ready` deltaP `13.449` edge `0.3138` maxDD `-3.1312`
- `risk_on_and_context->crypto_alt_4h` score `3.9718` n `62` status `ready` deltaP `13.449` edge `0.3138` maxDD `-3.1312`
- `market_context_high->crypto_alt_1h` score `1.0698` n `148` status `ready` deltaP `9.9086` edge `0.1337` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `1.0486` n `148` status `ready` deltaP `8.0312` edge `0.1144` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.3647` n `136` status `ready` deltaP `12.6793` edge `0.0504` maxDD `-1.6961`
- `risk_on_high->index_1h` score `0.0676` n `74` status `ready` deltaP `5.8559` edge `0.005` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.0676` n `74` status `ready` deltaP `5.8559` edge `0.005` maxDD `-0.7394`
- `risk_on_high->crypto_major_1h` score `-0.162` n `74` status `ready` deltaP `6.0042` edge `0.0187` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.162` n `74` status `ready` deltaP `6.0042` edge `0.0187` maxDD `-3.7781`
- `market_context_high->index_1h` score `-0.1753` n `148` status `ready` deltaP `7.2073` edge `0.0043` maxDD `-1.3195`
- `market_context_high->metal_1h` score `-0.2754` n `148` status `ready` deltaP `8.2497` edge `0.009` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.4609` n `74` status `ready` deltaP `1.4929` edge `0.0041` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4609` n `74` status `ready` deltaP `1.4929` edge `0.0041` maxDD `-0.8513`
- `market_context_high->equity_1h` score `-0.4689` n `148` status `ready` deltaP `8.3334` edge `0.0353` maxDD `-7.0778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
