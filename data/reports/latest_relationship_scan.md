# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T04:37:23.199719+00:00`
- Price records: `672`
- Market context records: `2529`
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

- `market_context_high->crypto_alt_4h` score `5.0296` n `162` status `ready` deltaP `23.4643` edge `0.5306` maxDD `-15.4319`
- `market_context_high->unknown_24h` score `4.8035` n `119` status `ready` deltaP `19.548` edge `0.3028` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `3.5121` n `162` status `ready` deltaP `16.8417` edge `0.3614` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `2.1755` n `119` status `ready` deltaP `11.6363` edge `0.5906` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `1.984` n `162` status `ready` deltaP `11.4009` edge `0.1943` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `1.0475` n `162` status `ready` deltaP `8.7344` edge `0.1478` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `0.6094` n `162` status `ready` deltaP `7.6495` edge `0.1192` maxDD `-4.2199`
- `market_context_high->index_4h` score `-0.015` n `162` status `ready` deltaP `7.2004` edge `0.0349` maxDD `-2.3986`
- `market_context_high->index_24h` score `-0.0858` n `119` status `ready` deltaP `3.1994` edge `0.0696` maxDD `-2.5127`
- `market_context_high->crypto_alt_24h` score `-0.1047` n `119` status `ready` deltaP `0.1838` edge `0.6811` maxDD `-43.6595`
- `market_context_high->equity_24h` score `-0.3716` n `119` status `ready` deltaP `16.7907` edge `0.0098` maxDD `-6.8828`
- `market_context_high->commodity_1h` score `-0.3898` n `162` status `ready` deltaP `3.9089` edge `0.0118` maxDD `-4.3601`
- `market_context_high->index_1h` score `-0.4124` n `162` status `ready` deltaP `1.4009` edge `0.0057` maxDD `-1.2855`
- `market_context_high->metal_1h` score `-0.4944` n `162` status `ready` deltaP `0.5803` edge `0.0087` maxDD `-3.0759`
- `market_context_high->fx_1h` score `-0.544` n `162` status `ready` deltaP `0.6358` edge `0.0039` maxDD `-0.278`
- `market_context_high->unknown_1h` score `-0.554` n `162` status `ready` deltaP `1.8888` edge `0.0132` maxDD `-3.0902`
- `market_context_high->equity_1h` score `-0.7742` n `162` status `ready` deltaP `0.3512` edge `0.017` maxDD `-2.7085`
- `market_context_high->fx_4h` score `-0.7938` n `162` status `ready` deltaP `1.0971` edge `0.0125` maxDD `-0.8774`
- `market_context_high->fx_24h` score `-0.909` n `119` status `ready` deltaP `2.2117` edge `0.0038` maxDD `-2.4729`
- `market_context_high->metal_4h` score `-0.9473` n `162` status `ready` deltaP `2.8663` edge `0.0407` maxDD `-4.7664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
