# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T15:37:27.738793+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11757`

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

- `market_context_high->metal_24h` score `1.9024` n `107` status `ready` deltaP `7.1688` edge `0.1725` maxDD `-2.2743`
- `market_context_high->commodity_1h` score `0.7423` n `121` status `ready` deltaP `10.9294` edge `0.0306` maxDD `-1.3282`
- `market_context_high->fx_24h` score `0.4412` n `107` status `ready` deltaP `19.6496` edge `0.0442` maxDD `-4.1573`
- `market_context_high->commodity_4h` score `0.3405` n `109` status `ready` deltaP `10.2428` edge `0.06` maxDD `-2.7703`
- `market_context_high->fx_1h` score `0.0774` n `121` status `ready` deltaP `8.528` edge `-0.0038` maxDD `-1.0616`
- `market_context_high->fx_4h` score `-0.2593` n `109` status `ready` deltaP `7.0163` edge `0.0002` maxDD `-1.7506`
- `market_context_high->metal_1h` score `-0.4361` n `121` status `ready` deltaP `-1.5205` edge `-0.0065` maxDD `-1.1422`
- `market_context_high->index_24h` score `-0.4366` n `107` status `ready` deltaP `1.9536` edge `0.1019` maxDD `-5.7715`
- `market_context_high->metal_4h` score `-0.7301` n `109` status `ready` deltaP `2.1748` edge `0.0025` maxDD `-1.5608`
- `market_context_high->crypto_alt_1h` score `-0.9193` n `121` status `ready` deltaP `-5.8866` edge `-0.0157` maxDD `-2.3669`
- `market_context_high->index_1h` score `-0.9884` n `121` status `ready` deltaP `-2.5746` edge `-0.0118` maxDD `-1.6054`
- `market_context_high->equity_1h` score `-1.3425` n `121` status `ready` deltaP `3.5941` edge `-0.0396` maxDD `-10.5179`
- `market_context_high->crypto_alt_4h` score `-1.8449` n `109` status `ready` deltaP `1.3874` edge `-0.024` maxDD `-5.7857`
- `market_context_high->index_4h` score `-2.1557` n `109` status `ready` deltaP `-4.7298` edge `-0.0285` maxDD `-4.2354`
- `market_context_high->crypto_major_1h` score `-2.5997` n `121` status `ready` deltaP `-6.7254` edge `-0.0421` maxDD `-7.0428`
- `market_context_high->crypto_alt_24h` score `-3.9364` n `107` status `ready` deltaP `-11.4635` edge `-0.1073` maxDD `-4.5445`
- `market_context_high->crypto_major_4h` score `-4.909` n `109` status `ready` deltaP `-7.6485` edge `-0.1848` maxDD `-25.1525`
- `market_context_high->crypto_major_24h` score `-5.6656` n `107` status `ready` deltaP `-4.4901` edge `-0.2687` maxDD `-25.2177`
- `market_context_high->equity_24h` score `-7.1072` n `107` status `ready` deltaP `-9.5849` edge `0.1477` maxDD `-45.0856`
- `market_context_high->unknown_1h` score `-8.2369` n `121` status `ready` deltaP `-0.1794` edge `-0.6405` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
