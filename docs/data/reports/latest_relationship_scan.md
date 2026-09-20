# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T00:22:25.837918+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8834`

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

- `news_risk_high->crypto_major_24h` score `50.895` n `72` status `ready` deltaP `26.7361` edge `4.1522` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `44.1435` n `72` status `ready` deltaP `32.4653` edge `3.6001` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `18.3027` n `101` status `ready` deltaP `-5.7821` edge `1.5871` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `8.4184` n `72` status `ready` deltaP `36.8055` edge `0.4604` maxDD `-0.0053`
- `market_context_high->commodity_24h` score `7.9196` n `101` status `ready` deltaP `39.0573` edge `0.4521` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `5.9954` n `98` status `ready` deltaP `22.8378` edge `0.4683` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.6718` n `98` status `ready` deltaP `23.2951` edge `0.3598` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `3.7454` n `101` status `ready` deltaP `34.3863` edge `0.0962` maxDD `-0.0659`
- `news_risk_high->crypto_alt_1h` score `3.2293` n `98` status `ready` deltaP `18.3246` edge `0.1935` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.4439` n `98` status `ready` deltaP `20.121` edge `0.1218` maxDD `-2.8494`
- `market_context_high->commodity_1h` score `1.7462` n `103` status `ready` deltaP `20.9421` edge `0.0311` maxDD `-0.3491`
- `news_risk_high->metal_24h` score `1.6834` n `72` status `ready` deltaP `22.3958` edge `0.0754` maxDD `-2.4203`
- `market_context_high->fx_4h` score `1.1344` n `101` status `ready` deltaP `20.9007` edge `0.002` maxDD `-0.0779`
- `news_risk_high->metal_4h` score `0.7955` n `98` status `ready` deltaP `18.8246` edge `0.0462` maxDD `-2.0994`
- `news_risk_high->metal_1h` score `0.6943` n `98` status `ready` deltaP `15.3061` edge `0.016` maxDD `-0.8144`
- `news_risk_high->fx_24h` score `0.6684` n `72` status `ready` deltaP `4.8612` edge `0.0415` maxDD `-0.1231`
- `market_context_high->fx_24h` score `0.5616` n `101` status `ready` deltaP `10.8155` edge `-0.0211` maxDD `-0.0027`
- `news_risk_high->equity_1h` score `0.4426` n `98` status `ready` deltaP `6.9657` edge `0.031` maxDD `-0.9112`
- `market_context_high->fx_1h` score `0.3595` n `103` status `ready` deltaP `8.017` edge `0.0023` maxDD `-0.063`
- `news_risk_high->fx_4h` score `-0.1049` n `98` status `ready` deltaP `4.9278` edge `0.022` maxDD `-0.421`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
