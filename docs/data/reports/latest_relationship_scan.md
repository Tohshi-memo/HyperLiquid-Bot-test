# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T15:52:25.599963+00:00`
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

- `market_context_high->crypto_major_24h` score `23.6618` n `49` status `ready` deltaP `40.9652` edge `1.7807` maxDD `-4.5585`
- `market_context_high->crypto_alt_24h` score `22.1289` n `49` status `ready` deltaP `29.1596` edge `1.7917` maxDD `-9.0284`
- `risk_on_high->crypto_alt_4h` score `4.0548` n `48` status `ready` deltaP `18.1911` edge `0.2614` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `4.0548` n `48` status `ready` deltaP `18.1911` edge `0.2614` maxDD `-1.9151`
- `risk_on_high->crypto_major_4h` score `3.6169` n `48` status `ready` deltaP `33.1301` edge `0.3281` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.6169` n `48` status `ready` deltaP `33.1301` edge `0.3281` maxDD `-4.1548`
- `market_context_high->crypto_alt_4h` score `3.3529` n `100` status `ready` deltaP `13.2744` edge `0.3358` maxDD `-9.2574`
- `market_context_high->crypto_major_4h` score `3.1738` n `100` status `ready` deltaP `16.9634` edge `0.3073` maxDD `-7.4722`
- `market_context_high->crypto_alt_1h` score `1.6496` n `100` status `ready` deltaP `12.3533` edge `0.1502` maxDD `-4.9401`
- `risk_on_high->crypto_alt_1h` score `1.0282` n `48` status `ready` deltaP `6.6866` edge `0.1008` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `1.0282` n `48` status `ready` deltaP `6.6866` edge `0.1008` maxDD `-2.4421`
- `market_context_high->metal_24h` score `0.7754` n `49` status `ready` deltaP `15.6569` edge `0.0625` maxDD `-1.3977`
- `market_context_high->crypto_major_1h` score `0.7232` n `100` status `ready` deltaP `4.6467` edge `0.1056` maxDD `-3.4384`
- `risk_on_high->crypto_major_1h` score `0.4584` n `48` status `ready` deltaP `5.8134` edge `0.0853` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `0.4584` n `48` status `ready` deltaP `5.8134` edge `0.0853` maxDD `-3.2233`
- `market_context_high->unknown_4h` score `-0.0283` n `100` status `ready` deltaP `-4.3841` edge `0.0915` maxDD `-1.8373`
- `market_context_high->index_1h` score `-0.0336` n `100` status `ready` deltaP `3.8498` edge `0.0031` maxDD `-0.3122`
- `market_context_high->metal_1h` score `-0.1189` n `100` status `ready` deltaP `6.2515` edge `0.0045` maxDD `-0.4868`
- `risk_on_high->metal_1h` score `-0.3016` n `48` status `ready` deltaP `3.4182` edge `0.004` maxDD `-0.4868`
- `risk_on_and_context->metal_1h` score `-0.3016` n `48` status `ready` deltaP `3.4182` edge `0.004` maxDD `-0.4868`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
