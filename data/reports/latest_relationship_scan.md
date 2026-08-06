# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-06T23:52:25.008744+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11765`

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

- `market_context_high->unknown_24h` score `32.271` n `109` status `ready` deltaP `3.7571` edge `2.6685` maxDD `-0.0104`
- `market_context_high->commodity_4h` score `1.1586` n `120` status `ready` deltaP `13.1071` edge `0.0938` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.9028` n `109` status `ready` deltaP `3.7004` edge `0.1674` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.5457` n `109` status `ready` deltaP `21.4854` edge `0.0473` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4787` n `120` status `ready` deltaP `7.7994` edge `0.0295` maxDD `-1.3282`
- `market_context_high->fx_1h` score `-0.0194` n `120` status `ready` deltaP `5.5539` edge `-0.0045` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.4084` n `120` status `ready` deltaP `5.2262` edge `-0.0012` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5544` n `120` status `ready` deltaP `-2.2255` edge `-0.0068` maxDD `-1.6224`
- `market_context_high->crypto_alt_1h` score `-0.7653` n `120` status `ready` deltaP `-2.8443` edge `-0.0081` maxDD `-3.0178`
- `market_context_high->index_1h` score `-1.0719` n `120` status `ready` deltaP `-3.1237` edge `-0.0151` maxDD `-1.6054`
- `market_context_high->index_24h` score `-1.3038` n `109` status `ready` deltaP `-3.5503` edge `0.076` maxDD `-7.8922`
- `market_context_high->metal_4h` score `-1.3104` n `120` status `ready` deltaP `1.2406` edge `0.006` maxDD `-3.211`
- `market_context_high->equity_1h` score `-1.4036` n `120` status `ready` deltaP `3.0489` edge `-0.0438` maxDD `-10.5179`
- `market_context_high->index_4h` score `-1.6907` n `120` status `ready` deltaP `-7.862` edge `-0.0389` maxDD `-4.7021`
- `market_context_high->crypto_alt_4h` score `-1.895` n `120` status `ready` deltaP `1.9004` edge `-0.0316` maxDD `-5.7857`
- `market_context_high->crypto_major_1h` score `-2.6022` n `120` status `ready` deltaP `-6.4521` edge `-0.0365` maxDD `-7.6533`
- `market_context_high->crypto_alt_24h` score `-3.0202` n `109` status `ready` deltaP `-6.1463` edge `-0.0664` maxDD `-4.5445`
- `market_context_high->equity_4h` score `-6.1152` n `120` status `ready` deltaP `-0.1245` edge `-0.2543` maxDD `-34.9766`
- `market_context_high->commodity_24h` score `-6.2939` n `109` status `ready` deltaP `9.8099` edge `0.0042` maxDD `-52.7876`
- `market_context_high->crypto_major_4h` score `-7.3024` n `120` status `ready` deltaP `-6.6063` edge `-0.1433` maxDD `-27.3622`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
