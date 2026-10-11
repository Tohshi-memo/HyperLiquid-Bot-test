# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T22:22:25.984108+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9132`

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

- `market_context_high->unknown_24h` score `1381.2693` n `40` status `ready` deltaP `-22.5694` edge `115.2926` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `46.9019` n `98` status `ready` deltaP `-3.4283` edge `3.9894` maxDD `-2.3109`
- `market_context_high->equity_24h` score `8.802` n `40` status `ready` deltaP `27.6736` edge `0.5919` maxDD `-1.0977`
- `market_context_high->index_24h` score `6.4132` n `40` status `ready` deltaP `52.4306` edge `0.1849` maxDD `0.0`
- `market_context_high->unknown_1h` score `4.0784` n `110` status `ready` deltaP `-2.5068` edge `0.3902` maxDD `-1.0231`
- `market_context_high->fx_24h` score `3.0514` n `40` status `ready` deltaP `34.6875` edge `0.036` maxDD `-0.0374`
- `risk_on_high->commodity_1h` score `1.8305` n `31` status `ready` deltaP `22.7787` edge `0.0144` maxDD `-0.0975`
- `risk_on_and_context->commodity_1h` score `1.8305` n `31` status `ready` deltaP `22.7787` edge `0.0144` maxDD `-0.0975`
- `market_context_high->crypto_major_24h` score `1.3828` n `40` status `ready` deltaP `-21.1111` edge `0.5708` maxDD `-17.8526`
- `risk_on_high->crypto_alt_1h` score `0.9618` n `31` status `ready` deltaP `10.0251` edge `0.112` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `0.9618` n `31` status `ready` deltaP `10.0251` edge `0.112` maxDD `-2.4421`
- `risk_on_high->metal_1h` score `0.867` n `31` status `ready` deltaP `15.4964` edge `0.0217` maxDD `-0.1086`
- `risk_on_and_context->metal_1h` score `0.867` n `31` status `ready` deltaP `15.4964` edge `0.0217` maxDD `-0.1086`
- `market_context_high->commodity_4h` score `0.6402` n `98` status `ready` deltaP `13.3027` edge `0.018` maxDD `-1.6002`
- `market_context_high->fx_4h` score `0.5853` n `98` status `ready` deltaP `10.5805` edge `0.0066` maxDD `-0.2692`
- `market_context_high->commodity_1h` score `0.3094` n `110` status `ready` deltaP `7.1775` edge `0.0063` maxDD `-0.6025`
- `risk_on_high->fx_1h` score `0.1069` n `31` status `ready` deltaP `6.3502` edge `-0.0017` maxDD `-0.1548`
- `risk_on_and_context->fx_1h` score `0.1069` n `31` status `ready` deltaP `6.3502` edge `-0.0017` maxDD `-0.1548`
- `risk_on_high->crypto_major_1h` score `0.1042` n `31` status `ready` deltaP `1.6129` edge `0.0679` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `0.1042` n `31` status `ready` deltaP `1.6129` edge `0.0679` maxDD `-3.2233`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
