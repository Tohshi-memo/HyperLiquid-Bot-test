# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T13:07:26.912522+00:00`
- Price records: `672`
- Market context records: `4830`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7588`

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

- `market_context_high->unknown_1h` score `13.7343` n `109` status `ready` deltaP `11.038` edge `1.1127` maxDD `-1.674`
- `market_context_high->unknown_4h` score `8.5829` n `107` status `ready` deltaP `18.7016` edge `0.7076` maxDD `-4.3628`
- `market_context_high->unknown_24h` score `3.2972` n `100` status `ready` deltaP `16.7569` edge `0.2279` maxDD `-2.521`
- `market_context_high->index_4h` score `0.8152` n `107` status `ready` deltaP `10.2305` edge `0.0464` maxDD `-0.7334`
- `market_context_high->equity_4h` score `0.6805` n `107` status `ready` deltaP `12.1197` edge `0.1446` maxDD `-6.3852`
- `market_context_high->commodity_4h` score `0.3857` n `107` status `ready` deltaP `14.7837` edge `0.0681` maxDD `-4.377`
- `market_context_high->commodity_1h` score `0.2316` n `109` status `ready` deltaP `6.8038` edge `0.0325` maxDD `-1.1869`
- `market_context_high->equity_1h` score `-0.0733` n `109` status `ready` deltaP `3.8098` edge `0.0268` maxDD `-2.928`
- `market_context_high->fx_4h` score `-0.3945` n `107` status `ready` deltaP `3.4035` edge `0.0013` maxDD `-1.2989`
- `market_context_high->index_1h` score `-0.5179` n `109` status `ready` deltaP `0.1785` edge `0.0079` maxDD `-0.7054`
- `market_context_high->fx_1h` score `-1.1216` n `109` status `ready` deltaP `-3.5873` edge `-0.0046` maxDD `-0.8626`
- `market_context_high->crypto_alt_1h` score `-2.0932` n `109` status `ready` deltaP `4.09` edge `-0.0135` maxDD `-12.7225`
- `market_context_high->crypto_major_1h` score `-2.2111` n `109` status `ready` deltaP `2.0477` edge `-0.0396` maxDD `-17.9354`
- `market_context_high->metal_1h` score `-2.2356` n `109` status `ready` deltaP `-0.7046` edge `-0.0716` maxDD `-13.4916`
- `market_context_high->fx_24h` score `-2.3008` n `100` status `ready` deltaP `-10.7708` edge `-0.0189` maxDD `-2.749`
- `market_context_high->crypto_alt_4h` score `-2.4842` n `107` status `ready` deltaP `10.098` edge `0.0606` maxDD `-31.3789`
- `market_context_high->commodity_24h` score `-2.545` n `100` status `ready` deltaP `16.5903` edge `0.074` maxDD `-27.5371`
- `market_context_high->index_24h` score `-4.049` n `100` status `ready` deltaP `-3.5486` edge `-0.1046` maxDD `-23.2678`
- `market_context_high->crypto_major_4h` score `-5.1893` n `107` status `ready` deltaP `6.7971` edge `-0.0547` maxDD `-48.1392`
- `market_context_high->metal_4h` score `-6.7596` n `107` status `ready` deltaP `6.5449` edge `-0.2661` maxDD `-47.8652`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
