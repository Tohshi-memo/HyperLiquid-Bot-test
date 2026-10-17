# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-17T23:22:25.613423+00:00`
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

- `risk_on_high->commodity_24h` score `7.0995` n `54` status `ready` deltaP `39.1986` edge `0.3303` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.0995` n `54` status `ready` deltaP `39.1986` edge `0.3303` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `0.9331` n `175` status `ready` deltaP `12.2116` edge `0.3368` maxDD `-15.2359`
- `market_context_high->crypto_major_1h` score `0.4605` n `175` status `ready` deltaP `4.5851` edge `0.0967` maxDD `-3.7781`
- `risk_on_high->crypto_major_4h` score `0.3627` n `91` status `ready` deltaP `14.9809` edge `0.1947` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `0.3627` n `91` status `ready` deltaP `14.9809` edge `0.1947` maxDD `-11.1788`
- `market_context_high->crypto_alt_1h` score `0.1146` n `175` status `ready` deltaP `7.5517` edge `0.1092` maxDD `-7.3329`
- `risk_on_high->index_1h` score `0.0272` n `91` status `ready` deltaP `5.1562` edge `0.0063` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.0272` n `91` status `ready` deltaP `5.1562` edge `0.0063` maxDD `-0.7394`
- `market_context_high->index_1h` score `-0.1979` n `175` status `ready` deltaP `6.5628` edge `0.0057` maxDD `-1.3195`
- `risk_on_high->fx_1h` score `-0.2726` n `91` status `ready` deltaP `0.8976` edge `-0.0029` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.2726` n `91` status `ready` deltaP `0.8976` edge `-0.0029` maxDD `-0.376`
- `market_context_high->metal_1h` score `-0.2821` n `175` status `ready` deltaP `6.3413` edge `0.0085` maxDD `-0.9556`
- `market_context_high->equity_1h` score `-0.3329` n `175` status `ready` deltaP `10.1664` edge `0.0435` maxDD `-7.3168`
- `risk_on_high->equity_1h` score `-0.3755` n `91` status `ready` deltaP `9.8588` edge `0.0326` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.3755` n `91` status `ready` deltaP `9.8588` edge `0.0326` maxDD `-5.3696`
- `risk_on_high->metal_1h` score `-0.4533` n `91` status `ready` deltaP `1.594` edge `0.0044` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4533` n `91` status `ready` deltaP `1.594` edge `0.0044` maxDD `-0.8513`
- `market_context_high->metal_4h` score `-0.5561` n `175` status `ready` deltaP `6.9539` edge `0.041` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.6926` n `91` status `ready` deltaP `-0.2501` edge `0.0048` maxDD `-4.6876`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
