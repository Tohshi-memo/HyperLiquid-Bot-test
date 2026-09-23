# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T05:07:32.570111+00:00`
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

- `market_context_high->unknown_4h` score `46.511` n `46` status `ready` deltaP `7.622` edge `3.8251` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `29.4327` n `46` status `ready` deltaP `13.5341` edge `2.3781` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.6777` n `46` status `ready` deltaP `12.1453` edge `1.3189` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `12.5784` n `46` status `ready` deltaP `10.5903` edge `0.9776` maxDD `0.0`
- `market_context_high->index_24h` score `5.6548` n `46` status `ready` deltaP `20.8258` edge `0.3411` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `4.7391` n `96` status `ready` deltaP `-9.2014` edge `1.1421` maxDD `-46.1999`
- `news_risk_high->commodity_24h` score `4.479` n `96` status `ready` deltaP `34.8958` edge `0.2585` maxDD `-2.431`
- `news_risk_high->crypto_major_4h` score `2.6468` n `98` status `ready` deltaP `13.0351` edge `0.1914` maxDD `-2.619`
- `market_context_high->index_4h` score `2.1465` n `46` status `ready` deltaP `25.1458` edge `0.0246` maxDD `-0.0692`
- `news_risk_high->crypto_alt_4h` score `2.029` n `98` status `ready` deltaP `8.1571` edge `0.2145` maxDD `-5.9838`
- `news_risk_high->crypto_alt_1h` score `1.8637` n `103` status `ready` deltaP `10.9121` edge `0.1316` maxDD `-1.5895`
- `news_risk_high->crypto_major_1h` score `1.3885` n `103` status `ready` deltaP `12.8583` edge `0.0735` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.3534` n `98` status `ready` deltaP `20.1717` edge `0.0419` maxDD `-0.421`
- `news_risk_high->fx_24h` score `0.9588` n `96` status `ready` deltaP `25.0` edge `0.1152` maxDD `-1.7159`
- `market_context_high->equity_1h` score `0.7574` n `46` status `ready` deltaP `6.4632` edge `0.0443` maxDD `-0.2751`
- `market_context_high->equity_4h` score `0.7131` n `46` status `ready` deltaP `5.5475` edge `0.0531` maxDD `-0.4529`
- `market_context_high->index_1h` score `0.6543` n `46` status `ready` deltaP `10.3554` edge `0.0108` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.417` n `103` status `ready` deltaP `12.8074` edge `0.0087` maxDD `-0.7468`
- `news_risk_high->metal_4h` score `0.358` n `98` status `ready` deltaP `13.0195` edge `0.0388` maxDD `-1.9941`
- `news_risk_high->fx_1h` score `0.3214` n `103` status `ready` deltaP `9.0053` edge `0.0111` maxDD `-0.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
