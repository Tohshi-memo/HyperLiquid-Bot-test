# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T02:37:26.826268+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9116`

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

- `news_risk_high->crypto_major_24h` score `43.3263` n `79` status `ready` deltaP `18.3676` edge `3.5919` maxDD `-5.9724`
- `news_risk_high->crypto_alt_24h` score `39.3493` n `79` status `ready` deltaP `31.5181` edge `3.2069` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `24.2322` n `94` status `ready` deltaP `-3.1688` edge `2.0638` maxDD `-0.5326`
- `market_context_high->commodity_24h` score `7.6911` n `92` status `ready` deltaP `38.436` edge `0.4372` maxDD `-0.8682`
- `news_risk_high->equity_24h` score `7.1959` n `79` status `ready` deltaP `35.7134` edge `0.3658` maxDD `-0.0053`
- `news_risk_high->crypto_alt_4h` score `5.9366` n `98` status `ready` deltaP `22.8378` edge `0.4634` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.6668` n `98` status `ready` deltaP `23.1427` edge `0.3604` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `3.9489` n `94` status `ready` deltaP `36.0145` edge `0.1023` maxDD `-0.0659`
- `news_risk_high->crypto_alt_1h` score `3.2808` n `98` status `ready` deltaP `18.624` edge `0.1958` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.5541` n `98` status `ready` deltaP `21.0192` edge `0.125` maxDD `-2.8494`
- `market_context_high->commodity_1h` score `1.9337` n `95` status `ready` deltaP `22.3464` edge `0.0332` maxDD `-0.3491`
- `news_risk_high->metal_24h` score `1.5983` n `79` status `ready` deltaP `23.2221` edge `0.0628` maxDD `-2.4203`
- `market_context_high->fx_4h` score `1.1359` n `94` status `ready` deltaP `20.7998` edge `0.0028` maxDD `-0.0779`
- `news_risk_high->metal_4h` score `0.832` n `98` status `ready` deltaP `19.2819` edge `0.0462` maxDD `-2.0994`
- `news_risk_high->metal_1h` score `0.7303` n `98` status `ready` deltaP `15.7552` edge `0.016` maxDD `-0.8144`
- `market_context_high->fx_24h` score `0.7209` n `92` status `ready` deltaP `12.2811` edge `-0.0176` maxDD `-0.0027`
- `market_context_high->fx_1h` score `0.4287` n `95` status `ready` deltaP `8.8213` edge `0.0027` maxDD `-0.063`
- `news_risk_high->equity_1h` score `0.3731` n `98` status `ready` deltaP `6.2172` edge `0.0302` maxDD `-0.9112`
- `news_risk_high->commodity_24h` score `0.1709` n `79` status `ready` deltaP `16.3942` edge `0.0432` maxDD `-3.4467`
- `news_risk_high->fx_4h` score `-0.0671` n `98` status `ready` deltaP `5.3851` edge `0.0221` maxDD `-0.421`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
