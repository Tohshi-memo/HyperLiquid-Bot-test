# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T16:07:24.007644+00:00`
- Price records: `672`
- Market context records: `2576`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9200`

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

- `market_context_high->crypto_alt_4h` score `6.2105` n `146` status `ready` deltaP `26.7207` edge `0.6073` maxDD `-15.4319`
- `market_context_high->unknown_24h` score `5.3374` n `119` status `ready` deltaP `19.2912` edge `0.349` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `4.3404` n `146` status `ready` deltaP `18.2697` edge `0.4209` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `3.1937` n `119` status `ready` deltaP `11.6363` edge `0.5605` maxDD `-22.4212`
- `market_context_high->crypto_alt_1h` score `1.5751` n `146` status `ready` deltaP `12.1791` edge `0.1688` maxDD `-6.1656`
- `market_context_high->unknown_4h` score `1.3068` n `146` status `ready` deltaP `9.9712` edge `0.1474` maxDD `-3.7312`
- `market_context_high->equity_24h` score `1.1851` n `119` status `ready` deltaP `19.5757` edge `0.0348` maxDD `-2.324`
- `market_context_high->crypto_major_1h` score `1.0578` n `146` status `ready` deltaP `10.6595` edge `0.1365` maxDD `-4.2199`
- `market_context_high->index_24h` score `0.6418` n `119` status `ready` deltaP `6.6235` edge `0.1074` maxDD `-2.5127`
- `market_context_high->crypto_alt_24h` score `0.3459` n `119` status `ready` deltaP `-0.1079` edge `0.6829` maxDD `-39.0265`
- `market_context_high->index_4h` score `0.3046` n `146` status `ready` deltaP `8.9751` edge `0.0497` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1419` n `146` status `ready` deltaP `3.7917` edge `0.0123` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.4104` n `146` status `ready` deltaP `1.8005` edge `0.0201` maxDD `-2.6375`
- `market_context_high->commodity_1h` score `-0.4171` n `146` status `ready` deltaP `5.502` edge `0.0164` maxDD `-4.3601`
- `market_context_high->metal_4h` score `-0.5908` n `146` status `ready` deltaP `4.5021` edge `0.0595` maxDD `-4.7664`
- `market_context_high->fx_1h` score `-0.6102` n `146` status `ready` deltaP `-0.2358` edge `0.0042` maxDD `-0.278`
- `market_context_high->metal_1h` score `-0.668` n `146` status `ready` deltaP `0.8121` edge `0.0137` maxDD `-2.9823`
- `market_context_high->fx_4h` score `-0.8244` n `146` status `ready` deltaP `0.5367` edge `0.0135` maxDD `-0.8621`
- `market_context_high->equity_1h` score `-0.8348` n `146` status `ready` deltaP `-0.527` edge `0.0178` maxDD `-2.7085`
- `market_context_high->equity_4h` score `-1.1114` n `146` status `ready` deltaP `1.9545` edge `0.0348` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
