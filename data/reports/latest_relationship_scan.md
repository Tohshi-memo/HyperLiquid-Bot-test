# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T00:52:32.943792+00:00`
- Price records: `672`
- Market context records: `5721`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8892`

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

- `market_context_high->crypto_major_4h` score `1.1293` n `271` status `ready` deltaP `9.6576` edge `0.1952` maxDD `-8.5712`
- `market_context_high->equity_24h` score `1.0062` n `218` status `ready` deltaP `16.9183` edge `0.5241` maxDD `-31.6316`
- `market_context_high->equity_4h` score `0.2226` n `271` status `ready` deltaP `7.6676` edge `0.1313` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.1934` n `283` status `ready` deltaP `3.3151` edge `0.0012` maxDD `-0.5144`
- `market_context_high->crypto_alt_4h` score `-0.424` n `271` status `ready` deltaP `7.0262` edge `0.1387` maxDD `-11.0033`
- `market_context_high->metal_1h` score `-0.451` n `283` status `ready` deltaP `1.5605` edge `-0.0007` maxDD `-2.0682`
- `market_context_high->equity_1h` score `-0.6159` n `283` status `ready` deltaP `3.2802` edge `0.0275` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.6246` n `283` status `ready` deltaP `0.4586` edge `0.0037` maxDD `-0.9472`
- `market_context_high->crypto_major_1h` score `-0.6506` n `283` status `ready` deltaP `2.8538` edge `0.0328` maxDD `-4.8164`
- `market_context_high->commodity_1h` score `-0.7553` n `283` status `ready` deltaP `-1.6684` edge `-0.005` maxDD `-3.7906`
- `market_context_high->crypto_alt_1h` score `-0.9737` n `283` status `ready` deltaP `0.758` edge `0.0284` maxDD `-5.1678`
- `market_context_high->fx_24h` score `-1.1121` n `218` status `ready` deltaP `11.0347` edge `0.0422` maxDD `-3.6674`
- `market_context_high->index_4h` score `-1.1689` n `271` status `ready` deltaP `1.2106` edge `0.0108` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.2586` n `271` status `ready` deltaP `2.5909` edge `0.0059` maxDD `-1.4288`
- `market_context_high->metal_4h` score `-2.5899` n `271` status `ready` deltaP `-6.7309` edge `-0.0496` maxDD `-11.6719`
- `market_context_high->index_24h` score `-2.8652` n `218` status `ready` deltaP `2.6153` edge `0.0297` maxDD `-18.1572`
- `market_context_high->commodity_4h` score `-3.8575` n `271` status `ready` deltaP `-3.8407` edge `-0.0283` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.3202` n `218` status `ready` deltaP `7.1961` edge `0.0377` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-7.53` n `218` status `ready` deltaP `-5.8661` edge `-0.2378` maxDD `-31.412`
- `market_context_high->commodity_24h` score `-11.3205` n `218` status `ready` deltaP `-9.3591` edge `-0.067` maxDD `-44.1188`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
