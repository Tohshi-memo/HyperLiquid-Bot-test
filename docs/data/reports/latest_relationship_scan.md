# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T23:07:34.122121+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9520`

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

- `market_context_high->unknown_4h` score `45.565` n `46` status `ready` deltaP `6.4024` edge `3.7544` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `29.6571` n `46` status `ready` deltaP `13.5341` edge `2.3968` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.2385` n `46` status `ready` deltaP `12.1453` edge `1.2823` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `13.332` n `46` status `ready` deltaP `10.5903` edge `1.0404` maxDD `0.0`
- `market_context_high->index_24h` score `5.5035` n `46` status `ready` deltaP `19.6105` edge `0.3366` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `4.9635` n `96` status `ready` deltaP `-9.2014` edge `1.1608` maxDD `-46.1999`
- `news_risk_high->commodity_24h` score `4.8941` n `96` status `ready` deltaP `36.9792` edge `0.2792` maxDD `-2.431`
- `news_risk_high->crypto_major_4h` score `2.9109` n `96` status `ready` deltaP `14.1768` edge `0.2058` maxDD `-2.619`
- `news_risk_high->crypto_alt_4h` score `2.5471` n `96` status `ready` deltaP `9.9085` edge `0.246` maxDD `-5.9838`
- `news_risk_high->crypto_alt_1h` score `1.9433` n `97` status `ready` deltaP `11.0702` edge `0.1277` maxDD `-1.1645`
- `market_context_high->index_4h` score `1.8218` n `46` status `ready` deltaP `21.7921` edge `0.0199` maxDD `-0.0692`
- `news_risk_high->crypto_major_1h` score `1.4164` n `97` status `ready` deltaP `12.8666` edge `0.0716` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.3694` n `96` status `ready` deltaP `20.4015` edge `0.0417` maxDD `-0.421`
- `news_risk_high->fx_24h` score `0.7508` n `96` status `ready` deltaP `22.3958` edge `0.1059` maxDD `-1.7159`
- `market_context_high->metal_24h` score `0.6859` n `46` status `ready` deltaP `19.837` edge `-0.0517` maxDD `-0.2042`
- `market_context_high->equity_1h` score `0.6399` n `46` status `ready` deltaP `5.7147` edge `0.0395` maxDD `-0.2751`
- `news_risk_high->metal_1h` score `0.6361` n `97` status `ready` deltaP `15.2309` edge `0.0108` maxDD `-0.7468`
- `market_context_high->index_1h` score `0.6076` n `46` status `ready` deltaP `9.9063` edge `0.0099` maxDD `-0.0249`
- `news_risk_high->crypto_alt_24h` score `0.4411` n `96` status `ready` deltaP `-9.2014` edge `0.5862` maxDD `-32.7147`
- `news_risk_high->metal_24h` score `0.2768` n `96` status `ready` deltaP `16.6667` edge `0.0088` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
