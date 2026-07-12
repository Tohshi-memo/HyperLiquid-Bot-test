# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T18:07:34.026347+00:00`
- Price records: `672`
- Market context records: `6525`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `7864`

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

- `news_risk_high->crypto_alt_24h` score `13.3015` n `32` status `ready` deltaP `36.211` edge `0.8818` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.5296` n `32` status `ready` deltaP `53.8995` edge `0.1848` maxDD `0.0`
- `market_context_high->unknown_24h` score `6.3086` n `143` status `ready` deltaP `11.6312` edge `0.7782` maxDD `-15.0689`
- `news_risk_high->crypto_major_24h` score `4.8754` n `32` status `ready` deltaP `20.911` edge `0.5636` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `3.6853` n `38` status `ready` deltaP `39.0164` edge `0.0516` maxDD `-0.0345`
- `market_context_high->unknown_1h` score `2.4495` n `186` status `ready` deltaP `-5.621` edge `0.3317` maxDD `-3.2083`
- `news_risk_high->commodity_24h` score `2.1401` n `32` status `ready` deltaP `23.0232` edge `0.0454` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `1.764` n `38` status `ready` deltaP `22.1636` edge `0.0173` maxDD `-0.1113`
- `market_context_high->commodity_24h` score `1.6875` n `143` status `ready` deltaP `14.872` edge `0.2283` maxDD `-5.2791`
- `market_context_high->index_4h` score `0.6604` n `175` status `ready` deltaP `14.0357` edge `0.0291` maxDD `-0.4108`
- `news_risk_high->crypto_major_1h` score `0.6081` n `38` status `ready` deltaP `5.4995` edge `0.095` maxDD `-2.6299`
- `market_context_high->crypto_alt_4h` score `0.4282` n `175` status `ready` deltaP `10.9129` edge `0.1183` maxDD `-6.7632`
- `news_risk_high->crypto_alt_1h` score `0.1147` n `38` status `ready` deltaP `2.0328` edge `0.0521` maxDD `-2.0756`
- `news_risk_high->index_24h` score `-0.2838` n `32` status `ready` deltaP `7.0299` edge `0.0039` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.3824` n `175` status `ready` deltaP `9.4286` edge `0.058` maxDD `-8.2573`
- `market_context_high->crypto_major_4h` score `-0.4268` n `175` status `ready` deltaP `12.5897` edge `0.0904` maxDD `-12.6576`
- `market_context_high->unknown_4h` score `-0.4337` n `175` status `ready` deltaP `-20.1707` edge `0.3389` maxDD `-10.5788`
- `market_context_high->fx_1h` score `-0.4349` n `186` status `ready` deltaP `-0.5586` edge `-0.0013` maxDD `-0.7249`
- `market_context_high->commodity_1h` score `-0.4781` n `186` status `ready` deltaP `1.3071` edge `-0.0017` maxDD `-2.1314`
- `market_context_high->crypto_major_1h` score `-0.5251` n `186` status `ready` deltaP `6.7446` edge `0.0143` maxDD `-6.7936`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
