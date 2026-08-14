# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-14T14:22:26.587650+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11796`

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

- `market_context_high->unknown_24h` score `108.7616` n `140` status `ready` deltaP `-33.2689` edge `9.5765` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `32.895` n `32` status `ready` deltaP `-44.9653` edge `4.5921` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `32.895` n `32` status `ready` deltaP `-44.9653` edge `4.5921` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `9.5523` n `36` status `ready` deltaP `9.8958` edge `0.768` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.1188` n `36` status `ready` deltaP `37.8049` edge `0.3412` maxDD `0.0`
- `risk_on_high->commodity_24h` score `4.8402` n `32` status `ready` deltaP `32.8125` edge `0.1846` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.8402` n `32` status `ready` deltaP `32.8125` edge `0.1846` maxDD `0.0`
- `market_context_high->commodity_24h` score `3.0503` n `140` status `ready` deltaP `22.0982` edge `0.1872` maxDD `-2.4263`
- `risk_on_high->commodity_4h` score `2.9418` n `32` status `ready` deltaP `20.503` edge `0.1267` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.9418` n `32` status `ready` deltaP `20.503` edge `0.1267` maxDD `-0.1258`
- `news_risk_high->index_24h` score `2.0404` n `36` status `ready` deltaP `13.7153` edge `0.0786` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `1.976` n `32` status `ready` deltaP `16.1458` edge `0.2613` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `1.976` n `32` status `ready` deltaP `16.1458` edge `0.2613` maxDD `-6.2481`
- `news_risk_high->index_4h` score `1.6385` n `36` status `ready` deltaP `19.3089` edge `0.021` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.6218` n `36` status `ready` deltaP `8.2835` edge `0.1118` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.2971` n `32` status `ready` deltaP `13.6602` edge `0.0403` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2971` n `32` status `ready` deltaP `13.6602` edge `0.0403` maxDD `-0.1957`
- `risk_on_high->fx_24h` score `1.2473` n `32` status `ready` deltaP `14.7569` edge `0.024` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.2473` n `32` status `ready` deltaP `14.7569` edge `0.024` maxDD `-0.1418`
- `market_context_high->commodity_4h` score `1.2387` n `140` status `ready` deltaP `15.2351` edge `0.0655` maxDD `-2.1077`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
