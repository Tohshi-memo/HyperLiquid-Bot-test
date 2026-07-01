# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T12:22:32.327929+00:00`
- Price records: `672`
- Market context records: `5351`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11468`

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

- `market_context_high->unknown_24h` score `15.6115` n `160` status `ready` deltaP `20.3472` edge `1.1743` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `5.485` n `160` status `ready` deltaP `21.6319` edge `0.7669` maxDD `-29.6555`
- `market_context_high->equity_24h` score `4.5449` n `160` status `ready` deltaP `17.6736` edge `0.8238` maxDD `-40.0306`
- `market_context_high->crypto_major_4h` score `2.7679` n `194` status `ready` deltaP `13.3361` edge `0.371` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `2.4972` n `194` status `ready` deltaP `10.512` edge `0.3021` maxDD `-9.46`
- `market_context_high->equity_4h` score `1.7278` n `194` status `ready` deltaP `9.7875` edge `0.2426` maxDD `-7.4425`
- `market_context_high->index_24h` score `0.8367` n `160` status `ready` deltaP `25.1042` edge `0.1034` maxDD `-7.413`
- `market_context_high->equity_1h` score `0.3754` n `196` status `ready` deltaP `7.2162` edge `0.0797` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.1284` n `160` status `ready` deltaP `9.3056` edge `0.0382` maxDD `-0.8294`
- `market_context_high->index_1h` score `-0.0026` n `196` status `ready` deltaP `5.7681` edge `0.0117` maxDD `-1.0296`
- `market_context_high->crypto_major_1h` score `-0.011` n `196` status `ready` deltaP `4.2802` edge `0.0951` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `-0.0406` n `196` status `ready` deltaP `1.5856` edge `0.0822` maxDD `-5.0257`
- `market_context_high->fx_1h` score `-0.4096` n `196` status `ready` deltaP `-0.4155` edge `-0.0008` maxDD `-0.5823`
- `market_context_high->index_4h` score `-0.4133` n `194` status `ready` deltaP `5.6119` edge `0.0255` maxDD `-2.9391`
- `market_context_high->metal_1h` score `-0.4916` n `196` status `ready` deltaP `0.5988` edge `0.0005` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-0.7175` n `194` status `ready` deltaP `1.221` edge `0.0028` maxDD `-1.567`
- `market_context_high->unknown_4h` score `-1.2665` n `194` status `ready` deltaP `7.7555` edge `-0.039` maxDD `-6.126`
- `market_context_high->commodity_1h` score `-1.4973` n `196` status `ready` deltaP `-3.8983` edge `-0.007` maxDD `-3.3428`
- `market_context_high->metal_4h` score `-2.6352` n `194` status `ready` deltaP `-7.5292` edge `-0.0352` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-3.8298` n `194` status `ready` deltaP `-7.1662` edge `-0.043` maxDD `-11.937`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
