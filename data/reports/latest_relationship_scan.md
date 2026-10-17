# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-17T09:52:25.296613+00:00`
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

- `risk_on_high->commodity_24h` score `7.0185` n `54` status `ready` deltaP `38.5017` edge `0.3282` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.0185` n `54` status `ready` deltaP `38.5017` edge `0.3282` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `6.6218` n `139` status `ready` deltaP `15.4249` edge `0.5571` maxDD `-4.9825`
- `risk_on_high->crypto_major_4h` score `6.2127` n `65` status `ready` deltaP `35.6684` edge `0.3652` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `6.2127` n `65` status `ready` deltaP `35.6684` edge `0.3652` maxDD `-4.1548`
- `market_context_high->crypto_major_4h` score `5.9737` n `139` status `ready` deltaP `23.8145` edge `0.4712` maxDD `-5.906`
- `risk_on_high->crypto_alt_4h` score `3.0661` n `65` status `ready` deltaP `10.7763` edge `0.2852` maxDD `-4.4563`
- `risk_on_and_context->crypto_alt_4h` score `3.0661` n `65` status `ready` deltaP `10.7763` edge `0.2852` maxDD `-4.4563`
- `market_context_high->crypto_major_1h` score `0.9539` n `151` status `ready` deltaP `7.4027` edge `0.1107` maxDD `-3.7781`
- `market_context_high->crypto_alt_1h` score `0.7677` n `151` status `ready` deltaP `8.7272` edge `0.1289` maxDD `-5.8485`
- `market_context_high->metal_4h` score `0.4114` n `139` status `ready` deltaP `13.3521` edge `0.0498` maxDD `-1.6961`
- `risk_on_high->index_1h` score `0.2318` n `77` status `ready` deltaP `7.804` edge `0.0057` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.2318` n `77` status `ready` deltaP `7.804` edge `0.0057` maxDD `-0.7394`
- `market_context_high->index_1h` score `-0.122` n `151` status `ready` deltaP `8.1738` edge `0.0047` maxDD `-1.3195`
- `risk_on_high->crypto_major_1h` score `-0.2763` n `77` status `ready` deltaP `4.9946` edge `0.0159` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.2763` n `77` status `ready` deltaP `4.9946` edge `0.0159` maxDD `-3.7781`
- `market_context_high->metal_1h` score `-0.2997` n `151` status `ready` deltaP `7.9609` edge `0.0089` maxDD `-0.9556`
- `market_context_high->equity_1h` score `-0.425` n `151` status `ready` deltaP `9.013` edge `0.0364` maxDD `-7.0778`
- `risk_on_high->metal_1h` score `-0.4849` n `77` status `ready` deltaP `1.0459` edge `0.004` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4849` n `77` status `ready` deltaP `1.0459` edge `0.004` maxDD `-0.8513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
