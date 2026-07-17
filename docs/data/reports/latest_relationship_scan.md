# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T08:07:28.199899+00:00`
- Price records: `672`
- Market context records: `7008`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11539`

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

- `market_context_high->unknown_24h` score `-0.1794` n `221` status `ready` deltaP `-5.2775` edge `0.4672` maxDD `-18.7342`
- `market_context_high->fx_1h` score `-0.2588` n `234` status `ready` deltaP `2.1175` edge `0.0012` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.4531` n `234` status `ready` deltaP `2.156` edge `0.0343` maxDD `-4.5815`
- `market_context_high->index_1h` score `-0.6421` n `234` status `ready` deltaP `1.0939` edge `0.0015` maxDD `-2.2895`
- `market_context_high->metal_1h` score `-0.6805` n `234` status `ready` deltaP `-1.5546` edge `-0.0001` maxDD `-2.1427`
- `market_context_high->commodity_1h` score `-0.7701` n `234` status `ready` deltaP `-1.9026` edge `-0.0139` maxDD `-2.4388`
- `market_context_high->crypto_major_1h` score `-0.8938` n `234` status `ready` deltaP `4.2083` edge `0.0327` maxDD `-7.1523`
- `market_context_high->fx_4h` score `-0.9603` n `234` status `ready` deltaP `11.4981` edge `0.0066` maxDD `-2.1765`
- `market_context_high->unknown_1h` score `-1.3133` n `234` status `ready` deltaP `-1.7913` edge `-0.0074` maxDD `-3.2083`
- `market_context_high->commodity_4h` score `-1.6426` n `234` status `ready` deltaP `-3.9008` edge `-0.0356` maxDD `-5.5853`
- `market_context_high->index_4h` score `-1.7425` n `234` status `ready` deltaP `8.2968` edge `-0.0088` maxDD `-12.2591`
- `market_context_high->equity_1h` score `-1.8028` n `234` status `ready` deltaP `4.0636` edge `-0.0028` maxDD `-15.7664`
- `market_context_high->metal_4h` score `-1.8944` n `234` status `ready` deltaP `6.7568` edge `0.0104` maxDD `-5.5324`
- `market_context_high->unknown_4h` score `-2.5034` n `234` status `ready` deltaP `-5.6337` edge `0.0655` maxDD `-10.2579`
- `market_context_high->crypto_alt_4h` score `-2.6607` n `234` status `ready` deltaP `2.1641` edge `0.023` maxDD `-22.2831`
- `market_context_high->commodity_24h` score `-3.5173` n `221` status `ready` deltaP `-5.6546` edge `-0.0912` maxDD `-4.4704`
- `market_context_high->fx_24h` score `-4.3687` n `221` status `ready` deltaP `-6.8085` edge `-0.0166` maxDD `-5.4985`
- `market_context_high->crypto_major_4h` score `-4.7823` n `234` status `ready` deltaP `2.1341` edge `0.0157` maxDD `-24.6094`
- `market_context_high->equity_4h` score `-7.2792` n `234` status `ready` deltaP `5.6376` edge `-0.0491` maxDD `-66.7371`
- `market_context_high->metal_24h` score `-13.36` n `221` status `ready` deltaP `-8.9249` edge `-0.0569` maxDD `-39.4213`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
