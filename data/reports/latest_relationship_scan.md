# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T03:37:19.194926+00:00`
- Price records: `672`
- Market context records: `2525`
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

- `market_context_high->crypto_alt_4h` score `4.8916` n `160` status `ready` deltaP `22.8354` edge `0.5233` maxDD `-15.4319`
- `market_context_high->unknown_24h` score `4.8623` n `119` status `ready` deltaP `19.548` edge `0.3077` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `3.4442` n `160` status `ready` deltaP `16.1433` edge `0.3604` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `2.2067` n `119` status `ready` deltaP `11.6363` edge `0.5946` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `2.0479` n `160` status `ready` deltaP `11.5244` edge `0.1988` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `1.0271` n `162` status `ready` deltaP `8.7344` edge `0.1461` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `0.6118` n `162` status `ready` deltaP `7.7992` edge `0.1184` maxDD `-4.2199`
- `market_context_high->index_24h` score `-0.0167` n `119` status `ready` deltaP `3.373` edge `0.0742` maxDD `-2.5127`
- `market_context_high->crypto_alt_24h` score `-0.023` n `119` status `ready` deltaP `0.7046` edge `0.6881` maxDD `-43.6595`
- `market_context_high->index_4h` score `-0.0903` n `160` status `ready` deltaP `6.7683` edge `0.0315` maxDD `-2.3986`
- `market_context_high->equity_24h` score `-0.244` n `119` status `ready` deltaP `17.4851` edge `0.0158` maxDD `-6.8828`
- `market_context_high->commodity_1h` score `-0.347` n `162` status `ready` deltaP `4.5077` edge `0.0133` maxDD `-4.3601`
- `market_context_high->index_1h` score `-0.4112` n `162` status `ready` deltaP `1.4009` edge `0.0058` maxDD `-1.2855`
- `market_context_high->metal_1h` score `-0.485` n `162` status `ready` deltaP `0.73` edge `0.0089` maxDD `-3.0759`
- `market_context_high->fx_1h` score `-0.556` n `162` status `ready` deltaP `0.4861` edge `0.0039` maxDD `-0.278`
- `market_context_high->unknown_1h` score `-0.6188` n `162` status `ready` deltaP `1.4397` edge `0.0108` maxDD `-3.0902`
- `market_context_high->fx_4h` score `-0.7962` n `160` status `ready` deltaP `1.1128` edge `0.0122` maxDD `-0.8774`
- `market_context_high->equity_1h` score `-0.8029` n `162` status `ready` deltaP `0.0518` edge `0.0166` maxDD `-2.7085`
- `market_context_high->metal_4h` score `-0.8505` n `160` status `ready` deltaP `3.4604` edge `0.0448` maxDD `-4.7664`
- `market_context_high->fx_24h` score `-0.8705` n `119` status `ready` deltaP `2.9062` edge `0.0041` maxDD `-2.4729`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
