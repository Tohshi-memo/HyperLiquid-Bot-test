# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T23:37:32.456591+00:00`
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

- `market_context_high->unknown_4h` score `45.6814` n `46` status `ready` deltaP `6.4024` edge `3.7641` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `29.6667` n `46` status `ready` deltaP `13.5341` edge `2.3976` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.2661` n `46` status `ready` deltaP `12.1453` edge `1.2846` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `13.2276` n `46` status `ready` deltaP `10.5903` edge `1.0317` maxDD `0.0`
- `market_context_high->index_24h` score `5.5047` n `46` status `ready` deltaP `19.6105` edge `0.3367` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `4.9731` n `96` status `ready` deltaP `-9.2014` edge `1.1616` maxDD `-46.1999`
- `news_risk_high->commodity_24h` score `4.8363` n `96` status `ready` deltaP `36.6319` edge `0.2767` maxDD `-2.431`
- `news_risk_high->crypto_major_4h` score `2.9121` n `96` status `ready` deltaP `14.1768` edge `0.2059` maxDD `-2.619`
- `news_risk_high->crypto_alt_4h` score `2.4555` n `96` status `ready` deltaP `9.6037` edge `0.2404` maxDD `-5.9838`
- `news_risk_high->crypto_alt_1h` score `1.8942` n `97` status `ready` deltaP `10.9205` edge `0.1246` maxDD `-1.1645`
- `market_context_high->index_4h` score `1.8376` n `46` status `ready` deltaP `21.9445` edge `0.0202` maxDD `-0.0692`
- `news_risk_high->crypto_major_1h` score `1.4044` n `97` status `ready` deltaP `12.8666` edge `0.0706` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.3986` n `96` status `ready` deltaP `20.7063` edge `0.0421` maxDD `-0.421`
- `news_risk_high->fx_24h` score `0.7782` n `96` status `ready` deltaP `22.7431` edge `0.1071` maxDD `-1.7159`
- `market_context_high->equity_1h` score `0.6423` n `46` status `ready` deltaP `5.7147` edge `0.0397` maxDD `-0.2751`
- `market_context_high->metal_24h` score `0.639` n `46` status `ready` deltaP `19.4898` edge `-0.0533` maxDD `-0.2042`
- `news_risk_high->metal_1h` score `0.6097` n `97` status `ready` deltaP `14.9315` edge `0.0106` maxDD `-0.7468`
- `market_context_high->index_1h` score `0.6076` n `46` status `ready` deltaP `9.9063` edge `0.0099` maxDD `-0.0249`
- `news_risk_high->crypto_alt_24h` score `0.3367` n `96` status `ready` deltaP `-9.2014` edge `0.5775` maxDD `-32.7147`
- `news_risk_high->fx_1h` score `0.2748` n `97` status `ready` deltaP `8.4974` edge `0.0106` maxDD `-0.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
