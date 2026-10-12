# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T21:07:28.003218+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9002`

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

- `risk_on_high->crypto_alt_4h` score `4.8438` n `48` status `ready` deltaP `20.4777` edge `0.3119` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `4.8438` n `48` status `ready` deltaP `20.4777` edge `0.3119` maxDD `-1.9151`
- `market_context_high->crypto_alt_4h` score `4.1419` n `100` status `ready` deltaP `15.561` edge `0.3863` maxDD `-9.2574`
- `risk_on_high->crypto_major_4h` score `3.9664` n `48` status `ready` deltaP `35.1118` edge `0.3597` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.9664` n `48` status `ready` deltaP `35.1118` edge `0.3597` maxDD `-4.1548`
- `market_context_high->crypto_major_4h` score `3.7116` n `100` status `ready` deltaP `18.9451` edge `0.3389` maxDD `-7.4722`
- `market_context_high->crypto_major_24h` score `3.5295` n `70` status `ready` deltaP `17.9464` edge `1.0078` maxDD `-44.9956`
- `market_context_high->crypto_alt_1h` score `1.6568` n `100` status `ready` deltaP `12.503` edge `0.1498` maxDD `-4.9401`
- `risk_on_high->crypto_alt_1h` score `1.0354` n `48` status `ready` deltaP `6.8363` edge `0.1004` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `1.0354` n `48` status `ready` deltaP `6.8363` edge `0.1004` maxDD `-2.4421`
- `market_context_high->unknown_4h` score `0.7511` n `100` status `ready` deltaP `-3.9268` edge `0.1534` maxDD `-1.8373`
- `market_context_high->crypto_major_1h` score `0.7028` n `100` status `ready` deltaP `4.6467` edge `0.1039` maxDD `-3.4384`
- `risk_on_high->crypto_major_1h` score `0.4451` n `48` status `ready` deltaP `5.8134` edge `0.0836` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `0.4451` n `48` status `ready` deltaP `5.8134` edge `0.0836` maxDD `-3.2233`
- `market_context_high->index_1h` score `0.0586` n `100` status `ready` deltaP `5.5015` edge `0.0039` maxDD `-0.3122`
- `market_context_high->metal_1h` score `-0.1201` n `100` status `ready` deltaP `6.2515` edge `0.0044` maxDD `-0.4868`
- `market_context_high->metal_4h` score `-0.1875` n `100` status `ready` deltaP `10.2866` edge `0.0111` maxDD `-1.624`
- `risk_on_high->metal_1h` score `-0.3028` n `48` status `ready` deltaP `3.4182` edge `0.0039` maxDD `-0.4868`
- `risk_on_and_context->metal_1h` score `-0.3028` n `48` status `ready` deltaP `3.4182` edge `0.0039` maxDD `-0.4868`
- `market_context_high->fx_1h` score `-0.3588` n `100` status `ready` deltaP `-1.003` edge `-0.0013` maxDD `-0.3742`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
