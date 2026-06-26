# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T10:52:32.284293+00:00`
- Price records: `672`
- Market context records: `4820`
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

- `market_context_high->unknown_1h` score `12.4102` n `114` status `ready` deltaP `11.3615` edge `1.0002` maxDD `-1.674`
- `market_context_high->unknown_4h` score `7.8558` n `114` status `ready` deltaP `17.7738` edge `0.6572` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `2.5839` n `107` status `ready` deltaP `13.6958` edge `0.2023` maxDD `-3.5957`
- `market_context_high->equity_4h` score `0.5162` n `114` status `ready` deltaP `10.9836` edge `0.1311` maxDD `-6.3852`
- `market_context_high->commodity_4h` score `0.2431` n `114` status `ready` deltaP `14.0672` edge `0.0546` maxDD `-4.377`
- `market_context_high->index_4h` score `0.1802` n `114` status `ready` deltaP `8.6943` edge `0.0277` maxDD `-2.6515`
- `market_context_high->commodity_1h` score `-0.0393` n `114` status `ready` deltaP `5.3682` edge `0.0197` maxDD `-2.0345`
- `market_context_high->fx_4h` score `-0.3746` n `114` status `ready` deltaP `4.156` edge `0.0019` maxDD `-1.5439`
- `market_context_high->equity_1h` score `-0.5274` n `114` status `ready` deltaP `2.6526` edge `0.0081` maxDD `-3.5788`
- `market_context_high->fx_1h` score `-1.0281` n `114` status `ready` deltaP `-2.5686` edge `-0.0036` maxDD `-0.8626`
- `market_context_high->index_1h` score `-1.3243` n `114` status `ready` deltaP `-0.8982` edge `-0.0069` maxDD `-2.4642`
- `market_context_high->metal_1h` score `-2.2749` n `114` status `ready` deltaP `-1.0716` edge `-0.0718` maxDD `-13.683`
- `market_context_high->commodity_24h` score `-2.2924` n `107` status `ready` deltaP `19.1216` edge `0.0895` maxDD `-27.5371`
- `market_context_high->crypto_alt_1h` score `-2.3679` n `114` status `ready` deltaP `3.2514` edge `-0.0308` maxDD `-12.7225`
- `market_context_high->crypto_major_1h` score `-2.5262` n `114` status `ready` deltaP `1.4103` edge `-0.0588` maxDD `-19.2914`
- `market_context_high->fx_24h` score `-2.5555` n `107` status `ready` deltaP `-12.2176` edge `-0.0193` maxDD `-2.9766`
- `market_context_high->crypto_alt_4h` score `-3.7992` n `114` status `ready` deltaP `7.7797` edge `0.0062` maxDD `-38.2779`
- `market_context_high->index_24h` score `-4.1876` n `107` status `ready` deltaP `-5.1029` edge `-0.112` maxDD `-23.2678`
- `market_context_high->crypto_major_4h` score `-7.4544` n `114` status `ready` deltaP `4.7657` edge `-0.152` maxDD `-61.504`
- `market_context_high->metal_4h` score `-8.5822` n `114` status `ready` deltaP `5.4477` edge `-0.3237` maxDD `-60.3654`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
