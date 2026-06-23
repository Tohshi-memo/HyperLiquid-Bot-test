# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T14:07:35.519780+00:00`
- Price records: `672`
- Market context records: `4523`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9771`

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

- `risk_on_high->unknown_4h` score `161.4818` n `40` status `ready` deltaP `18.872` edge `13.4501` maxDD `-7.5275`
- `risk_on_and_context->unknown_4h` score `161.4818` n `40` status `ready` deltaP `18.872` edge `13.4501` maxDD `-7.5275`
- `market_context_high->unknown_1h` score `48.7286` n `187` status `ready` deltaP `6.1946` edge `4.0778` maxDD `-2.3371`
- `market_context_high->unknown_4h` score `28.5017` n `187` status `ready` deltaP `8.3907` edge `2.4758` maxDD `-7.5275`
- `risk_on_high->crypto_major_4h` score `7.1369` n `40` status `ready` deltaP `38.3232` edge `0.3486` maxDD `-0.0812`
- `risk_on_and_context->crypto_major_4h` score `7.1369` n `40` status `ready` deltaP `38.3232` edge `0.3486` maxDD `-0.0812`
- `risk_on_high->unknown_24h` score `5.6191` n `40` status `ready` deltaP `17.7083` edge `0.3502` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `5.6191` n `40` status `ready` deltaP `17.7083` edge `0.3502` maxDD `0.0`
- `risk_on_high->equity_4h` score `5.3232` n `40` status `ready` deltaP `42.2256` edge `0.1621` maxDD `0.0`
- `risk_on_and_context->equity_4h` score `5.3232` n `40` status `ready` deltaP `42.2256` edge `0.1621` maxDD `0.0`
- `risk_on_high->metal_24h` score `3.6599` n `40` status `ready` deltaP `-6.3542` edge `0.6095` maxDD `-4.834`
- `risk_on_and_context->metal_24h` score `3.6599` n `40` status `ready` deltaP `-6.3542` edge `0.6095` maxDD `-4.834`
- `risk_on_high->crypto_major_1h` score `2.2677` n `40` status `ready` deltaP `14.8054` edge `0.112` maxDD `-0.7379`
- `risk_on_and_context->crypto_major_1h` score `2.2677` n `40` status `ready` deltaP `14.8054` edge `0.112` maxDD `-0.7379`
- `risk_on_high->equity_1h` score `2.1642` n `40` status `ready` deltaP `22.1108` edge `0.0526` maxDD `-0.2389`
- `risk_on_and_context->equity_1h` score `2.1642` n `40` status `ready` deltaP `22.1108` edge `0.0526` maxDD `-0.2389`
- `risk_on_high->metal_4h` score `2.0892` n `40` status `ready` deltaP `15.6098` edge `0.1036` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `2.0892` n `40` status `ready` deltaP `15.6098` edge `0.1036` maxDD `-1.3516`
- `risk_on_high->crypto_alt_4h` score `1.7798` n `40` status `ready` deltaP `10.5183` edge `0.1348` maxDD `-1.8615`
- `risk_on_and_context->crypto_alt_4h` score `1.7798` n `40` status `ready` deltaP `10.5183` edge `0.1348` maxDD `-1.8615`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
