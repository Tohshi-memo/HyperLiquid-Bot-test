# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-17T06:07:28.062620+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8268`

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

- `market_context_high->crypto_alt_4h` score `8.1675` n `127` status `ready` deltaP `20.8913` edge `0.6328` maxDD `-4.9825`
- `risk_on_high->commodity_24h` score `7.0917` n `54` status `ready` deltaP `38.5017` edge `0.3343` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.0917` n `54` status `ready` deltaP `38.5017` edge `0.3343` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `6.3583` n `127` status `ready` deltaP `24.0169` edge `0.5019` maxDD `-5.906`
- `risk_on_high->crypto_alt_4h` score `6.1865` n `54` status `ready` deltaP `23.3119` edge `0.4048` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `6.1865` n `54` status `ready` deltaP `23.3119` edge `0.4048` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `4.3845` n `54` status `ready` deltaP `36.2071` edge `0.406` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.3845` n `54` status `ready` deltaP `36.2071` edge `0.406` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.6847` n `136` status `ready` deltaP `14.1203` edge `0.1527` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `1.0193` n `136` status `ready` deltaP `6.7806` edge `0.1203` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.5571` n `127` status `ready` deltaP `14.6941` edge `0.053` maxDD `-1.6961`
- `risk_on_high->index_1h` score `-0.1569` n `62` status `ready` deltaP `3.2307` edge `0.0038` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.1569` n `62` status `ready` deltaP `3.2307` edge `0.0038` maxDD `-0.7394`
- `market_context_high->index_1h` score `-0.2183` n `136` status `ready` deltaP `6.4565` edge `0.0038` maxDD `-1.3195`
- `market_context_high->metal_1h` score `-0.248` n `136` status `ready` deltaP `8.577` edge `0.0091` maxDD `-0.9556`
- `risk_on_high->crypto_alt_1h` score `-0.4221` n `62` status `ready` deltaP `4.9884` edge `0.0149` maxDD `-5.8485`
- `risk_on_and_context->crypto_alt_1h` score `-0.4221` n `62` status `ready` deltaP `4.9884` edge `0.0149` maxDD `-5.8485`
- `risk_on_high->metal_1h` score `-0.4877` n `62` status `ready` deltaP `1.0817` edge `0.0034` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4877` n `62` status `ready` deltaP `1.0817` edge `0.0034` maxDD `-0.8513`
- `market_context_high->equity_1h` score `-0.4993` n `136` status `ready` deltaP `8.1081` edge `0.0329` maxDD `-7.0778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
