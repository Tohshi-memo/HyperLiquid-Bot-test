# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-08T01:22:23.677694+00:00`
- Price records: `672`
- Market context records: `3235`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9724`

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

- `market_context_high->crypto_alt_24h` score `14.4672` n `103` status `ready` deltaP `19.5186` edge `2.7088` maxDD `-70.3986`
- `market_context_high->commodity_24h` score `13.8267` n `103` status `ready` deltaP `50.0776` edge `0.8612` maxDD `-2.0927`
- `market_context_high->index_24h` score `9.7846` n `103` status `ready` deltaP `32.7046` edge `0.8528` maxDD `-16.1026`
- `market_context_high->equity_24h` score `6.7764` n `103` status `ready` deltaP `20.2636` edge `1.5753` maxDD `-53.663`
- `market_context_high->crypto_major_24h` score `2.9207` n `103` status `ready` deltaP `23.5892` edge `2.2871` maxDD `-152.2601`
- `risk_on_high->crypto_major_1h` score `2.5673` n `31` status `ready` deltaP `10.5273` edge `0.3659` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `2.5673` n `31` status `ready` deltaP `10.5273` edge `0.3659` maxDD `-5.8885`
- `market_context_high->commodity_4h` score `2.0311` n `133` status `ready` deltaP `17.4961` edge `0.1419` maxDD `-3.4758`
- `risk_on_high->crypto_alt_1h` score `0.6513` n `31` status `ready` deltaP `3.559` edge `0.2035` maxDD `-8.1649`
- `risk_on_and_context->crypto_alt_1h` score `0.6513` n `31` status `ready` deltaP `3.559` edge `0.2035` maxDD `-8.1649`
- `risk_on_high->metal_1h` score `0.4623` n `31` status `ready` deltaP `8.0645` edge `0.074` maxDD `-1.4793`
- `risk_on_and_context->metal_1h` score `0.4623` n `31` status `ready` deltaP `8.0645` edge `0.074` maxDD `-1.4793`
- `risk_on_high->equity_1h` score `0.2978` n `31` status `ready` deltaP `2.2117` edge `0.1138` maxDD `-3.5625`
- `risk_on_and_context->equity_1h` score `0.2978` n `31` status `ready` deltaP `2.2117` edge `0.1138` maxDD `-3.5625`
- `risk_on_high->index_1h` score `-0.1461` n `31` status `ready` deltaP `-0.1159` edge `0.0444` maxDD `-1.3216`
- `risk_on_and_context->index_1h` score `-0.1461` n `31` status `ready` deltaP `-0.1159` edge `0.0444` maxDD `-1.3216`
- `market_context_high->commodity_1h` score `-0.4522` n `145` status `ready` deltaP `3.7022` edge `0.0192` maxDD `-2.5251`
- `market_context_high->index_1h` score `-0.4961` n `145` status `ready` deltaP `3.9108` edge `0.0166` maxDD `-4.5023`
- `market_context_high->unknown_4h` score `-0.6766` n `133` status `ready` deltaP `10.0781` edge `0.103` maxDD `-15.1257`
- `market_context_high->crypto_major_1h` score `-0.7196` n `145` status `ready` deltaP `3.9645` edge `0.1076` maxDD `-15.1032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
