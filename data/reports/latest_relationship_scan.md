# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T13:07:22.691067+00:00`
- Price records: `672`
- Market context records: `3076`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6937`

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

- `market_context_high->crypto_alt_24h` score `17.3935` n `90` status `ready` deltaP `13.0208` edge `2.5348` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `15.0817` n `90` status `ready` deltaP `47.8472` edge `0.9619` maxDD `-1.2589`
- `market_context_high->unknown_24h` score `13.7198` n `90` status `ready` deltaP `23.4722` edge `1.0333` maxDD `-1.7175`
- `market_context_high->index_24h` score `12.7077` n `90` status `ready` deltaP `30.9028` edge `0.941` maxDD `-4.7103`
- `market_context_high->equity_24h` score `11.4414` n `90` status `ready` deltaP `25.625` edge `1.5712` maxDD `-18.3486`
- `market_context_high->commodity_4h` score `2.2721` n `127` status `ready` deltaP `15.6832` edge `0.1495` maxDD `-2.8438`
- `market_context_high->unknown_4h` score `-0.1085` n `127` status `ready` deltaP `3.0596` edge `0.0759` maxDD `-3.7602`
- `market_context_high->commodity_1h` score `-0.2823` n `127` status `ready` deltaP `-0.3548` edge `0.0211` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.602` n `127` status `ready` deltaP `2.3398` edge `0.0135` maxDD `-4.5023`
- `market_context_high->crypto_alt_1h` score `-0.6911` n `127` status `ready` deltaP `4.2529` edge `0.096` maxDD `-14.7034`
- `market_context_high->fx_24h` score `-0.7309` n `90` status `ready` deltaP `-0.243` edge `-0.0049` maxDD `-0.6418`
- `market_context_high->fx_1h` score `-0.9726` n `127` status `ready` deltaP `-6.2827` edge `-0.0019` maxDD `-0.3147`
- `market_context_high->unknown_1h` score `-1.0512` n `127` status `ready` deltaP `2.0522` edge `-0.0282` maxDD `-3.1801`
- `market_context_high->crypto_major_1h` score `-1.1051` n `127` status `ready` deltaP `1.6962` edge `0.0733` maxDD `-15.1032`
- `market_context_high->equity_1h` score `-1.1175` n `127` status `ready` deltaP `-0.0554` edge `0.0025` maxDD `-8.6319`
- `market_context_high->fx_4h` score `-1.28` n `127` status `ready` deltaP `-11.0608` edge `-0.006` maxDD `-1.0829`
- `market_context_high->metal_1h` score `-1.3785` n `127` status `ready` deltaP `-5.0132` edge `-0.0065` maxDD `-7.278`
- `market_context_high->index_4h` score `-1.455` n `127` status `ready` deltaP `7.9892` edge `0.0511` maxDD `-17.6057`
- `market_context_high->crypto_alt_4h` score `-2.9675` n `127` status `ready` deltaP `18.7104` edge `0.2993` maxDD `-58.6918`
- `market_context_high->metal_4h` score `-3.7703` n `127` status `ready` deltaP `-7.4767` edge `-0.0094` maxDD `-24.9302`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
