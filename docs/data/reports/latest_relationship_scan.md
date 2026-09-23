# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-23T04:52:38.646615+00:00`
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

- `market_context_high->unknown_4h` score `46.409` n `46` status `ready` deltaP `7.622` edge `3.8166` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `29.4567` n `46` status `ready` deltaP `13.5341` edge `2.3801` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.6729` n `46` status `ready` deltaP `12.1453` edge `1.3185` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `12.6132` n `46` status `ready` deltaP `10.5903` edge `0.9805` maxDD `0.0`
- `market_context_high->index_24h` score `5.6536` n `46` status `ready` deltaP `20.8258` edge `0.341` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `4.7631` n `96` status `ready` deltaP `-9.2014` edge `1.1441` maxDD `-46.1999`
- `news_risk_high->commodity_24h` score `4.4838` n `96` status `ready` deltaP `34.8958` edge `0.2589` maxDD `-2.431`
- `news_risk_high->crypto_major_4h` score `2.671` n `98` status `ready` deltaP `13.1876` edge `0.1924` maxDD `-2.619`
- `market_context_high->index_4h` score `2.1331` n `46` status `ready` deltaP `24.9933` edge `0.0245` maxDD `-0.0692`
- `news_risk_high->crypto_alt_4h` score `2.0616` n `98` status `ready` deltaP `8.3095` edge `0.2162` maxDD `-5.9838`
- `news_risk_high->crypto_alt_1h` score `1.8637` n `103` status `ready` deltaP `10.9121` edge `0.1316` maxDD `-1.5895`
- `news_risk_high->crypto_major_1h` score `1.3861` n `103` status `ready` deltaP `12.8583` edge `0.0733` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.34` n `98` status `ready` deltaP `20.0193` edge `0.0418` maxDD `-0.421`
- `news_risk_high->fx_24h` score `0.9466` n `96` status `ready` deltaP `24.8264` edge `0.1148` maxDD `-1.7159`
- `market_context_high->equity_1h` score `0.755` n `46` status `ready` deltaP `6.4632` edge `0.0441` maxDD `-0.2751`
- `market_context_high->equity_4h` score `0.6925` n `46` status `ready` deltaP `5.395` edge `0.0524` maxDD `-0.4529`
- `market_context_high->index_1h` score `0.6531` n `46` status `ready` deltaP `10.3554` edge `0.0107` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.4301` n `103` status `ready` deltaP `12.9571` edge `0.0088` maxDD `-0.7468`
- `news_risk_high->metal_4h` score `0.3568` n `98` status `ready` deltaP `13.0195` edge `0.0387` maxDD `-1.9941`
- `news_risk_high->fx_1h` score `0.3082` n `103` status `ready` deltaP `8.8556` edge `0.011` maxDD `-0.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
