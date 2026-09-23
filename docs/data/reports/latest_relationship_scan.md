# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T05:22:29.471983+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9818`

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

- `market_context_high->unknown_4h` score `46.6444` n `46` status `ready` deltaP `7.7744` edge `3.8352` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `29.3991` n `46` status `ready` deltaP `13.5341` edge `2.3753` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.6765` n `46` status `ready` deltaP `12.1453` edge `1.3188` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `12.5268` n `46` status `ready` deltaP `10.5903` edge `0.9733` maxDD `0.0`
- `market_context_high->index_24h` score `5.6536` n `46` status `ready` deltaP `20.8258` edge `0.341` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `4.7055` n `96` status `ready` deltaP `-9.2014` edge `1.1393` maxDD `-46.1999`
- `news_risk_high->commodity_24h` score `4.4754` n `96` status `ready` deltaP `34.8958` edge `0.2582` maxDD `-2.431`
- `news_risk_high->crypto_major_4h` score `2.6238` n `98` status `ready` deltaP `12.8827` edge `0.1905` maxDD `-2.619`
- `market_context_high->index_4h` score `2.1599` n `46` status `ready` deltaP `25.2982` edge `0.0247` maxDD `-0.0692`
- `news_risk_high->crypto_alt_4h` score `1.994` n `98` status `ready` deltaP `8.0047` edge `0.2126` maxDD `-5.9838`
- `news_risk_high->crypto_alt_1h` score `1.8446` n `103` status `ready` deltaP `10.7624` edge `0.131` maxDD `-1.5895`
- `news_risk_high->crypto_major_1h` score `1.3957` n `103` status `ready` deltaP `12.8583` edge `0.0741` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.3534` n `98` status `ready` deltaP `20.1717` edge `0.0419` maxDD `-0.421`
- `news_risk_high->fx_24h` score `0.9709` n `96` status `ready` deltaP `25.1736` edge `0.1156` maxDD `-1.7159`
- `market_context_high->equity_1h` score `0.7742` n `46` status `ready` deltaP `6.6129` edge `0.0447` maxDD `-0.2751`
- `market_context_high->equity_4h` score `0.7337` n `46` status `ready` deltaP `5.6999` edge `0.0538` maxDD `-0.4529`
- `market_context_high->index_1h` score `0.6675` n `46` status `ready` deltaP `10.5051` edge `0.0109` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.417` n `103` status `ready` deltaP `12.8074` edge `0.0087` maxDD `-0.7468`
- `news_risk_high->metal_4h` score `0.358` n `98` status `ready` deltaP `13.0195` edge `0.0388` maxDD `-1.9941`
- `news_risk_high->fx_1h` score `0.3214` n `103` status `ready` deltaP `9.0053` edge `0.0111` maxDD `-0.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
