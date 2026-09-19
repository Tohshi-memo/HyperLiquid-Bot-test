# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T23:37:26.715460+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8828`

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

- `news_risk_high->crypto_major_24h` score `51.0085` n `72` status `ready` deltaP `26.9097` edge `4.1605` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `44.3472` n `72` status `ready` deltaP `32.9862` edge `3.6136` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `16.4675` n `104` status `ready` deltaP `-5.3822` edge `1.4315` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `8.5096` n `72` status `ready` deltaP `36.8055` edge `0.468` maxDD `-0.0053`
- `market_context_high->commodity_24h` score `7.9465` n `104` status `ready` deltaP `39.1693` edge `0.4536` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `5.9144` n `98` status `ready` deltaP `22.3805` edge `0.4646` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.5992` n `98` status `ready` deltaP `22.8378` edge `0.3568` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `3.5475` n `104` status `ready` deltaP `32.3874` edge `0.0932` maxDD `-0.0795`
- `news_risk_high->crypto_alt_1h` score `3.2245` n `98` status `ready` deltaP `18.3246` edge `0.1931` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.4283` n `98` status `ready` deltaP `19.9713` edge `0.1215` maxDD `-2.8494`
- `news_risk_high->metal_24h` score `1.6906` n `72` status `ready` deltaP `22.3958` edge `0.076` maxDD `-2.4203`
- `market_context_high->commodity_1h` score `1.6666` n `106` status `ready` deltaP `20.0966` edge `0.0301` maxDD `-0.3491`
- `market_context_high->fx_4h` score `1.1421` n `104` status `ready` deltaP `21.0718` edge `0.0015` maxDD `-0.0779`
- `news_risk_high->metal_4h` score `0.7577` n `98` status `ready` deltaP `18.3673` edge `0.0461` maxDD `-2.0994`
- `news_risk_high->metal_1h` score `0.6824` n `98` status `ready` deltaP `15.1564` edge `0.016` maxDD `-0.8144`
- `news_risk_high->fx_24h` score `0.6172` n `72` status `ready` deltaP `4.3403` edge `0.0407` maxDD `-0.1231`
- `market_context_high->fx_24h` score `0.5055` n `104` status `ready` deltaP `10.3232` edge `-0.0225` maxDD `-0.0027`
- `news_risk_high->equity_1h` score `0.4306` n `98` status `ready` deltaP `6.816` edge `0.031` maxDD `-0.9112`
- `market_context_high->fx_1h` score `0.2897` n `106` status `ready` deltaP `7.1744` edge `0.0021` maxDD `-0.063`
- `news_risk_high->fx_4h` score `-0.1427` n `98` status `ready` deltaP `4.4705` edge `0.0219` maxDD `-0.421`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
