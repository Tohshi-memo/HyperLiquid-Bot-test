# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T10:22:27.388908+00:00`
- Price records: `672`
- Market context records: `4818`
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

- `market_context_high->unknown_1h` score `12.1527` n `115` status `ready` deltaP `11.3825` edge `0.9786` maxDD `-1.674`
- `market_context_high->unknown_4h` score `7.812` n `115` status `ready` deltaP `17.7359` edge `0.6538` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `2.4887` n `108` status `ready` deltaP `13.368` edge `0.1998` maxDD `-3.8557`
- `market_context_high->equity_4h` score `0.4358` n `115` status `ready` deltaP `10.4573` edge `0.1243` maxDD `-6.3852`
- `market_context_high->commodity_4h` score `0.2021` n `115` status `ready` deltaP `13.579` edge `0.0526` maxDD `-4.377`
- `market_context_high->commodity_1h` score `0.0188` n `115` status `ready` deltaP `5.7953` edge `0.0217` maxDD `-2.0345`
- `market_context_high->index_4h` score `-0.0108` n `115` status `ready` deltaP `8.1985` edge `0.0234` maxDD `-3.355`
- `market_context_high->fx_4h` score `-0.3485` n `115` status `ready` deltaP `4.5679` edge `0.0025` maxDD `-1.5439`
- `market_context_high->equity_1h` score `-0.7207` n `115` status `ready` deltaP `2.0528` edge `0.003` maxDD `-4.1397`
- `market_context_high->fx_1h` score `-1.034` n `115` status `ready` deltaP `-2.6582` edge `-0.0035` maxDD `-0.8626`
- `market_context_high->index_1h` score `-1.428` n `115` status `ready` deltaP `-1.4827` edge `-0.0087` maxDD `-2.6999`
- `market_context_high->commodity_24h` score `-2.2446` n `108` status `ready` deltaP `19.5024` edge `0.0931` maxDD `-27.5371`
- `market_context_high->metal_1h` score `-2.3077` n `115` status `ready` deltaP `-1.3109` edge `-0.072` maxDD `-13.8767`
- `market_context_high->crypto_alt_1h` score `-2.5118` n `115` status `ready` deltaP `2.8013` edge `-0.0353` maxDD `-13.082`
- `market_context_high->fx_24h` score `-2.6152` n `108` status `ready` deltaP `-12.2685` edge `-0.0192` maxDD `-3.0218`
- `market_context_high->crypto_major_1h` score `-2.6837` n `115` status `ready` deltaP `0.9984` edge `-0.065` maxDD `-20.1912`
- `market_context_high->crypto_alt_4h` score `-3.8641` n `115` status `ready` deltaP `7.2839` edge `0.0031` maxDD `-38.4308`
- `market_context_high->index_24h` score `-4.2344` n `108` status `ready` deltaP `-5.6135` edge `-0.1146` maxDD `-23.2678`
- `market_context_high->crypto_major_4h` score `-7.6576` n `115` status `ready` deltaP `4.308` edge `-0.1583` maxDD `-62.8401`
- `market_context_high->metal_4h` score `-8.5846` n `115` status `ready` deltaP `5.3406` edge `-0.3199` maxDD `-60.6373`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
