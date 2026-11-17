# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T04:52:27.354578+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4434`

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

- `market_context_high->unknown_24h` score `2085.1055` n `59` status `ready` deltaP `3.4483` edge `173.7358` maxDD `0.0`
- `news_risk_high->equity_24h` score `55.4974` n `50` status `ready` deltaP `60.5862` edge `4.2915` maxDD `-3.6503`
- `news_risk_high->crypto_major_24h` score `18.9973` n `50` status `ready` deltaP `35.4138` edge `2.3138` maxDD `-6.8139`
- `market_context_high->crypto_alt_24h` score `16.4766` n `59` status `ready` deltaP `12.6622` edge `1.501` maxDD `-13.3222`
- `news_risk_high->equity_4h` score `14.3532` n `50` status `ready` deltaP `43.4878` edge `1.0192` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `12.2122` n `59` status `ready` deltaP `36.7358` edge `1.6478` maxDD `-22.8301`
- `news_risk_high->crypto_alt_24h` score `9.2266` n `50` status `ready` deltaP `21.069` edge `1.493` maxDD `-29.0448`
- `news_risk_high->index_24h` score `8.3543` n `50` status `ready` deltaP `51.9655` edge `0.3801` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `7.5683` n `50` status `ready` deltaP `46.3793` edge `0.3215` maxDD `0.0`
- `news_risk_high->metal_4h` score `5.2035` n `50` status `ready` deltaP `45.9085` edge `0.1652` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.5372` n `50` status `ready` deltaP `26.9939` edge `0.3417` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `4.4926` n `50` status `ready` deltaP `22.5449` edge `0.2871` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `4.2573` n `50` status `ready` deltaP `21.9085` edge `0.3463` maxDD `-9.0062`
- `news_risk_high->commodity_4h` score `4.1397` n `50` status `ready` deltaP `37.4878` edge `0.1204` maxDD `-0.3611`
- `news_risk_high->index_4h` score `3.12` n `50` status `ready` deltaP `29.2195` edge `0.1002` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.1934` n `50` status `ready` deltaP `24.5449` edge `0.0446` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.5179` n `50` status `ready` deltaP `19.4431` edge `0.027` maxDD `-0.4103`
- `news_risk_high->metal_24h` score `0.7996` n `50` status `ready` deltaP `18.3448` edge `0.1975` maxDD `-7.3825`
- `news_risk_high->crypto_alt_1h` score `0.7329` n `50` status `ready` deltaP `16.3952` edge `0.0826` maxDD `-6.1688`
- `news_risk_high->crypto_major_1h` score `0.6993` n `50` status `ready` deltaP `18.2455` edge `0.0732` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
