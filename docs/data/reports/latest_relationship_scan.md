# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T22:37:27.820982+00:00`
- Price records: `672`
- Market context records: `6860`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11809`

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

- `market_context_high->unknown_24h` score `1.1859` n `176` status `ready` deltaP `-1.6268` edge `0.5381` maxDD `-12.3511`
- `market_context_high->fx_1h` score `-0.2534` n `224` status `ready` deltaP `2.1614` edge `0.0016` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.6292` n `224` status `ready` deltaP `1.5435` edge `0.0137` maxDD `-3.7803`
- `market_context_high->commodity_1h` score `-0.6749` n `224` status `ready` deltaP `-1.8685` edge `-0.0056` maxDD `-2.1443`
- `market_context_high->crypto_major_1h` score `-0.6839` n `224` status `ready` deltaP `3.1797` edge `0.0122` maxDD `-4.2314`
- `market_context_high->commodity_24h` score `-0.7018` n `176` status `ready` deltaP `5.6454` edge `0.0907` maxDD `-5.2791`
- `market_context_high->index_1h` score `-0.864` n `224` status `ready` deltaP `-2.4524` edge `-0.0033` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.9392` n `224` status `ready` deltaP `-5.4199` edge `-0.0075` maxDD `-2.1427`
- `market_context_high->fx_4h` score `-1.0014` n `222` status `ready` deltaP `10.7841` edge `0.0061` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.3685` n `222` status `ready` deltaP `-2.6944` edge `-0.0085` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.6436` n `224` status `ready` deltaP `-3.1897` edge `-0.0256` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.9537` n `224` status `ready` deltaP `-0.0828` edge `-0.0319` maxDD `-13.1084`
- `market_context_high->index_4h` score `-2.0549` n `222` status `ready` deltaP `2.8693` edge `-0.0246` maxDD `-11.3047`
- `market_context_high->metal_4h` score `-2.4352` n `222` status `ready` deltaP `-0.2818` edge `-0.012` maxDD `-5.5324`
- `market_context_high->unknown_4h` score `-3.1464` n `222` status `ready` deltaP `-9.1262` edge `0.0352` maxDD `-10.2579`
- `market_context_high->crypto_major_4h` score `-3.1524` n `222` status `ready` deltaP `-1.8059` edge `-0.0594` maxDD `-16.9508`
- `market_context_high->crypto_alt_4h` score `-3.2171` n `222` status `ready` deltaP `-1.1847` edge `-0.0462` maxDD `-20.6678`
- `market_context_high->fx_24h` score `-4.5361` n `176` status `ready` deltaP `-9.8816` edge `-0.0085` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.5929` n `222` status `ready` deltaP `-0.399` edge `-0.1763` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-9.0249` n `176` status `ready` deltaP `-18.9332` edge `-0.1823` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
