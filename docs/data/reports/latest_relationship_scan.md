# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T04:52:34.718599+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9858`

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

- `market_context_high->unknown_1h` score `72.3522` n `47` status `ready` deltaP `10.8645` edge `5.964` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `38.2078` n `46` status `ready` deltaP `25.5133` edge `3.0295` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `22.9149` n `46` status `ready` deltaP `20.4861` edge `1.773` maxDD `0.0`
- `market_context_high->equity_24h` score `22.0712` n `46` status `ready` deltaP `22.9091` edge `1.6966` maxDD `-0.1382`
- `market_context_high->index_24h` score `7.3789` n `46` status `ready` deltaP `31.9369` edge `0.4107` maxDD `-0.03`
- `news_risk_high->crypto_alt_4h` score `4.9935` n `103` status `ready` deltaP `14.6889` edge `0.418` maxDD `-5.9838`
- `news_risk_high->crypto_major_4h` score `4.8159` n `103` status `ready` deltaP `18.8048` edge `0.3337` maxDD `-2.619`
- `news_risk_high->crypto_major_24h` score `4.4666` n `103` status `ready` deltaP `-2.1777` edge `1.291` maxDD `-63.6743`
- `news_risk_high->crypto_alt_1h` score `2.624` n `103` status `ready` deltaP `14.0559` edge `0.174` maxDD `-1.5895`
- `market_context_high->index_4h` score `2.5988` n `47` status `ready` deltaP `30.5202` edge `0.0285` maxDD `-0.2323`
- `market_context_high->metal_24h` score `2.4896` n `46` status `ready` deltaP `25.9134` edge `0.0581` maxDD `-0.2042`
- `news_risk_high->commodity_24h` score `2.246` n `103` status `ready` deltaP `22.3587` edge `0.156` maxDD `-2.431`
- `news_risk_high->crypto_major_1h` score `2.1284` n `103` status `ready` deltaP `16.4511` edge `0.1112` maxDD `-1.8141`
- `market_context_high->equity_4h` score `1.711` n `47` status `ready` deltaP `13.3335` edge `0.0955` maxDD `-1.3444`
- `news_risk_high->fx_4h` score `1.5868` n `103` status `ready` deltaP `23.224` edge `0.041` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.2249` n `103` status `ready` deltaP `29.6639` edge `0.1224` maxDD `-1.7159`
- `market_context_high->index_1h` score `0.8553` n `47` status `ready` deltaP `13.5622` edge `0.0087` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.6909` n `47` status `ready` deltaP `9.67` edge `0.0334` maxDD `-1.5564`
- `news_risk_high->metal_1h` score `0.6661` n `103` status `ready` deltaP `15.502` edge `0.0115` maxDD `-0.7468`
- `news_risk_high->crypto_alt_24h` score `0.6528` n `103` status `ready` deltaP `-4.7566` edge `0.7874` maxDD `-49.7699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
