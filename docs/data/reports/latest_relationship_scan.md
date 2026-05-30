# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-30T13:22:16.092056+00:00`
- Price records: `672`
- Market context records: `2353`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9176`

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

- `news_risk_high->crypto_alt_24h` score `21.3937` n `43` status `ready` deltaP `50.0363` edge `1.5081` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `17.1843` n `43` status `ready` deltaP `45.4175` edge `1.1732` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.7163` n `43` status `ready` deltaP `29.7925` edge `1.0592` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `11.1842` n `43` status `ready` deltaP `19.7674` edge `0.8583` maxDD `-3.3119`
- `market_context_high->crypto_major_24h` score `9.7113` n `140` status `ready` deltaP `20.0` edge `1.0652` maxDD `-25.1408`
- `news_risk_high->unknown_24h` score `7.7013` n `43` status `ready` deltaP `27.6405` edge `0.4801` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `6.7901` n `140` status `ready` deltaP `24.4346` edge `0.4441` maxDD `-1.626`
- `market_context_high->crypto_major_4h` score `6.4828` n `156` status `ready` deltaP `25.2502` edge `0.5529` maxDD `-10.1468`
- `market_context_high->crypto_alt_4h` score `6.3968` n `156` status `ready` deltaP `22.4047` edge `0.6516` maxDD `-15.4319`
- `market_context_high->unknown_4h` score `5.7407` n `156` status `ready` deltaP `23.2293` edge `0.3845` maxDD `-1.8773`
- `news_risk_high->index_24h` score `4.9456` n `43` status `ready` deltaP `13.0976` edge `0.3667` maxDD `-1.3507`
- `news_risk_high->commodity_4h` score `3.964` n `43` status `ready` deltaP `33.5294` edge `0.3518` maxDD `-3.0367`
- `news_risk_high->fx_24h` score `3.4054` n `43` status `ready` deltaP `36.1879` edge `0.061` maxDD `-0.1442`
- `market_context_high->index_24h` score `2.4245` n `140` status `ready` deltaP `12.5992` edge `0.1698` maxDD `-1.4737`
- `news_risk_high->fx_4h` score `1.9869` n `43` status `ready` deltaP `25.4502` edge `0.0143` maxDD `-0.1382`
- `market_context_high->index_4h` score `1.9762` n `156` status `ready` deltaP `19.8249` edge `0.1151` maxDD `-2.2732`
- `market_context_high->equity_24h` score `1.9628` n `140` status `ready` deltaP `19.9752` edge `0.1831` maxDD `-6.8828`
- `market_context_high->crypto_alt_1h` score `1.5753` n `161` status `ready` deltaP `11.0862` edge `0.1761` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `1.574` n `161` status `ready` deltaP `12.8222` edge `0.1651` maxDD `-4.2199`
- `market_context_high->equity_4h` score `1.1169` n `156` status `ready` deltaP `10.8935` edge `0.1609` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
