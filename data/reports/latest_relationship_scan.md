# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-21T14:07:27.243712+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2590`

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

- `market_context_high->unknown_1h` score `10007.8314` n `126` status `ready` deltaP `0.8649` edge `834.0` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6081.7095` n `126` status `ready` deltaP `-0.7719` edge `506.8448` maxDD `-0.7759`
- `market_context_high->metal_1h` score `-0.2202` n `126` status `ready` deltaP `3.6522` edge `0.0139` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.3513` n `126` status `ready` deltaP `1.9603` edge `0.0031` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.6654` n `126` status `ready` deltaP `9.6617` edge `0.0309` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.4166` n `126` status `ready` deltaP `-9.1056` edge `-0.0014` maxDD `-0.4757`
- `market_context_high->fx_4h` score `-1.8693` n `126` status `ready` deltaP `-5.9645` edge `0.0017` maxDD `-1.794`
- `market_context_high->equity_1h` score `-1.9702` n `126` status `ready` deltaP `4.9401` edge `0.0088` maxDD `-13.1399`
- `market_context_high->commodity_1h` score `-2.3062` n `126` status `ready` deltaP `-8.5211` edge `-0.0222` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.6184` n `126` status `ready` deltaP `-5.7757` edge `-0.0164` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-2.9261` n `126` status `ready` deltaP `1.2118` edge `-0.0201` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-3.5828` n `126` status `ready` deltaP `-5.3916` edge `-0.0349` maxDD `-13.8848`
- `market_context_high->crypto_major_4h` score `-5.3002` n `126` status `ready` deltaP `-3.2424` edge `0.035` maxDD `-47.4317`
- `market_context_high->fx_24h` score `-6.4392` n `124` status `ready` deltaP `-12.9649` edge `-0.0068` maxDD `-6.8027`
- `market_context_high->commodity_4h` score `-6.9758` n `126` status `ready` deltaP `-19.7299` edge `-0.0805` maxDD `-15.5426`
- `market_context_high->metal_24h` score `-7.4186` n `124` status `ready` deltaP `8.9774` edge `0.1166` maxDD `-51.5731`
- `market_context_high->crypto_alt_4h` score `-8.8884` n `126` status `ready` deltaP `-4.3095` edge `-0.0307` maxDD `-46.5016`
- `market_context_high->crypto_major_24h` score `-11.1368` n `124` status `ready` deltaP `18.0724` edge `0.4442` maxDD `-147.398`
- `market_context_high->crypto_alt_24h` score `-14.4038` n `124` status `ready` deltaP `7.1405` edge `0.1629` maxDD `-152.572`
- `market_context_high->index_24h` score `-14.7107` n `124` status `ready` deltaP `-27.1057` edge `-0.1197` maxDD `-39.372`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
