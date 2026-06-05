# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T09:07:25.616605+00:00`
- Price records: `672`
- Market context records: `2955`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6954`

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

- `market_context_high->crypto_alt_24h` score `17.2667` n `127` status `ready` deltaP `13.6004` edge `1.7399` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `8.2819` n `127` status `ready` deltaP `16.7296` edge `0.6251` maxDD `-1.7175`
- `market_context_high->equity_24h` score `8.1101` n `127` status `ready` deltaP `18.3919` edge `0.7536` maxDD `-12.6963`
- `market_context_high->commodity_24h` score `5.689` n `127` status `ready` deltaP `23.6125` edge `0.4723` maxDD `-5.117`
- `market_context_high->index_24h` score `3.1737` n `127` status `ready` deltaP `14.1076` edge `0.2685` maxDD `-2.5127`
- `market_context_high->equity_4h` score `2.6886` n `128` status `ready` deltaP `14.5769` edge `0.1897` maxDD `-2.6927`
- `market_context_high->crypto_alt_4h` score `1.7879` n `128` status `ready` deltaP `20.8841` edge `0.4659` maxDD `-30.8239`
- `market_context_high->unknown_4h` score `0.8158` n `128` status `ready` deltaP `6.2881` edge `0.1314` maxDD `-3.7602`
- `market_context_high->index_4h` score `0.6844` n `128` status `ready` deltaP `13.7385` edge `0.0803` maxDD `-2.3986`
- `market_context_high->index_1h` score `0.0694` n `128` status `ready` deltaP `5.5342` edge `0.0214` maxDD `-1.2855`
- `market_context_high->equity_1h` score `-0.0876` n `128` status `ready` deltaP `1.9087` edge `0.0509` maxDD `-2.0072`
- `market_context_high->fx_1h` score `-0.2225` n `128` status `ready` deltaP `1.2116` edge `0.0041` maxDD `-0.1244`
- `market_context_high->crypto_alt_1h` score `-0.4287` n `128` status `ready` deltaP `4.9869` edge `0.0878` maxDD `-10.747`
- `market_context_high->commodity_1h` score `-0.4975` n `128` status `ready` deltaP `-0.5005` edge `0.0021` maxDD `-3.3365`
- `market_context_high->metal_1h` score `-0.6772` n `128` status `ready` deltaP `0.0187` edge `0.0018` maxDD `-3.4325`
- `market_context_high->commodity_4h` score `-0.7044` n `128` status `ready` deltaP `6.593` edge `0.0447` maxDD `-8.9839`
- `market_context_high->crypto_major_1h` score `-0.7057` n `128` status `ready` deltaP `4.0746` edge `0.0693` maxDD `-9.622`
- `market_context_high->fx_4h` score `-0.7218` n `128` status `ready` deltaP `1.1433` edge `0.0101` maxDD `-0.5631`
- `market_context_high->unknown_1h` score `-0.7827` n `128` status `ready` deltaP `1.3286` edge `-0.001` maxDD `-3.1801`
- `market_context_high->crypto_major_4h` score `-0.8781` n `128` status `ready` deltaP `10.6897` edge `0.3287` maxDD `-33.6701`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
