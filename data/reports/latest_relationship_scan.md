# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T12:52:23.336246+00:00`
- Price records: `672`
- Market context records: `3075`
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

- `market_context_high->crypto_alt_24h` score `17.3439` n `90` status `ready` deltaP `12.8472` edge `2.5296` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `15.0487` n `90` status `ready` deltaP `47.6736` edge `0.9603` maxDD `-1.2589`
- `market_context_high->unknown_24h` score `13.6903` n `90` status `ready` deltaP `23.2986` edge `1.032` maxDD `-1.7175`
- `market_context_high->index_24h` score `12.6441` n `90` status `ready` deltaP `30.9028` edge `0.9357` maxDD `-4.7103`
- `market_context_high->equity_24h` score `11.345` n `90` status `ready` deltaP `25.4514` edge `1.56` maxDD `-18.3486`
- `market_context_high->commodity_4h` score `2.2769` n `127` status `ready` deltaP `15.6832` edge `0.1499` maxDD `-2.8438`
- `market_context_high->unknown_4h` score `-0.0977` n `127` status `ready` deltaP `3.0596` edge `0.0768` maxDD `-3.7602`
- `market_context_high->commodity_1h` score `-0.2823` n `127` status `ready` deltaP `-0.3548` edge `0.0211` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.5989` n `127` status `ready` deltaP `2.3398` edge `0.0139` maxDD `-4.5023`
- `market_context_high->crypto_alt_1h` score `-0.6857` n `127` status `ready` deltaP `4.2529` edge `0.0967` maxDD `-14.7034`
- `market_context_high->fx_24h` score `-0.7341` n `90` status `ready` deltaP `-0.243` edge `-0.0053` maxDD `-0.6418`
- `market_context_high->fx_1h` score `-0.9726` n `127` status `ready` deltaP `-6.2827` edge `-0.0019` maxDD `-0.3147`
- `market_context_high->unknown_1h` score `-1.0345` n `127` status `ready` deltaP `2.2019` edge `-0.0278` maxDD `-3.1801`
- `market_context_high->crypto_major_1h` score `-1.1051` n `127` status `ready` deltaP `1.6962` edge `0.0733` maxDD `-15.1032`
- `market_context_high->equity_1h` score `-1.1144` n `127` status `ready` deltaP `-0.0554` edge `0.0029` maxDD `-8.6319`
- `market_context_high->fx_4h` score `-1.2713` n `127` status `ready` deltaP `-10.9084` edge `-0.0059` maxDD `-1.0829`
- `market_context_high->metal_1h` score `-1.3707` n `127` status `ready` deltaP `-4.8635` edge `-0.0065` maxDD `-7.278`
- `market_context_high->index_4h` score `-1.4455` n `127` status `ready` deltaP `8.1417` edge `0.0513` maxDD `-17.6057`
- `market_context_high->crypto_alt_4h` score `-2.9785` n `127` status `ready` deltaP `18.5579` edge `0.2989` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-3.7691` n `127` status `ready` deltaP `6.1852` edge `-0.0006` maxDD `-36.242`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
