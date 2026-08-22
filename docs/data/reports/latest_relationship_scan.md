# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T13:22:25.659626+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14754`

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

- `market_context_high->unknown_1h` score `0.8922` n `146` status `ready` deltaP `6.7304` edge `0.0522` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.5863` n `140` status `ready` deltaP `18.6411` edge `-0.0315` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.1126` n `140` status `ready` deltaP `8.2186` edge `0.0099` maxDD `-0.3539`
- `market_context_high->index_1h` score `0.0102` n `146` status `ready` deltaP `7.4707` edge `0.0046` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.0198` n `146` status `ready` deltaP `4.2819` edge `0.0048` maxDD `-0.2043`
- `market_context_high->metal_4h` score `-0.249` n `140` status `ready` deltaP `7.0165` edge `-0.0171` maxDD `-1.5942`
- `market_context_high->metal_1h` score `-0.3287` n `146` status `ready` deltaP `0.7075` edge `-0.005` maxDD `-0.6822`
- `market_context_high->equity_1h` score `-0.362` n `146` status `ready` deltaP `4.2408` edge `0.0323` maxDD `-5.2257`
- `market_context_high->index_4h` score `-0.4581` n `140` status `ready` deltaP `5.0` edge `0.0115` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.7612` n `140` status `ready` deltaP `-2.243` edge `0.0024` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.9747` n `146` status `ready` deltaP `-7.4256` edge `-0.0022` maxDD `-1.1941`
- `market_context_high->fx_24h` score `-1.7221` n `126` status `ready` deltaP `1.0912` edge `0.0102` maxDD `-2.2121`
- `market_context_high->equity_4h` score `-1.7405` n `140` status `ready` deltaP `-1.6681` edge `0.0685` maxDD `-16.1079`
- `market_context_high->crypto_alt_4h` score `-2.0682` n `140` status `ready` deltaP `4.4991` edge `-0.0638` maxDD `-6.4167`
- `market_context_high->commodity_24h` score `-2.1041` n `126` status `ready` deltaP `-5.8531` edge `0.047` maxDD `-4.666`
- `market_context_high->crypto_alt_1h` score `-2.459` n `146` status `ready` deltaP `-2.4957` edge `-0.0388` maxDD `-7.9582`
- `market_context_high->crypto_major_1h` score `-3.5013` n `146` status `ready` deltaP `-4.9811` edge `-0.1127` maxDD `-7.6697`
- `market_context_high->index_24h` score `-4.5398` n `126` status `ready` deltaP `-8.8294` edge `-0.0442` maxDD `-20.9835`
- `market_context_high->metal_24h` score `-5.4955` n `126` status `ready` deltaP `-25.0744` edge `-0.2066` maxDD `-11.4635`
- `market_context_high->crypto_major_4h` score `-5.5237` n `140` status `ready` deltaP `-0.9103` edge `-0.3246` maxDD `-5.3711`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
