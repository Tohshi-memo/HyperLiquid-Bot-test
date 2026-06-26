# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T04:52:25.747274+00:00`
- Price records: `672`
- Market context records: `4794`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7548`

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

- `market_context_high->unknown_4h` score `7.7495` n `122` status `ready` deltaP `19.0249` edge `0.64` maxDD `-4.6834`
- `market_context_high->unknown_1h` score `7.4353` n `122` status `ready` deltaP `12.4301` edge `0.5785` maxDD `-1.674`
- `market_context_high->unknown_24h` score `2.2077` n `111` status `ready` deltaP `12.6314` edge `0.1921` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `0.1189` n `122` status `ready` deltaP `5.6812` edge `0.0308` maxDD `-2.0345`
- `market_context_high->commodity_4h` score `0.0519` n `122` status `ready` deltaP `11.8153` edge `0.0451` maxDD `-4.377`
- `market_context_high->equity_4h` score `-0.0566` n `122` status `ready` deltaP `8.5391` edge `0.1044` maxDD `-8.8203`
- `market_context_high->index_4h` score `-0.3371` n `122` status `ready` deltaP `7.2996` edge `0.015` maxDD `-5.5505`
- `market_context_high->fx_4h` score `-0.4337` n `122` status `ready` deltaP `2.9738` edge `0.0022` maxDD `-1.5439`
- `market_context_high->equity_1h` score `-0.7199` n `122` status `ready` deltaP `1.5682` edge `0.0063` maxDD `-4.1397`
- `market_context_high->fx_1h` score `-0.898` n `122` status `ready` deltaP `-1.0332` edge `-0.003` maxDD `-0.8626`
- `market_context_high->index_1h` score `-1.3644` n `122` status `ready` deltaP `-1.1976` edge `-0.0053` maxDD `-2.6999`
- `market_context_high->commodity_24h` score `-2.1862` n `111` status `ready` deltaP `19.5289` edge `0.1004` maxDD `-27.5371`
- `market_context_high->metal_1h` score `-2.2462` n `122` status `ready` deltaP `-0.7976` edge `-0.0651` maxDD `-14.0715`
- `market_context_high->crypto_alt_1h` score `-3.1388` n `122` status `ready` deltaP `1.0479` edge `-0.0446` maxDD `-15.2495`
- `market_context_high->fx_24h` score `-3.2725` n `111` status `ready` deltaP `-14.452` edge `-0.0214` maxDD `-3.3968`
- `market_context_high->crypto_major_1h` score `-4.4828` n `122` status `ready` deltaP `0.8344` edge `-0.0701` maxDD `-22.0555`
- `market_context_high->crypto_alt_4h` score `-4.7132` n `122` status `ready` deltaP `5.2029` edge `0.0035` maxDD `-46.0617`
- `market_context_high->index_24h` score `-6.35` n `111` status `ready` deltaP `-7.0899` edge `-0.1176` maxDD `-21.1438`
- `market_context_high->crypto_major_4h` score `-8.0073` n `122` status `ready` deltaP `3.9634` edge `-0.1299` maxDD `-68.5143`
- `market_context_high->metal_4h` score `-8.2875` n `122` status `ready` deltaP `6.6873` edge `-0.283` maxDD `-61.2596`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
