# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T13:52:31.967557+00:00`
- Price records: `672`
- Market context records: `5884`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10248`

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

- `news_risk_high->fx_4h` score `3.7752` n `30` status `ready` deltaP `39.3902` edge `0.0566` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.0501` n `30` status `ready` deltaP `24.8303` edge `0.0192` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.3045` n `230` status `ready` deltaP `7.9851` edge `0.1655` maxDD `-4.1352`
- `news_risk_high->crypto_major_1h` score `0.9595` n `30` status `ready` deltaP `11.6866` edge `0.0918` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.2894` n `30` status `ready` deltaP `5.3194` edge `0.0478` maxDD `-1.6923`
- `market_context_high->equity_1h` score `-0.0722` n `233` status `ready` deltaP `5.6051` edge `0.046` maxDD `-4.4103`
- `market_context_high->metal_1h` score `-0.2956` n `233` status `ready` deltaP `3.5684` edge `0.0054` maxDD `-2.0339`
- `news_risk_high->metal_1h` score `-0.4266` n `30` status `ready` deltaP `1.5369` edge `-0.0283` maxDD `-1.2643`
- `market_context_high->crypto_major_1h` score `-0.4645` n `233` status `ready` deltaP `4.1473` edge `0.0449` maxDD `-6.2348`
- `market_context_high->commodity_1h` score `-0.5068` n `233` status `ready` deltaP `-0.9734` edge `-0.0014` maxDD `-1.9006`
- `market_context_high->crypto_alt_1h` score `-0.5358` n `233` status `ready` deltaP `3.1591` edge `0.0437` maxDD `-6.6758`
- `market_context_high->index_1h` score `-0.5389` n `233` status `ready` deltaP `1.5124` edge `0.0056` maxDD `-0.7819`
- `market_context_high->fx_1h` score `-0.7704` n `233` status `ready` deltaP `-2.1511` edge `-0.001` maxDD `-0.5751`
- `news_risk_high->index_1h` score `-1.2728` n `30` status `ready` deltaP `-12.994` edge `-0.0251` maxDD `-1.1161`
- `market_context_high->crypto_major_4h` score `-1.5945` n `230` status `ready` deltaP `8.9727` edge `0.173` maxDD `-25.6458`
- `news_risk_high->commodity_4h` score `-1.7881` n `30` status `ready` deltaP `-13.4248` edge `-0.0522` maxDD `-2.3372`
- `market_context_high->index_4h` score `-1.879` n `230` status `ready` deltaP `-0.3381` edge `0.0144` maxDD `-3.165`
- `news_risk_high->index_4h` score `-2.3032` n `30` status `ready` deltaP `-16.8598` edge `-0.0795` maxDD `-2.9371`
- `market_context_high->commodity_4h` score `-2.3996` n `230` status `ready` deltaP `-1.8306` edge `-0.0164` maxDD `-6.3754`
- `market_context_high->metal_4h` score `-2.4637` n `230` status `ready` deltaP `-1.9923` edge `-0.0288` maxDD `-5.725`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
