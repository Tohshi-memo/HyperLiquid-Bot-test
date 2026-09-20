# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T06:22:47.405544+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9222`

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

- `news_risk_high->crypto_major_24h` score `40.9296` n `81` status `ready` deltaP `17.1103` edge `3.4635` maxDD `-10.3413`
- `news_risk_high->crypto_alt_24h` score `37.3886` n `81` status `ready` deltaP `28.6844` edge `3.0624` maxDD `-9.3661`
- `market_context_high->commodity_24h` score `7.0897` n `77` status `ready` deltaP `36.3186` edge `0.4012` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `6.289` n `98` status `ready` deltaP `23.4476` edge `0.4887` maxDD `-7.675`
- `news_risk_high->equity_24h` score `6.2272` n `81` status `ready` deltaP `33.2755` edge `0.3107` maxDD `-0.4217`
- `news_risk_high->crypto_major_4h` score `4.8864` n `98` status `ready` deltaP `23.1427` edge `0.3787` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `3.8218` n `80` status `ready` deltaP `33.7805` edge `0.1066` maxDD `-0.0659`
- `news_risk_high->crypto_alt_1h` score `3.4104` n `98` status `ready` deltaP `18.9234` edge `0.2046` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.6501` n `98` status `ready` deltaP `21.3186` edge `0.131` maxDD `-2.8494`
- `market_context_high->fx_4h` score `2.3577` n `80` status `ready` deltaP `31.128` edge `0.0063` maxDD `-0.0543`
- `market_context_high->commodity_1h` score `1.7581` n `80` status `ready` deltaP `19.8054` edge `0.0355` maxDD `-0.3491`
- `news_risk_high->metal_24h` score `1.4424` n `81` status `ready` deltaP `22.2029` edge `0.0566` maxDD `-2.4203`
- `market_context_high->fx_24h` score `1.0119` n `77` status `ready` deltaP `14.6735` edge `-0.0093` maxDD `-0.0027`
- `news_risk_high->metal_4h` score `0.8966` n `98` status `ready` deltaP `20.0441` edge `0.0465` maxDD `-2.0994`
- `news_risk_high->metal_1h` score `0.7446` n `98` status `ready` deltaP `15.9049` edge `0.0162` maxDD `-0.8144`
- `market_context_high->fx_1h` score `0.6302` n `80` status `ready` deltaP `11.1602` edge `0.0039` maxDD `-0.063`
- `news_risk_high->equity_1h` score `0.3504` n `98` status `ready` deltaP `5.7681` edge `0.0313` maxDD `-0.9112`
- `news_risk_high->commodity_24h` score `0.3395` n `81` status `ready` deltaP `17.2068` edge `0.0594` maxDD `-3.4467`
- `news_risk_high->fx_4h` score `-0.1305` n `98` status `ready` deltaP `4.6229` edge `0.0219` maxDD `-0.421`
- `news_risk_high->index_1h` score `-0.4436` n `98` status `ready` deltaP `-0.2719` edge `0.0015` maxDD `-0.5244`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
