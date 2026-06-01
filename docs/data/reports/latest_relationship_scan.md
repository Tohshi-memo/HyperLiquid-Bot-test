# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T03:52:21.139764+00:00`
- Price records: `672`
- Market context records: `2526`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9312`

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

- `market_context_high->crypto_alt_4h` score `4.9395` n `161` status `ready` deltaP `22.9984` edge `0.5262` maxDD `-15.4319`
- `market_context_high->unknown_24h` score `4.8347` n `119` status `ready` deltaP `19.548` edge `0.3054` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `3.4553` n `161` status `ready` deltaP `16.3413` edge `0.36` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `2.1966` n `119` status `ready` deltaP `11.6363` edge `0.5933` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `2.0496` n `161` status `ready` deltaP `11.6204` edge `0.1983` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `1.0247` n `162` status `ready` deltaP `8.7344` edge `0.1459` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `0.5938` n `162` status `ready` deltaP `7.6495` edge `0.1179` maxDD `-4.2199`
- `market_context_high->index_24h` score `-0.0287` n `119` status `ready` deltaP `3.373` edge `0.0732` maxDD `-2.5127`
- `market_context_high->crypto_alt_24h` score `-0.0378` n `119` status `ready` deltaP `0.7046` edge `0.6862` maxDD `-43.6595`
- `market_context_high->index_4h` score `-0.0441` n `161` status `ready` deltaP `6.9857` edge `0.0339` maxDD `-2.3986`
- `market_context_high->equity_24h` score `-0.2711` n `119` status `ready` deltaP `17.3115` edge `0.0147` maxDD `-6.8828`
- `market_context_high->commodity_1h` score `-0.3563` n `162` status `ready` deltaP `4.358` edge `0.0131` maxDD `-4.3601`
- `market_context_high->index_1h` score `-0.4124` n `162` status `ready` deltaP `1.4009` edge `0.0057` maxDD `-1.2855`
- `market_context_high->metal_1h` score `-0.4835` n `162` status `ready` deltaP `0.73` edge `0.0091` maxDD `-3.0759`
- `market_context_high->fx_1h` score `-0.556` n `162` status `ready` deltaP `0.4861` edge `0.0039` maxDD `-0.278`
- `market_context_high->unknown_1h` score `-0.6164` n `162` status `ready` deltaP `1.4397` edge `0.011` maxDD `-3.0902`
- `market_context_high->fx_4h` score `-0.7821` n `161` status `ready` deltaP `1.2593` edge `0.0124` maxDD `-0.8774`
- `market_context_high->equity_1h` score `-0.8041` n `162` status `ready` deltaP `0.0518` edge `0.0165` maxDD `-2.7085`
- `market_context_high->fx_24h` score `-0.8803` n `119` status `ready` deltaP `2.7326` edge `0.004` maxDD `-2.4729`
- `market_context_high->metal_4h` score `-0.8972` n `161` status `ready` deltaP `3.1615` edge `0.0429` maxDD `-4.7664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
