# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T23:07:23.922455+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14792`

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

- `news_risk_high->unknown_24h` score `45.3677` n `51` status `ready` deltaP `9.2014` edge `3.7193` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.6294` n `53` status `ready` deltaP `24.5225` edge `0.8989` maxDD `-0.1281`
- `news_risk_high->equity_24h` score `7.1913` n `51` status `ready` deltaP `29.9939` edge `0.4924` maxDD `-4.7801`
- `news_risk_high->index_24h` score `3.9872` n `51` status `ready` deltaP `40.2676` edge `0.079` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.209` n `53` status `ready` deltaP `16.0123` edge `0.1962` maxDD `-0.8426`
- `news_risk_high->fx_4h` score `2.9956` n `53` status `ready` deltaP `35.7254` edge `0.0249` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `2.6708` n `133` status `ready` deltaP `22.6641` edge `0.1123` maxDD `-0.5994`
- `news_risk_high->crypto_alt_24h` score `2.6016` n `51` status `ready` deltaP `25.6944` edge `0.0455` maxDD `0.0`
- `news_risk_high->equity_4h` score `1.4866` n `53` status `ready` deltaP `18.3646` edge `0.0785` maxDD `-2.164`
- `news_risk_high->fx_1h` score `1.1513` n `53` status `ready` deltaP `15.9191` edge `0.0068` maxDD `-0.0257`
- `news_risk_high->metal_24h` score `0.6065` n `51` status `ready` deltaP `27.2059` edge `-0.1266` maxDD `-0.0053`
- `news_risk_high->commodity_1h` score `0.4739` n `53` status `ready` deltaP `11.2756` edge `-0.0044` maxDD `-0.5024`
- `news_risk_high->equity_1h` score `0.3671` n `53` status `ready` deltaP `12.476` edge `0.0003` maxDD `-0.9128`
- `market_context_high->unknown_1h` score `0.1914` n `133` status `ready` deltaP `11.5719` edge `-0.0163` maxDD `-1.5916`
- `news_risk_high->index_4h` score `0.0163` n `53` status `ready` deltaP `5.5943` edge `0.0038` maxDD `-0.1788`
- `news_risk_high->index_1h` score `-0.0854` n `53` status `ready` deltaP `3.7002` edge `-0.0003` maxDD `-0.1583`
- `market_context_high->unknown_24h` score `-0.2395` n `125` status `ready` deltaP `9.2014` edge `-0.0813` maxDD `0.0`
- `market_context_high->fx_1h` score `-0.4428` n `133` status `ready` deltaP `2.4988` edge `-0.0002` maxDD `-0.8587`
- `news_risk_high->metal_1h` score `-0.6223` n `53` status `ready` deltaP `-2.4093` edge `-0.0132` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.7491` n `53` status `ready` deltaP `2.833` edge `-0.0282` maxDD `-0.249`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
