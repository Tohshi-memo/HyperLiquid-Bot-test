# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T19:52:31.997883+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8574`

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

- `news_risk_high->crypto_major_24h` score `51.1972` n `72` status `ready` deltaP `27.6041` edge `4.1716` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `44.7231` n `72` status `ready` deltaP `33.6806` edge `3.6403` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `42.7717` n `119` status `ready` deltaP `-3.6854` edge `3.6122` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `8.9118` n `72` status `ready` deltaP `37.1528` edge `0.4992` maxDD `-0.0053`
- `market_context_high->commodity_24h` score `7.8083` n `119` status `ready` deltaP `40.3813` edge `0.434` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `5.5546` n `98` status `ready` deltaP `20.7037` edge `0.4458` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.2469` n `98` status `ready` deltaP `21.3134` edge `0.3376` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `3.2328` n `98` status `ready` deltaP `18.624` edge `0.1918` maxDD `-2.058`
- `market_context_high->commodity_4h` score `2.622` n `119` status `ready` deltaP `27.0023` edge `0.0803` maxDD `-0.345`
- `news_risk_high->crypto_major_1h` score `2.3468` n `98` status `ready` deltaP `19.5222` edge `0.1177` maxDD `-2.8494`
- `news_risk_high->metal_24h` score `1.7261` n `72` status `ready` deltaP `22.5694` edge `0.0778` maxDD `-2.4203`
- `market_context_high->commodity_1h` score `1.4374` n `119` status `ready` deltaP `17.8018` edge `0.0263` maxDD `-0.3491`
- `news_risk_high->metal_4h` score `0.849` n `98` status `ready` deltaP `19.4344` edge `0.0466` maxDD `-2.0994`
- `news_risk_high->metal_1h` score `0.7315` n `98` status `ready` deltaP `15.7552` edge `0.0161` maxDD `-0.8144`
- `market_context_high->fx_4h` score `0.6974` n `119` status `ready` deltaP `15.9484` edge `-0.0014` maxDD `-0.0779`
- `news_risk_high->equity_1h` score `0.5193` n `98` status `ready` deltaP `7.7142` edge `0.0324` maxDD `-0.9112`
- `news_risk_high->fx_24h` score `0.3927` n `72` status `ready` deltaP `1.9098` edge `0.0382` maxDD `-0.1231`
- `market_context_high->fx_24h` score `0.2271` n `119` status `ready` deltaP `8.0139` edge `-0.0303` maxDD `-0.0027`
- `news_risk_high->equity_4h` score `0.0243` n `98` status `ready` deltaP `9.5134` edge `0.083` maxDD `-5.2186`
- `market_context_high->fx_1h` score `-0.0313` n `119` status `ready` deltaP `3.3425` edge `0.0009` maxDD `-0.063`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
