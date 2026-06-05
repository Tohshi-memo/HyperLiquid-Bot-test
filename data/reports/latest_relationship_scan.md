# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T19:07:29.704523+00:00`
- Price records: `672`
- Market context records: `2997`
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

- `market_context_high->crypto_alt_24h` score `18.1857` n `98` status `ready` deltaP `6.1579` edge `1.8661` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `12.3297` n `98` status `ready` deltaP `42.4674` edge `0.7554` maxDD `-0.2165`
- `market_context_high->unknown_24h` score `11.7272` n `98` status `ready` deltaP `18.3957` edge `0.9011` maxDD `-1.7175`
- `market_context_high->equity_24h` score `8.704` n `98` status `ready` deltaP `17.1309` edge `0.8115` maxDD `-12.6963`
- `market_context_high->index_24h` score `5.4023` n `98` status `ready` deltaP `16.9147` edge `0.4355` maxDD `-2.5127`
- `market_context_high->commodity_4h` score `2.1687` n `102` status `ready` deltaP `16.3857` edge `0.1362` maxDD `-2.8438`
- `market_context_high->index_4h` score `1.2734` n `102` status `ready` deltaP `18.496` edge `0.1112` maxDD `-5.9381`
- `market_context_high->equity_4h` score `0.974` n `102` status `ready` deltaP `13.9019` edge `0.1742` maxDD `-9.0276`
- `market_context_high->index_1h` score `0.0256` n `105` status `ready` deltaP `5.6872` edge `0.0256` maxDD `-2.4852`
- `market_context_high->commodity_1h` score `-0.0497` n `105` status `ready` deltaP `1.0337` edge `0.0197` maxDD `-0.9706`
- `market_context_high->equity_1h` score `-0.3126` n `105` status `ready` deltaP `3.8495` edge `0.0362` maxDD `-5.1553`
- `market_context_high->crypto_alt_4h` score `-0.3332` n `102` status `ready` deltaP `22.5012` edge `0.3574` maxDD `-38.3432`
- `market_context_high->fx_1h` score `-0.3502` n `105` status `ready` deltaP `-2.0274` edge `0.0008` maxDD `-0.2412`
- `market_context_high->crypto_alt_1h` score `-1.0398` n `105` status `ready` deltaP `6.4899` edge `0.0263` maxDD `-13.8964`
- `market_context_high->fx_4h` score `-1.1156` n `102` status `ready` deltaP `-9.8039` edge `0.0002` maxDD `-0.5631`
- `market_context_high->metal_1h` score `-1.1803` n `105` status `ready` deltaP `-2.448` edge `-0.0101` maxDD `-6.3255`
- `market_context_high->unknown_4h` score `-1.3691` n `102` status `ready` deltaP `-0.8489` edge `-0.0031` maxDD `-3.7602`
- `market_context_high->crypto_major_1h` score `-1.4972` n `105` status `ready` deltaP `4.069` edge `-0.0024` maxDD `-14.6674`
- `market_context_high->unknown_1h` score `-1.858` n `105` status `ready` deltaP `1.2375` edge `-0.09` maxDD `-3.1801`
- `market_context_high->fx_24h` score `-1.9292` n `98` status `ready` deltaP `-7.0011` edge `-0.0269` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
