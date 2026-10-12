# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T16:07:38.649729+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7550`

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

- `market_context_high->crypto_major_24h` score `22.742` n `50` status `ready` deltaP `39.4653` edge `1.7364` maxDD `-6.0137`
- `market_context_high->crypto_alt_24h` score `20.7155` n `50` status `ready` deltaP `27.4861` edge `1.7178` maxDD `-11.3131`
- `risk_on_high->crypto_alt_4h` score `4.068` n `48` status `ready` deltaP `18.1911` edge `0.2625` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `4.068` n `48` status `ready` deltaP `18.1911` edge `0.2625` maxDD `-1.9151`
- `risk_on_high->crypto_major_4h` score `3.6215` n `48` status `ready` deltaP `33.1301` edge `0.3287` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.6215` n `48` status `ready` deltaP `33.1301` edge `0.3287` maxDD `-4.1548`
- `market_context_high->crypto_alt_4h` score `3.3661` n `100` status `ready` deltaP `13.2744` edge `0.3369` maxDD `-9.2574`
- `market_context_high->crypto_major_4h` score `3.181` n `100` status `ready` deltaP `16.9634` edge `0.3079` maxDD `-7.4722`
- `market_context_high->crypto_alt_1h` score `1.6221` n `100` status `ready` deltaP `12.2036` edge `0.1489` maxDD `-4.9401`
- `risk_on_high->crypto_alt_1h` score `1.0006` n `48` status `ready` deltaP `6.5369` edge `0.0995` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `1.0006` n `48` status `ready` deltaP `6.5369` edge `0.0995` maxDD `-2.4421`
- `market_context_high->crypto_major_1h` score `0.7004` n `100` status `ready` deltaP `4.497` edge `0.1047` maxDD `-3.4384`
- `market_context_high->metal_24h` score `0.6269` n `50` status `ready` deltaP `14.1875` edge `0.0589` maxDD `-1.516`
- `risk_on_high->crypto_major_1h` score `0.4436` n `48` status `ready` deltaP `5.6637` edge `0.0844` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `0.4436` n `48` status `ready` deltaP `5.6637` edge `0.0844` maxDD `-3.2233`
- `market_context_high->unknown_4h` score `-0.0283` n `100` status `ready` deltaP `-4.3841` edge `0.0915` maxDD `-1.8373`
- `market_context_high->index_1h` score `-0.0336` n `100` status `ready` deltaP `3.8498` edge `0.0031` maxDD `-0.3122`
- `market_context_high->metal_1h` score `-0.1321` n `100` status `ready` deltaP `6.1018` edge `0.0044` maxDD `-0.4868`
- `risk_on_high->metal_1h` score `-0.3147` n `48` status `ready` deltaP `3.2685` edge `0.0039` maxDD `-0.4868`
- `risk_on_and_context->metal_1h` score `-0.3147` n `48` status `ready` deltaP `3.2685` edge `0.0039` maxDD `-0.4868`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
