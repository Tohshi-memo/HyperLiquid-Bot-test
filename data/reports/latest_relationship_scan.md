# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T01:07:30.779422+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9740`

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

- `market_context_high->unknown_4h` score `45.8404` n `46` status `ready` deltaP `6.8598` edge `3.7743` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `29.6955` n `46` status `ready` deltaP `13.5341` edge `2.4` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.4053` n `46` status `ready` deltaP `12.1453` edge `1.2962` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `13.0512` n `46` status `ready` deltaP `10.5903` edge `1.017` maxDD `0.0`
- `market_context_high->index_24h` score `5.5215` n `46` status `ready` deltaP `19.6105` edge `0.3381` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `5.0019` n `96` status `ready` deltaP `-9.2014` edge `1.164` maxDD `-46.1999`
- `news_risk_high->commodity_24h` score `4.657` n `96` status `ready` deltaP `35.5903` edge `0.2687` maxDD `-2.431`
- `news_risk_high->crypto_major_4h` score `2.924` n `97` status `ready` deltaP `14.3701` edge `0.2056` maxDD `-2.619`
- `news_risk_high->crypto_alt_4h` score `2.3626` n `97` status `ready` deltaP `9.4921` edge `0.2334` maxDD `-5.9838`
- `market_context_high->index_4h` score `1.9216` n `46` status `ready` deltaP `22.8592` edge `0.0211` maxDD `-0.0692`
- `news_risk_high->crypto_alt_1h` score `1.7911` n `97` status `ready` deltaP `10.3216` edge `0.12` maxDD `-1.1645`
- `news_risk_high->fx_4h` score `1.3803` n `97` status `ready` deltaP `20.5086` edge `0.0419` maxDD `-0.421`
- `news_risk_high->crypto_major_1h` score `1.3528` n `97` status `ready` deltaP `12.7169` edge `0.0673` maxDD `-1.8141`
- `news_risk_high->fx_24h` score `0.824` n `96` status `ready` deltaP `23.2639` edge `0.1095` maxDD `-1.7159`
- `news_risk_high->metal_1h` score `0.6373` n `97` status `ready` deltaP `15.2309` edge `0.0109` maxDD `-0.7468`
- `market_context_high->equity_1h` score `0.6363` n `46` status `ready` deltaP `5.7147` edge `0.0392` maxDD `-0.2751`
- `market_context_high->index_1h` score `0.61` n `46` status `ready` deltaP `9.9063` edge `0.0101` maxDD `-0.0249`
- `market_context_high->metal_24h` score `0.5371` n `46` status `ready` deltaP `18.6217` edge `-0.056` maxDD `-0.2042`
- `news_risk_high->fx_1h` score `0.3431` n `97` status `ready` deltaP `9.2459` edge `0.0113` maxDD `-0.2147`
- `market_context_high->equity_4h` score `0.3309` n `46` status `ready` deltaP `3.2609` edge `0.0365` maxDD `-0.4529`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
