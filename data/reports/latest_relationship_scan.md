# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T06:22:20.126008+00:00`
- Price records: `672`
- Market context records: `2536`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9252`

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

- `market_context_high->crypto_alt_4h` score `5.133` n `159` status `ready` deltaP `23.7373` edge `0.5374` maxDD `-15.4319`
- `market_context_high->unknown_24h` score `4.5546` n `116` status `ready` deltaP `19.3307` edge `0.2835` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `3.6182` n `159` status `ready` deltaP `17.1623` edge `0.3681` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `2.9433` n `116` status `ready` deltaP `13.2663` edge `0.6317` maxDD `-22.424`
- `market_context_high->unknown_4h` score `1.999` n `159` status `ready` deltaP `11.5585` edge `0.1945` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `1.2139` n `159` status `ready` deltaP `9.869` edge `0.1541` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `0.7247` n `159` status `ready` deltaP `8.4614` edge `0.1234` maxDD `-4.2199`
- `market_context_high->equity_24h` score `0.2044` n `116` status `ready` deltaP `17.7921` edge `0.0276` maxDD `-6.001`
- `market_context_high->crypto_alt_24h` score `0.0412` n `116` status `ready` deltaP `0.5328` edge `0.6878` maxDD `-42.8858`
- `market_context_high->index_4h` score `-0.0801` n `159` status `ready` deltaP `6.7006` edge `0.0328` maxDD `-2.3986`
- `market_context_high->index_24h` score `-0.1545` n `116` status `ready` deltaP `2.4605` edge `0.0688` maxDD `-2.5127`
- `market_context_high->unknown_1h` score `-0.3353` n `159` status `ready` deltaP `2.8905` edge `0.0218` maxDD `-2.8543`
- `market_context_high->index_1h` score `-0.3494` n `159` status `ready` deltaP `1.8134` edge `0.0082` maxDD `-1.2855`
- `market_context_high->commodity_1h` score `-0.3586` n `159` status `ready` deltaP `4.0287` edge `0.015` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.4463` n `159` status `ready` deltaP `1.7522` edge `0.0046` maxDD `-0.278`
- `market_context_high->metal_1h` score `-0.5059` n `159` status `ready` deltaP `0.5837` edge `0.0072` maxDD `-3.0759`
- `market_context_high->fx_4h` score `-0.7974` n `159` status `ready` deltaP `0.9625` edge `0.0131` maxDD `-0.8774`
- `market_context_high->equity_1h` score `-0.814` n `159` status `ready` deltaP `-0.0715` edge `0.0165` maxDD `-2.7085`
- `market_context_high->fx_24h` score `-0.8557` n `116` status `ready` deltaP `3.125` edge `0.0042` maxDD `-2.446`
- `market_context_high->metal_4h` score `-0.9286` n `159` status `ready` deltaP `2.8292` edge `0.0425` maxDD `-4.7664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
