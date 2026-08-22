# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T03:22:24.901980+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14774`

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

- `market_context_high->unknown_1h` score `1.4278` n `133` status `ready` deltaP `9.7351` edge `0.0768` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.8502` n `133` status `ready` deltaP `22.6148` edge `-0.036` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.1976` n `133` status `ready` deltaP `9.7344` edge `0.0107` maxDD `-0.3539`
- `market_context_high->index_1h` score `0.1359` n `133` status `ready` deltaP `9.8577` edge `0.0048` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.1377` n `133` status `ready` deltaP `2.0294` edge `0.0047` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.2085` n `133` status `ready` deltaP `6.714` edge `0.0355` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.2841` n `133` status `ready` deltaP `1.5803` edge `-0.0051` maxDD `-0.6822`
- `market_context_high->metal_4h` score `-0.3641` n `133` status `ready` deltaP `5.2517` edge `-0.0201` maxDD `-1.5942`
- `market_context_high->commodity_4h` score `-0.5679` n `133` status `ready` deltaP `0.3633` edge `0.0098` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.6441` n `133` status `ready` deltaP `-3.9721` edge `0.0005` maxDD `-1.1941`
- `market_context_high->index_4h` score `-0.6758` n `133` status `ready` deltaP `1.0969` edge `0.0096` maxDD `-2.618`
- `market_context_high->crypto_alt_1h` score `-1.0243` n `133` status `ready` deltaP `0.1205` edge `-0.006` maxDD `-2.413`
- `market_context_high->commodity_24h` score `-1.3401` n `105` status `ready` deltaP `-3.3978` edge `0.0943` maxDD `-4.666`
- `market_context_high->crypto_major_1h` score `-1.4152` n `133` status `ready` deltaP `-0.9511` edge `-0.0726` maxDD `-4.1996`
- `market_context_high->equity_4h` score `-1.8612` n `133` status `ready` deltaP `-2.4299` edge `0.0581` maxDD `-16.1079`
- `market_context_high->crypto_alt_4h` score `-2.2048` n `133` status `ready` deltaP `3.5932` edge `-0.0807` maxDD `-5.4926`
- `market_context_high->fx_24h` score `-2.2959` n `105` status `ready` deltaP `-4.8363` edge `0.0019` maxDD `-2.2121`
- `market_context_high->index_24h` score `-4.3376` n `105` status `ready` deltaP `-7.3314` edge `-0.057` maxDD `-18.6848`
- `market_context_high->crypto_major_4h` score `-4.9763` n `133` status `ready` deltaP `-0.7346` edge `-0.3077` maxDD `-3.1677`
- `market_context_high->metal_24h` score `-5.0789` n `105` status `ready` deltaP `-20.8879` edge `-0.1811` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
