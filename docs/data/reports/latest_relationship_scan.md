# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T09:37:26.603002+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9810`

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

- `market_context_high->unknown_4h` score `46.7896` n `46` status `ready` deltaP `7.7744` edge `3.8473` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `29.4262` n `46` status `ready` deltaP `13.7078` edge `2.3764` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.6237` n `46` status `ready` deltaP `12.1453` edge `1.3144` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `12.3132` n `46` status `ready` deltaP `10.5903` edge `0.9555` maxDD `0.0`
- `market_context_high->index_24h` score `5.6296` n `46` status `ready` deltaP `20.8258` edge `0.339` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `4.7326` n `96` status `ready` deltaP `-9.0277` edge `1.1404` maxDD `-46.1999`
- `news_risk_high->commodity_24h` score `4.1627` n `96` status `ready` deltaP `33.5069` edge `0.2414` maxDD `-2.431`
- `news_risk_high->crypto_major_4h` score `2.9321` n `103` status `ready` deltaP `14.2316` edge `0.2072` maxDD `-2.619`
- `news_risk_high->crypto_alt_4h` score `2.3091` n `103` status `ready` deltaP `9.0487` edge `0.2319` maxDD `-5.9838`
- `market_context_high->index_4h` score `2.256` n `46` status `ready` deltaP `26.3653` edge `0.0256` maxDD `-0.0692`
- `news_risk_high->crypto_alt_1h` score `1.8877` n `103` status `ready` deltaP `11.0618` edge `0.1326` maxDD `-1.5895`
- `news_risk_high->crypto_major_1h` score `1.6032` n `103` status `ready` deltaP `14.0559` edge `0.0834` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.2823` n `103` status `ready` deltaP `19.7179` edge `0.039` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.0991` n `96` status `ready` deltaP `27.0833` edge `0.1193` maxDD `-1.7159`
- `market_context_high->equity_1h` score `0.8976` n `46` status `ready` deltaP `7.8105` edge `0.047` maxDD `-0.2751`
- `market_context_high->equity_4h` score `0.8936` n `46` status `ready` deltaP `6.9194` edge `0.059` maxDD `-0.4529`
- `market_context_high->index_1h` score `0.7322` n `46` status `ready` deltaP `11.2536` edge `0.0113` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.5452` n `103` status `ready` deltaP `14.1547` edge `0.0104` maxDD `-0.7468`
- `news_risk_high->fx_1h` score `0.2364` n `103` status `ready` deltaP `8.1071` edge `0.01` maxDD `-0.2147`
- `news_risk_high->metal_4h` score `0.179` n `103` status `ready` deltaP `12.1359` edge `0.0378` maxDD `-1.9941`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
