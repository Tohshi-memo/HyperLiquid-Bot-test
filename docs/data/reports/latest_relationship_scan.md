# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-17T10:07:26.035707+00:00`
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

- `risk_on_high->commodity_24h` score `7.0197` n `54` status `ready` deltaP `38.5017` edge `0.3283` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.0197` n `54` status `ready` deltaP `38.5017` edge `0.3283` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `6.4635` n `140` status `ready` deltaP `15.1045` edge `0.551` maxDD `-5.046`
- `risk_on_high->crypto_major_4h` score `6.046` n `66` status `ready` deltaP `34.4097` edge `0.3597` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `6.046` n `66` status `ready` deltaP `34.4097` edge `0.3597` maxDD `-4.1548`
- `market_context_high->crypto_major_4h` score `5.8922` n `140` status `ready` deltaP `23.3058` edge `0.4678` maxDD `-5.906`
- `risk_on_high->crypto_alt_4h` score `2.7568` n `66` status `ready` deltaP `9.9963` edge `0.2753` maxDD `-4.9768`
- `risk_on_and_context->crypto_alt_4h` score `2.7568` n `66` status `ready` deltaP `9.9963` edge `0.2753` maxDD `-4.9768`
- `market_context_high->crypto_major_1h` score `0.9035` n `152` status `ready` deltaP `7.028` edge `0.109` maxDD `-3.7781`
- `market_context_high->crypto_alt_1h` score `0.6666` n `152` status `ready` deltaP `8.3438` edge `0.1272` maxDD `-5.8485`
- `market_context_high->metal_4h` score `0.4303` n `140` status `ready` deltaP `13.6193` edge `0.0496` maxDD `-1.6961`
- `risk_on_high->index_1h` score `0.2715` n `78` status `ready` deltaP `8.2698` edge `0.0059` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.2715` n `78` status `ready` deltaP `8.2698` edge `0.0059` maxDD `-0.7394`
- `market_context_high->index_1h` score `-0.1127` n `152` status `ready` deltaP `8.3373` edge `0.0048` maxDD `-1.3195`
- `market_context_high->metal_1h` score `-0.3178` n `152` status `ready` deltaP `7.749` edge `0.0088` maxDD `-0.9556`
- `risk_on_high->crypto_major_1h` score `-0.3551` n `78` status `ready` deltaP `4.2953` edge `0.014` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.3551` n `78` status `ready` deltaP `4.2953` edge `0.014` maxDD `-3.7781`
- `market_context_high->equity_1h` score `-0.4139` n `152` status `ready` deltaP `9.1809` edge `0.0367` maxDD `-7.0778`
- `risk_on_high->equity_1h` score `-0.4737` n `78` status `ready` deltaP `9.7713` edge `0.025` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.4737` n `78` status `ready` deltaP `9.7713` edge `0.025` maxDD `-5.3696`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
