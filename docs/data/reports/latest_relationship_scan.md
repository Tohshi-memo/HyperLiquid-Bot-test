# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T03:07:13.487317+00:00`
- Price records: `608`
- Market context records: `712`
- Flow alert records: `2012`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `901`

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

- `market_context_high->crypto_major_24h` score `11.1839` n `146` status `ready` deltaP `27.1324` edge `0.7845` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.4695` n `146` status `ready` deltaP `8.1042` edge `0.4899` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.2592` n `149` status `ready` deltaP `6.5276` edge `0.0104` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.2939` n `149` status `ready` deltaP `2.7181` edge `0.002` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.4551` n `149` status `ready` deltaP `2.4933` edge `0.0429` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6135` n `149` status `ready` deltaP `0.5694` edge `0.0029` maxDD `-2.8282`
- `market_context_high->index_24h` score `-0.8376` n `146` status `ready` deltaP `-2.0979` edge `0.1437` maxDD `-5.9609`
- `market_context_high->crypto_major_4h` score `-1.0812` n `149` status `ready` deltaP `16.7536` edge `0.1203` maxDD `-22.648`
- `market_context_high->equity_1h` score `-1.1677` n `149` status `ready` deltaP `-1.6018` edge `-0.0056` maxDD `-4.4826`
- `market_context_high->unknown_1h` score `-1.2009` n `149` status `ready` deltaP `-4.1613` edge `-0.012` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.3297` n `149` status `ready` deltaP `4.8091` edge `-0.0114` maxDD `-8.1842`
- `market_context_high->crypto_major_1h` score `-1.5518` n `149` status `ready` deltaP `6.5681` edge `-0.0008` maxDD `-11.4508`
- `market_context_high->index_4h` score `-1.7677` n `149` status `ready` deltaP `1.8536` edge `-0.0074` maxDD `-6.5149`
- `market_context_high->equity_24h` score `-1.8632` n `146` status `ready` deltaP `-3.9882` edge `0.1318` maxDD `-10.5047`
- `market_context_high->crypto_alt_4h` score `-1.9596` n `149` status `ready` deltaP `3.9112` edge `0.0676` maxDD `-15.2248`
- `market_context_high->equity_4h` score `-2.7043` n `149` status `ready` deltaP `-1.2076` edge `-0.0021` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.3611` n `149` status `ready` deltaP `-4.9446` edge `-0.0512` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.7408` n `149` status `ready` deltaP `-6.0962` edge `0.079` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-4.2379` n `149` status `ready` deltaP `3.2945` edge `-0.1873` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-5.098` n `146` status `ready` deltaP `-12.5715` edge `-0.0526` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
