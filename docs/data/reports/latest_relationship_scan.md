# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T06:22:26.050113+00:00`
- Price records: `672`
- Market context records: `4801`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7530`

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

- `market_context_high->unknown_1h` score `10.5817` n `122` status `ready` deltaP `12.2804` edge `0.8417` maxDD `-1.674`
- `market_context_high->unknown_4h` score `7.7633` n `121` status `ready` deltaP `19.0927` edge `0.6407` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `2.4008` n `115` status `ready` deltaP `13.6654` edge `0.2013` maxDD `-4.7201`
- `market_context_high->equity_4h` score `0.1513` n `121` status `ready` deltaP `9.4638` edge `0.1178` maxDD `-8.2527`
- `market_context_high->commodity_1h` score `0.0578` n `122` status `ready` deltaP `5.3818` edge `0.0277` maxDD `-2.0345`
- `market_context_high->commodity_4h` score `0.051` n `121` status `ready` deltaP `11.7983` edge `0.0451` maxDD `-4.377`
- `market_context_high->index_4h` score `-0.2556` n `121` status `ready` deltaP `8.204` edge `0.0183` maxDD `-5.461`
- `market_context_high->fx_4h` score `-0.3737` n `121` status `ready` deltaP `4.0239` edge `0.0029` maxDD `-1.5439`
- `market_context_high->equity_1h` score `-0.6172` n `122` status `ready` deltaP `2.5375` edge `0.0084` maxDD `-4.1397`
- `market_context_high->fx_1h` score `-0.9001` n `122` status `ready` deltaP `-1.1044` edge `-0.0027` maxDD `-0.8626`
- `market_context_high->index_1h` score `-1.2904` n `122` status `ready` deltaP `-0.3779` edge `-0.0046` maxDD `-2.6999`
- `market_context_high->commodity_24h` score `-2.0226` n `115` status `ready` deltaP `20.5918` edge `0.1143` maxDD `-27.5371`
- `market_context_high->metal_1h` score `-2.2166` n `122` status `ready` deltaP `-0.4982` edge `-0.0633` maxDD `-14.0715`
- `market_context_high->fx_24h` score `-3.0063` n `115` status `ready` deltaP `-12.2569` edge `-0.0185` maxDD `-3.3581`
- `market_context_high->crypto_alt_1h` score `-3.009` n `122` status `ready` deltaP `1.3473` edge `-0.0393` maxDD `-14.9676`
- `market_context_high->crypto_major_1h` score `-4.3904` n `122` status `ready` deltaP `1.1338` edge `-0.0644` maxDD `-22.0555`
- `market_context_high->crypto_alt_4h` score `-4.6382` n `121` status `ready` deltaP `5.9414` edge `0.0048` maxDD `-45.7906`
- `market_context_high->index_24h` score `-7.1134` n `115` status `ready` deltaP `-8.9388` edge `-0.1331` maxDD `-24.007`
- `market_context_high->crypto_major_4h` score `-8.0332` n `121` status `ready` deltaP `3.8551` edge `-0.1325` maxDD `-68.5143`
- `market_context_high->metal_4h` score `-8.2821` n `121` status `ready` deltaP `7.0159` edge `-0.2845` maxDD `-61.2596`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
