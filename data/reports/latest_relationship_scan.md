# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T20:22:29.282985+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8978`

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

- `risk_on_high->crypto_alt_4h` score `4.774` n `48` status `ready` deltaP `20.3252` edge `0.3071` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `4.774` n `48` status `ready` deltaP `20.3252` edge `0.3071` maxDD `-1.9151`
- `market_context_high->crypto_major_24h` score `4.7513` n `67` status `ready` deltaP `20.569` edge `1.0745` maxDD `-40.1989`
- `market_context_high->crypto_alt_4h` score `4.0721` n `100` status `ready` deltaP `15.4085` edge `0.3815` maxDD `-9.2574`
- `risk_on_high->crypto_major_4h` score `3.9319` n `48` status `ready` deltaP `34.9594` edge `0.3563` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.9319` n `48` status `ready` deltaP `34.9594` edge `0.3563` maxDD `-4.1548`
- `market_context_high->crypto_major_4h` score `3.6586` n `100` status `ready` deltaP `18.7927` edge `0.3355` maxDD `-7.4722`
- `market_context_high->crypto_alt_1h` score `1.634` n `100` status `ready` deltaP `12.3533` edge `0.1489` maxDD `-4.9401`
- `risk_on_high->crypto_alt_1h` score `1.0126` n `48` status `ready` deltaP `6.6866` edge `0.0995` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `1.0126` n `48` status `ready` deltaP `6.6866` edge `0.0995` maxDD `-2.4421`
- `market_context_high->unknown_4h` score `0.8017` n `100` status `ready` deltaP `-3.7744` edge `0.1566` maxDD `-1.8373`
- `market_context_high->crypto_major_1h` score `0.698` n `100` status `ready` deltaP `4.6467` edge `0.1035` maxDD `-3.4384`
- `risk_on_high->crypto_major_1h` score `0.442` n `48` status `ready` deltaP `5.8134` edge `0.0832` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `0.442` n `48` status `ready` deltaP `5.8134` edge `0.0832` maxDD `-3.2233`
- `market_context_high->index_1h` score `0.0508` n `100` status `ready` deltaP `5.3514` edge `0.0039` maxDD `-0.3122`
- `market_context_high->metal_1h` score `-0.1069` n `100` status `ready` deltaP `6.4012` edge `0.0045` maxDD `-0.4868`
- `market_context_high->metal_4h` score `-0.1863` n `100` status `ready` deltaP `10.2866` edge `0.0112` maxDD `-1.624`
- `risk_on_high->metal_1h` score `-0.2896` n `48` status `ready` deltaP `3.5679` edge `0.004` maxDD `-0.4868`
- `risk_on_and_context->metal_1h` score `-0.2896` n `48` status `ready` deltaP `3.5679` edge `0.004` maxDD `-0.4868`
- `market_context_high->fx_1h` score `-0.3752` n `100` status `ready` deltaP `-1.3033` edge `-0.0014` maxDD `-0.3742`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
