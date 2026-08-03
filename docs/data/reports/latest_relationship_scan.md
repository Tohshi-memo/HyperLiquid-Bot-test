# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T04:07:26.243151+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5935`

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

- `news_risk_high->unknown_24h` score `3229.8875` n `46` status `ready` deltaP `21.6862` edge `269.0548` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `13.7847` n `40` status `ready` deltaP `51.4583` edge `0.8454` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `11.1174` n `40` status `ready` deltaP `51.3194` edge `0.5971` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `2.6222` n `46` status `ready` deltaP `3.7778` edge `0.2697` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.1044` n `46` status `ready` deltaP `10.6045` edge `0.0594` maxDD `-0.3783`
- `market_context_high->commodity_1h` score `0.365` n `47` status `ready` deltaP `7.5646` edge `0.0338` maxDD `-1.3282`
- `market_context_high->commodity_4h` score `0.3372` n `47` status `ready` deltaP `5.0338` edge `0.0943` maxDD `-2.7703`
- `news_risk_high->metal_4h` score `0.2384` n `46` status `ready` deltaP `7.7811` edge `0.0138` maxDD `-0.8085`
- `news_risk_high->metal_1h` score `0.1981` n `46` status `ready` deltaP `7.049` edge `0.0104` maxDD `-0.5599`
- `market_context_high->fx_4h` score `0.0293` n `47` status `ready` deltaP `13.8752` edge `-0.0044` maxDD `-1.8531`
- `news_risk_high->index_1h` score `0.0195` n `46` status `ready` deltaP `4.2762` edge `0.0063` maxDD `-0.5845`
- `market_context_high->fx_1h` score `-0.0162` n `47` status `ready` deltaP `6.8161` edge `-0.0086` maxDD `-0.7804`
- `news_risk_high->commodity_1h` score `-0.0281` n `46` status `ready` deltaP `8.7672` edge `-0.0141` maxDD `-1.5026`
- `news_risk_high->fx_1h` score `-0.0503` n `46` status `ready` deltaP `3.6709` edge `0.0036` maxDD `-0.2475`
- `news_risk_high->equity_1h` score `-0.0846` n `46` status `ready` deltaP `2.4798` edge `0.0587` maxDD `-2.916`
- `market_context_high->crypto_alt_4h` score `-0.211` n `47` status `ready` deltaP `2.2963` edge `0.0482` maxDD `-4.9116`
- `news_risk_high->crypto_alt_1h` score `-0.3263` n `46` status `ready` deltaP `3.6709` edge `0.0019` maxDD `-3.1233`
- `news_risk_high->fx_4h` score `-0.334` n `46` status `ready` deltaP `4.0694` edge `0.0258` maxDD `-0.6604`
- `news_risk_high->crypto_major_1h` score `-0.6002` n `46` status `ready` deltaP `1.9461` edge `-0.0179` maxDD `-3.762`
- `market_context_high->fx_24h` score `-0.6983` n `40` status `ready` deltaP `0.6597` edge `0.0354` maxDD `-2.506`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
