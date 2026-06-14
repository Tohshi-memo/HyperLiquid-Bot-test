# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T20:22:34.053563+00:00`
- Price records: `672`
- Market context records: `3925`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11427`

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

- `risk_on_high->unknown_4h` score `64.8621` n `56` status `ready` deltaP `3.4844` edge `8.5066` maxDD `-13.467`
- `risk_on_and_context->unknown_4h` score `64.8621` n `56` status `ready` deltaP `3.4844` edge `8.5066` maxDD `-13.467`
- `risk_on_high->equity_24h` score `14.0315` n `40` status `ready` deltaP `42.0139` edge `0.8892` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `14.0315` n `40` status `ready` deltaP `42.0139` edge `0.8892` maxDD `0.0`
- `market_context_high->unknown_4h` score `13.3659` n `192` status `ready` deltaP `-2.096` edge `1.6687` maxDD `-35.6052`
- `risk_on_high->crypto_major_4h` score `7.3111` n `56` status `ready` deltaP `28.8763` edge `0.4833` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `7.3111` n `56` status `ready` deltaP `28.8763` edge `0.4833` maxDD `-2.6576`
- `risk_on_high->equity_4h` score `6.5469` n `56` status `ready` deltaP `38.8066` edge `0.2916` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `6.5469` n `56` status `ready` deltaP `38.8066` edge `0.2916` maxDD `-0.0458`
- `risk_on_high->index_24h` score `5.6956` n `40` status `ready` deltaP `30.0347` edge `0.2744` maxDD `0.0`
- `risk_on_and_context->index_24h` score `5.6956` n `40` status `ready` deltaP `30.0347` edge `0.2744` maxDD `0.0`
- `market_context_high->equity_24h` score `4.4952` n `165` status `ready` deltaP `20.8018` edge `0.5389` maxDD `-14.5715`
- `market_context_high->index_24h` score `3.954` n `165` status `ready` deltaP `25.7923` edge `0.2715` maxDD `-7.1159`
- `market_context_high->crypto_major_4h` score `2.9195` n `192` status `ready` deltaP `19.0549` edge `0.2927` maxDD `-9.4488`
- `risk_on_high->crypto_major_1h` score `2.5179` n `56` status `ready` deltaP `12.2006` edge `0.1827` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `2.5179` n `56` status `ready` deltaP `12.2006` edge `0.1827` maxDD `-2.3372`
- `market_context_high->metal_24h` score `2.4425` n `165` status `ready` deltaP `16.2973` edge `0.2464` maxDD `-9.1203`
- `market_context_high->equity_4h` score `1.8142` n `192` status `ready` deltaP `16.8572` edge `0.2092` maxDD `-8.2982`
- `risk_on_high->equity_1h` score `1.5597` n `56` status `ready` deltaP `11.8691` edge `0.0902` maxDD `-0.8151`
- `risk_on_and_context->equity_1h` score `1.5597` n `56` status `ready` deltaP `11.8691` edge `0.0902` maxDD `-0.8151`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
