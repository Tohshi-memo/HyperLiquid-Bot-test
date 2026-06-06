# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T13:22:28.047675+00:00`
- Price records: `672`
- Market context records: `3077`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6893`

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

- `market_context_high->crypto_alt_24h` score `17.3752` n `89` status `ready` deltaP `12.4454` edge `2.5363` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `15.2096` n `89` status `ready` deltaP `47.9459` edge `0.9719` maxDD `-1.2589`
- `market_context_high->unknown_24h` score `13.8427` n `89` status `ready` deltaP `23.4336` edge `1.0438` maxDD `-1.7175`
- `market_context_high->index_24h` score `12.9632` n `89` status `ready` deltaP `31.7767` edge `0.9523` maxDD `-4.7103`
- `market_context_high->equity_24h` score `11.4506` n `89` status `ready` deltaP `25.4116` edge `1.5738` maxDD `-18.3486`
- `market_context_high->commodity_4h` score `2.4383` n `126` status `ready` deltaP `16.0932` edge `0.1525` maxDD `-2.5277`
- `market_context_high->unknown_4h` score `-0.2051` n `126` status `ready` deltaP `2.7222` edge `0.0701` maxDD `-3.7602`
- `market_context_high->commodity_1h` score `-0.3174` n `126` status `ready` deltaP `-0.7485` edge `0.0208` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.6303` n `126` status `ready` deltaP `1.9461` edge `0.0125` maxDD `-4.5023`
- `market_context_high->crypto_alt_1h` score `-0.7192` n `126` status `ready` deltaP `3.878` edge `0.0949` maxDD `-14.7034`
- `market_context_high->fx_24h` score `-0.7366` n `89` status `ready` deltaP `-0.4565` edge `-0.0042` maxDD `-0.6418`
- `market_context_high->fx_1h` score `-1.0103` n `126` status `ready` deltaP `-6.7389` edge `-0.002` maxDD `-0.3147`
- `market_context_high->unknown_1h` score `-1.0631` n `126` status `ready` deltaP `1.7085` edge `-0.0269` maxDD `-3.1801`
- `market_context_high->crypto_major_1h` score `-1.1389` n `126` status `ready` deltaP `1.2712` edge `0.0718` maxDD `-15.1032`
- `market_context_high->equity_1h` score `-1.1481` n `126` status `ready` deltaP `-0.4491` edge `0.0012` maxDD `-8.6319`
- `market_context_high->fx_4h` score `-1.3075` n `126` status `ready` deltaP `-11.5733` edge `-0.0061` maxDD `-1.0829`
- `market_context_high->index_4h` score `-1.4437` n `126` status `ready` deltaP `8.268` edge `0.0507` maxDD `-17.6057`
- `market_context_high->metal_1h` score `-2.1643` n `126` status `ready` deltaP `-5.4819` edge `-0.007` maxDD `-7.278`
- `market_context_high->crypto_alt_4h` score `-2.991` n `126` status `ready` deltaP `18.5129` edge `0.2976` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-3.7637` n `126` status `ready` deltaP `6.4702` edge `-0.0018` maxDD `-36.242`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
