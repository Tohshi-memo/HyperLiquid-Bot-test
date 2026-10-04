# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T00:52:33.915206+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4256`

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

- `market_context_high->unknown_1h` score `382.2774` n `50` status `ready` deltaP `13.1198` edge `31.7739` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `321.6714` n `50` status `ready` deltaP `12.6524` edge `26.7216` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `13.2624` n `50` status `ready` deltaP `29.286` edge `1.0803` maxDD `-11.6271`
- `market_context_high->crypto_major_24h` score `11.1719` n `50` status `ready` deltaP `35.5529` edge `0.8356` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `10.5942` n `62` status `ready` deltaP `28.7444` edge `0.7397` maxDD `-2.8784`
- `news_risk_high->crypto_major_4h` score `10.4798` n `68` status `ready` deltaP `38.1815` edge `0.6391` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.1649` n `68` status `ready` deltaP `25.2422` edge `0.5632` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.0799` n `50` status `ready` deltaP `16.4756` edge `0.5505` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.4482` n `50` status `ready` deltaP `14.3598` edge `0.4872` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.4402` n `62` status `ready` deltaP `31.9031` edge `0.1732` maxDD `-0.2696`
- `news_risk_high->equity_4h` score `3.8291` n `68` status `ready` deltaP `26.9637` edge `0.2006` maxDD `-2.9013`
- `market_context_high->crypto_alt_1h` score `2.9869` n `50` status `ready` deltaP `12.5569` edge `0.2315` maxDD `-3.6376`
- `news_risk_high->index_4h` score `2.9595` n `68` status `ready` deltaP `32.3888` edge `0.0569` maxDD `-0.4296`
- `market_context_high->fx_4h` score `2.9335` n `50` status `ready` deltaP `32.8415` edge `0.039` maxDD `-0.0791`
- `news_risk_high->crypto_major_1h` score `2.8624` n `68` status `ready` deltaP `12.6101` edge `0.19` maxDD `-1.5096`
- `market_context_high->crypto_major_1h` score `2.7976` n `50` status `ready` deltaP `11.9042` edge `0.1988` maxDD `-2.2692`
- `news_risk_high->metal_4h` score `2.3746` n `68` status `ready` deltaP `20.1399` edge `0.1052` maxDD `-0.993`
- `news_risk_high->index_1h` score `1.9959` n `68` status `ready` deltaP `24.6478` edge `0.017` maxDD `-0.1997`
- `market_context_high->fx_1h` score `1.5454` n `50` status `ready` deltaP `21.5389` edge `0.0116` maxDD `-0.113`
- `market_context_high->equity_24h` score `1.4584` n `50` status `ready` deltaP `8.0347` edge `0.3196` maxDD `-11.8957`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
