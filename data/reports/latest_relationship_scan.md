# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T01:33:40.356034+00:00`
- Price records: `672`
- Market context records: `3025`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6987`

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

- `market_context_high->crypto_alt_24h` score `22.0671` n `99` status `ready` deltaP `10.2904` edge `2.162` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `12.6531` n `99` status `ready` deltaP `22.0644` edge `0.9538` maxDD `-1.7175`
- `market_context_high->commodity_24h` score `12.6305` n `99` status `ready` deltaP `42.3769` edge `0.7941` maxDD `-1.2589`
- `market_context_high->equity_24h` score `7.2761` n `99` status `ready` deltaP `20.9438` edge `1.0684` maxDD `-18.3486`
- `market_context_high->index_24h` score `7.1177` n `99` status `ready` deltaP `20.5335` edge `0.5818` maxDD `-4.7103`
- `market_context_high->commodity_4h` score `2.6502` n `116` status `ready` deltaP `18.955` edge `0.1592` maxDD `-2.8438`
- `market_context_high->equity_4h` score `0.4559` n `116` status `ready` deltaP `13.7878` edge `0.1662` maxDD `-13.6407`
- `market_context_high->crypto_alt_4h` score `0.2888` n `116` status `ready` deltaP `23.4493` edge `0.4355` maxDD `-38.7172`
- `market_context_high->index_4h` score `0.2189` n `116` status `ready` deltaP `16.7893` edge `0.1059` maxDD `-10.8483`
- `market_context_high->commodity_1h` score `0.0995` n `128` status `ready` deltaP `3.008` edge `0.0305` maxDD `-1.7142`
- `market_context_high->equity_1h` score `-0.3761` n `128` status `ready` deltaP `3.7051` edge `0.0367` maxDD `-5.7692`
- `market_context_high->index_1h` score `-0.3843` n `128` status `ready` deltaP `4.2056` edge `0.0241` maxDD `-4.1126`
- `market_context_high->crypto_alt_1h` score `-0.5094` n `128` status `ready` deltaP `6.9985` edge `0.101` maxDD `-14.7034`
- `market_context_high->fx_1h` score `-0.5355` n `128` status `ready` deltaP `-4.8372` edge `0.0002` maxDD `-0.2615`
- `market_context_high->unknown_4h` score `-0.6395` n `116` status `ready` deltaP `0.6518` edge `0.0477` maxDD `-3.7602`
- `market_context_high->unknown_1h` score `-0.7015` n `128` status `ready` deltaP `4.5191` edge `-0.0155` maxDD `-3.1801`
- `market_context_high->crypto_major_1h` score `-0.944` n `128` status `ready` deltaP `5.0056` edge `0.0719` maxDD `-15.1032`
- `market_context_high->metal_1h` score `-1.1187` n `128` status `ready` deltaP `-1.2772` edge `-0.0031` maxDD `-6.8783`
- `market_context_high->fx_4h` score `-1.5036` n `116` status `ready` deltaP `-6.7967` edge `-0.001` maxDD `-0.6521`
- `market_context_high->fx_24h` score `-1.6528` n `99` status `ready` deltaP `-4.0562` edge `-0.0235` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
