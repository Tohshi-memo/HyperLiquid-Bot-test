# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-11T06:52:25.801872+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12334`

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

- `news_risk_high->unknown_1h` score `750.8753` n `59` status `ready` deltaP `-6.3585` edge `62.6575` maxDD `-1.7068`
- `risk_on_high->crypto_alt_24h` score `21.492` n `91` status `ready` deltaP `38.0819` edge `1.5601` maxDD `-0.8386`
- `risk_on_and_context->crypto_alt_24h` score `21.492` n `91` status `ready` deltaP `38.0819` edge `1.5601` maxDD `-0.8386`
- `market_context_high->crypto_alt_24h` score `18.629` n `180` status `ready` deltaP `34.6875` edge `1.4039` maxDD `-3.9523`
- `news_risk_high->unknown_4h` score `13.2858` n `52` status `ready` deltaP `-22.7134` edge `1.3479` maxDD `-4.1464`
- `market_context_high->equity_24h` score `8.9447` n `180` status `ready` deltaP `32.6389` edge `0.5278` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `8.9183` n `91` status `ready` deltaP `41.1837` edge `0.5058` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `8.9183` n `91` status `ready` deltaP `41.1837` edge `0.5058` maxDD `-1.9733`
- `risk_on_high->equity_24h` score `8.2043` n `91` status `ready` deltaP `32.6389` edge `0.4661` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `8.2043` n `91` status `ready` deltaP `32.6389` edge `0.4661` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `7.6691` n `91` status `ready` deltaP `32.0491` edge `0.5113` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `7.6691` n `91` status `ready` deltaP `32.0491` edge `0.5113` maxDD `-3.8693`
- `risk_on_high->crypto_major_24h` score `7.2963` n `91` status `ready` deltaP `25.021` edge `1.1754` maxDD `-24.5429`
- `risk_on_and_context->crypto_major_24h` score `7.2963` n `91` status `ready` deltaP `25.021` edge `1.1754` maxDD `-24.5429`
- `risk_on_high->index_24h` score `5.2248` n `91` status `ready` deltaP `48.4394` edge `0.1167` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `5.2248` n `91` status `ready` deltaP `48.4394` edge `0.1167` maxDD `-0.0051`
- `market_context_high->index_24h` score `4.1986` n `180` status `ready` deltaP `41.7361` edge `0.111` maxDD `-0.1483`
- `risk_on_high->equity_4h` score `3.7262` n `91` status `ready` deltaP `34.5651` edge `0.0894` maxDD `-0.079`
- `risk_on_and_context->equity_4h` score `3.7262` n `91` status `ready` deltaP `34.5651` edge `0.0894` maxDD `-0.079`
- `market_context_high->equity_4h` score `2.4163` n `180` status `ready` deltaP `27.2696` edge `0.1051` maxDD `-2.843`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
