# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T23:47:44.161251+00:00`
- Price records: `672`
- Market context records: `4985`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9536`

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

- `market_context_high->unknown_1h` score `12.9159` n `88` status `ready` deltaP `3.3479` edge `1.1041` maxDD `-1.674`
- `market_context_high->crypto_major_4h` score `6.0174` n `88` status `ready` deltaP `17.0732` edge `0.5363` maxDD `-7.8936`
- `market_context_high->unknown_24h` score `5.8583` n `75` status `ready` deltaP `28.2222` edge `0.3343` maxDD `-1.4072`
- `market_context_high->crypto_alt_4h` score `5.1264` n `88` status `ready` deltaP `12.7494` edge `0.4816` maxDD `-7.8181`
- `market_context_high->unknown_4h` score `1.5177` n `88` status `ready` deltaP `20.5932` edge `0.0903` maxDD `-5.4224`
- `market_context_high->metal_4h` score `1.1431` n `88` status `ready` deltaP `11.5577` edge `0.1261` maxDD `-1.9651`
- `market_context_high->equity_1h` score `0.949` n `88` status `ready` deltaP `8.4036` edge `0.0804` maxDD `-2.5875`
- `market_context_high->crypto_major_1h` score `0.8976` n `88` status `ready` deltaP `5.9268` edge `0.1277` maxDD `-4.7265`
- `market_context_high->equity_4h` score `0.5994` n `88` status `ready` deltaP `4.9335` edge `0.1821` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.36` n `88` status `ready` deltaP `5.4047` edge `0.0423` maxDD `-0.8666`
- `market_context_high->metal_1h` score `0.2362` n `88` status `ready` deltaP `4.6407` edge `0.0384` maxDD `-1.3057`
- `market_context_high->crypto_alt_1h` score `0.1526` n `88` status `ready` deltaP `4.6067` edge `0.0911` maxDD `-5.5126`
- `market_context_high->fx_24h` score `-0.2088` n `75` status `ready` deltaP `6.5903` edge `0.0055` maxDD `-1.7626`
- `market_context_high->index_1h` score `-0.3141` n `88` status `ready` deltaP `2.96` edge `0.0141` maxDD `-0.5946`
- `market_context_high->commodity_1h` score `-0.4941` n `88` status `ready` deltaP `-0.4151` edge `0.0054` maxDD `-1.278`
- `market_context_high->fx_4h` score `-0.7532` n `88` status `ready` deltaP `0.2218` edge `-0.001` maxDD `-1.0967`
- `market_context_high->commodity_4h` score `-1.1998` n `88` status `ready` deltaP `4.2267` edge `-0.0029` maxDD `-5.021`
- `market_context_high->fx_1h` score `-1.5094` n `88` status `ready` deltaP `-9.3563` edge `-0.0036` maxDD `-0.4511`
- `market_context_high->commodity_24h` score `-3.8438` n `75` status `ready` deltaP `8.7431` edge `-0.0402` maxDD `-27.5371`
- `market_context_high->metal_24h` score `-4.3498` n `75` status `ready` deltaP `-2.5764` edge `0.005` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
