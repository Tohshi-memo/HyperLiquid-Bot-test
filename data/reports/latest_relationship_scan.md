# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-11T01:22:27.286958+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11352`

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

- `news_risk_high->unknown_1h` score `1271.1516` n `42` status `ready` deltaP `-4.0348` edge `105.9916` maxDD `-1.1656`
- `news_risk_high->unknown_4h` score `488.5241` n `30` status `ready` deltaP `-27.2662` edge `40.9565` maxDD `-2.1509`
- `risk_on_high->crypto_alt_24h` score `20.4368` n `91` status `ready` deltaP `36.1722` edge `1.4849` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `20.4368` n `91` status `ready` deltaP `36.1722` edge `1.4849` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `15.9713` n `200` status `ready` deltaP `28.1667` edge `1.2259` maxDD `-3.9523`
- `risk_on_high->crypto_alt_4h` score `9.0167` n `91` status `ready` deltaP `42.0983` edge `0.5079` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `9.0167` n `91` status `ready` deltaP `42.0983` edge `0.5079` maxDD `-1.9733`
- `market_context_high->equity_24h` score `8.1004` n `200` status `ready` deltaP `28.8194` edge `0.4829` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `7.7609` n `91` status `ready` deltaP `32.5064` edge `0.5159` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `7.7609` n `91` status `ready` deltaP `32.5064` edge `0.5159` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `7.2386` n `91` status `ready` deltaP `25.021` edge `1.168` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.2386` n `91` status `ready` deltaP `25.021` edge `1.168` maxDD `-24.5429`
- `risk_on_high->equity_24h` score `6.5452` n `91` status `ready` deltaP `28.8194` edge `0.3533` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `6.5452` n `91` status `ready` deltaP `28.8194` edge `0.3533` maxDD `0.0`
- `risk_on_high->index_24h` score `4.7296` n `91` status `ready` deltaP `44.62` edge `0.1009` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `4.7296` n `91` status `ready` deltaP `44.62` edge `0.1009` maxDD `-0.0051`
- `market_context_high->index_24h` score `3.8495` n `200` status `ready` deltaP `38.9167` edge `0.1007` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `3.5394` n `91` status `ready` deltaP `33.0407` edge `0.084` maxDD `-0.079`
- `risk_on_and_context->equity_4h` score `3.5394` n `91` status `ready` deltaP `33.0407` edge `0.084` maxDD `-0.079`
- `news_risk_high->commodity_4h` score `2.5086` n `30` status `ready` deltaP `13.2927` edge `0.1551` maxDD `-0.7736`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
