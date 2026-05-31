# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T05:22:18.359803+00:00`
- Price records: `672`
- Market context records: `2426`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9180`

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

- `news_risk_high->crypto_alt_24h` score `19.5808` n `43` status `ready` deltaP `44.6544` edge `1.3929` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `18.671` n `43` status `ready` deltaP `51.1466` edge `1.2589` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.9995` n `43` status `ready` deltaP `29.7925` edge `1.0828` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `10.1921` n `43` status `ready` deltaP `18.0313` edge `0.7872` maxDD `-3.3119`
- `news_risk_high->unknown_24h` score `7.6421` n `43` status `ready` deltaP `25.7307` edge `0.4879` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `5.885` n `101` status `ready` deltaP `24.4413` edge `0.3603` maxDD `-1.626`
- `news_risk_high->index_24h` score `5.053` n `43` status `ready` deltaP `9.6254` edge `0.3988` maxDD `-1.3507`
- `market_context_high->crypto_alt_4h` score `4.6529` n `124` status `ready` deltaP `22.5806` edge `0.5051` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `4.5786` n `124` status `ready` deltaP `21.2333` edge `0.421` maxDD `-10.1468`
- `news_risk_high->fx_24h` score `3.457` n `43` status `ready` deltaP `36.1879` edge `0.0653` maxDD `-0.1442`
- `news_risk_high->commodity_4h` score `3.1833` n `43` status `ready` deltaP `28.9563` edge `0.2822` maxDD `-3.0367`
- `market_context_high->unknown_4h` score `2.707` n `124` status `ready` deltaP `13.8376` edge `0.1943` maxDD `-1.8773`
- `market_context_high->index_24h` score `2.5536` n `101` status `ready` deltaP `13.7239` edge `0.147` maxDD `-0.3888`
- `market_context_high->crypto_major_24h` score `2.5036` n `101` status `ready` deltaP `10.6401` edge `0.6393` maxDD `-25.1408`
- `news_risk_high->fx_4h` score `2.111` n `43` status `ready` deltaP `26.8221` edge `0.0155` maxDD `-0.1382`
- `news_risk_high->unknown_4h` score `1.7773` n `43` status `ready` deltaP `16.1444` edge `0.1128` maxDD `-2.7857`
- `market_context_high->crypto_major_1h` score `1.1977` n `124` status `ready` deltaP `11.073` edge `0.1454` maxDD `-4.2199`
- `news_risk_high->unknown_1h` score `1.1492` n `43` status `ready` deltaP `20.7457` edge `0.0044` maxDD `-1.7548`
- `market_context_high->crypto_alt_1h` score `1.0102` n `124` status `ready` deltaP `8.6875` edge `0.145` maxDD `-6.1656`
- `news_risk_high->commodity_1h` score `0.5484` n `43` status `ready` deltaP `9.2675` edge `0.0765` maxDD `-2.1052`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
