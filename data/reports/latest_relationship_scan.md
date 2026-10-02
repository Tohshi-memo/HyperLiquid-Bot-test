# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T02:37:28.812485+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6602`

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

- `market_context_high->unknown_1h` score `338.85` n `50` status `ready` deltaP `9.5269` edge `28.1789` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `287.9683` n `50` status `ready` deltaP `8.9939` edge `23.9374` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `18.3313` n `76` status `ready` deltaP `38.5142` edge `1.2918` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `11.0255` n `50` status `ready` deltaP `36.1667` edge `0.8193` maxDD `-9.3299`
- `market_context_high->crypto_alt_24h` score `7.3933` n `50` status `ready` deltaP `15.1458` edge `0.6861` maxDD `-11.6768`
- `market_context_high->crypto_major_4h` score `7.0555` n `50` status `ready` deltaP `18.0` edge `0.5383` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.7945` n `50` status `ready` deltaP `15.5793` edge `0.425` maxDD `-7.6792`
- `news_risk_high->crypto_alt_4h` score `3.6224` n `89` status `ready` deltaP `14.1186` edge `0.3421` maxDD `-6.4152`
- `market_context_high->equity_24h` score `3.4354` n `50` status `ready` deltaP `17.4792` edge `0.5101` maxDD `-11.8957`
- `news_risk_high->equity_24h` score `3.2538` n `76` status `ready` deltaP `20.5318` edge `0.4454` maxDD `-6.8764`
- `market_context_high->crypto_major_1h` score `2.9723` n `50` status `ready` deltaP `14.5988` edge `0.1954` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.9009` n `50` status `ready` deltaP `32.689` edge `0.0373` maxDD `-0.0791`
- `market_context_high->crypto_alt_1h` score `2.8247` n `50` status `ready` deltaP `13.1557` edge `0.214` maxDD `-3.6387`
- `news_risk_high->crypto_major_24h` score `2.4999` n `76` status `ready` deltaP `12.0614` edge `0.4433` maxDD `-15.8971`
- `news_risk_high->equity_4h` score `2.4922` n `89` status `ready` deltaP `22.8419` edge `0.125` maxDD `-2.9013`
- `news_risk_high->commodity_24h` score `1.5634` n `76` status `ready` deltaP `25.265` edge `0.1444` maxDD `-3.9922`
- `market_context_high->fx_1h` score `1.4472` n `50` status `ready` deltaP `20.3413` edge `0.0114` maxDD `-0.113`
- `news_risk_high->metal_24h` score `1.3192` n `76` status `ready` deltaP `12.6645` edge `0.2121` maxDD `-2.192`
- `news_risk_high->index_24h` score `1.1474` n `76` status `ready` deltaP `15.8443` edge `0.0378` maxDD `-0.4916`
- `market_context_high->index_24h` score `0.9221` n `50` status `ready` deltaP `14.7917` edge `0.0767` maxDD `-1.2338`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
