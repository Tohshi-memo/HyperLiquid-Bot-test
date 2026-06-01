# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T18:22:28.457305+00:00`
- Price records: `672`
- Market context records: `2585`
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

- `market_context_high->unknown_24h` score `7.1518` n `128` status `ready` deltaP `18.3159` edge `0.5067` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `6.0399` n `146` status `ready` deltaP `26.5683` edge `0.5941` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `4.2628` n `146` status `ready` deltaP `17.66` edge `0.4185` maxDD `-10.1468`
- `market_context_high->crypto_alt_24h` score `1.5908` n `128` status `ready` deltaP `2.8646` edge `0.7513` maxDD `-39.0265`
- `market_context_high->crypto_alt_1h` score `1.436` n `146` status `ready` deltaP `11.73` edge `0.1602` maxDD `-6.1656`
- `market_context_high->unknown_4h` score `1.1532` n `146` status `ready` deltaP `9.0565` edge `0.1407` maxDD `-3.7312`
- `market_context_high->crypto_major_1h` score `0.9211` n `146` status `ready` deltaP `10.0607` edge `0.1291` maxDD `-4.2199`
- `market_context_high->index_24h` score `0.8031` n `128` status `ready` deltaP `8.1597` edge `0.1106` maxDD `-2.5127`
- `market_context_high->equity_24h` score `0.5004` n `128` status `ready` deltaP `17.448` edge `-0.0076` maxDD `-2.3615`
- `market_context_high->index_4h` score `0.3148` n `146` status `ready` deltaP `9.4325` edge `0.0475` maxDD `-2.3986`
- `market_context_high->crypto_major_24h` score `0.2016` n `128` status `ready` deltaP `7.3785` edge `0.4632` maxDD `-29.3141`
- `market_context_high->index_1h` score `-0.2018` n `146` status `ready` deltaP `3.4923` edge `0.0093` maxDD `-1.2855`
- `market_context_high->commodity_1h` score `-0.3811` n `146` status `ready` deltaP `5.502` edge `0.0194` maxDD `-4.3601`
- `market_context_high->unknown_1h` score `-0.4487` n `146` status `ready` deltaP `1.5011` edge `0.0189` maxDD `-2.6375`
- `market_context_high->metal_4h` score `-0.5494` n `146` status `ready` deltaP `4.9594` edge `0.0599` maxDD `-4.7664`
- `market_context_high->metal_1h` score `-0.6668` n `146` status `ready` deltaP `0.8121` edge `0.0138` maxDD `-2.9823`
- `market_context_high->fx_1h` score `-0.7012` n `146` status `ready` deltaP `-1.2837` edge `0.0036` maxDD `-0.278`
- `market_context_high->fx_4h` score `-0.895` n `146` status `ready` deltaP `-0.2255` edge `0.0127` maxDD `-0.8621`
- `market_context_high->equity_1h` score `-0.9295` n `146` status `ready` deltaP `-1.1258` edge `0.0139` maxDD `-2.7085`
- `market_context_high->fx_24h` score `-0.9871` n `128` status `ready` deltaP `2.4306` edge `0.0009` maxDD `-1.6157`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
