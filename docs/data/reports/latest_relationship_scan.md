# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-09T03:07:26.823144+00:00`
- Price records: `672`
- Market context records: `6151`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11131`

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

- `news_risk_high->crypto_alt_24h` score `12.0046` n `30` status `ready` deltaP `41.9444` edge `0.7355` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `7.6595` n `30` status `ready` deltaP `67.7083` edge `0.1869` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.2921` n `32` status `ready` deltaP `44.7409` edge `0.064` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.4027` n `32` status `ready` deltaP `28.8922` edge `0.0215` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.5198` n `195` status `ready` deltaP `0.6549` edge `0.2231` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.2932` n `32` status `ready` deltaP `13.8286` edge `0.1203` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.6876` n `32` status `ready` deltaP `8.9259` edge `0.0748` maxDD `-1.6923`
- `news_risk_high->crypto_major_24h` score `0.5499` n `30` status `ready` deltaP `12.6389` edge `0.0642` maxDD `-4.2368`
- `market_context_high->equity_4h` score `0.056` n `195` status `ready` deltaP `2.6829` edge `0.0785` maxDD `-2.671`
- `news_risk_high->index_24h` score `-0.2282` n `30` status `ready` deltaP `7.5` edge `0.0079` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.2684` n `195` status `ready` deltaP `1.5845` edge `-0.0004` maxDD `-0.5659`
- `market_context_high->unknown_4h` score `-0.3157` n `195` status `ready` deltaP `-2.3069` edge `0.2423` maxDD `-11.925`
- `market_context_high->metal_24h` score `-0.3818` n `195` status `ready` deltaP `18.1197` edge `0.0871` maxDD `-11.8809`
- `market_context_high->metal_4h` score `-0.5754` n `195` status `ready` deltaP `4.1518` edge `0.0173` maxDD `-3.4996`
- `news_risk_high->commodity_24h` score `-0.6091` n `30` status `ready` deltaP `14.0973` edge `-0.1242` maxDD `-0.3101`
- `news_risk_high->metal_1h` score `-0.7341` n `32` status `ready` deltaP `-2.5449` edge `-0.0274` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.7637` n `195` status `ready` deltaP `2.8397` edge `-0.0027` maxDD `-2.0564`
- `market_context_high->commodity_1h` score `-0.7775` n `195` status `ready` deltaP `-2.2885` edge `-0.0049` maxDD `-0.5708`
- `market_context_high->equity_1h` score `-0.8562` n `195` status `ready` deltaP `-1.4571` edge `0.0115` maxDD `-4.2573`
- `market_context_high->crypto_alt_1h` score `-0.8883` n `195` status `ready` deltaP `3.9099` edge `0.0353` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
