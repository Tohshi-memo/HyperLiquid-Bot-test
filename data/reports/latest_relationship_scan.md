# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T23:52:27.050573+00:00`
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

- `news_risk_high->crypto_major_24h` score `50.9574` n `72` status `ready` deltaP `26.7361` edge `4.1574` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `44.2769` n `72` status `ready` deltaP `32.8125` edge `3.6089` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `17.0655` n `103` status `ready` deltaP `-5.5129` edge `1.4822` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `8.4784` n `72` status `ready` deltaP `36.8055` edge `0.4654` maxDD `-0.0053`
- `market_context_high->commodity_24h` score `7.9505` n `103` status `ready` deltaP `39.2496` edge `0.4534` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `5.9434` n `98` status `ready` deltaP `22.5329` edge `0.466` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.6246` n `98` status `ready` deltaP `22.9902` edge `0.3579` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `3.6135` n `103` status `ready` deltaP `33.0378` edge `0.0942` maxDD `-0.0659`
- `news_risk_high->crypto_alt_1h` score `3.2245` n `98` status `ready` deltaP `18.3246` edge `0.1931` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.4283` n `98` status `ready` deltaP `19.9713` edge `0.1215` maxDD `-2.8494`
- `market_context_high->commodity_1h` score `1.7159` n `105` status `ready` deltaP `20.6387` edge `0.0306` maxDD `-0.3491`
- `news_risk_high->metal_24h` score `1.687` n `72` status `ready` deltaP `22.3958` edge `0.0757` maxDD `-2.4203`
- `market_context_high->fx_4h` score `1.1402` n `103` status `ready` deltaP `21.0188` edge `0.0017` maxDD `-0.0779`
- `news_risk_high->metal_4h` score `0.7711` n `98` status `ready` deltaP `18.5197` edge `0.0462` maxDD `-2.0994`
- `news_risk_high->metal_1h` score `0.6824` n `98` status `ready` deltaP `15.1564` edge `0.016` maxDD `-0.8144`
- `news_risk_high->fx_24h` score `0.6346` n `72` status `ready` deltaP `4.5139` edge `0.041` maxDD `-0.1231`
- `market_context_high->fx_24h` score `0.5234` n `103` status `ready` deltaP `10.4874` edge `-0.0221` maxDD `-0.0027`
- `news_risk_high->equity_1h` score `0.4306` n `98` status `ready` deltaP `6.816` edge `0.031` maxDD `-0.9112`
- `market_context_high->fx_1h` score `0.3383` n `105` status `ready` deltaP `7.7673` edge `0.0022` maxDD `-0.063`
- `news_risk_high->fx_4h` score `-0.1293` n `98` status `ready` deltaP `4.6229` edge `0.022` maxDD `-0.421`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
