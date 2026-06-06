# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T22:07:22.521102+00:00`
- Price records: `672`
- Market context records: `3116`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7023`

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

- `market_context_high->commodity_24h` score `14.6635` n `95` status `ready` deltaP `46.6027` edge `0.9541` maxDD `-2.0927`
- `market_context_high->crypto_alt_24h` score `13.0753` n `95` status `ready` deltaP `11.2664` edge `2.381` maxDD `-53.716`
- `market_context_high->unknown_24h` score `12.8655` n `95` status `ready` deltaP `22.3391` edge `0.972` maxDD `-1.9039`
- `market_context_high->index_24h` score `10.3199` n `95` status `ready` deltaP `32.5713` edge `0.8983` maxDD `-16.1026`
- `market_context_high->equity_24h` score `5.4892` n `95` status `ready` deltaP `13.6878` edge `1.3267` maxDD `-47.137`
- `market_context_high->commodity_4h` score `2.9976` n `121` status `ready` deltaP `18.1944` edge `0.1743` maxDD `-1.9973`
- `market_context_high->commodity_1h` score `0.0196` n `133` status `ready` deltaP `2.4886` edge `0.0273` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.3989` n `133` status `ready` deltaP `5.1799` edge `0.0206` maxDD `-4.5023`
- `market_context_high->fx_24h` score `-0.5535` n `95` status `ready` deltaP `4.0552` edge `-0.0004` maxDD `-0.4876`
- `market_context_high->crypto_alt_1h` score `-0.725` n `133` status `ready` deltaP `3.8258` edge `0.0945` maxDD `-14.7034`
- `market_context_high->equity_1h` score `-1.0215` n `133` status `ready` deltaP `0.9781` edge `0.0111` maxDD `-8.8863`
- `market_context_high->fx_4h` score `-1.3674` n `121` status `ready` deltaP `-13.0266` edge `-0.0041` maxDD `-1.0829`
- `market_context_high->index_4h` score `-1.4067` n `121` status `ready` deltaP `9.8329` edge `0.045` maxDD `-17.6057`
- `market_context_high->fx_1h` score `-1.6627` n `133` status `ready` deltaP `-10.4565` edge `-0.0056` maxDD `-0.7266`
- `market_context_high->crypto_major_1h` score `-2.046` n `133` status `ready` deltaP `-0.2567` edge `0.0575` maxDD `-15.1032`
- `market_context_high->unknown_4h` score `-2.1099` n `121` status `ready` deltaP `3.6472` edge `0.0024` maxDD `-13.8701`
- `market_context_high->metal_1h` score `-2.2655` n `133` status `ready` deltaP `-6.2582` edge `-0.0077` maxDD `-7.4828`
- `market_context_high->unknown_1h` score `-2.768` n `133` status `ready` deltaP `3.101` edge `-0.0487` maxDD `-14.2111`
- `market_context_high->crypto_alt_4h` score `-3.9204` n `121` status `ready` deltaP `12.1749` edge `0.2207` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-4.0174` n `121` status `ready` deltaP `6.2865` edge `-0.0264` maxDD `-36.7784`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
