# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T04:07:30.413961+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8064`

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

- `market_context_high->unknown_24h` score `7240.5979` n `44` status `ready` deltaP `1.3889` edge `603.3739` maxDD `0.0`
- `market_context_high->unknown_4h` score `435.4749` n `47` status `ready` deltaP `9.1463` edge `36.2286` maxDD `0.0`
- `market_context_high->unknown_1h` score `65.3377` n `49` status `ready` deltaP `5.2151` edge `5.4211` maxDD `-0.2178`
- `market_context_high->equity_24h` score `19.2096` n `44` status `ready` deltaP `42.3454` edge `1.3421` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `13.7973` n `94` status `ready` deltaP `33.9133` edge `1.0593` maxDD `-6.8493`
- `market_context_high->commodity_24h` score `6.7782` n `44` status `ready` deltaP `44.8705` edge `0.2968` maxDD `-0.8203`
- `market_context_high->crypto_alt_4h` score `6.499` n `47` status `ready` deltaP `28.2466` edge `0.3827` maxDD `-1.6876`
- `market_context_high->index_24h` score `6.3774` n `44` status `ready` deltaP `49.1319` edge `0.2039` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `5.3489` n `47` status `ready` deltaP `29.3202` edge `0.2839` maxDD `-1.6901`
- `market_context_high->equity_4h` score `3.9164` n `47` status `ready` deltaP `3.9407` edge `0.3703` maxDD `-2.283`
- `market_context_high->commodity_4h` score `2.974` n `47` status `ready` deltaP `30.5462` edge `0.0699` maxDD `-1.0567`
- `news_risk_high->crypto_alt_4h` score `2.2602` n `126` status `ready` deltaP `9.0132` edge `0.2669` maxDD `-7.4246`
- `market_context_high->equity_1h` score `2.1339` n `49` status `ready` deltaP `6.5441` edge `0.1867` maxDD `-1.5336`
- `market_context_high->crypto_alt_1h` score `1.6415` n `49` status `ready` deltaP `4.9523` edge `0.165` maxDD `-2.2314`
- `market_context_high->crypto_major_1h` score `1.4788` n `49` status `ready` deltaP `6.3944` edge `0.1315` maxDD `-1.4048`
- `market_context_high->fx_1h` score `1.2093` n `49` status `ready` deltaP `16.4487` edge `0.0087` maxDD `-0.0736`
- `market_context_high->crypto_alt_24h` score `1.1288` n `44` status `ready` deltaP `-9.0751` edge `0.357` maxDD `-8.8096`
- `market_context_high->metal_4h` score `0.9235` n `47` status `ready` deltaP `17.0375` edge `0.0473` maxDD `-0.7323`
- `market_context_high->crypto_major_24h` score `0.8901` n `44` status `ready` deltaP `1.7677` edge `0.17` maxDD `-3.0799`
- `market_context_high->metal_1h` score `0.6115` n `49` status `ready` deltaP `8.9942` edge `0.0167` maxDD `-0.3895`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
