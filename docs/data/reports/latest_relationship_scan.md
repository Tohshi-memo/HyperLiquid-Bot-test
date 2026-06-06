# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T11:52:23.997273+00:00`
- Price records: `672`
- Market context records: `3070`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6955`

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

- `market_context_high->crypto_alt_24h` score `17.1291` n `90` status `ready` deltaP `12.1527` edge `2.5067` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `14.8911` n `90` status `ready` deltaP `46.9791` edge `0.9518` maxDD `-1.2589`
- `market_context_high->unknown_24h` score `13.6049` n `90` status `ready` deltaP `22.9514` edge `1.0272` maxDD `-1.7175`
- `market_context_high->index_24h` score `12.3513` n `90` status `ready` deltaP `30.9028` edge `0.9113` maxDD `-4.7103`
- `market_context_high->equity_24h` score `10.929` n `90` status `ready` deltaP `24.757` edge `1.5113` maxDD `-18.3486`
- `market_context_high->commodity_4h` score `2.3701` n `127` status `ready` deltaP `16.2929` edge `0.1536` maxDD `-2.8438`
- `market_context_high->unknown_4h` score `-0.1593` n `127` status `ready` deltaP `2.7547` edge `0.0737` maxDD `-3.7602`
- `market_context_high->commodity_1h` score `-0.3099` n `127` status `ready` deltaP `-0.6542` edge `0.0208` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.588` n `127` status `ready` deltaP `2.3398` edge `0.0153` maxDD `-4.5023`
- `market_context_high->crypto_alt_1h` score `-0.6771` n `127` status `ready` deltaP `4.2529` edge `0.0978` maxDD `-14.7034`
- `market_context_high->fx_24h` score `-0.7654` n `90` status `ready` deltaP `-0.5902` edge `-0.007` maxDD `-0.6418`
- `market_context_high->fx_1h` score `-0.9726` n `127` status `ready` deltaP `-6.2827` edge `-0.0019` maxDD `-0.3147`
- `market_context_high->unknown_1h` score `-0.9853` n `127` status `ready` deltaP `2.651` edge `-0.0267` maxDD `-3.1801`
- `market_context_high->crypto_major_1h` score `-1.0973` n `127` status `ready` deltaP `1.6962` edge `0.0743` maxDD `-15.1032`
- `market_context_high->equity_1h` score `-1.1011` n `127` status `ready` deltaP `-0.0554` edge `0.0046` maxDD `-8.6319`
- `market_context_high->fx_4h` score `-1.2555` n `127` status `ready` deltaP `-10.6035` edge `-0.0059` maxDD `-1.0829`
- `market_context_high->metal_1h` score `-1.3357` n `127` status `ready` deltaP `-4.2647` edge `-0.006` maxDD `-7.278`
- `market_context_high->index_4h` score `-1.3991` n `127` status `ready` deltaP `8.599` edge `0.0542` maxDD `-17.6057`
- `market_context_high->crypto_alt_4h` score `-3.0405` n `127` status `ready` deltaP `18.1006` edge `0.294` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-3.7236` n `127` status `ready` deltaP `6.4901` edge `0.0032` maxDD `-36.242`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
