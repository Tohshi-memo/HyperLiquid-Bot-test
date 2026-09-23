# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T06:07:32.142381+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9786`

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

- `market_context_high->unknown_4h` score `47.0143` n `46` status `ready` deltaP `8.0793` edge `3.864` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `29.3343` n `46` status `ready` deltaP `13.5341` edge `2.3699` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.6549` n `46` status `ready` deltaP `12.1453` edge `1.317` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `12.42` n `46` status `ready` deltaP `10.5903` edge `0.9644` maxDD `0.0`
- `market_context_high->index_24h` score `5.6488` n `46` status `ready` deltaP `20.8258` edge `0.3406` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `4.6407` n `96` status `ready` deltaP `-9.2014` edge `1.1339` maxDD `-46.1999`
- `news_risk_high->commodity_24h` score `4.4538` n `96` status `ready` deltaP `34.8958` edge `0.2564` maxDD `-2.431`
- `news_risk_high->crypto_major_4h` score `2.6262` n `101` status `ready` deltaP `13.1233` edge `0.1891` maxDD `-2.619`
- `market_context_high->index_4h` score `2.1623` n `46` status `ready` deltaP `25.2982` edge `0.0249` maxDD `-0.0692`
- `news_risk_high->crypto_alt_4h` score `2.0791` n `101` status `ready` deltaP `8.0928` edge `0.2191` maxDD `-5.9838`
- `news_risk_high->crypto_alt_1h` score `1.8482` n `103` status `ready` deltaP `10.7624` edge `0.1313` maxDD `-1.5895`
- `news_risk_high->crypto_major_1h` score `1.4413` n `103` status `ready` deltaP `13.008` edge `0.0769` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.4017` n `101` status `ready` deltaP `20.8358` edge `0.0415` maxDD `-0.421`
- `news_risk_high->fx_24h` score `0.996` n `96` status `ready` deltaP `25.5208` edge `0.1165` maxDD `-1.7159`
- `market_context_high->equity_1h` score `0.8233` n `46` status `ready` deltaP `7.062` edge `0.0458` maxDD `-0.2751`
- `market_context_high->equity_4h` score `0.7543` n `46` status `ready` deltaP `5.8524` edge `0.0545` maxDD `-0.4529`
- `market_context_high->index_1h` score `0.695` n `46` status `ready` deltaP `10.8045` edge `0.0112` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.4349` n `103` status `ready` deltaP `12.9571` edge `0.0092` maxDD `-0.7468`
- `news_risk_high->fx_1h` score `0.2807` n `103` status `ready` deltaP `8.5562` edge `0.0107` maxDD `-0.2147`
- `market_context_high->metal_24h` score `0.1961` n `46` status `ready` deltaP `15.8439` edge `-0.0659` maxDD `-0.2042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
