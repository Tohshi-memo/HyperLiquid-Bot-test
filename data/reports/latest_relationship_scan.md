# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T05:52:24.159301+00:00`
- Price records: `672`
- Market context records: `3044`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6988`

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

- `market_context_high->crypto_alt_24h` score `24.8572` n `99` status `ready` deltaP `12.7209` edge `2.3783` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `13.492` n `99` status `ready` deltaP `24.495` edge `1.0075` maxDD `-1.7175`
- `market_context_high->commodity_24h` score `13.1591` n `99` status `ready` deltaP `43.4186` edge `0.8312` maxDD `-1.2589`
- `market_context_high->equity_24h` score `9.2345` n `99` status `ready` deltaP `23.8952` edge `1.2998` maxDD `-18.3486`
- `market_context_high->index_24h` score `8.8574` n `99` status `ready` deltaP `23.4849` edge `0.7071` maxDD `-4.7103`
- `market_context_high->commodity_4h` score `2.6445` n `129` status `ready` deltaP `17.8637` edge `0.166` maxDD `-2.8438`
- `market_context_high->commodity_1h` score `-0.1547` n `132` status `ready` deltaP `1.0751` edge `0.0222` maxDD `-1.7142`
- `market_context_high->unknown_4h` score `-0.4766` n `129` status `ready` deltaP `1.6981` edge `0.0543` maxDD `-3.7602`
- `market_context_high->index_1h` score `-0.512` n `132` status `ready` deltaP `3.62` edge `0.0165` maxDD `-4.5023`
- `market_context_high->fx_1h` score `-0.5328` n `132` status `ready` deltaP `-4.7042` edge `0.0` maxDD `-0.289`
- `market_context_high->crypto_alt_1h` score `-0.6925` n `132` status `ready` deltaP `6.3419` edge `0.0819` maxDD `-14.7034`
- `market_context_high->equity_1h` score `-0.7364` n `132` status `ready` deltaP `2.8988` edge `0.0276` maxDD `-8.3065`
- `market_context_high->unknown_1h` score `-0.9377` n `132` status `ready` deltaP `4.5818` edge `-0.0356` maxDD `-3.1801`
- `market_context_high->index_4h` score `-0.955` n `129` status `ready` deltaP `12.7127` edge `0.0621` maxDD `-16.8761`
- `market_context_high->crypto_major_1h` score `-1.0479` n `132` status `ready` deltaP `4.3413` edge `0.063` maxDD `-15.1032`
- `market_context_high->fx_4h` score `-1.1458` n `129` status `ready` deltaP `-8.9407` edge `-0.0038` maxDD `-1.0127`
- `market_context_high->metal_1h` score `-1.2042` n `132` status `ready` deltaP `-2.0369` edge `-0.004` maxDD `-7.278`
- `market_context_high->fx_24h` score `-1.3279` n `99` status `ready` deltaP `-1.1048` edge `-0.0161` maxDD `-0.6418`
- `market_context_high->equity_4h` score `-2.9354` n `129` status `ready` deltaP `9.6899` edge `0.0518` maxDD `-34.4188`
- `market_context_high->crypto_alt_4h` score `-3.257` n `129` status `ready` deltaP `17.7171` edge `0.2688` maxDD `-58.6918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
