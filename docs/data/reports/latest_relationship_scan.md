# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-19T17:37:24.037220+00:00`
- Price records: `672`
- Market context records: `7273`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13791`

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

- `market_context_high->fx_1h` score `-0.2835` n `138` status `ready` deltaP `1.8736` edge `0.0001` maxDD `-0.5817`
- `market_context_high->commodity_1h` score `-0.7174` n `138` status `ready` deltaP `-2.2784` edge `-0.0147` maxDD `-1.9668`
- `market_context_high->crypto_alt_1h` score `-0.7337` n `138` status `ready` deltaP `-0.5511` edge `0.0135` maxDD `-5.9775`
- `market_context_high->crypto_major_1h` score `-0.9413` n `138` status `ready` deltaP `1.2996` edge `0.0117` maxDD `-7.6171`
- `market_context_high->fx_4h` score `-0.969` n `137` status `ready` deltaP `3.9365` edge `0.0095` maxDD `-1.4649`
- `market_context_high->unknown_4h` score `-1.2593` n `137` status `ready` deltaP `7.2336` edge `0.0827` maxDD `-6.2026`
- `market_context_high->unknown_1h` score `-1.3203` n `138` status `ready` deltaP `-1.5035` edge `-0.0969` maxDD `-1.3212`
- `market_context_high->index_1h` score `-1.4541` n `138` status `ready` deltaP `-6.587` edge `-0.0099` maxDD `-2.3889`
- `market_context_high->commodity_4h` score `-1.514` n `137` status `ready` deltaP `-0.4398` edge `-0.0197` maxDD `-2.9494`
- `market_context_high->commodity_24h` score `-2.1901` n `126` status `ready` deltaP `-1.0711` edge `-0.0956` maxDD `-2.3815`
- `market_context_high->fx_24h` score `-2.1921` n `126` status `ready` deltaP `-6.3824` edge `-0.009` maxDD `-2.1564`
- `market_context_high->metal_1h` score `-2.2876` n `138` status `ready` deltaP `-10.1515` edge `-0.0071` maxDD `-1.9351`
- `market_context_high->metal_4h` score `-4.232` n `137` status `ready` deltaP `-12.9317` edge `-0.0189` maxDD `-4.8045`
- `market_context_high->equity_1h` score `-4.5153` n `138` status `ready` deltaP `-8.7609` edge `-0.0652` maxDD `-15.5469`
- `market_context_high->index_4h` score `-5.6017` n `137` status `ready` deltaP `-17.3151` edge `-0.0634` maxDD `-12.7045`
- `market_context_high->crypto_alt_4h` score `-5.7726` n `137` status `ready` deltaP `-3.2668` edge `-0.061` maxDD `-23.8617`
- `market_context_high->crypto_major_4h` score `-6.1591` n `137` status `ready` deltaP `-4.2227` edge `-0.0682` maxDD `-25.019`
- `market_context_high->unknown_24h` score `-6.6852` n `127` status `ready` deltaP `-14.6599` edge `-0.0696` maxDD `-19.1816`
- `market_context_high->metal_24h` score `-13.2128` n `127` status `ready` deltaP `-33.4331` edge `-0.1716` maxDD `-30.5266`
- `market_context_high->index_24h` score `-15.9122` n `126` status `ready` deltaP `-29.619` edge `-0.2086` maxDD `-43.93`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
