# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-29T14:07:46.325975+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7060`

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

- `market_context_high->unknown_24h` score `1408.2356` n `142` status `ready` deltaP `-2.8487` edge `117.4647` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `47.1985` n `142` status `ready` deltaP `5.6101` edge `3.9091` maxDD `-0.3966`
- `market_context_high->index_24h` score `1.5609` n `142` status `ready` deltaP `22.056` edge `0.0059` maxDD `-0.4958`
- `market_context_high->commodity_4h` score `0.2837` n `142` status `ready` deltaP `13.5327` edge `0.0553` maxDD `-1.0837`
- `market_context_high->fx_1h` score `0.0845` n `142` status `ready` deltaP `6.2938` edge `0.0009` maxDD `-0.1986`
- `market_context_high->metal_1h` score `-0.0457` n `142` status `ready` deltaP `8.4781` edge `0.0074` maxDD `-0.9158`
- `market_context_high->fx_4h` score `-0.2015` n `142` status `ready` deltaP `4.8931` edge `0.0014` maxDD `-0.4545`
- `market_context_high->metal_4h` score `-0.2673` n `142` status `ready` deltaP `10.4174` edge `0.0051` maxDD `-3.3719`
- `market_context_high->commodity_1h` score `-0.3527` n `142` status `ready` deltaP `1.4527` edge `0.0131` maxDD `-0.5075`
- `market_context_high->crypto_major_1h` score `-0.6066` n `142` status `ready` deltaP `4.0314` edge `0.0229` maxDD `-6.87`
- `market_context_high->index_1h` score `-0.7383` n `142` status `ready` deltaP `-3.8479` edge `-0.0035` maxDD `-1.2406`
- `market_context_high->fx_24h` score `-0.9978` n `142` status `ready` deltaP `5.6436` edge `0.0123` maxDD `-0.9792`
- `market_context_high->equity_1h` score `-1.1809` n `142` status `ready` deltaP `-0.2994` edge `0.0064` maxDD `-7.1309`
- `market_context_high->crypto_alt_1h` score `-1.6866` n `142` status `ready` deltaP `1.0753` edge `0.0059` maxDD `-11.6774`
- `market_context_high->metal_24h` score `-2.108` n `142` status `ready` deltaP `1.4451` edge `-0.0027` maxDD `-10.5088`
- `market_context_high->index_4h` score `-2.8192` n `142` status `ready` deltaP `-9.1829` edge `-0.029` maxDD `-4.5769`
- `market_context_high->crypto_major_4h` score `-3.3036` n `142` status `ready` deltaP `2.6216` edge `-0.0437` maxDD `-24.4524`
- `market_context_high->equity_4h` score `-3.4623` n `142` status `ready` deltaP `-3.9054` edge `-0.0909` maxDD `-19.4894`
- `market_context_high->crypto_major_24h` score `-3.8968` n `142` status `ready` deltaP `-4.196` edge `0.0141` maxDD `-29.1905`
- `market_context_high->equity_24h` score `-4.323` n `142` status `ready` deltaP `5.1546` edge `-0.1189` maxDD `-14.0571`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
