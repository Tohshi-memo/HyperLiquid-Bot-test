# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T18:37:22.838527+00:00`
- Price records: `672`
- Market context records: `2995`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6984`

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

- `market_context_high->crypto_alt_24h` score `17.6372` n `98` status `ready` deltaP `5.8107` edge `1.8227` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `12.2661` n `98` status `ready` deltaP `42.4674` edge `0.7501` maxDD `-0.2165`
- `market_context_high->unknown_24h` score `11.6143` n `98` status `ready` deltaP `18.0485` edge `0.894` maxDD `-1.7175`
- `market_context_high->equity_24h` score `8.3294` n `98` status `ready` deltaP `16.7836` edge `0.7826` maxDD `-12.6963`
- `market_context_high->index_24h` score `5.1849` n `98` status `ready` deltaP `16.5675` edge `0.4197` maxDD `-2.5127`
- `market_context_high->equity_4h` score `3.1677` n `100` status `ready` deltaP `14.9695` edge `0.227` maxDD `-2.6927`
- `market_context_high->index_4h` score `2.386` n `100` status `ready` deltaP `19.5244` edge `0.1475` maxDD `-1.9733`
- `market_context_high->commodity_4h` score `2.38` n `100` status `ready` deltaP `17.5122` edge `0.1463` maxDD `-2.8438`
- `market_context_high->crypto_alt_4h` score `0.9377` n `100` status `ready` deltaP `23.7561` edge `0.42` maxDD `-30.9862`
- `market_context_high->index_1h` score `-0.0118` n `105` status `ready` deltaP `5.3878` edge `0.0228` maxDD `-2.4852`
- `market_context_high->commodity_1h` score `-0.0466` n `105` status `ready` deltaP `1.0337` edge `0.0201` maxDD `-0.9706`
- `market_context_high->equity_1h` score `-0.3602` n `105` status `ready` deltaP `3.5501` edge `0.0321` maxDD `-5.1553`
- `market_context_high->fx_1h` score `-0.3666` n `105` status `ready` deltaP `-2.3268` edge `0.0007` maxDD `-0.2412`
- `market_context_high->unknown_4h` score `-0.9732` n `100` status `ready` deltaP `0.1707` edge `0.0231` maxDD `-3.7602`
- `market_context_high->fx_4h` score `-1.059` n `100` status `ready` deltaP `-9.0` edge `0.0021` maxDD `-0.5631`
- `market_context_high->crypto_alt_1h` score `-1.1318` n `105` status `ready` deltaP `6.1905` edge `0.0165` maxDD `-13.8964`
- `market_context_high->metal_1h` score `-1.1912` n `105` status `ready` deltaP `-2.448` edge `-0.0115` maxDD `-6.3255`
- `market_context_high->crypto_major_1h` score `-1.5799` n `105` status `ready` deltaP `3.7696` edge `-0.011` maxDD `-14.6674`
- `market_context_high->unknown_1h` score `-1.87` n `105` status `ready` deltaP `1.2375` edge `-0.091` maxDD `-3.1801`
- `market_context_high->fx_24h` score `-1.9466` n `98` status `ready` deltaP `-7.1747` edge `-0.0272` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
