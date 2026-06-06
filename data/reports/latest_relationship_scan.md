# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T04:52:20.667327+00:00`
- Price records: `672`
- Market context records: `3039`
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

- `market_context_high->crypto_alt_24h` score `24.1068` n `99` status `ready` deltaP `12.0265` edge `2.3204` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `13.3044` n `99` status `ready` deltaP `23.8005` edge `0.9965` maxDD `-1.7175`
- `market_context_high->commodity_24h` score `12.9715` n `99` status `ready` deltaP `42.7241` edge `0.8202` maxDD `-1.2589`
- `market_context_high->equity_24h` score `8.7639` n `99` status `ready` deltaP `23.2008` edge `1.2441` maxDD `-18.3486`
- `market_context_high->index_24h` score `8.4335` n `99` status `ready` deltaP `22.7904` edge `0.6764` maxDD `-4.7103`
- `market_context_high->commodity_4h` score `2.6277` n `129` status `ready` deltaP `17.8637` edge `0.1646` maxDD `-2.8438`
- `market_context_high->commodity_1h` score `-0.0208` n `130` status `ready` deltaP `2.1787` edge `0.026` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.4049` n `130` status `ready` deltaP `4.1248` edge `0.022` maxDD `-4.1126`
- `market_context_high->unknown_4h` score `-0.433` n `129` status `ready` deltaP `2.003` edge `0.0559` maxDD `-3.7602`
- `market_context_high->fx_1h` score `-0.5187` n `130` status `ready` deltaP `-4.4657` edge `0.0001` maxDD `-0.2801`
- `market_context_high->equity_1h` score `-0.5651` n `130` status `ready` deltaP `3.5882` edge `0.0341` maxDD `-7.438`
- `market_context_high->crypto_alt_1h` score `-0.5672` n `130` status `ready` deltaP `6.4118` edge `0.0975` maxDD `-14.7034`
- `market_context_high->unknown_1h` score `-0.7487` n `130` status `ready` deltaP `4.0788` edge `-0.0165` maxDD `-3.1801`
- `market_context_high->crypto_major_1h` score `-0.9816` n `130` status `ready` deltaP `4.3413` edge `0.0715` maxDD `-15.1032`
- `market_context_high->index_4h` score `-1.0162` n `129` status `ready` deltaP `12.2554` edge `0.0573` maxDD `-16.8761`
- `market_context_high->metal_1h` score `-1.1341` n `130` status `ready` deltaP `-1.6836` edge `-0.002` maxDD `-6.9069`
- `market_context_high->fx_4h` score `-1.1791` n `129` status `ready` deltaP `-9.5505` edge `-0.004` maxDD `-1.0127`
- `market_context_high->fx_24h` score `-1.4026` n `99` status `ready` deltaP `-1.7992` edge `-0.0177` maxDD `-0.6418`
- `market_context_high->equity_4h` score `-3.0334` n `129` status `ready` deltaP `9.0801` edge `0.0433` maxDD `-34.4188`
- `market_context_high->crypto_alt_4h` score `-3.4115` n `129` status `ready` deltaP `17.7171` edge `0.249` maxDD `-58.6918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
