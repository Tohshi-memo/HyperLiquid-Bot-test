# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T22:22:33.508378+00:00`
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

- `market_context_high->unknown_4h` score `45.4152` n `46` status `ready` deltaP `6.5549` edge `3.7409` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `29.642` n `46` status `ready` deltaP `13.3605` edge `2.3967` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.2145` n `46` status `ready` deltaP `12.1453` edge `1.2803` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `13.5314` n `46` status `ready` deltaP `10.9375` edge `1.0547` maxDD `0.0`
- `market_context_high->index_24h` score `5.5047` n `46` status `ready` deltaP `19.6105` edge `0.3367` maxDD `-0.03`
- `news_risk_high->commodity_24h` score `4.9838` n `96` status `ready` deltaP `37.5` edge `0.2832` maxDD `-2.431`
- `news_risk_high->crypto_major_24h` score `4.9484` n `96` status `ready` deltaP `-9.375` edge `1.1607` maxDD `-46.1999`
- `news_risk_high->crypto_major_4h` score `2.9219` n `96` status `ready` deltaP `14.3293` edge `0.2057` maxDD `-2.619`
- `news_risk_high->crypto_alt_4h` score `2.6519` n `96` status `ready` deltaP `10.2134` edge `0.2527` maxDD `-5.9838`
- `news_risk_high->crypto_alt_1h` score `1.9769` n `97` status `ready` deltaP `11.0702` edge `0.1305` maxDD `-1.1645`
- `market_context_high->index_4h` score `1.8206` n `46` status `ready` deltaP `21.7921` edge `0.0198` maxDD `-0.0692`
- `news_risk_high->crypto_major_1h` score `1.4608` n `97` status `ready` deltaP `13.166` edge `0.0733` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.328` n `96` status `ready` deltaP `19.9441` edge `0.0413` maxDD `-0.421`
- `market_context_high->metal_24h` score `0.76` n `46` status `ready` deltaP `20.3578` edge `-0.049` maxDD `-0.2042`
- `news_risk_high->fx_24h` score `0.7089` n `96` status `ready` deltaP `21.875` edge `0.104` maxDD `-1.7159`
- `market_context_high->equity_1h` score `0.6818` n `46` status `ready` deltaP `6.1638` edge `0.04` maxDD `-0.2751`
- `news_risk_high->metal_1h` score `0.6756` n `97` status `ready` deltaP `15.68` edge `0.0111` maxDD `-0.7468`
- `news_risk_high->crypto_alt_24h` score `0.6405` n `96` status `ready` deltaP `-8.8542` edge `0.6005` maxDD `-32.7147`
- `market_context_high->index_1h` score `0.6315` n `46` status `ready` deltaP `10.2057` edge `0.0099` maxDD `-0.0249`
- `news_risk_high->metal_24h` score `0.325` n `96` status `ready` deltaP `17.1875` edge `0.0115` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
