# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T07:07:31.813768+00:00`
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

- `market_context_high->unknown_4h` score `47.1319` n `46` status `ready` deltaP `8.0793` edge `3.8738` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `29.2743` n `46` status `ready` deltaP `13.5341` edge `2.3649` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.6189` n `46` status `ready` deltaP `12.1453` edge `1.314` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `12.3` n `46` status `ready` deltaP `10.5903` edge `0.9544` maxDD `0.0`
- `market_context_high->index_24h` score `5.6392` n `46` status `ready` deltaP `20.8258` edge `0.3398` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `4.5807` n `96` status `ready` deltaP `-9.2014` edge `1.1289` maxDD `-46.1999`
- `news_risk_high->commodity_24h` score `4.4226` n `96` status `ready` deltaP `34.8958` edge `0.2538` maxDD `-2.431`
- `news_risk_high->crypto_major_4h` score `2.5719` n `103` status `ready` deltaP `13.1645` edge `0.1843` maxDD `-2.619`
- `market_context_high->index_4h` score `2.1587` n `46` status `ready` deltaP `25.2982` edge `0.0246` maxDD `-0.0692`
- `news_risk_high->crypto_alt_4h` score `2.0906` n `103` status `ready` deltaP `7.9816` edge `0.2208` maxDD `-5.9838`
- `news_risk_high->crypto_alt_1h` score `1.7702` n `103` status `ready` deltaP `10.3133` edge `0.1278` maxDD `-1.5895`
- `news_risk_high->crypto_major_1h` score `1.4233` n `103` status `ready` deltaP `13.008` edge `0.0754` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.4196` n `103` status `ready` deltaP `21.0899` edge `0.0413` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.0391` n `96` status `ready` deltaP `26.2153` edge `0.1174` maxDD `-1.7159`
- `market_context_high->equity_1h` score `0.8353` n `46` status `ready` deltaP `7.2117` edge `0.0458` maxDD `-0.2751`
- `market_context_high->equity_4h` score `0.7495` n `46` status `ready` deltaP `5.8524` edge `0.0541` maxDD `-0.4529`
- `market_context_high->index_1h` score `0.6555` n `46` status `ready` deltaP `10.3554` edge `0.0109` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.4637` n `103` status `ready` deltaP `13.2565` edge `0.0096` maxDD `-0.7468`
- `news_risk_high->fx_1h` score `0.2256` n `103` status `ready` deltaP `7.9574` edge `0.0101` maxDD `-0.2147`
- `market_context_high->metal_24h` score `0.1105` n `46` status `ready` deltaP `15.1495` edge `-0.0684` maxDD `-0.2042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
