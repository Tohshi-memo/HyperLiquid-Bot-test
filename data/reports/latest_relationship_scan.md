# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T18:37:16.866838+00:00`
- Price records: `672`
- Market context records: `1764`
- Flow alert records: `6979`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8872`

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

- `market_context_high->metal_24h` score `7.1864` n `173` status `ready` deltaP `27.9695` edge `0.655` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `6.175` n `195` status `ready` deltaP `21.7949` edge `0.5459` maxDD `-9.1295`
- `market_context_high->crypto_major_4h` score `4.7422` n `195` status `ready` deltaP `23.3615` edge `0.48` maxDD `-10.9117`
- `market_context_high->index_24h` score `3.947` n `173` status `ready` deltaP `18.6537` edge `0.3274` maxDD `-4.1604`
- `market_context_high->equity_4h` score `3.2243` n `195` status `ready` deltaP `17.3608` edge `0.2624` maxDD `-5.0894`
- `news_risk_high->commodity_1h` score `3.1019` n `30` status `ready` deltaP `24.2715` edge `0.1284` maxDD `-1.2043`
- `market_context_high->unknown_4h` score `3.0763` n `195` status `ready` deltaP `13.6319` edge `0.3926` maxDD `-11.1695`
- `market_context_high->unknown_24h` score `3.0333` n `173` status `ready` deltaP `14.5974` edge `0.6875` maxDD `-35.8966`
- `market_context_high->equity_24h` score `2.776` n `173` status `ready` deltaP `17.036` edge `0.6076` maxDD `-33.1875`
- `market_context_high->index_4h` score `1.046` n `195` status `ready` deltaP `12.9252` edge `0.1099` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `0.7966` n `195` status `ready` deltaP `7.5825` edge `0.1182` maxDD `-4.1892`
- `market_context_high->crypto_major_24h` score `0.519` n `173` status `ready` deltaP `19.1153` edge `0.7744` maxDD `-62.3533`
- `market_context_high->crypto_major_1h` score `0.2983` n `195` status `ready` deltaP `5.1904` edge `0.0976` maxDD `-3.9211`
- `market_context_high->equity_1h` score `0.0916` n `195` status `ready` deltaP `5.1428` edge `0.0542` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.1525` n `195` status `ready` deltaP `4.3751` edge `0.0213` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.204` n `195` status `ready` deltaP `12.6056` edge `0.159` maxDD `-12.5349`
- `news_risk_high->fx_1h` score `-0.5014` n `30` status `ready` deltaP `-5.5788` edge `-0.0009` maxDD `-0.0948`
- `news_risk_high->unknown_1h` score `-0.53` n `30` status `ready` deltaP `16.2575` edge `-0.1291` maxDD `-2.1115`
- `market_context_high->metal_1h` score `-0.5336` n `195` status `ready` deltaP `5.4261` edge `0.029` maxDD `-6.3532`
- `market_context_high->fx_24h` score `-0.5387` n `173` status `ready` deltaP `7.7121` edge `0.0086` maxDD `-1.3925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
