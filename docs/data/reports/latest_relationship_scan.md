# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T12:00:48.379299+00:00`
- Price records: `672`
- Market context records: `3071`
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

- `market_context_high->crypto_alt_24h` score `17.1842` n `90` status `ready` deltaP `12.3264` edge `2.5126` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `14.9338` n `90` status `ready` deltaP `47.1527` edge `0.9542` maxDD `-1.2589`
- `market_context_high->unknown_24h` score `13.6416` n `90` status `ready` deltaP `23.125` edge `1.0291` maxDD `-1.7175`
- `market_context_high->index_24h` score `12.4305` n `90` status `ready` deltaP `30.9028` edge `0.9179` maxDD `-4.7103`
- `market_context_high->equity_24h` score `11.0387` n `90` status `ready` deltaP `24.9306` edge `1.5242` maxDD `-18.3486`
- `market_context_high->commodity_4h` score `2.3411` n `127` status `ready` deltaP `16.1405` edge `0.1522` maxDD `-2.8438`
- `market_context_high->unknown_4h` score `-0.1593` n `127` status `ready` deltaP `2.7547` edge `0.0737` maxDD `-3.7602`
- `market_context_high->commodity_1h` score `-0.2955` n `127` status `ready` deltaP `-0.5045` edge `0.021` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.588` n `127` status `ready` deltaP `2.3398` edge `0.0153` maxDD `-4.5023`
- `market_context_high->crypto_alt_1h` score `-0.6779` n `127` status `ready` deltaP `4.2529` edge `0.0977` maxDD `-14.7034`
- `market_context_high->fx_24h` score `-0.7524` n `90` status `ready` deltaP `-0.4166` edge `-0.0065` maxDD `-0.6418`
- `market_context_high->fx_1h` score `-0.9726` n `127` status `ready` deltaP `-6.2827` edge `-0.0019` maxDD `-0.3147`
- `market_context_high->unknown_1h` score `-1.0033` n `127` status `ready` deltaP `2.5013` edge `-0.0272` maxDD `-3.1801`
- `market_context_high->crypto_major_1h` score `-1.0989` n `127` status `ready` deltaP `1.6962` edge `0.0741` maxDD `-15.1032`
- `market_context_high->equity_1h` score `-1.1019` n `127` status `ready` deltaP `-0.0554` edge `0.0045` maxDD `-8.6319`
- `market_context_high->fx_4h` score `-1.2555` n `127` status `ready` deltaP `-10.6035` edge `-0.0059` maxDD `-1.0829`
- `market_context_high->metal_1h` score `-1.3442` n `127` status `ready` deltaP `-4.4144` edge `-0.0061` maxDD `-7.278`
- `market_context_high->index_4h` score `-1.4118` n `127` status `ready` deltaP `8.4466` edge `0.0536` maxDD `-17.6057`
- `market_context_high->crypto_alt_4h` score `-3.0287` n `127` status `ready` deltaP `18.2531` edge `0.2945` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-3.7275` n `127` status `ready` deltaP `6.4901` edge `0.0027` maxDD `-36.242`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
