# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T08:59:16.243175+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7468`

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

- `news_risk_high->unknown_24h` score `769.2196` n `135` status `ready` deltaP `1.9097` edge `64.0889` maxDD `0.0`
- `market_context_high->unknown_1h` score `548.342` n `41` status `ready` deltaP `9.7305` edge `45.6303` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `17.7462` n `135` status `ready` deltaP `28.3796` edge `1.3106` maxDD `-1.0093`
- `news_risk_high->equity_24h` score `7.7466` n `135` status `ready` deltaP `26.9907` edge `0.7005` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `7.4313` n `135` status `ready` deltaP `23.9931` edge `0.7747` maxDD `-15.8971`
- `news_risk_high->index_24h` score `3.6673` n `135` status `ready` deltaP `33.1829` edge `0.1322` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `3.2827` n `135` status `ready` deltaP `25.3588` edge `0.2319` maxDD `-2.192`
- `news_risk_high->equity_4h` score `2.8348` n `135` status `ready` deltaP `29.0187` edge `0.2029` maxDD `-9.143`
- `news_risk_high->crypto_alt_4h` score `1.7275` n `135` status `ready` deltaP `10.5025` edge `0.3399` maxDD `-15.9436`
- `market_context_high->crypto_alt_1h` score `1.652` n `41` status `ready` deltaP `10.2271` edge `0.1358` maxDD `-3.6387`
- `market_context_high->crypto_major_1h` score `1.1922` n `41` status `ready` deltaP `7.401` edge `0.111` maxDD `-3.546`
- `news_risk_high->crypto_alt_1h` score `1.0814` n `135` status `ready` deltaP `9.2515` edge `0.1195` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.89` n `135` status `ready` deltaP `9.2515` edge `0.0748` maxDD `-1.6514`
- `market_context_high->equity_1h` score `0.8542` n `41` status `ready` deltaP `12.6661` edge `0.0676` maxDD `-2.4027`
- `market_context_high->fx_1h` score `0.8057` n `41` status `ready` deltaP `13.0276` edge `0.0067` maxDD `-0.113`
- `news_risk_high->index_1h` score `0.4802` n `135` status `ready` deltaP `8.6682` edge `0.011` maxDD `-0.302`
- `market_context_high->metal_1h` score `0.3515` n `41` status `ready` deltaP `6.8022` edge `0.0218` maxDD `-0.4338`
- `market_context_high->index_1h` score `0.0827` n `41` status `ready` deltaP `3.8082` edge `0.0152` maxDD `-0.3627`
- `news_risk_high->index_4h` score `-0.216` n `135` status `ready` deltaP `6.0343` edge `0.0271` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.6151` n `135` status `ready` deltaP `1.8906` edge `0.0644` maxDD `-7.2607`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
