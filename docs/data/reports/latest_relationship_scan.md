# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T14:52:29.339619+00:00`
- Price records: `672`
- Market context records: `2571`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9200`

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

- `market_context_high->crypto_alt_4h` score `6.0043` n `146` status `ready` deltaP `25.9585` edge `0.5952` maxDD `-15.4319`
- `market_context_high->crypto_major_24h` score `5.5483` n `115` status `ready` deltaP `13.8285` edge `0.6355` maxDD `-15.2264`
- `market_context_high->unknown_24h` score `4.4908` n `115` status `ready` deltaP `19.4338` edge `0.2775` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `4.1598` n `146` status `ready` deltaP `17.8124` edge `0.4089` maxDD `-10.1468`
- `market_context_high->equity_24h` score `1.8134` n `115` status `ready` deltaP `21.3406` edge `0.0672` maxDD `-2.0014`
- `market_context_high->crypto_alt_1h` score `1.5559` n `146` status `ready` deltaP `12.0294` edge `0.1682` maxDD `-6.1656`
- `market_context_high->unknown_4h` score `1.3656` n `146` status `ready` deltaP `9.9712` edge `0.1523` maxDD `-3.7312`
- `market_context_high->crypto_major_1h` score `1.0026` n `146` status `ready` deltaP `10.2104` edge `0.1349` maxDD `-4.2199`
- `market_context_high->index_24h` score `0.6374` n `115` status `ready` deltaP `5.8635` edge `0.1121` maxDD `-2.5127`
- `market_context_high->crypto_alt_24h` score `0.3872` n `115` status `ready` deltaP `-0.0936` edge `0.6881` maxDD `-39.0265`
- `market_context_high->index_4h` score `0.2112` n `146` status `ready` deltaP `8.2129` edge `0.047` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1251` n `146` status `ready` deltaP `3.9414` edge `0.0127` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.4284` n `146` status `ready` deltaP `1.6508` edge `0.0196` maxDD `-2.6375`
- `market_context_high->commodity_1h` score `-0.4446` n `146` status `ready` deltaP `5.3523` edge `0.0151` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.5467` n `146` status `ready` deltaP `0.5127` edge `0.0045` maxDD `-0.278`
- `market_context_high->fx_24h` score `-0.5672` n `115` status `ready` deltaP `1.9958` edge `0.005` maxDD `-1.6157`
- `market_context_high->metal_1h` score `-0.62` n `146` status `ready` deltaP `1.1115` edge `0.0157` maxDD `-2.9823`
- `market_context_high->equity_1h` score `-0.7533` n `146` status `ready` deltaP `-0.2276` edge `0.0226` maxDD `-2.7085`
- `market_context_high->metal_4h` score `-0.755` n `146` status `ready` deltaP `3.7399` edge `0.0509` maxDD `-4.7664`
- `market_context_high->fx_4h` score `-0.8256` n `146` status `ready` deltaP `0.5367` edge `0.0134` maxDD `-0.8621`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
