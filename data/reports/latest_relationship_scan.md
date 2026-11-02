# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-02T00:52:28.368471+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7488`

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

- `market_context_high->unknown_24h` score `7652.1019` n `55` status `ready` deltaP `1.3889` edge `637.6659` maxDD `0.0`
- `market_context_high->unknown_4h` score `331.1462` n `55` status `ready` deltaP `7.1757` edge `27.552` maxDD `-0.0124`
- `market_context_high->unknown_1h` score `27.2876` n `57` status `ready` deltaP `4.8929` edge `2.2524` maxDD `-0.2178`
- `market_context_high->equity_24h` score `21.352` n `55` status `ready` deltaP `42.7999` edge `1.5176` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `13.4597` n `94` status `ready` deltaP `32.0035` edge `1.0439` maxDD `-6.8493`
- `market_context_high->index_24h` score `6.1626` n `55` status `ready` deltaP `49.1319` edge `0.186` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `6.0159` n `55` status `ready` deltaP `23.9024` edge `0.3714` maxDD `-1.6876`
- `market_context_high->commodity_24h` score `5.8849` n `55` status `ready` deltaP `40.7545` edge `0.2498` maxDD `-0.8203`
- `market_context_high->crypto_major_4h` score `5.4175` n `55` status `ready` deltaP `30.2827` edge `0.2832` maxDD `-1.6901`
- `market_context_high->equity_4h` score `3.1408` n `55` status `ready` deltaP `5.2855` edge `0.2967` maxDD `-2.283`
- `market_context_high->commodity_4h` score `2.9952` n `55` status `ready` deltaP `28.7805` edge `0.0828` maxDD `-0.3387`
- `market_context_high->crypto_major_24h` score `2.4556` n `55` status `ready` deltaP `10.8586` edge `0.3101` maxDD `-3.0799`
- `news_risk_high->crypto_alt_4h` score `2.3379` n `126` status `ready` deltaP `9.7754` edge `0.2683` maxDD `-7.4246`
- `market_context_high->crypto_alt_24h` score `2.0592` n `55` status `ready` deltaP `-3.2576` edge `0.4375` maxDD `-8.8096`
- `market_context_high->metal_4h` score `1.7519` n `55` status `ready` deltaP `20.6374` edge `0.0509` maxDD `-0.7323`
- `market_context_high->equity_1h` score `1.6132` n `57` status `ready` deltaP `4.386` edge `0.1577` maxDD `-1.5336`
- `market_context_high->crypto_major_1h` score `1.0927` n `57` status `ready` deltaP `5.9907` edge `0.1121` maxDD `-2.2118`
- `market_context_high->crypto_alt_1h` score `1.0039` n `57` status `ready` deltaP `1.7754` edge `0.1389` maxDD `-2.3659`
- `market_context_high->metal_1h` score `0.7793` n `57` status `ready` deltaP `9.8829` edge `0.0239` maxDD `-0.3209`
- `market_context_high->fx_1h` score `0.6388` n `57` status `ready` deltaP `14.6129` edge `0.0029` maxDD `-0.1407`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
