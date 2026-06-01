# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T02:52:23.590823+00:00`
- Price records: `672`
- Market context records: `2522`
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

- `market_context_high->unknown_24h` score `4.9307` n `119` status `ready` deltaP `19.548` edge `0.3134` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `4.7387` n `157` status `ready` deltaP `22.3338` edge `0.5139` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.4293` n `157` status `ready` deltaP `15.6866` edge `0.3622` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `2.2555` n `119` status `ready` deltaP `11.8099` edge `0.5997` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `2.0703` n `157` status `ready` deltaP `11.5494` edge `0.2005` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `1.0871` n `162` status `ready` deltaP `8.8841` edge `0.1501` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `0.6741` n `162` status `ready` deltaP `8.0986` edge `0.1216` maxDD `-4.2199`
- `market_context_high->crypto_alt_24h` score `0.0344` n `119` status `ready` deltaP `0.8782` edge `0.6943` maxDD `-43.6595`
- `market_context_high->index_24h` score `0.0145` n `119` status `ready` deltaP `3.373` edge `0.0768` maxDD `-2.5127`
- `market_context_high->equity_24h` score `-0.1742` n `119` status `ready` deltaP `17.8324` edge `0.0193` maxDD `-6.8828`
- `market_context_high->index_4h` score `-0.223` n `157` status `ready` deltaP `6.0995` edge `0.0249` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.3752` n `162` status `ready` deltaP `1.4009` edge `0.0088` maxDD `-1.2855`
- `market_context_high->commodity_1h` score `-0.3773` n `162` status `ready` deltaP `4.0586` edge `0.0124` maxDD `-4.3601`
- `market_context_high->metal_1h` score `-0.4881` n `162` status `ready` deltaP `0.73` edge `0.0085` maxDD `-3.0759`
- `market_context_high->fx_1h` score `-0.5189` n `162` status `ready` deltaP `0.9352` edge `0.004` maxDD `-0.278`
- `market_context_high->unknown_1h` score `-0.5864` n `162` status `ready` deltaP `1.7391` edge `0.0115` maxDD `-3.0902`
- `market_context_high->equity_1h` score `-0.7862` n `162` status `ready` deltaP `0.2015` edge `0.017` maxDD `-2.7085`
- `market_context_high->fx_4h` score `-0.8428` n `157` status `ready` deltaP `0.6505` edge `0.0114` maxDD `-0.8774`
- `market_context_high->fx_24h` score `-0.8501` n `119` status `ready` deltaP `3.2534` edge `0.0044` maxDD `-2.4729`
- `market_context_high->metal_4h` score `-0.898` n `157` status `ready` deltaP `2.9265` edge `0.0444` maxDD `-4.7664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
